from django.contrib import admin

from apps.contact.models import ContactFAQ, ContactPageSettings, ContactSubmission, OperatingHours, WhyChoosePoint
from apps.main.admin import SingletonAdminMixin


@admin.register(ContactPageSettings)
class ContactPageSettingsAdmin(SingletonAdminMixin):
    fieldsets = (
        (
            None,
            {
                'fields': (
                    'hero_title',
                    'hero_subtitle',
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


@admin.register(WhyChoosePoint)
class WhyChoosePointAdmin(admin.ModelAdmin):
    list_display = ('text', 'is_active', 'order')
    list_filter = ('is_active',)
    list_editable = ('is_active', 'order')
    search_fields = ('text',)


@admin.register(OperatingHours)
class OperatingHoursAdmin(admin.ModelAdmin):
    list_display = ('day_label', 'time_range', 'is_active', 'order')
    list_filter = ('is_active',)
    list_editable = ('is_active', 'order')
    search_fields = ('day_label', 'time_range', 'note')


@admin.register(ContactFAQ)
class ContactFAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'is_active', 'order')
    list_filter = ('is_active',)
    list_editable = ('is_active', 'order')
    search_fields = ('question', 'answer')


@admin.register(ContactSubmission)
class ContactSubmissionAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'subject', 'is_read', 'created_at')
    list_filter = ('is_read', 'subject', 'created_at')
    list_editable = ('is_read',)
    readonly_fields = ('full_name', 'email', 'phone', 'subject', 'message', 'created_at')
    search_fields = ('full_name', 'email', 'phone', 'message')

    def has_add_permission(self, request):
        return False

