# Tasks: Academy Backend CMS

**Input**: Design documents from `/media/eslam/work/backend/premium_academy/specs/007-academy-backend-cms/`
**Prerequisites**: [plan.md](/media/eslam/work/backend/premium_academy/specs/007-academy-backend-cms/plan.md), [spec.md](/media/eslam/work/backend/premium_academy/specs/007-academy-backend-cms/spec.md), [research.md](/media/eslam/work/backend/premium_academy/specs/007-academy-backend-cms/research.md), [data-model.md](/media/eslam/work/backend/premium_academy/specs/007-academy-backend-cms/data-model.md), [contracts/public-routes.md](/media/eslam/work/backend/premium_academy/specs/007-academy-backend-cms/contracts/public-routes.md), [contracts/page-contexts.md](/media/eslam/work/backend/premium_academy/specs/007-academy-backend-cms/contracts/page-contexts.md)

**Tests**: Include tests because the feature spec defines independent tests, acceptance scenarios, query-budget expectations, and end-to-end form behavior that must be verified during implementation.

**Organization**: Tasks are grouped by user story so each story can be implemented, verified, and demoed independently once the foundational phase is complete.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (`US1` ... `US7`)
- Every task includes an exact file path or target directory

## Path Conventions

- Django project root: `manage.py`, `config/`, `apps/`
- App code lives in `apps/about/`, `apps/blogs/`, `apps/contact/`, `apps/course/`, `apps/main/`, `apps/price/`, and `apps/teacher/`
- New tests should use per-app test packages such as `apps/main/tests/`

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Prepare the Django project skeleton for multi-app CMS work.

- [X] T001 Configure installed apps, template directories, media settings, and the shared site-settings context processor in `config/settings.py`
- [X] T002 Wire root routing and create placeholder domain URL modules in `config/urls.py`, `apps/main/urls.py`, `apps/about/urls.py`, `apps/teacher/urls.py`, `apps/blogs/urls.py`, `apps/contact/urls.py`, and `apps/price/urls.py`
- [X] T003 [P] Create per-app test packages in `apps/main/tests/__init__.py`, `apps/about/tests/__init__.py`, `apps/teacher/tests/__init__.py`, `apps/blogs/tests/__init__.py`, `apps/contact/tests/__init__.py`, and `apps/price/tests/__init__.py`
- [X] T004 [P] Add shared admin/view utility stubs for singleton handling and site-settings loading in `apps/main/admin.py` and `apps/main/context_processors.py`

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core shared models and infrastructure that block all page-specific stories.

**⚠️ CRITICAL**: No user story work should begin until this phase is complete.

- [X] T005 Implement shared global content models in `apps/main/models.py` for `SiteSettings`, `SocialLink`, `Partner`, `Testimonial`, `FAQ`, `CTABlock`, `PageMeta`, `RelatedLink`, and `LegalPage`
- [X] T006 Implement the `Subject` catalog model and admin registration in `apps/course/models.py` and `apps/course/admin.py`
- [X] T007 Register shared admin configurations, singleton admins, list filters, and inline support for foundational models in `apps/main/admin.py`
- [X] T008 Implement the shared site-settings context processor and base queryset helpers in `apps/main/context_processors.py`
- [X] T009 Generate and apply foundational migrations in `apps/main/migrations/`, `apps/course/migrations/`, and `db.sqlite3`
- [X] T010 [P] Create foundational admin and context-processor tests in `apps/main/tests/test_foundations.py` and `apps/course/tests/test_foundations.py`
- [X] T011 [P] Seed minimal shared records for development bootstrap in `apps/main/migrations/` and `apps/course/migrations/`

**Checkpoint**: Foundation ready. User stories can now proceed in priority order, with some later stories parallelizable by app ownership.

---

## Phase 3: User Story 1 - Admin Manages Homepage Content (Priority: P1) 🎯 MVP

**Goal**: Make every homepage section admin-manageable without changing the locked homepage layout.

