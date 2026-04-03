from django.shortcuts import render

from apps.about.models import (
    Achievement,
    ContentBlock,
    HowItWorksStep,
    PageContent,
    ParentFeature,
    Statistic,
    TeamMember,
    WhyUsFeature,
)
from apps.main.context_processors import get_active_ordered_queryset
from apps.main.models import CTABlock, Partner, Testimonial, TestimonialPage


def about_page(request):
    page = PageContent.objects.filter(slug='about').first()
    block_queryset = get_active_ordered_queryset(ContentBlock) or []
    blocks = {block.slug.replace('-', '_'): block for block in block_queryset}
    context = {
        'page': page,
        'page_meta': page,
        'blocks': blocks,
        'statistics': get_active_ordered_queryset(Statistic) or [],
        'team_members': get_active_ordered_queryset(TeamMember) or [],
        'achievements': get_active_ordered_queryset(Achievement) or [],
        'partners': get_active_ordered_queryset(Partner) or [],
        'cta': CTABlock.objects.filter(slug='about-cta', is_active=True).first(),
    }
    return render(request, 'about.html', context)


def how_it_works_page(request):
    page = PageContent.objects.filter(slug='how-it-works').first()
    parent_features = get_active_ordered_queryset(ParentFeature) or []
    context = {
        'page': page,
        'page_meta': page,
        'steps': get_active_ordered_queryset(HowItWorksStep) or [],
        'why_us_features': get_active_ordered_queryset(WhyUsFeature) or [],
        'success_testimonials': Testimonial.objects.filter(
            is_active=True,
            page=TestimonialPage.HOW_IT_WORKS,
        ).order_by('order', 'id')[:3],
        'parent_features': parent_features,
        'core_parent_features': [feature for feature in parent_features if feature.feature_type == ParentFeature.FeatureType.CORE],
        'capability_parent_features': [
            feature for feature in parent_features
            if feature.feature_type == ParentFeature.FeatureType.CAPABILITY
        ],
        'cta': CTABlock.objects.filter(slug='how-it-works-cta', is_active=True).first(),
    }
    return render(request, 'how-it-works.html', context)
