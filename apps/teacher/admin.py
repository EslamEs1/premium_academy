from django.contrib import admin

from apps.main.admin import SingletonAdminMixin
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


class TeacherFeatureInline(admin.TabularInline):
    model = TeacherFeature
    extra = 0
    ordering = ('order', 'id')


class TeacherSpecializationInline(admin.TabularInline):
    model = TeacherSpecialization
    extra = 0
    ordering = ('order', 'id')


class TeacherReviewInline(admin.StackedInline):
    model = TeacherReview
    extra = 0
    ordering = ('order', 'id')


class TeacherAvailabilityInline(admin.TabularInline):
    model = TeacherAvailability
    extra = 0
    ordering = ('order', 'id')


@admin.register(TeacherPageSettings)
class TeacherPageSettingsAdmin(SingletonAdminMixin):
    fieldsets = (
        (
            None,
            {
                'fields': (
                    'hero_title',
                    'hero_subtitle',
                    'hero_image',
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


@admin.register(TeacherStat)
class TeacherStatAdmin(admin.ModelAdmin):
    list_display = ('label', 'number', 'is_active', 'order')
    list_filter = ('is_active',)
    list_editable = ('is_active', 'order')
    search_fields = ('label', 'description')


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'primary_subject', 'rating', 'is_active', 'is_featured', 'order')
    list_filter = ('is_active', 'is_featured', 'primary_subject')
    list_editable = ('is_active', 'is_featured', 'order')
    search_fields = ('name', 'title', 'short_bio', 'full_bio')
    prepopulated_fields = {'slug': ('name',)}
    inlines = [
        TeacherFeatureInline,
        TeacherSpecializationInline,
        TeacherReviewInline,
        TeacherAvailabilityInline,
    ]


# ── Teacher Application ──────────────────────────────────────────────────────

class TeacherApplicationAttachmentInline(admin.TabularInline):
    model = TeacherApplicationAttachment
    extra = 0
    readonly_fields = ('attachment_type', 'file', 'uploaded_at')
    can_delete = False

    def has_add_permission(self, request, obj=None):
        return False


@admin.register(TeacherApplication)
class TeacherApplicationAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone', 'specialization', 'experience', 'status', 'submitted_at')
    list_filter = ('status', 'experience')
    list_editable = ('status',)
    search_fields = ('full_name', 'phone', 'specialization', 'courses', 'description')
    readonly_fields = ('submitted_at', 'reviewed_at')
    ordering = ('-submitted_at',)
    inlines = [TeacherApplicationAttachmentInline]
    fieldsets = (
        ('معلومات شخصية', {
            'fields': ('full_name', 'phone', 'email'),
        }),
        ('التفاصيل المهنية', {
            'fields': ('specialization', 'experience', 'courses', 'description'),
        }),
        ('إدارة الطلب', {
            'fields': ('status', 'admin_notes', 'submitted_at', 'reviewed_at'),
        }),
    )