**Independent Test**: An admin edits the homepage hero and FAQ ordering in Django admin, refreshes `/`, and sees the updated homepage content immediately with the featured teachers and targeted testimonials still rendering correctly.

### Tests for User Story 1

- [X] T012 [P] [US1] Add homepage model, admin, and query-budget tests in `apps/main/tests/test_homepage.py`
- [X] T013 [P] [US1] Add homepage integration smoke coverage for shared footer/header context in `apps/main/tests/test_homepage.py`

### Implementation for User Story 1

- [X] T014 [US1] Implement homepage-specific models in `apps/main/models.py` for `HeroSection`, `TrustStat`, `EducationalService`, `ServiceFeature`, `FeatureBlock`, `FeaturePoint`, `FeatureTab`, `FeatureTabPoint`, `ProcessStep`, and `AppPromoSection`
- [X] T015 [US1] Register homepage admins and nested inline editing in `apps/main/admin.py`
- [X] T016 [US1] Generate homepage migrations in `apps/main/migrations/`
- [X] T017 [US1] Implement the homepage view and homepage route in `apps/main/views.py` and `apps/main/urls.py`
- [X] T018 [US1] Replace hardcoded homepage content with dynamic template bindings in `apps/main/templates/index.html`
- [X] T019 [US1] Add homepage seed data matching the current frontend in `apps/main/migrations/`
- [X] T020 [US1] Run homepage end-to-end validation against the MVP acceptance scenarios in `apps/main/tests/test_homepage.py`

**Checkpoint**: User Story 1 is complete when the homepage is fully dynamic and independently testable as the MVP slice.

---

## Phase 4: User Story 2 - Admin Manages Teachers (Priority: P1)

**Goal**: Make the teachers listing and teacher profile pages fully driven by admin-managed teacher data.

**Independent Test**: An admin creates a new active featured teacher with reviews, availability, and specializations, and the teacher appears on `/teachers/`, `/teachers/<slug>/`, and the homepage showcase.

### Tests for User Story 2

- [X] T021 [P] [US2] Add teacher listing, teacher detail, and subject-filter tests in `apps/teacher/tests/test_teacher_pages.py`
- [X] T022 [P] [US2] Add admin tests for teacher inlines and slug generation in `apps/teacher/tests/test_teacher_admin.py`

### Implementation for User Story 2

- [X] T023 [US2] Implement teacher domain models in `apps/teacher/models.py` for `TeacherPageSettings`, `TeacherStat`, `Teacher`, `TeacherFeature`, `TeacherSpecialization`, `TeacherReview`, and `TeacherAvailability`
- [X] T024 [US2] Register teacher admin screens, list displays, and inline editing in `apps/teacher/admin.py`
- [X] T025 [US2] Generate teacher migrations in `apps/teacher/migrations/`
- [X] T026 [US2] Implement teacher listing and teacher detail views plus filtering in `apps/teacher/views.py` and `apps/teacher/urls.py`
- [X] T027 [US2] Replace hardcoded listing-page content with template variables in `apps/teacher/templates/teachers.html`
- [X] T028 [US2] Replace hardcoded profile-page content with template variables in `apps/teacher/templates/teacher-profile.html`
- [X] T029 [US2] Add teacher seed data that preserves the current frontend cards and profile content in `apps/teacher/migrations/`

**Checkpoint**: User Story 2 is complete when teacher management works independently and integrates cleanly with the homepage featured-teacher query.

---

## Phase 5: User Story 3 - Admin Publishes Blog Posts (Priority: P2)

**Goal**: Deliver a publish/draft blog workflow with category filtering and related posts.

**Independent Test**: An admin publishes one post and leaves another in draft; the published post appears on `/blog/` and `/blog/<slug>/`, while the draft stays hidden from public routes.

### Tests for User Story 3

- [X] T030 [P] [US3] Add blog listing, detail, category-filter, and draft-visibility tests in `apps/blogs/tests/test_blog_pages.py`
- [X] T031 [P] [US3] Add blog admin and slug/meta tests in `apps/blogs/tests/test_blog_admin.py`

