# Implementation Plan: Academy Backend — Django Data Layer & CMS

**Branch**: `005-academy-backend-spec` | **Date**: 2026-03-28 | **Spec**: [spec.md](spec.md)
**Input**: Feature specification from `/specs/005-academy-backend-spec/spec.md`

## Summary

Build the Django backend that powers SanaAcademy's existing static HTML frontend, converting 12 templates across 7 apps into a fully dynamic, admin-managed website. The implementation uses Django 6.0.3 with django-solo for singleton settings, django-ckeditor-5 for rich text with Arabic RTL support, django-admin-sortable2 for drag-and-drop ordering, and Pillow for image handling. It defines 27 models, a custom User model (for Layer 2 readiness), a publication workflow (draft/published/archived), SEO metadata, and a honeypot-protected contact form. No API layer — server-side rendering only.

## Technical Context

**Language/Version**: Python 3.11+, Django 6.0.3
**Primary Dependencies**: django-solo 2.5.1, django-ckeditor-5 0.2.20, django-admin-sortable2 2.3.1, Pillow
**Storage**: SQLite3 (development), PostgreSQL (production)
**Testing**: Django's built-in test framework (`python manage.py test`)
**Target Platform**: Linux server (production), local development
**Project Type**: Web application (server-side rendered Django)
**Performance Goals**: All pages load within 2 seconds, teacher filtering within 1 second
**Constraints**: Arabic RTL content, Saudi market, no API in Layer 1, no SPA frameworks
**Scale/Scope**: 500 teachers, 1000 blog posts, 200 FAQs, 12 public pages, 7 Django apps

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

The constitution (`constitution.md` v3.0.0) is a **Frontend Constitution** — its 15 sections govern design, typography, RTL, trust signals, and frontend code rules. The backend plan is evaluated for alignment:

| Constitution Section | Relevance to Backend | Status |
| --- | --- | --- |
| S1: Project Identity | Arabic-first, premium brand — backend serves Arabic content | PASS |
| S2: Product Intent | "Real, operational academy" — backend enables dynamic content management | PASS |
| S3: Arabic-First & RTL | Backend serves Arabic text, Arabic slugs, RTL-configured CKEditor | PASS |
| S4: Visual Language | Frontend responsibility — backend does not alter design | N/A |
| S5: Color & Design | Frontend responsibility | N/A |
| S6: Homepage Richness | Backend provides 13+ data sources for homepage sections | PASS |
| S7: Section Depth | Backend models map to all required content sections | PASS |
| S8: Trust-Building | Backend manages testimonials, partners, statistics, teacher credentials | PASS |
| S9: UX Quality Bar | Frontend responsibility — backend preserves existing UX | N/A |
| S10: Responsive | Frontend responsibility | N/A |
| S11: Content Tone (Arabic) | Backend stores and serves Arabic content as-is; CKEditor configured for Arabic | PASS |
| S12: Component Consistency | Frontend responsibility | N/A |
| S13: Frontend Code Rules | Backend does not introduce SPA/framework; templates use Django tags only | PASS |
| S14: Non-Goals for Frontend Phase | Backend IS the next phase — constitution anticipated it: "frontend MUST be architectured so [backend] can be integrated later" | PASS |
| S15: Definition of Success | Backend enables the "Saudi Parent Test" by making content admin-managed and dynamic | PASS |

**Gate Result**: PASS — No violations. The backend plan fulfills the constitution's Section 14 "Future Integration Readiness" requirement.

### Post-Design Re-Check

After Phase 1 design completion:
- Arabic slug generation uses `allow_unicode=True` (S3 compliance)
- CKEditor 5 configured with `language.content: 'ar'` (S3, S11 compliance)
- All 27 models map to frontend sections identified in constitution S6, S7, S8
- No SPA frameworks introduced (S13 compliance)
- Existing template structure preserved — Django tags replace hardcoded content only

**Post-Design Gate Result**: PASS

## Project Structure

### Documentation (this feature)

```text
specs/005-academy-backend-spec/
├── spec.md              # Feature specification
├── plan.md              # This file
├── research.md          # Phase 0: Technology research & decisions
├── data-model.md        # Phase 1: Full data model definition
├── quickstart.md        # Phase 1: Setup & development guide
├── checklists/
│   └── requirements.md  # Spec quality checklist
└── tasks.md             # Phase 2 output (created by /speckit.tasks)
```

