from django.db.models import Prefetch
from django.shortcuts import get_object_or_404, redirect, render

from apps.course.models import Subject
from apps.main.context_processors import get_active_ordered_queryset, get_singleton_instance
from apps.main.models import CTABlock, Testimonial
from apps.teacher.forms import TeacherApplicationForm
from apps.teacher.models import (
    Teacher,
    TeacherApplication,
    TeacherApplicationAttachment,
    TeacherAvailability,
    TeacherFeature,
    TeacherPageSettings,
    TeacherReview,
    TeacherSpecialization,
    TeacherStat,
)


def teacher_list(request):
    active_subject_slug = request.GET.get('subject', '').strip()
    page_settings = get_singleton_instance(TeacherPageSettings)
    subjects = Subject.objects.filter(is_active=True).order_by('order', 'name')
    teachers = Teacher.objects.filter(is_active=True).select_related('primary_subject').order_by('order', 'id')
    if active_subject_slug:
        teachers = teachers.filter(primary_subject__slug=active_subject_slug)

    context = {
        'page_meta': page_settings,
        'page_settings': page_settings,
        'subjects': subjects,
        'teachers': teachers,
        'stats': get_active_ordered_queryset(TeacherStat) or [],
        'testimonials': Testimonial.objects.filter(is_active=True, page='teachers').order_by('order', 'id')[:4],
        'cta': CTABlock.objects.filter(slug='teachers-cta', is_active=True).first(),
        'active_subject_slug': active_subject_slug,
    }
    return render(request, 'teachers.html', context)


def teacher_detail(request, slug):
    teacher = get_object_or_404(
        Teacher.objects.select_related('primary_subject').prefetch_related(
            Prefetch(
                'features',
                queryset=TeacherFeature.objects.filter(is_active=True).order_by('order', 'id'),
            ),
            Prefetch(
                'specializations',
                queryset=TeacherSpecialization.objects.filter(is_active=True)
                .select_related('subject')
                .order_by('order', 'id'),
            ),
            Prefetch(
                'reviews',
                queryset=TeacherReview.objects.filter(is_active=True).order_by('order', 'id'),
            ),
            Prefetch(
                'availability',
                queryset=TeacherAvailability.objects.filter(is_active=True).order_by('order', 'id'),
            ),
        ),
        slug=slug,
        is_active=True,
    )

    similar_teachers = list(
        Teacher.objects.filter(
            is_active=True,
            primary_subject=teacher.primary_subject,
        )
        .exclude(pk=teacher.pk)
        .select_related('primary_subject')
        .order_by('order', 'id')[:4]
    )
    if len(similar_teachers) < 4:
        missing_count = 4 - len(similar_teachers)
        existing_ids = [teacher.pk, *[item.pk for item in similar_teachers]]
        fallback_teachers = list(
            Teacher.objects.filter(is_active=True)
            .exclude(pk__in=existing_ids)
            .select_related('primary_subject')
            .order_by('order', 'id')[:missing_count]
        )
        similar_teachers.extend(fallback_teachers)

    context = {
        'page_meta': teacher,
        'teacher': teacher,
        'features': teacher.features.all(),
        'specializations': teacher.specializations.all(),
        'reviews': teacher.reviews.all(),
        'availability': teacher.availability.all(),
        'similar_teachers': similar_teachers,
        'cta': CTABlock.objects.filter(slug='teacher-profile-cta', is_active=True).first(),
    }
    return render(request, 'teacher-profile.html', context)


def teacher_apply(request):
    """Public page for teachers who want to join the academy."""
    success = request.GET.get('success') == '1'

    if request.method == 'POST':
        form = TeacherApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save()
            attachments = form.cleaned_data.get('attachments') or []
            if not isinstance(attachments, (list, tuple)):
                attachments = [attachments]
            for uploaded_file in attachments:
                if uploaded_file:
                    TeacherApplicationAttachment.objects.create(
                        application=application,
                        file=uploaded_file,
                    )
            return redirect(f'{request.path}?success=1')
    else:
        form = TeacherApplicationForm()

    context = {
        'form': form,
        'success': success,
        'page_meta': None,
    }
    return render(request, 'teacher-apply.html', context)
