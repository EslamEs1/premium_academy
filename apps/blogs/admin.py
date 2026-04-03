from django.contrib import admin

from apps.blogs.models import Author, BlogPageSettings, BlogPost, Category
from apps.main.admin import SingletonAdminMixin


@admin.register(BlogPageSettings)
class BlogPageSettingsAdmin(SingletonAdminMixin):
    fieldsets = (
        (
            'محتوى صفحة المدونة',
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


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'is_active', 'order')
    list_filter = ('is_active',)
    list_editable = ('is_active', 'order')
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'is_active', 'order')
    list_filter = ('is_active',)
    list_editable = ('is_active', 'order')
    search_fields = ('name', 'title', 'bio')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'author', 'status', 'is_featured', 'published_date')
    list_filter = ('status', 'is_featured', 'category', 'author')
    search_fields = ('title', 'excerpt', 'content', 'meta_title', 'meta_description')
    prepopulated_fields = {'slug': ('title',)}
    autocomplete_fields = ('category', 'author')
    fieldsets = (
        (
            'محتوى المقالة',
            {
                'fields': (
                    'title',
                    'slug',
                    'category',
                    'author',
                    'cover_image',
                    'excerpt',
                    'content',
                    'read_time',
                )
            },
        ),
        (
            'النشر والظهور',
            {
                'fields': (
                    'status',
                    'is_featured',
                    'published_date',
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