### Source Code (repository root)

```text
apps/
├── accounts/                    # NEW: Custom User model
│   ├── models.py               # User(AbstractUser)
│   ├── admin.py                # UserAdmin registration
│   └── migrations/
├── main/
│   ├── abstract_models.py      # NEW: TimeStampedModel, SEOModel, PublishableModel
│   ├── models.py               # SiteSettings, HeroSection, Statistic, Service,
│   │                           # Partner, Testimonial, HowItWorksStep, Feature,
│   │                           # PricingPackage, PackageFeature, FAQ, FAQCategory,
│   │                           # StaticPage
│   ├── admin.py                # All main model admins with inlines & sortable
│   ├── views.py                # index, how_it_works, pricing, faq, static_page
│   ├── urls.py                 # / , /how-it-works/, /pricing/, /faq/, /privacy/, /terms/
│   ├── forms.py                # (none needed — no public forms in main)
│   ├── context_processors.py   # site_settings context processor
│   └── templates/main/
│       ├── index.html          # Existing → add Django template tags
│       ├── how-it-works.html
│       ├── pricing.html
│       ├── faq.html
│       ├── privacy.html
│       └── terms.html
├── teacher/
│   ├── models.py               # Teacher, TeacherSubject, TeacherAvailability,
│   │                           # TeacherReview
│   ├── admin.py                # TeacherAdmin with inlines
│   ├── views.py                # teacher_list, teacher_profile
│   ├── urls.py                 # /teachers/, /teachers/<slug>/
│   └── templates/teacher/
│       ├── teachers.html       # Existing → add Django template tags
│       └── teacher-profile.html
├── courses/
│   ├── models.py               # Subject, GradeLevel, SubjectLevel, ProgramTrack
│   ├── admin.py                # SubjectAdmin with SubjectLevel inline
│   └── (no views/urls — data consumed by main and teacher views)
├── blogs/
│   ├── models.py               # BlogCategory, BlogPost
│   ├── admin.py                # BlogPostAdmin
│   ├── views.py                # blog_list, blog_detail
│   ├── urls.py                 # /blog/, /blog/<slug>/
│   └── templates/blogs/
│       ├── blog.html           # Existing → add Django template tags
│       ├── blog-post.html
│       └── _post_cards.html    # NEW: Partial for AJAX load-more
├── about/
│   ├── models.py               # AboutPage, TeamMember
│   ├── admin.py                # AboutPageAdmin (singleton), TeamMemberAdmin
│   ├── views.py                # about_page
│   ├── urls.py                 # /about/
│   └── templates/about/
│       └── about.html          # Existing → add Django template tags
├── contact/
│   ├── models.py               # ContactSubmission
│   ├── admin.py                # ContactSubmissionAdmin (read-only fields)
│   ├── views.py                # contact_page (form processing)
│   ├── urls.py                 # /contact/
│   ├── forms.py                # ContactForm with honeypot
│   └── templates/contact/
│       └── contact.html        # Existing → add Django template tags
config/
├── settings.py                 # Updated: INSTALLED_APPS, AUTH_USER_MODEL, MEDIA, CKEDITOR
├── urls.py                     # Updated: all app URL includes + media serving
templates/
├── base.html                   # Updated: SEO meta block, site_settings context
├── 404.html
└── 500.html
media/                          # NEW: User-uploaded files (gitignored)
```

**Structure Decision**: Django multi-app architecture following existing project layout. 7 apps under `apps/` directory (6 existing + 1 new `accounts`). Shared abstract models in `main/abstract_models.py`. No new structural patterns — standard Django MVT.

## Complexity Tracking

No constitution violations found. No complexity justifications needed.

## Implementation Phases

### Phase 1A — Foundation (Priority: Critical)

