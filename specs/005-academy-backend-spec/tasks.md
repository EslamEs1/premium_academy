# Tasks: Academy Backend — Django Data Layer & CMS

**Input**: Design documents from `/specs/005-academy-backend-spec/`
**Prerequisites**: plan.md, spec.md, research.md, data-model.md, quickstart.md

**Tests**: Not explicitly requested in feature specification. Test tasks omitted.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- Django apps: `apps/<app_name>/`
- Config: `config/`
- Root templates: `templates/`
- App templates: `apps/<app_name>/templates/<app_name>/`

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Install dependencies, create accounts app, register apps, configure settings

- [ ] T001 Install Python dependencies: `pip install django-solo django-ckeditor-5 django-admin-sortable2 Pillow` and update requirements file
- [ ] T002 Create `accounts` app directory structure at `apps/accounts/` with `__init__.py`, `apps.py`, `models.py`, `admin.py`, `migrations/__init__.py`
- [ ] T003 Implement minimal custom User model extending `AbstractUser` in `apps/accounts/models.py`
- [ ] T004 Register User with `UserAdmin` in `apps/accounts/admin.py`
- [ ] T005 Configure `AccountsConfig` in `apps/accounts/apps.py` with `name = 'apps.accounts'` and `default_auto_field`
- [ ] T006 Update `config/settings.py`: add `AUTH_USER_MODEL = 'accounts.User'`, register all 7 apps and 3 third-party apps in `INSTALLED_APPS`, configure `MEDIA_URL`, `MEDIA_ROOT`, `SOLO_CACHE`, `SOLO_CACHE_TIMEOUT`, and `CKEDITOR_5_CONFIGS` with Arabic RTL content language
- [ ] T007 [P] Update `config/settings.py` TEMPLATES setting to include `apps` directory and add `'apps.main.context_processors.site_settings'` to context processors
- [ ] T008 [P] Add `.gitignore` entry for `media/` directory if not already present

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Abstract models, site settings, URL routing, migrations — MUST be complete before ANY user story

**CRITICAL**: No user story work can begin until this phase is complete

- [ ] T009 Create abstract base models `TimeStampedModel`, `SEOModel`, `PublishableModel` with custom `PublishedManager` in `apps/main/abstract_models.py`
- [ ] T010 Create `SiteSettings` singleton model (inheriting `SingletonModel` from django-solo) with all fields (site_name, contact info, social URLs, app store URLs, footer text) in `apps/main/models.py`
- [ ] T011 Register `SiteSettings` with `SingletonModelAdmin` in `apps/main/admin.py` with fieldsets (General, Contact, Social, App Links, Footer)
- [ ] T012 Create context processor function `site_settings` returning `SiteSettings.get_solo()` in `apps/main/context_processors.py`
- [ ] T013 Create `Statistic` model (label, value, icon, description, order) in `apps/main/models.py`
- [ ] T014 Register `Statistic` with `SortableAdminMixin` in `apps/main/admin.py` with list_display and search
- [ ] T015 Set up root URL configuration in `config/urls.py`: include all app URL modules (`apps.main.urls`, `apps.teacher.urls`, `apps.blogs.urls`, `apps.about.urls`, `apps.contact.urls`), admin, ckeditor5 URLs, and media serving in DEBUG mode
- [ ] T016 Create empty `urls.py` files with app_name in each app: `apps/main/urls.py`, `apps/teacher/urls.py`, `apps/blogs/urls.py`, `apps/about/urls.py`, `apps/contact/urls.py`
- [ ] T017 Run `python manage.py makemigrations accounts` then `python manage.py makemigrations main` then `python manage.py migrate`
- [ ] T018 Update `templates/base.html`: add SEO meta block (`{% block meta_title %}`, `{% block meta_description %}`, OG tags) and replace hardcoded site name/contact/social links with `{{ site_settings.field }}` template variables
- [ ] T019 Customize Django admin site: set `admin.site.site_header`, `admin.site.site_title`, `admin.site.index_title` to "SanaAcademy Admin" in `apps/main/admin.py`

**Checkpoint**: Foundation ready — admin can edit site settings, base.html shows dynamic data, all apps registered, migrations applied

---

## Phase 3: User Story 1 — Admin Manages Website Content (Priority: P1) MVP

