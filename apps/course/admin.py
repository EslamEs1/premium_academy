from django.contrib import admin

from apps.course.models import Subject


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'order', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('name', 'description')
    list_editable = ('order', 'is_active')
    prepopulated_fields = {'slug': ('name',)}
    fieldsets = (
        (
            'بيانات المادة',
            {
                'fields': (
                    'name',
                    'slug',
                    'description',
                    'icon',
                )
            },
        ),
        (
            'الإعدادات',
            {
                'fields': (
                    'is_active',
                    'order',
                )
            },
        ),
    )
