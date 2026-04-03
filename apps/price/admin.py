from django.contrib import admin

from apps.main.admin import SingletonAdminMixin
from apps.price.models import ComparisonFeature, PlanFeature, PricingFAQ, PricingPageSettings, PricingPlan


class PlanFeatureInline(admin.TabularInline):
    model = PlanFeature
    extra = 0
    ordering = ('order', 'id')


@admin.register(PricingPageSettings)
class PricingPageSettingsAdmin(SingletonAdminMixin):
    fieldsets = (
        (
            None,
            {
                'fields': (
                    'title',
                    'subtitle',
                    'description',
                )
            },
        ),
        (
            'SEO',
            {
                'fields': (
                    'meta_title',
                    'meta_description',
                )
            },
        ),
    )


@admin.register(PricingPlan)
class PricingPlanAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'is_popular', 'is_active', 'order')
    list_filter = ('is_popular', 'is_active')
    list_editable = ('is_popular', 'is_active', 'order')
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}
    inlines = [PlanFeatureInline]


@admin.register(ComparisonFeature)
class ComparisonFeatureAdmin(admin.ModelAdmin):
    list_display = ('label', 'is_active', 'order')
    list_filter = ('is_active',)
    list_editable = ('is_active', 'order')
    search_fields = ('label', 'basic_value', 'premium_value', 'professional_value')


@admin.register(PricingFAQ)
class PricingFAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'is_active', 'order')
    list_filter = ('is_active',)
    list_editable = ('is_active', 'order')
    search_fields = ('question', 'answer')