**Goal**: Admin can manage all homepage content sections through Django admin; changes appear immediately on the public homepage

**Independent Test**: Admin logs in, edits SiteSettings phone number, saves, and sees updated phone on homepage footer. Admin creates a Testimonial with status=published and it appears on the homepage.

### Implementation for User Story 1

- [ ] T020 [P] [US1] Create `HeroSection` model (title, subtitle, CTAs, image, social_proof_text; inherits TimeStampedModel, PublishableModel) in `apps/main/models.py`
- [ ] T021 [P] [US1] Create `Service` model (title, subtitle, description, image, icon, features; inherits TimeStampedModel, PublishableModel) in `apps/main/models.py`
- [ ] T022 [P] [US1] Create `Partner` model (name, logo, url, order, is_active; inherits TimeStampedModel) in `apps/main/models.py`
- [ ] T023 [P] [US1] Create `Testimonial` model (student_name, subject, grade_level, title, content, rating, image, testimonial_type; inherits TimeStampedModel, PublishableModel) in `apps/main/models.py`
- [ ] T024 [P] [US1] Create `HowItWorksStep` model (step_number unique, title, description, icon; inherits TimeStampedModel) in `apps/main/models.py`
- [ ] T025 [P] [US1] Create `Feature` model (title, description, icon, order, page choices; inherits TimeStampedModel) in `apps/main/models.py`
- [ ] T026 [US1] Register all Phase 3 models in `apps/main/admin.py`: HeroSectionAdmin, ServiceAdmin, PartnerAdmin, TestimonialAdmin, HowItWorksStepAdmin, FeatureAdmin — each with `SortableAdminMixin`, appropriate list_display, list_filter, search_fields
- [ ] T027 [US1] Create `Subject` model (name unique, slug allow_unicode, icon, description, order, is_active; inherits TimeStampedModel) in `apps/courses/models.py`
- [ ] T028 [P] [US1] Create `GradeLevel` model (name unique, slug, order; inherits TimeStampedModel) in `apps/courses/models.py`
- [ ] T029 [P] [US1] Create `SubjectLevel` through model (subject FK, grade_level FK, description; unique_together) in `apps/courses/models.py`
- [ ] T030 [US1] Create `ProgramTrack` model (name, slug, subtitle, description, image, features, cta_text, cta_url; inherits TimeStampedModel, PublishableModel, SEOModel) in `apps/courses/models.py`
- [ ] T031 [US1] Register courses models in `apps/courses/admin.py`: SubjectAdmin with SubjectLevel inline (SortableTabularInline), GradeLevelAdmin, ProgramTrackAdmin — each with SortableAdminMixin
- [ ] T032 [US1] Run `python manage.py makemigrations main courses` then `python manage.py migrate`
- [ ] T033 [US1] Create homepage view in `apps/main/views.py`: query HeroSection (first published), Statistics, Services, Partners, FeaturedTeachers, ProgramTracks, Subjects+SubjectLevels, Testimonials (limit 4), HowItWorksSteps, FAQs (homepage, limit 10) — pass all to context
- [ ] T034 [US1] Add URL pattern for homepage (`/`) in `apps/main/urls.py`
- [ ] T035 [US1] Wire `apps/main/templates/main/index.html`: replace all hardcoded homepage content with Django template tags (`{% for %}`, `{{ }}`) for hero, stats, services, partners, teachers, programs, subjects, testimonials, how-it-works, FAQ sections
- [ ] T036 [US1] Create data seeding management command `apps/main/management/commands/seed_homepage.py`: populate Statistics (6), Services (3), Partners (8), Testimonials (4), HowItWorksSteps (6), Features, Subjects (8), GradeLevels (4), SubjectLevels (~16), ProgramTracks (3) from current frontend content

**Checkpoint**: Homepage is fully dynamic — admin can edit every section via Django admin and see changes on the public site

---

## Phase 4: User Story 2 — Visitor Browses Teachers and Views Profile (Priority: P1)

**Goal**: Visitors can browse teachers with subject filtering, view full teacher profiles with bio, credentials, availability, and reviews

**Independent Test**: Visit `/teachers/`, click "Mathematics" filter, see only math teachers. Click a teacher card, see full profile at `/teachers/<slug>/` with bio, availability, and reviews.

### Implementation for User Story 2