| Step | Task | Output |
| --- | --- | --- |
| 1 | Create `accounts` app with `User(AbstractUser)` | `apps/accounts/models.py`, `apps/accounts/admin.py` |
| 2 | Set `AUTH_USER_MODEL = 'accounts.User'` in settings | `config/settings.py` |
| 3 | Register all 7 apps in `INSTALLED_APPS` | `config/settings.py` |
| 4 | Install and add third-party apps (solo, ckeditor-5, adminsortable2) | `config/settings.py`, `requirements.txt` |
| 5 | Create `main/abstract_models.py` (TimeStampedModel, SEOModel, PublishableModel) | `apps/main/abstract_models.py` |
| 6 | Create SiteSettings singleton model + admin | `apps/main/models.py`, `apps/main/admin.py` |
| 7 | Create Statistic model + admin | `apps/main/models.py`, `apps/main/admin.py` |
| 8 | Configure MEDIA_URL/MEDIA_ROOT, CKEditor settings | `config/settings.py` |
| 9 | Create context processor for SiteSettings | `apps/main/context_processors.py`, `config/settings.py` |
| 10 | Set up root URL configuration with all app includes | `config/urls.py` |
| 11 | Run initial migrations | All `migrations/0001_initial.py` |
| 12 | Create superuser | — |
| 13 | Update base.html with SEO meta block + site_settings | `templates/base.html` |

**Milestone**: Admin can edit site settings; base infrastructure is in place.

### Phase 1B — Core Content Models (Priority: High)

| Step | Task | Output |
| --- | --- | --- |
| 1 | Create Subject, GradeLevel, SubjectLevel models | `apps/courses/models.py` |
| 2 | Create SubjectAdmin with SubjectLevel inline (sortable) | `apps/courses/admin.py` |
| 3 | Create Teacher, TeacherSubject, TeacherAvailability, TeacherReview models | `apps/teacher/models.py` |
| 4 | Create TeacherAdmin with all inlines, bulk actions, sortable | `apps/teacher/admin.py` |
| 5 | Create ProgramTrack model + admin | `apps/courses/models.py`, `apps/courses/admin.py` |
| 6 | Create teacher list view (with subject filtering) + URL | `apps/teacher/views.py`, `apps/teacher/urls.py` |
| 7 | Create teacher profile view + URL | `apps/teacher/views.py`, `apps/teacher/urls.py` |
| 8 | Wire teacher templates to database (replace hardcoded content) | `apps/teacher/templates/teacher/` |
| 9 | Run migrations | New migration files |
| 10 | Seed initial data: 8 subjects, 4 grade levels, ~16 subject-levels, 8 teachers, 3 program tracks | Management command or admin |

**Milestone**: Teacher listing and profile pages are fully dynamic.

### Phase 1C — Homepage & Main Content (Priority: High)

| Step | Task | Output |
| --- | --- | --- |
| 1 | Create HeroSection, Service, Partner, Testimonial models + admin | `apps/main/models.py`, `apps/main/admin.py` |
| 2 | Create HowItWorksStep, Feature models + admin | `apps/main/models.py`, `apps/main/admin.py` |
| 3 | Create PricingPackage, PackageFeature models + admin (with inline) | `apps/main/models.py`, `apps/main/admin.py` |
| 4 | Create FAQ, FAQCategory models + admin | `apps/main/models.py`, `apps/main/admin.py` |
| 5 | Create homepage view (pulling all 13+ data sources) | `apps/main/views.py` |
| 6 | Create How It Works, Pricing, FAQ views + URLs | `apps/main/views.py`, `apps/main/urls.py` |
| 7 | Wire homepage template sections to database | `apps/main/templates/main/index.html` |
| 8 | Wire How It Works, Pricing, FAQ templates | Respective template files |
| 9 | Run migrations | New migration files |
| 10 | Seed homepage content: statistics, services, partners, testimonials, steps, features, FAQ, pricing | Management command or admin |

**Milestone**: Homepage and all main pages are fully dynamic.

### Phase 1D — Blog, About & Contact (Priority: Medium)