### Implementation for User Story 3

- [X] T032 [US3] Implement blog models in `apps/blogs/models.py` for `BlogPageSettings`, `Category`, `Author`, and `BlogPost`
- [X] T033 [US3] Register blog admin workflows for status, featured posts, authors, and categories in `apps/blogs/admin.py`
- [X] T034 [US3] Generate blog migrations in `apps/blogs/migrations/`
- [X] T035 [US3] Implement blog listing and detail views with related-post queries in `apps/blogs/views.py` and `apps/blogs/urls.py`
- [X] T036 [US3] Replace hardcoded blog listing content with dynamic bindings in `apps/blogs/templates/blog.html`
- [X] T037 [US3] Replace hardcoded blog detail content with dynamic bindings in `apps/blogs/templates/blog-post.html`
- [X] T038 [US3] Add blog seed data that matches the current frontend categories and featured article content in `apps/blogs/migrations/`

**Checkpoint**: User Story 3 is complete when the blog can be managed independently with publish/draft behavior and category filtering.

---

## Phase 6: User Story 4 - Admin Manages Pricing Plans (Priority: P2)

**Goal**: Make pricing plans, comparison rows, and pricing FAQs editable in admin while preserving the pricing page layout.

**Independent Test**: An admin changes a plan price and popular flag in admin, refreshes `/pricing/`, and sees the updated pricing cards and comparison table immediately.

### Tests for User Story 4

- [X] T039 [P] [US4] Add pricing page rendering and comparison-table tests in `apps/price/tests/test_pricing_page.py`
- [X] T040 [P] [US4] Add pricing admin inline and validation tests in `apps/price/tests/test_pricing_admin.py`

### Implementation for User Story 4

- [X] T041 [US4] Implement pricing models in `apps/price/models.py` for `PricingPageSettings`, `PricingPlan`, `PlanFeature`, `ComparisonFeature`, and `PricingFAQ`
- [X] T042 [US4] Register pricing admins and plan-feature inlines in `apps/price/admin.py`
- [X] T043 [US4] Generate pricing migrations in `apps/price/migrations/`
- [X] T044 [US4] Implement the pricing page view and route in `apps/price/views.py` and `apps/price/urls.py`
- [X] T045 [US4] Replace hardcoded pricing content with dynamic bindings in `apps/price/templates/pricing.html`
- [X] T046 [US4] Add pricing seed data that preserves the current frontend plans, comparison rows, and FAQ content in `apps/price/migrations/`

**Checkpoint**: User Story 4 is complete when pricing changes are admin-driven and independently testable on the pricing page.

---

## Phase 7: User Story 5 - Visitors Submit Contact Forms (Priority: P2)

**Goal**: Implement the contact page CMS content and a working contact submission flow stored in Django admin.

**Independent Test**: A visitor submits a valid contact form and sees a success message; staff can view the unread submission in admin, and invalid email input is rejected without saving.

### Tests for User Story 5

- [X] T047 [P] [US5] Add contact form validation, submission, and success-message tests in `apps/contact/tests/test_contact_page.py`
- [X] T048 [P] [US5] Add admin tests for read-only submission handling and `is_read` toggling in `apps/contact/tests/test_contact_admin.py`

### Implementation for User Story 5

- [X] T049 [US5] Implement contact models in `apps/contact/models.py` for `ContactSubmission`, `ContactPageSettings`, `WhyChoosePoint`, `OperatingHours`, and `ContactFAQ`
- [X] T050 [US5] Register contact admin workflows and read-only submission behavior in `apps/contact/admin.py`
- [X] T051 [US5] Implement the contact form and validation rules in `apps/contact/forms.py`
- [X] T052 [US5] Generate contact migrations in `apps/contact/migrations/`
- [X] T053 [US5] Implement the contact page view, submission handling, and route in `apps/contact/views.py` and `apps/contact/urls.py`
- [X] T054 [US5] Replace hardcoded contact-page content with dynamic bindings in `apps/contact/templates/contact.html`
- [X] T055 [US5] Add contact-page seed data and baseline inquiry choices in `apps/contact/migrations/`