- [ ] T037 [P] [US2] Create `Teacher` model (name, title, slug allow_unicode, initials, bio, image, years_of_experience, rating manual decimal, student_count, total_sessions, education, teaching_approach, grade_levels, session_rate_min, availability_notes; inherits TimeStampedModel, PublishableModel, SEOModel) in `apps/teacher/models.py`
- [ ] T038 [P] [US2] Create `TeacherSubject` through model (teacher FK, subject FK, is_primary; unique_together) in `apps/teacher/models.py`
- [ ] T039 [P] [US2] Create `TeacherAvailability` model (teacher FK, day_of_week choices Saturday-Thursday, start_time, end_time; unique_together; inherits TimeStampedModel) in `apps/teacher/models.py`
- [ ] T040 [P] [US2] Create `TeacherReview` model (teacher FK, reviewer_name, rating 1-5, content, review_date auto; inherits TimeStampedModel, PublishableModel) in `apps/teacher/models.py`
- [ ] T041 [US2] Add M2M relationship `subjects = ManyToManyField(Subject, through='TeacherSubject')` on Teacher model and auto-slug generation in `save()` method in `apps/teacher/models.py`
- [ ] T042 [US2] Register Teacher in `apps/teacher/admin.py`: TeacherAdmin with SortableAdminMixin, TeacherSubject TabularInline, TeacherAvailability TabularInline, TeacherReview StackedInline; list_display (name, primary subject, status, rating, student_count), list_filter (status, is_featured, subjects), search_fields (name), fieldsets (Profile, Credentials, Statistics, Availability, SEO), bulk actions (publish, unpublish, feature, unfeature)
- [ ] T043 [US2] Run `python manage.py makemigrations teacher` then `python manage.py migrate`
- [ ] T044 [US2] Create teacher list view in `apps/teacher/views.py`: query published Teachers, filter by subject slug from GET param, get all active Subjects for filter tabs, pass statistics (total teachers, avg rating, total sessions)
- [ ] T045 [US2] Create teacher profile view in `apps/teacher/views.py`: get Teacher by slug (published only, 404 otherwise), prefetch subjects, availability, published reviews ordered by review_date desc
- [ ] T046 [US2] Add URL patterns in `apps/teacher/urls.py`: `/teachers/` (list), `/teachers/<slug:slug>/` (profile)
- [ ] T047 [US2] Wire `apps/teacher/templates/teacher/teachers.html`: replace hardcoded teacher cards with `{% for teacher in teachers %}` loop, replace filter tabs with dynamic Subject list, replace statistics bar with context data
- [ ] T048 [US2] Wire `apps/teacher/templates/teacher/teacher-profile.html`: replace hardcoded profile content with Teacher model fields — bio, education, subjects, availability table, reviews, rating, session rate, CTA links
- [ ] T049 [US2] Create data seeding management command `apps/teacher/management/commands/seed_teachers.py`: populate 8 teachers with subjects, availability, and reviews from current frontend content

**Checkpoint**: Teacher listing with filtering and full profile pages are dynamic — admin can add/edit/publish teachers

---

## Phase 5: User Story 3 + User Story 5 — Blog System (Priority: P2)

**Goal**: Visitors can browse blog articles by category with load-more, read full articles with related posts. Admin can create, categorize, and publish blog posts with rich text.

**Independent Test**: Visit `/blog/`, filter by "Study Tips", see only matching articles. Click an article, read full content with author info and 3 related posts. Admin creates a draft post (not visible), publishes it (appears on blog).

### Implementation for User Story 3 + 5

