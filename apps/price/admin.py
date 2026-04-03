from django.contrib import admin

from apps.main.admin import SingletonAdminMixin
from apps.price.models import ComparisonFeature, PlanFeature, PricingFAQ, PricingPageSettings, PricingPlan


class PlanFeatureInline(admin.TabularInline):
    model = PlanFeature
    extra = 0
    ordering = ('order', 'id')
    verbose_name = 'ميزة الباقة'
    verbose_name_plural = 'ميزات الباقة'


@admin.register(PricingPageSettings)
class PricingPageSettingsAdmin(SingletonAdminMixin):
    fieldsets = (
        (
            'محتوى صفحة الأسعار',
            {
                'fields': (
                    'title',
                    'subtitle',
                    'description',
                )
            },
        ),
        (
            'تحسين محركات البحث (SEO)',
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
    fieldsets = (
        (
            'تفاصيل الباقة',
            {
                'fields': (
                    'name',
                    'slug',
                    'label',
                    'description',
                    'price',
                    'period',
                    'currency',
                )
            },
        ),
        (
            'الإعدادات',
            {
                'fields': (
                    'is_popular',
                    'is_active',
                    'order',
                    'cta_text',
                    'cta_url',
                )
            },
        ),
    )


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