**Checkpoint**: User Story 5 is complete when the contact page content and submission flow work end to end without relying on hardcoded content.

---

## Phase 8: User Story 6 - Admin Manages About & How It Works Pages (Priority: P3)

**Goal**: Make the about and how-it-works pages editable through structured admin-managed content.

**Independent Test**: An admin updates a team member and adds a new how-it-works step, then sees the changes reflected on `/about/` and `/how-it-works/` in the correct order.

### Tests for User Story 6

- [X] T056 [P] [US6] Add about-page and how-it-works page rendering tests in `apps/about/tests/test_about_pages.py`
- [X] T057 [P] [US6] Add admin tests for team, achievements, and ordered process content in `apps/about/tests/test_about_admin.py`

### Implementation for User Story 6

- [X] T058 [US6] Implement about-domain models in `apps/about/models.py` for `PageContent`, `ContentBlock`, `Statistic`, `TeamMember`, `Achievement`, `HowItWorksStep`, `WhyUsFeature`, and `ParentFeature`
- [X] T059 [US6] Register about admins, list displays, and ordering behavior in `apps/about/admin.py`
- [X] T060 [US6] Generate about migrations in `apps/about/migrations/`
- [X] T061 [US6] Implement about and how-it-works views plus routes in `apps/about/views.py` and `apps/about/urls.py`
- [X] T062 [US6] Replace hardcoded about-page content with dynamic bindings in `apps/about/templates/about.html`
- [X] T063 [US6] Replace hardcoded how-it-works content with dynamic bindings in `apps/about/templates/how-it-works.html`
- [X] T064 [US6] Add about-page and how-it-works seed data that preserves current frontend content in `apps/about/migrations/`

**Checkpoint**: User Story 6 is complete when both informational pages are fully CMS-managed and independently testable.

---

## Phase 9: User Story 7 - Admin Manages FAQs Across Pages (Priority: P3)

**Goal**: Deliver the dedicated FAQ page and the shared FAQ management workflow across homepage and FAQ page surfaces.

**Independent Test**: An admin creates an FAQ with `show_on_homepage=True`, then confirms it appears on `/faq/` and on the homepage FAQ section with correct category grouping/filtering.

### Tests for User Story 7

- [X] T065 [P] [US7] Add FAQ page rendering, category grouping, and homepage-visibility tests in `apps/main/tests/test_faq_page.py`
- [X] T066 [P] [US7] Add FAQ admin filter and ordering tests in `apps/main/tests/test_faq_admin.py`

### Implementation for User Story 7

- [X] T067 [US7] Implement the FAQ page view and related-link query logic in `apps/main/views.py` and `apps/main/urls.py`
- [X] T068 [US7] Create the Django FAQ template from the locked frontend contract in `apps/main/templates/faq.html`
- [X] T069 [US7] Finalize FAQ admin workflow, category choices, and homepage visibility behavior in `apps/main/admin.py`
- [X] T070 [US7] Add FAQ page seed data and related links matching the current frontend in `apps/main/migrations/`

**Checkpoint**: User Story 7 is complete when shared FAQs are manageable in admin and the dedicated FAQ page works without breaking homepage FAQ behavior.

---

## Phase 10: Polish & Cross-Cutting Concerns

**Purpose**: Complete shared concerns that span multiple stories and harden the CMS for acceptance.