- [ ] T050 [P] [US3] Create `BlogCategory` model (name unique, slug allow_unicode, icon, order; inherits TimeStampedModel) in `apps/blogs/models.py`
- [ ] T051 [P] [US3] Create `BlogPost` model (title, slug allow_unicode, category FK nullable, author_name, author_title, author_bio, excerpt max 500, content CKEditor5Field, featured_image, read_time_minutes; inherits TimeStampedModel, PublishableModel, SEOModel) with auto-slug and auto-published_at in `apps/blogs/models.py`
- [ ] T052 [US3] Register blogs models in `apps/blogs/admin.py`: BlogCategoryAdmin with SortableAdminMixin; BlogPostAdmin with list_display (title, category, status, is_featured, published_at), list_filter (category, status, is_featured), search_fields (title, content, author_name), fieldsets (Content, Author, Publishing, SEO)
- [ ] T053 [US3] Run `python manage.py makemigrations blogs` then `python manage.py migrate`
- [ ] T054 [US3] Create blog list view in `apps/blogs/views.py`: query published BlogPosts, filter by category slug from GET param, get featured post (published + is_featured, first by order), paginate 6 per page using Django Paginator, return partial HTML for AJAX requests (X-Requested-With header check)
- [ ] T055 [US3] Create blog detail view in `apps/blogs/views.py`: get BlogPost by slug (published only, 404 otherwise), query 3 related posts (same category, exclude current, published)
- [ ] T056 [US3] Create `apps/blogs/templates/blogs/_post_cards.html` partial template: blog card markup for AJAX load-more response
- [ ] T057 [US3] Add URL patterns in `apps/blogs/urls.py`: `/blog/` (list), `/blog/<slug:slug>/` (detail)
- [ ] T058 [US3] Wire `apps/blogs/templates/blogs/blog.html`: replace hardcoded blog cards with `{% for post in page_obj %}` loop, replace category filters with dynamic BlogCategory list, add featured post section, wire load-more button to AJAX endpoint
- [ ] T059 [US3] Wire `apps/blogs/templates/blogs/blog-post.html`: replace hardcoded content with BlogPost fields — title, category, author (name, title, bio), published_at, read_time, rich text content, related posts section
- [ ] T060 [US3] Update `static/js/main.js` or create `static/js/blog-loadmore.js`: implement load-more button AJAX handler that fetches `?page=N` with XMLHttpRequest header and appends returned HTML
- [ ] T061 [US3] Create data seeding management command `apps/blogs/management/commands/seed_blog.py`: populate 4 BlogCategories and 6 sample BlogPosts from current frontend content

**Checkpoint**: Blog listing with category filtering, load-more pagination, and full article view with related posts — all admin-managed

---

## Phase 6: User Story 4 — Visitor Submits Contact Form (Priority: P2)

**Goal**: Visitors can submit a contact form with validation and honeypot spam protection; submissions are stored and manageable in admin

**Independent Test**: Fill out contact form, submit, see success message. Submit with invalid email, see validation error. Check Django admin — submission appears with status "new".

### Implementation for User Story 4

- [ ] T062 [P] [US4] Create `ContactSubmission` model (full_name, email, phone, subject choices, message, status choices, admin_notes, resolved_at; inherits TimeStampedModel) in `apps/contact/models.py`
- [ ] T063 [P] [US4] Create `ContactForm` Django form class with honeypot field, Saudi phone validation, and all form fields (full_name, email, phone, subject dropdown, message) in `apps/contact/forms.py`
- [ ] T064 [US4] Register ContactSubmission in `apps/contact/admin.py`: list_display (full_name, email, subject, status, created_at), list_filter (status, subject, created_at), search_fields (full_name, email, message), readonly_fields (full_name, email, phone, subject, message, created_at), editable fields (status, admin_notes)
- [ ] T065 [US4] Run `python manage.py makemigrations contact` then `python manage.py migrate`
- [ ] T066 [US4] Create contact page view in `apps/contact/views.py`: handle GET (empty form) and POST (validate form, check honeypot, save ContactSubmission, display success message), pass SiteSettings contact info to template
- [ ] T067 [US4] Add URL pattern in `apps/contact/urls.py`: `/contact/` (contact page)
- [ ] T068 [US4] Wire `apps/contact/templates/contact/contact.html`: replace hardcoded form with Django form rendering (`{{ form.as_p }}` or manual field rendering), add CSRF token, add hidden honeypot field, replace contact info sidebar with `{{ site_settings }}` fields, add success/error message display

**Checkpoint**: Contact form validates, rejects spam via honeypot, stores submissions — admin can view and manage inquiries

---

## Phase 7: User Story 6 — Visitor Views Pricing Packages (Priority: P3)

**Goal**: Visitors see admin-managed pricing packages with feature comparison on the pricing page

**Independent Test**: Visit `/pricing/`, see 3 packages with correct prices, features (included/excluded), and CTAs matching admin data.

### Implementation for User Story 6

