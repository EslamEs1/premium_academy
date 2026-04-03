from django.apps import apps
from django.db.utils import OperationalError, ProgrammingError
from django.shortcuts import get_object_or_404, render

from apps.course.models import Subject
from apps.main.context_processors import get_active_ordered_queryset, get_singleton_instance
from apps.main.models import (
    AppPromoSection,
    CTABlock,
    EducationalService,
    FAQ,
    FAQCategory,
    FeatureBlock,
    HeroSection,
    LegalPage,
    PageMeta,
    Partner,
    ProcessStep,
    RelatedLink,
    Testimonial,
    TrustStat,
)


DEFAULT_TEACHER_SHOWCASE = [
    {
        'initials': 'رش',
        'name': 'أ. عبدالرحمن الشمري',
        'subject': 'الرياضيات',
        'experience': '10 سنوات خبرة',
        'rating': '4.9',
        'student_count': '230 طالبًا',
        'profile_url': '/teachers/',
        'gradient': 'from-[#F51140] to-pink-600',
    },
    {
        'initials': 'سك',
        'name': 'أ. سارة خالد',
        'subject': 'اللغة الإنجليزية',
        'experience': '8 سنوات خبرة',
        'rating': '4.8',
        'student_count': '185 طالبًا',
        'profile_url': '/teachers/',
        'gradient': 'from-[#FF8A2C] to-orange-600',
    },
    {
        'initials': 'فع',
        'name': 'د. فاطمة العتيبي',
        'subject': 'الكيمياء',
        'experience': '12 سنة خبرة',
        'rating': '4.9',
        'student_count': '260 طالبًا',
        'profile_url': '/teachers/',
        'gradient': 'from-[#FFDE05] to-yellow-500',
    },
    {
        'initials': 'مع',
        'name': 'أ. محمد العمري',
        'subject': 'الفيزياء',
        'experience': '9 سنوات خبرة',
        'rating': '4.7',
        'student_count': '172 طالبًا',
        'profile_url': '/teachers/',
        'gradient': 'from-[#F59E0B] to-yellow-600',
    },
]

FAQ_CATEGORY_LABELS = {
    FAQCategory.GENERAL: 'عام',
    FAQCategory.PRICING: 'الأسعار',
    FAQCategory.TEACHERS: 'المعلمون',
    FAQCategory.SCHEDULING: 'الجدولة',
    FAQCategory.PLATFORM: 'المنصة',
}

FAQ_RELATED_LINK_TITLES = (
    'كيف نعمل',
    'الأسعار والباقات',
    'تواصل معنا',
)


def _get_featured_teachers():
    try:
        teacher_model = apps.get_model('teacher', 'Teacher')
    except LookupError:
        return DEFAULT_TEACHER_SHOWCASE

    try:
        if not teacher_model._meta.managed:
            return DEFAULT_TEACHER_SHOWCASE
        teachers = teacher_model.objects.filter(
            is_active=True,
            is_featured=True,
        ).select_related('primary_subject').order_by('order')[:8]
    except (OperationalError, ProgrammingError):
        return DEFAULT_TEACHER_SHOWCASE

    if not teachers:
        return DEFAULT_TEACHER_SHOWCASE

    teacher_cards = []
    gradients = [
        'from-[#F51140] to-pink-600',
        'from-[#FF8A2C] to-orange-600',
        'from-[#FFDE05] to-yellow-500',
        'from-[#3B82F6] to-blue-800',
    ]
    for index, teacher in enumerate(teachers):
        teacher_cards.append(
            {
                'initials': getattr(teacher, 'initials', '') or teacher.name[:2],
                'name': teacher.name,
                'subject': getattr(getattr(teacher, 'primary_subject', None), 'name', ''),
                'experience': f"{getattr(teacher, 'experience_years', 0)} سنوات خبرة",
                'rating': getattr(teacher, 'rating', ''),
                'student_count': f"{getattr(teacher, 'student_count', 0)} طالبًا",
                'profile_url': getattr(teacher, 'get_absolute_url', lambda: '/teachers/')(),
                'gradient': gradients[index % len(gradients)],
            }
        )
    return teacher_cards


def home(request):
    hero = get_singleton_instance(HeroSection)
    page_meta = PageMeta.objects.filter(slug='home', is_active=True).first()
    stats = get_active_ordered_queryset(TrustStat)
    services = get_active_ordered_queryset(EducationalService, prefetch_related=('features',))
    partners = get_active_ordered_queryset(Partner)
    feature_blocks = FeatureBlock.objects.filter(
        slug__in=['private-tutoring', 'aptitude-tests'],
        is_active=True,
    ).prefetch_related('points', 'tabs__points').order_by('order')
    feature_blocks_by_slug = {block.slug: block for block in feature_blocks}
    subjects = Subject.objects.filter(is_active=True).order_by('order')
    testimonials = Testimonial.objects.filter(is_active=True, page='homepage').order_by('order')[:4]
    steps = get_active_ordered_queryset(ProcessStep)
    faqs = FAQ.objects.filter(is_active=True, show_on_homepage=True).order_by('order')[:10]
    app_promo = get_singleton_instance(AppPromoSection)
    cta = CTABlock.objects.filter(slug='homepage-cta', is_active=True).first()

    context = {
        'hero': hero,
        'page_meta': page_meta,
        'stats': stats or [],
        'services': services or [],
        'partners': partners or [],
        'tutoring_block': feature_blocks_by_slug.get('private-tutoring'),
        'aptitude_block': feature_blocks_by_slug.get('aptitude-tests'),
        'subjects': subjects,
        'teachers': _get_featured_teachers(),
        'testimonials': testimonials,
        'steps': steps or [],
        'faqs': faqs,
        'app_promo': app_promo,
        'cta': cta,
    }
    return render(request, 'index.html', context)


def faq_page(request):
    faqs = FAQ.objects.filter(is_active=True).order_by('category', 'order', 'id')
    faq_categories = [
        {
            'value': value,
            'label': FAQ_CATEGORY_LABELS.get(value, label),
        }
        for value, label in FAQCategory.choices
    ]
    context = {
        'page_meta': PageMeta.objects.filter(slug='faq', is_active=True).first(),
        'faqs': faqs,
        'faq_categories': faq_categories,
        'related_links': (
            RelatedLink.objects.filter(is_active=True, title__in=FAQ_RELATED_LINK_TITLES)
            .order_by('order', 'id')
        ),
    }
    return render(request, 'faq.html', context)


def privacy_page(request):
    legal_page = get_object_or_404(LegalPage, slug='privacy')
    context = {
        'legal_page': legal_page,
        'page_meta': legal_page,
    }
    return render(request, 'privacy.html', context)


def terms_page(request):
    legal_page = get_object_or_404(LegalPage, slug='terms')
    context = {
        'legal_page': legal_page,
        'page_meta': legal_page,
    }
    return render(request, 'terms.html', context)
