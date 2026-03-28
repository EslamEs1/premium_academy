# Research: Academy Backend — Django Data Layer & CMS

**Branch**: `005-academy-backend-spec` | **Date**: 2026-03-28

---

## 1. Django Singleton Model Pattern

**Decision**: Use `django-solo` v2.5.1

**Rationale**: Provides `SingletonModel` base class, `SingletonModelAdmin` (skips list page, hides add/delete), and `{% get_solo %}` template tag. Built-in caching via Django's cache framework. Supports Django 6.0. Last released January 2026. Zero boilerplate — inherit and register.

**Alternatives Considered**:
- Custom `save()` override with pk=1: Works but ~30 lines of boilerplate per singleton, no caching, no template tag, no admin UX polish.
- Custom ModelAdmin only: Same boilerplate problem. django-solo does this in tested, maintained code.

---

## 2. Arabic Slug Generation

**Decision**: Use Django's built-in `slugify()` with `allow_unicode=True` + `SlugField(allow_unicode=True)`

**Rationale**: `slugify('دورة الرياضيات المتقدمة', allow_unicode=True)` produces `دورة-الرياضيات-المتقدمة`. Clean, readable Arabic slugs with zero external dependencies. Mixed Arabic/Latin works correctly.

**Important Gotcha**: Django admin's `prepopulated_fields` uses JavaScript that only handles ASCII transliteration. It will NOT generate correct Arabic slugs. Rely on the model's `save()` method for auto-generation.

**Alternatives Considered**:
- django-autoslug: Last released April 2023, no Django 6.x support. Unnecessary dependency.
- python-slugify: Works but adds dependency when Django's built-in does the same thing.

---

## 3. Rich Text Editor for Django Admin

**Decision**: Use `django-ckeditor-5` v0.2.20

**Rationale**: CKEditor 5 has first-class RTL/Arabic support (`language: {ui: 'en', content: 'ar'}`). Supports Django 6.0. Last released February 2026. Built-in image upload. Configurable toolbar.

**Alternatives Considered**:
- django-tinymce v4.1.0: Only supports Django up to 5.2. Last released June 2024.
- django-summernote: Dead project, no updates since October 2021.
- django-quill-editor: Weaker RTL support than CKEditor 5.

---

## 4. Django Admin Ordering/Sortable

**Decision**: Use `django-admin-sortable2` v2.3.1

**Rationale**: Drag-and-drop reordering for list views, stacked inlines, and tabular inlines. Uses Sortable.JS (no jQuery). Works as a mixin on admin class — just needs an integer `order` field (already in spec). Supports Django 6.0. Last released January 2026.

**Alternatives Considered**:
- django-ordered-model: Last stable release March 2023, Django 4.x only. Uses up/down arrows instead of drag-and-drop.
- Custom JS: Significant effort for something django-admin-sortable2 does in 3 lines.

---

## 5. Django Image Upload

**Decision**: Use Django's `ImageField` + Pillow directly. Skip thumbnail generation for Layer 1.

**Rationale**: `ImageField` handles upload, storage, and validation out of the box. Frontend controls image sizing via CSS/Tailwind. Thumbnail generation adds complexity (cache invalidation, storage management) with no benefit when CSS handles responsive display. Pillow is already a dependency of django-ckeditor-5.

**Alternatives Considered**:
- django-imagekit: Compatible with Django 6.x but adds unnecessary dependencies. Better suited for Layer 2 if thumbnails are needed.

---

## 6. Context Processor for Site Settings

**Decision**: Use django-solo's `{% get_solo %}` template tag as primary, with a thin context processor for automatic availability.

**Rationale**: django-solo provides the template tag out of the box. A context processor adds `site_settings` to all templates automatically. django-solo's built-in caching means the database is hit once, then cached. Cache auto-invalidates on admin save.

**Cache Configuration**:
- `SOLO_CACHE = 'default'`
- `SOLO_CACHE_TIMEOUT = 600` (10 minutes, auto-invalidated on save)
- Use LocMemCache for development, Redis/Memcached for production.

---

## 7. Custom User Model

**Decision**: Create `accounts` app with `User(AbstractUser)` before any migrations.

**Rationale**: Django's official recommendation. Changing the user model after migrations is extremely painful. Layer 2 needs student/teacher/parent accounts. The project has no migrations yet — now is the only easy time.

**Critical Gotchas**:
1. `AUTH_USER_MODEL` must be set before first `migrate`
2. `accounts` app must be in `INSTALLED_APPS` before first `makemigrations`
3. Always reference user model via `settings.AUTH_USER_MODEL` (strings) or `get_user_model()` — never direct import in other apps
4. Using `AbstractUser` (not `AbstractBaseUser`) gives all default fields and admin compatibility

---

## 8. Blog Pagination (Load More)

**Decision**: Django's built-in `Paginator` with `?page=N` query parameter, returning partial HTML for AJAX requests.

**Rationale**: Frontend has "Load More" button. Server returns page 1 initially; button fetches `?page=2` via AJAX, server returns just the card HTML partial, JS appends it. SEO-friendly — initial page has full content, `?page=N` URLs are crawlable. ~20 lines of code, zero dependencies.

**Alternatives Considered**:
- Full page pagination: Doesn't match frontend's load-more design.
- htmx: Good option but adding htmx for one button isn't justified.
- DRF JSON API: Overkill for server-side rendering in Layer 1.

---

## Dependency Summary

| Package | Version | Purpose | Django 6.x |
| --- | --- | --- | --- |
| django-solo | 2.5.1 | Singleton models (SiteSettings, AboutPage) | Yes |
| django-ckeditor-5 | 0.2.20 | Rich text editor with RTL/Arabic support | Yes |
| django-admin-sortable2 | 2.3.1 | Drag-and-drop admin ordering | Yes |
| Pillow | latest | Image processing (dependency of ckeditor-5) | Yes |

**Total new pip dependencies**: 4 packages (Pillow is a sub-dependency of django-ckeditor-5).