- [ ] T069 [P] [US6] Create `PricingPackage` model (name, slug, subtitle, price, currency, unit, session_duration_minutes, description, badge_text, cta_text, cta_url; inherits TimeStampedModel, PublishableModel, SEOModel) in `apps/main/models.py`
- [ ] T070 [P] [US6] Create `PackageFeature` model (package FK, feature_text, is_included, order; inherits TimeStampedModel) in `apps/main/models.py`
- [ ] T071 [US6] Register pricing models in `apps/main/admin.py`: PricingPackageAdmin with SortableAdminMixin, PackageFeature as SortableTabularInline; list_display (name, price, status, order)
- [ ] T072 [US6] Run `python manage.py makemigrations main` then `python manage.py migrate`
- [ ] T073 [US6] Create pricing view in `apps/main/views.py`: query published PricingPackages with prefetched PackageFeatures, ordered by `order`
- [ ] T074 [US6] Add URL pattern for pricing (`/pricing/`) in `apps/main/urls.py`
- [ ] T075 [US6] Wire `apps/main/templates/main/pricing.html`: replace hardcoded package cards with `{% for package in packages %}` loop, render features with included/excluded visual indicators, display badges and CTAs from model data
- [ ] T076 [US6] Seed pricing data: 3 packages (Basic 150 SAR, Premium 200 SAR, Professional 300 SAR) with their features via `seed_homepage.py` command or separate seeder

**Checkpoint**: Pricing page shows admin-managed packages with feature comparison

---

## Phase 8: User Story 7 — Visitor Browses FAQ (Priority: P3)

**Goal**: Visitors see FAQ entries organized by category tabs with accordion expand/collapse, and homepage shows selected FAQs

**Independent Test**: Visit `/faq/`, see questions grouped by category tabs. Click a category, see only those FAQs. Visit homepage, see FAQs marked `show_on_homepage=True`.

### Implementation for User Story 7

- [ ] T077 [P] [US7] Create `FAQCategory` model (name unique, slug allow_unicode, order; inherits TimeStampedModel) in `apps/main/models.py`
- [ ] T078 [P] [US7] Create `FAQ` model (category FK nullable, question, answer, show_on_homepage; inherits TimeStampedModel, PublishableModel) in `apps/main/models.py`
- [ ] T079 [US7] Register FAQ models in `apps/main/admin.py`: FAQCategoryAdmin with SortableAdminMixin; FAQAdmin with SortableAdminMixin, list_display (question truncated, category, status, show_on_homepage), list_filter (category, status, show_on_homepage)
- [ ] T080 [US7] Run `python manage.py makemigrations main` then `python manage.py migrate`
- [ ] T081 [US7] Create FAQ page view in `apps/main/views.py`: query all FAQCategories ordered by `order`, query published FAQs grouped by category, pass active category from GET param for tab highlighting
- [ ] T082 [US7] Add URL pattern for FAQ (`/faq/`) in `apps/main/urls.py`
- [ ] T083 [US7] Wire `apps/main/templates/main/faq.html`: replace hardcoded FAQ accordion with `{% for category in categories %}` and nested `{% for faq in category.faqs %}` loops, wire category tabs to filter
- [ ] T084 [US7] Update homepage view (T033) to include FAQ query: published FAQs where `show_on_homepage=True`, limit 10, ordered by `order`
- [ ] T085 [US7] Seed FAQ data: 5 FAQCategories, 14 FAQ entries from frontend content via management command `apps/main/management/commands/seed_faq.py`

**Checkpoint**: FAQ page shows categorized questions with accordion — homepage shows selected FAQs

---

## Phase 9: About Page & Static Pages (Supporting Content)

**Purpose**: About page, team members, privacy/terms pages — supporting content not covered by primary user stories

