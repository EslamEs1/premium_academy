from django.shortcuts import render

from apps.main.context_processors import get_active_ordered_queryset, get_singleton_instance
from apps.main.models import CTABlock, Testimonial, TestimonialPage
from apps.price.models import ComparisonFeature, PricingFAQ, PricingPageSettings, PricingPlan


def pricing_page(request):
    page_settings = get_singleton_instance(PricingPageSettings)
    context = {
        'page_meta': page_settings,
        'page_settings': page_settings,
        'plans': get_active_ordered_queryset(PricingPlan, prefetch_related=('features',)) or [],
        'comparison_features': get_active_ordered_queryset(ComparisonFeature) or [],
        'pricing_faqs': get_active_ordered_queryset(PricingFAQ) or [],
        'testimonials': Testimonial.objects.filter(is_active=True, page=TestimonialPage.PRICING).order_by('order', 'id')[:3],
        'cta': CTABlock.objects.filter(slug='pricing-cta', is_active=True).first(),
    }
    return render(request, 'pricing.html', context)
