# Quickstart: Academy Backend — Django Data Layer & CMS

**Branch**: `005-academy-backend-spec` | **Date**: 2026-03-28

---

## Prerequisites

- Python 3.11+ (already in venv)
- Django 6.0.3 (already installed)
- Node.js / npm (for Tailwind CSS build — already configured)

## Setup Steps

### 1. Install New Dependencies

```bash
pip install django-solo django-ckeditor-5 django-admin-sortable2 Pillow
```

### 2. Create the `accounts` App

```bash
cd /media/eslam/work/backend/premium_academy
python manage.py startapp accounts apps/accounts
```

Create `apps/accounts/models.py`:
```python
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def __str__(self):
        return self.get_full_name() or self.username
```

### 3. Update `config/settings.py`

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Third-party
    'solo',
    'django_ckeditor_5',
    'adminsortable2',
    # Project apps
    'apps.accounts',
    'apps.main',
    'apps.teacher',
    'apps.courses',
    'apps.blogs',
    'apps.about',
    'apps.contact',
]

AUTH_USER_MODEL = 'accounts.User'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

SOLO_CACHE = 'default'
SOLO_CACHE_TIMEOUT = 600

CKEDITOR_5_CONFIGS = {
    'default': {
        'toolbar': ['heading', '|', 'bold', 'italic', 'link',
                     'bulletedList', 'numberedList', 'blockQuote',
                     'imageUpload', '|', 'undo', 'redo'],
        'language': {'ui': 'en', 'content': 'ar'},
    }
}
```

### 4. Run Initial Migrations

```bash
python manage.py makemigrations accounts
python manage.py makemigrations main teacher courses blogs about contact
python manage.py migrate
python manage.py createsuperuser
```

### 5. Update URL Configuration

In `config/urls.py`:
```python
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.main.urls')),
    path('teachers/', include('apps.teacher.urls')),
    path('blog/', include('apps.blogs.urls')),
    path('about/', include('apps.about.urls')),
    path('contact/', include('apps.contact.urls')),
    path("ckeditor5/", include('django_ckeditor_5.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

### 6. Verify

```bash
python manage.py runserver
# Visit http://127.0.0.1:8000/admin/
# Login with superuser credentials
# Verify SiteSettings is accessible
```

## Development Workflow

1. **Models first**: Define models → `makemigrations` → `migrate`
2. **Admin second**: Register models with customized ModelAdmin
3. **Seed data**: Create management command or use admin to populate initial content
4. **Views third**: Create views pulling from models
5. **Templates last**: Replace hardcoded content with template tags

## Key Patterns

- **Singleton access**: `SiteSettings.get_solo()` or `{% get_solo 'main.SiteSettings' as site %}`
- **Published content**: `Model.objects.filter(status='published')` or use custom `PublishedManager`
- **Arabic slugs**: Auto-generated in `save()` via `slugify(title, allow_unicode=True)`
- **Rich text**: Use `CKEditor5Field` for blog content and static pages
- **Ordering**: Use `SortableAdminMixin` on ModelAdmin, `SortableTabularInline` on inlines
- **Context processor**: `site_settings` available in all templates automatically
