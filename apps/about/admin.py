from django.contrib import admin

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


@admin.register(PageContent)
class PageContentAdmin(admin.ModelAdmin):
    list_display = ('slug', 'title')
    search_fields = ('slug', 'title', 'subtitle', 'meta_title', 'meta_description')
    prepopulated_fields = {'slug': ('title',)}
    fieldsets = (
        (
            'قسم الهيرو',
            {
                'fields': (
                    'slug',
                    'badge_text',
                    'title',
                    'subtitle',
                    'header_icon',
                )
            },
        ),
        (
            'أزرار الدعوة للتصرف',
            {
                'fields': (
                    'primary_cta_text',
                    'primary_cta_url',
                    'secondary_cta_text',
                    'secondary_cta_url',
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


@admin.register(ContentBlock)
class ContentBlockAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'is_active', 'order')
    list_filter = ('is_active',)
    list_editable = ('is_active', 'order')
    search_fields = ('title', 'slug', 'content')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Statistic)
class StatisticAdmin(admin.ModelAdmin):
    list_display = ('label', 'number', 'is_active', 'order')
    list_filter = ('is_active',)
    list_editable = ('is_active', 'order')
    search_fields = ('label', 'number', 'icon')


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'is_active', 'order')
    list_filter = ('is_active',)
    list_editable = ('is_active', 'order')
    search_fields = ('name', 'title', 'description')


@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ('label', 'number', 'is_active', 'order')
    list_filter = ('is_active',)
    list_editable = ('is_active', 'order')
    search_fields = ('label', 'number', 'icon')


@admin.register(HowItWorksStep)
class HowItWorksStepAdmin(admin.ModelAdmin):
    list_display = ('step_number', 'title', 'is_active', 'order')
    list_filter = ('is_active',)
    list_editable = ('is_active', 'order')
    search_fields = ('title', 'description', 'icon')


@admin.register(WhyUsFeature)
class WhyUsFeatureAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'order')
    list_filter = ('is_active',)
    list_editable = ('is_active', 'order')
    search_fields = ('title', 'description', 'icon')


@admin.register(ParentFeature)
class ParentFeatureAdmin(admin.ModelAdmin):
    list_display = ('title', 'feature_type', 'is_active', 'order')
    list_filter = ('feature_type', 'is_active')
    list_editable = ('is_active', 'order')
    search_fields = ('title', 'description', 'icon')