- [ ] T086 [P] Create `AboutPage` singleton model (mission, vision, story, founding_year; inherits TimeStampedModel, SEOModel) using django-solo `SingletonModel` in `apps/about/models.py`
- [ ] T087 [P] Create `TeamMember` model (name, title, image, bio, order, is_active; inherits TimeStampedModel) in `apps/about/models.py`
- [ ] T088 Register about models in `apps/about/admin.py`: AboutPageAdmin with SingletonModelAdmin; TeamMemberAdmin with SortableAdminMixin, list_display, is_active filter
- [ ] T089 Create `StaticPage` model (slug unique, title, content CKEditor5Field, is_active; inherits TimeStampedModel, SEOModel) in `apps/main/models.py`
- [ ] T090 Register StaticPage in `apps/main/admin.py` with list_display and slug prepopulation fallback
- [ ] T091 Run `python manage.py makemigrations about main` then `python manage.py migrate`
- [ ] T092 Create about page view in `apps/about/views.py`: get AboutPage.get_solo(), query active TeamMembers ordered by `order`, query active Partners
- [ ] T093 Add URL pattern in `apps/about/urls.py`: `/about/`
- [ ] T094 Wire `apps/about/templates/about/about.html`: replace hardcoded about content with AboutPage fields (mission, vision, story), TeamMember loop, Partner loop, statistics
- [ ] T095 Create static page view in `apps/main/views.py`: get StaticPage by slug, 404 if not active
- [ ] T096 Add URL patterns for `/privacy/` and `/terms/` in `apps/main/urls.py` pointing to static page view
- [ ] T097 Wire `apps/main/templates/main/privacy.html` and `apps/main/templates/main/terms.html` (or create a generic `static_page.html` template) to render StaticPage content
- [ ] T098 Seed about data: AboutPage (mission, vision, story), 6 TeamMembers from frontend content

**Checkpoint**: About page, privacy, and terms pages are dynamic and admin-managed

---

## Phase 10: Polish & Cross-Cutting Concerns

**Purpose**: SEO, admin polish, production readiness, and final validation

- [ ] T099 Implement SEO meta tags in `templates/base.html`: `{% block meta_title %}`, `{% block meta_description %}`, `{% block meta_keywords %}`, Open Graph tags (`og:title`, `og:description`, `og:image`), with fallback to SiteSettings defaults
- [ ] T100 Pass SEO context from every view: update all views in `apps/main/views.py`, `apps/teacher/views.py`, `apps/blogs/views.py`, `apps/about/views.py`, `apps/contact/views.py` to include `meta_title`, `meta_description`, `meta_image` in template context from model SEO fields
- [ ] T101 [P] Create Django sitemap classes in `apps/main/sitemaps.py`: StaticViewSitemap (homepage, about, how-it-works, pricing, faq, contact), TeacherSitemap, BlogPostSitemap, ProgramTrackSitemap
- [ ] T102 [P] Register sitemaps in `config/urls.py` at `/sitemap.xml`
- [ ] T103 Admin polish pass: review and refine all ModelAdmin classes across all apps — ensure consistent fieldsets, list_display, list_filter, search_fields, and inline configurations match the spec requirements
- [ ] T104 [P] Create admin permission groups via data migration or management command: "Content Editor" group (blog, FAQ, testimonials, static pages) and "Teacher Manager" group (teachers, reviews, subjects) in `apps/accounts/management/commands/create_groups.py`
- [ ] T105 [P] Wire `templates/404.html` and `templates/500.html` to use `site_settings` context (custom error handlers in `config/urls.py` if needed)
- [ ] T106 Create `apps/main/views.py` how_it_works view: query HowItWorksSteps, Features (page=why_us + how_it_works + parent_features), Testimonials
- [ ] T107 Add URL pattern for `/how-it-works/` in `apps/main/urls.py`
- [ ] T108 Wire `apps/main/templates/main/how-it-works.html`: replace hardcoded content with HowItWorksStep loop, Features grouped by page type, Testimonial cards, parent features section
- [ ] T109 [P] Create production settings: split `config/settings.py` into base/dev/prod or use environment variables for `SECRET_KEY`, `DEBUG`, `ALLOWED_HOSTS`, `DATABASES` (PostgreSQL), `STATIC_ROOT`
- [ ] T110 Final validation: run all seed commands, visit every public URL, verify all 12 pages render dynamic content from database, verify admin CRUD works for all models, verify publication workflow (draft not shown, published shown, archived 404)

**Checkpoint**: Production-ready public website with full CMS capabilities, SEO, sitemaps, permission groups, and all content dynamic

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies — can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion — BLOCKS all user stories
- **US1 (Phase 3)**: Depends on Foundational — RECOMMENDED first (creates shared models: Subject, GradeLevel)
- **US2 (Phase 4)**: Depends on Foundational + Subject model from US1 (T027)
- **US3+US5 (Phase 5)**: Depends on Foundational only — no dependency on US1 or US2
- **US4 (Phase 6)**: Depends on Foundational only — no dependency on other stories
- **US6 (Phase 7)**: Depends on Foundational only — no dependency on other stories
- **US7 (Phase 8)**: Depends on Foundational only — no dependency on other stories (but homepage integration in T084 depends on US1 homepage view T033)
- **About & Static (Phase 9)**: Depends on Foundational only
- **Polish (Phase 10)**: Depends on all content phases being complete