- [X] T071 [P] Add legal-page rendering and page-meta plumbing for `/privacy/` and `/terms/` in `apps/main/views.py`, `apps/main/urls.py`, `apps/main/templates/privacy.html`, and `apps/main/templates/terms.html`
- [X] T072 [P] Add cross-page query-count, slug-route, and shared-context regression tests in `apps/main/tests/test_sitewide_queries.py`, `apps/teacher/tests/test_teacher_pages.py`, and `apps/blogs/tests/test_blog_pages.py`
- [X] T073 Implement final base-template integration for SEO metadata, shared navigation, and footer data in `apps/templates/base.html`
- [X] T074 Create a consolidated initial-content seeding pass for all remaining frontend content in `apps/main/migrations/`, `apps/about/migrations/`, `apps/blogs/migrations/`, `apps/contact/migrations/`, `apps/price/migrations/`, and `apps/teacher/migrations/`
- [X] T075 Run the full quickstart validation workflow and document any implementation gaps in `specs/007-academy-backend-cms/quickstart.md`

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies; start immediately.
- **Foundational (Phase 2)**: Depends on Setup; blocks all story work.
- **User Stories (Phases 3-9)**: Depend on Foundational completion.
- **Polish (Phase 10)**: Depends on all desired user stories being complete.

### User Story Dependencies

- **US1 (P1)**: Starts immediately after Phase 2 and defines the MVP.
- **US2 (P1)**: Starts after Phase 2; integrates with US1 through homepage featured-teacher rendering.
- **US3 (P2)**: Starts after Phase 2; independent of US1/US2 except for shared site settings and CTA blocks.
- **US4 (P2)**: Starts after Phase 2; independent of US1/US2 except for shared site settings and CTA blocks.
- **US5 (P2)**: Starts after Phase 2; independent of US1-US4 except for shared site settings and CTA blocks.
- **US6 (P3)**: Starts after Phase 2; independent of US1-US5 except for shared site settings, partners, testimonials, and CTA blocks.
- **US7 (P3)**: Starts after Phase 2 but functionally depends on US1 because homepage FAQ rendering is verified there.

### Within Each User Story

- Tests are written before implementation and should fail before feature code is added.
- Models and migrations come before admin/view/template integration.
- Views and routes come before template conversion.
- Seed data follows structure changes so the page can be visually verified against the locked frontend.

### Parallel Opportunities

- `T003` and `T004` can run in parallel during setup.
- `T010` and `T011` can run in parallel once foundational models are in place.
- After Phase 2, US3, US4, US5, and US6 can be worked on in parallel by separate owners.
- Within each story, the test tasks marked `[P]` can run together before implementation.

---

## Parallel Example: User Story 2

```bash
# Launch teacher-page test tasks together:
Task: "Add teacher listing, teacher detail, and subject-filter tests in apps/teacher/tests/test_teacher_pages.py"
Task: "Add admin tests for teacher inlines and slug generation in apps/teacher/tests/test_teacher_admin.py"
```

---

## Parallel Example: User Story 5

```bash
# Launch contact-page validation and admin coverage together:
Task: "Add contact form validation, submission, and success-message tests in apps/contact/tests/test_contact_page.py"
Task: "Add admin tests for read-only submission handling and is_read toggling in apps/contact/tests/test_contact_admin.py"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational
3. Complete Phase 3: User Story 1
4. Validate homepage admin editing, FAQ ordering, and shared site settings
5. Demo the MVP before expanding into additional pages

### Incremental Delivery

1. Complete Setup + Foundational once
2. Deliver US1 and validate the homepage CMS
3. Deliver US2 to unlock teacher-driven conversion pages
4. Deliver US3, US4, and US5 as independent P2 increments
5. Finish US6 and US7, then complete legal/SEO/query-budget polish

### Parallel Team Strategy

With multiple developers after Phase 2:

1. Developer A owns `apps/main/` homepage and FAQ work
2. Developer B owns `apps/teacher/`
3. Developer C owns `apps/blogs/` and `apps/price/`
4. Developer D owns `apps/contact/` and `apps/about/`

---

## Notes

- All tasks follow the required checklist format with IDs, optional `[P]`, optional story labels, and explicit paths.
- Migrations are intentionally called out as separate tasks so model changes are not left unapplied.
- Seed-data tasks are included because the acceptance criteria require the current hardcoded frontend content to be migrated into database records.