| Step | Task | Output |
| --- | --- | --- |
| 1 | Create BlogCategory, BlogPost models + admin | `apps/blogs/models.py`, `apps/blogs/admin.py` |
| 2 | Create blog list view (category filtering, pagination, AJAX load-more) | `apps/blogs/views.py` |
| 3 | Create blog detail view (related posts) | `apps/blogs/views.py` |
| 4 | Create `_post_cards.html` partial for AJAX | `apps/blogs/templates/blogs/_post_cards.html` |
| 5 | Wire blog templates + URLs | `apps/blogs/urls.py`, template files |
| 6 | Create AboutPage singleton, TeamMember models + admin | `apps/about/models.py`, `apps/about/admin.py` |
| 7 | Create about page view + URL | `apps/about/views.py`, `apps/about/urls.py` |
| 8 | Wire about template | `apps/about/templates/about/about.html` |
| 9 | Create ContactSubmission model + admin (read-only fields) | `apps/contact/models.py`, `apps/contact/admin.py` |
| 10 | Create ContactForm with honeypot field | `apps/contact/forms.py` |
| 11 | Create contact view (form processing, validation) + URL | `apps/contact/views.py`, `apps/contact/urls.py` |
| 12 | Wire contact template | `apps/contact/templates/contact/contact.html` |
| 13 | Create StaticPage model + admin | `apps/main/models.py`, `apps/main/admin.py` |
| 14 | Create static page view for privacy/terms | `apps/main/views.py` |
| 15 | Run migrations | New migration files |
| 16 | Seed: blog categories, sample posts, about page, team members | Management command or admin |

**Milestone**: All public pages are dynamic. Content is fully admin-managed.

### Phase 1E — SEO, Polish & Production (Priority: Medium)

| Step | Task | Output |
| --- | --- | --- |
| 1 | Implement SEO meta tags in base.html (title, description, keywords, OG tags) | `templates/base.html` |
| 2 | Pass SEO context from every view | All view files |
| 3 | Admin polish: custom list displays, filters, search, fieldsets on all models | All admin files |
| 4 | Enable drag-and-drop ordering via adminsortable2 on all orderable models | All admin files |
| 5 | Configure django.contrib.sitemaps | `apps/main/sitemaps.py`, `config/urls.py` |
| 6 | Wire 404/500 templates to use site_settings context | `templates/404.html`, `templates/500.html` |
| 7 | Admin permission groups: Content Editor, Teacher Manager | Data migration or management command |
| 8 | Production settings: PostgreSQL, ALLOWED_HOSTS, SECRET_KEY from env, DEBUG=False | `config/settings.py` or split settings |
| 9 | Final data seeding validation — all frontend content migrated | — |

**Milestone**: Production-ready public website with full CMS capabilities.

## Key Technical Decisions

| Decision | Choice | Rationale | Reference |
| --- | --- | --- | --- |
| Singleton pattern | django-solo | Zero boilerplate, built-in caching, template tag | research.md #1 |
| Arabic slugs | Django built-in `slugify(allow_unicode=True)` | Zero dependencies, works perfectly | research.md #2 |
| Rich text editor | django-ckeditor-5 | First-class RTL/Arabic support, Django 6.x | research.md #3 |
| Admin ordering | django-admin-sortable2 | Drag-and-drop, works on lists and inlines | research.md #4 |
| Image handling | Django ImageField + Pillow | No thumbnail generation needed in Layer 1 | research.md #5 |
| Site settings access | Context processor + django-solo caching | Available in all templates, auto-invalidating cache | research.md #6 |
| User model | Custom `AbstractUser` in `accounts` app | Django best practice, Layer 2 readiness | research.md #7 |
| Blog pagination | Django Paginator + AJAX partial | Matches frontend load-more, SEO friendly | research.md #8 |
| Teacher rating | Admin-managed field | Independent of reviews in Layer 1 | spec.md clarifications |
| Spam protection | Honeypot field on contact form | Zero dependencies, catches automated bots | spec.md clarifications |
| New apps | Only `accounts` added | Minimal — shared abstracts in `main/abstract_models.py` | spec.md #7 |

## Risks & Mitigations

| Risk | Impact | Mitigation |
| --- | --- | --- |
| Arabic slug edge cases (mixed text, special chars) | Medium | Test with real Arabic content during seed data step; custom `clean_slug()` if needed |
| Homepage 13+ queries per request | Low (dev), Medium (prod) | django-solo caching for SiteSettings; add `select_related`/`prefetch_related` on teacher queries; database-level indexing on `order` and `status` fields |
| CKEditor 5 image uploads directory management | Low | Organize via `upload_to` functions with date/model subdirectories |
| Template conversion breaking existing JS | Medium | Incremental conversion — one section at a time; test existing accordion/carousel/navigation JS after each template change |
| Seed data mismatch with frontend | Low | Create management command that extracts content directly from template HTML analysis |