### User Story Dependencies

- **US1 (P1)**: Start after Foundational — creates Subject/GradeLevel models that US2 needs
- **US2 (P1)**: Start after US1 completes (needs Subject model) — or start in parallel if Subject model is extracted to Foundational
- **US3+US5 (P2)**: Fully independent — can start after Foundational
- **US4 (P2)**: Fully independent — can start after Foundational
- **US6 (P3)**: Fully independent — can start after Foundational
- **US7 (P3)**: Mostly independent — homepage FAQ integration (T084) depends on US1 homepage view

### Within Each User Story

- Models before admin registration
- Admin registration before views (so data can be seeded)
- Migrations after all models in that phase
- Views before template wiring
- Seed data after views and templates

### Parallel Opportunities

- T020-T025: All US1 models can be created in parallel (different models, same file but independent sections)
- T037-T040: All US2 teacher-related models in parallel
- T050-T051: BlogCategory and BlogPost models in parallel
- T062-T063: ContactSubmission model and ContactForm in parallel
- T069-T070: PricingPackage and PackageFeature in parallel
- T077-T078: FAQCategory and FAQ in parallel
- T086-T087: AboutPage and TeamMember in parallel
- T099-T102: SEO and sitemap tasks in parallel
- US3+US5, US4, US6, US7 can all proceed in parallel after Foundational

---

## Parallel Example: User Story 2 (Teacher Browsing)

```bash
# Launch all models in parallel (T037-T040):
Task: "Create Teacher model in apps/teacher/models.py"
Task: "Create TeacherSubject through model in apps/teacher/models.py"
Task: "Create TeacherAvailability model in apps/teacher/models.py"
Task: "Create TeacherReview model in apps/teacher/models.py"

# Then sequentially:
Task: "Add M2M relationship and auto-slug on Teacher" (depends on T037-T040)
Task: "Register Teacher admin with inlines" (depends on T041)
Task: "Run migrations" (depends on T042)
Task: "Create teacher list view" (depends on T043)
Task: "Create teacher profile view" (depends on T043)

# Views and URL in parallel:
Task: "Add URL patterns" (depends on T044-T045)

# Template wiring (depends on views + URLs):
Task: "Wire teachers.html template"
Task: "Wire teacher-profile.html template"

# Seed data (depends on everything above):
Task: "Seed 8 teachers with subjects, availability, reviews"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational
3. Complete Phase 3: User Story 1 (Admin manages homepage)
4. **STOP and VALIDATE**: Admin can edit homepage content and see changes immediately
5. Deploy/demo if ready — homepage is fully dynamic

### Incremental Delivery

1. Setup + Foundational → Foundation ready
2. Add US1 (homepage CMS) → Test → **MVP!**
3. Add US2 (teachers) → Test → Teacher pages dynamic
4. Add US3+US5 (blog) + US4 (contact) → Test → Blog and contact working
5. Add US6 (pricing) + US7 (FAQ) → Test → All content pages dynamic
6. Add Phase 9 (about/static) + Phase 10 (polish) → Test → Production ready

### Parallel Team Strategy

With multiple developers after Foundational is complete:

- **Developer A**: US1 (homepage) → US2 (teachers)
- **Developer B**: US3+US5 (blog) → US6 (pricing)
- **Developer C**: US4 (contact) → US7 (FAQ) → Phase 9 (about/static)
- **All**: Phase 10 (polish) together

---

## Notes

- [P] tasks = different files or independent code sections, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- All models use `allow_unicode=True` on SlugField for Arabic slugs
- All admin classes use `SortableAdminMixin` from django-admin-sortable2 for ordering
- All publishable models use custom `PublishedManager` for frontend queries
- Rich text fields use `CKEditor5Field` configured for Arabic RTL
- Singletons (SiteSettings, AboutPage) use `SingletonModel` + `SingletonModelAdmin` from django-solo
