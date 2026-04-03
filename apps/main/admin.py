from django.contrib import admin
from django.http import HttpResponseRedirect
from django.urls import reverse

from apps.main.models import (
    AppPromoSection,
    CTABlock,
    EducationalService,
    FAQ,
    FeatureBlock,
    FeaturePoint,
    FeatureTab,
    FeatureTabPoint,
    HeroSection,
    LegalPage,
    PageMeta,
    Partner,
    ProcessStep,
    RelatedLink,
    ServiceFeature,
    SiteSettings,
    SocialLink,
    Testimonial,
    TrustStat,
)


class SingletonAdminMixin(admin.ModelAdmin):
    """قاعدة للنماذج التي يجب أن يكون لها سجل واحد فقط."""

    def has_add_permission(self, request):
        if not super().has_add_permission(request):
            return False
        return not self.model.objects.exists()

    def changelist_view(self, request, extra_context=None):
        instance = self.model.objects.only('pk').first()
        if instance is None and self.has_add_permission(request):
            instance = self.model.objects.create()
        if instance is None:
            return super().changelist_view(request, extra_context)
        return HttpResponseRedirect(
            reverse(
                f'admin:{self.model._meta.app_label}_{self.model._meta.model_name}_change',
                args=(instance.pk,),
            )
        )


class SocialLinkInline(admin.TabularInline):
    model = SocialLink
    extra = 0
    ordering = ('order', 'id')
    verbose_name = 'رابط تواصل اجتماعي'
    verbose_name_plural = 'روابط التواصل الاجتماعي'


class ServiceFeatureInline(admin.TabularInline):
    model = ServiceFeature
    extra = 0
    ordering = ('order', 'id')
    verbose_name = 'ميزة الخدمة'
    verbose_name_plural = 'ميزات الخدمة'


class FeaturePointInline(admin.TabularInline):
    model = FeaturePoint
    extra = 0
    ordering = ('order', 'id')
    verbose_name = 'نقطة'
    verbose_name_plural = 'النقاط'


class FeatureTabInline(admin.TabularInline):
    model = FeatureTab
    extra = 0
    ordering = ('order', 'id')
    verbose_name = 'تبويب'
    verbose_name_plural = 'التبويبات'


class FeatureTabPointInline(admin.TabularInline):
    model = FeatureTabPoint
    extra = 0
    ordering = ('order', 'id')
    verbose_name = 'نقطة تبويب'
    verbose_name_plural = 'نقاط التبويب'


@admin.register(SiteSettings)
class SiteSettingsAdmin(SingletonAdminMixin):
    inlines = [SocialLinkInline]
    fieldsets = (
        (
            'الهوية البصرية',
            {
                'fields': (
                    'site_name',
                    'site_description',
                    'logo',
                    'logo_white',
                    'accreditation_badge',
                    'accreditation_text',
                )
            },
        ),
        (
            'معلومات التواصل',
            {
                'fields': (
                    'phone',
                    'email',
                    'whatsapp',
                    'address',
                    'google_maps_url',
                    'copyright_text',
                )
            },
        ),
    )


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active', 'order')
    list_filter = ('is_active',)
    list_editable = ('is_active', 'order')
    search_fields = ('name',)


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('student_name', 'page', 'rating', 'is_active', 'is_featured', 'order')
    list_filter = ('page', 'is_active', 'is_featured')
    list_editable = ('is_active', 'is_featured', 'order')
    search_fields = ('student_name', 'quote')


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question_preview', 'category', 'is_active', 'show_on_homepage', 'order')
    list_filter = ('category', 'is_active', 'show_on_homepage')
    list_editable = ('is_active', 'show_on_homepage', 'order')
    search_fields = ('question', 'answer')
    ordering = ('category', 'order', 'id')

    @admin.display(description='السؤال')
    def question_preview(self, obj):
        return obj.question[:60]


@admin.register(CTABlock)
class CTABlockAdmin(admin.ModelAdmin):
    list_display = ('heading', 'slug', 'is_active')
    list_filter = ('is_active',)
    list_editable = ('is_active',)
    search_fields = ('heading', 'slug')
    prepopulated_fields = {'slug': ('heading',)}


@admin.register(PageMeta)
class PageMetaAdmin(admin.ModelAdmin):
    list_display = ('slug', 'meta_title', 'is_active')
    list_filter = ('is_active',)
    list_editable = ('is_active',)
    search_fields = ('slug', 'meta_title', 'meta_description')


@admin.register(RelatedLink)
class RelatedLinkAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'order')
    list_filter = ('is_active',)
    list_editable = ('is_active', 'order')
    search_fields = ('title', 'description', 'url')


@admin.register(LegalPage)
class LegalPageAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'updated_at')
    readonly_fields = ('updated_at',)
    search_fields = ('title', 'slug', 'content', 'meta_title', 'meta_description')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(HeroSection)
class HeroSectionAdmin(SingletonAdminMixin):
    fieldsets = (
        (
            'محتوى القسم الرئيسي',
            {
                'fields': (
                    'headline',
                    'subheading',
                    'description',
                    'hero_image',
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
    )


@admin.register(TrustStat)
class TrustStatAdmin(admin.ModelAdmin):
    list_display = ('label', 'number', 'is_active', 'order')
    list_filter = ('is_active',)
    list_editable = ('is_active', 'order')
    search_fields = ('label', 'description')


@admin.register(EducationalService)
class EducationalServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'order')
    list_filter = ('is_active',)
    list_editable = ('is_active', 'order')
    search_fields = ('title', 'description')
    inlines = [ServiceFeatureInline]


@admin.register(FeatureBlock)
class FeatureBlockAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'is_active', 'order')
    list_filter = ('is_active',)
    list_editable = ('is_active', 'order')
    search_fields = ('title', 'slug', 'description')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [FeaturePointInline, FeatureTabInline]


@admin.register(FeatureTab)
class FeatureTabAdmin(admin.ModelAdmin):
    list_display = ('title', 'feature_block', 'order')
    list_editable = ('order',)
    search_fields = ('title', 'feature_block__title')
    inlines = [FeatureTabPointInline]


@admin.register(ProcessStep)
class ProcessStepAdmin(admin.ModelAdmin):
    list_display = ('step_number', 'title', 'is_active', 'order')
    list_filter = ('is_active',)
    list_editable = ('is_active', 'order')
    search_fields = ('title', 'description')


@admin.register(AppPromoSection)
class AppPromoSectionAdmin(SingletonAdminMixin):
    fieldsets = (
        (
            'محتوى قسم التطبيق',
            {
                'fields': (
                    'title',
                    'subtitle',
                    'description',
                    'preview_image',
                    'is_active',
                )
            },
        ),
        (
            'روابط المتاجر',
            {
                'fields': (
                    'google_play_url',
                    'app_store_url',
                )
            },
        ),
    )
