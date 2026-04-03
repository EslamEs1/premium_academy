from django.contrib import messages
from django.shortcuts import redirect, render

from apps.contact.forms import ContactSubmissionForm
from apps.contact.models import ContactFAQ, ContactPageSettings, ContactSubmission, OperatingHours, WhyChoosePoint
from apps.main.context_processors import get_active_ordered_queryset, get_singleton_instance
from apps.main.models import CTABlock, SiteSettings


def contact_page(request):
    if request.method == 'POST':
        form = ContactSubmissionForm(request.POST)
        if form.is_valid():
            submission = form.save(commit=False)
            submission.is_read = False
            submission.save()
            messages.success(request, 'تم إرسال رسالتك بنجاح! سنرد عليك في أقرب وقت ممكن.')
            return redirect('contact:contact')
    else:
        form = ContactSubmissionForm()

    site_contact = SiteSettings.objects.first()
    page_settings = get_singleton_instance(ContactPageSettings)
    context = {
        'page_meta': page_settings,
        'page_settings': page_settings,
        'form': form,
        'why_choose_points': get_active_ordered_queryset(WhyChoosePoint) or [],
        'operating_hours': get_active_ordered_queryset(OperatingHours) or [],
        'contact_faqs': get_active_ordered_queryset(ContactFAQ) or [],
        'site_contact': site_contact,
        'cta': CTABlock.objects.filter(slug='contact-cta', is_active=True).first(),
    }
    return render(request, 'contact.html', context)
