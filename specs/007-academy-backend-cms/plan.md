# Implementation Plan: Academy Backend CMS

**Branch**: `007-academy-backend-cms` | **Date**: 2026-04-02 | **Spec**: [/media/eslam/work/backend/premium_academy/specs/007-academy-backend-cms/spec.md](/media/eslam/work/backend/premium_academy/specs/007-academy-backend-cms/spec.md)
**Input**: Feature specification from `/media/eslam/work/backend/premium_academy/specs/007-academy-backend-cms/spec.md`

## Summary

Convert the existing static Sana Academy Django templates into a fully admin-managed CMS across the existing domain apps. The implementation will use normalized Django models, singleton settings models, inline-admin editing for owned child records, slug-based public routes, a shared site-settings context processor, and query plans that preserve the locked Arabic RTL frontend while eliminating hardcoded section content.

## Technical Context

**Language/Version**: Python 3.12, Django 6.0.3
**Primary Dependencies**: Django admin, ORM, forms, template engine, messages framework; Pillow for `ImageField` support
**Storage**: SQLite3 database for development, Django default media storage for uploaded assets
**Testing**: Django `TestCase` via `python manage.py test`, form validation tests, model/admin smoke tests, query-count assertions for key public views
**Target Platform**: Linux-hosted server-rendered Django application consumed in desktop and mobile browsers
**Project Type**: Django CMS-style web application
**Performance Goals**: Major public pages stay at or under 5 ORM queries where specified in the spec; admin edits become visible after one page refresh; contact submissions persist synchronously on submit
**Constraints**: Existing frontend templates are locked presentation contracts; Arabic/RTL output must remain intact; no supported section may remain hardcoded; slug URLs must resolve for teachers and blog posts; N+1 queries must be prevented with `select_related` and `prefetch_related`
**Scale/Scope**: 7 domain apps, roughly 40 content models including singleton and inline-owned models, 12 public pages, 100+ rendered sections, seeded initial content matching the current frontend

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- PASS: The plan preserves the locked frontend templates instead of redesigning them.
- PASS: Arabic-first and RTL-first presentation rules remain satisfied because backend work feeds existing Arabic templates rather than replacing them.
- PASS: Section richness and trust-heavy content depth are preserved by mapping every page section to admin-managed data sources.
- PASS: Shared settings, CTA blocks, testimonials, and FAQs are centralized so site-wide consistency can be maintained without template drift.
- Verification required during implementation: manual RTL/template smoke review plus query-budget tests on homepage, teachers, blog, pricing, contact, and FAQ pages.

Post-design re-check:

- PASS: The data model covers all page sections called out in the spec.
- PASS: The route and template-context contracts preserve the current page surface without introducing API-first divergence.
- PASS: The implementation structure fits the existing Django project and does not conflict with constitution constraints.

## Project Structure

### Documentation (this feature)

```text
specs/007-academy-backend-cms/
├── plan.md
├── research.md
├── data-model.md
├── quickstart.md
├── contracts/
│   ├── page-contexts.md
│   └── public-routes.md
└── tasks.md
```

### Source Code (repository root)

```text
manage.py
config/
├── settings.py
├── urls.py
├── asgi.py
└── wsgi.py

apps/
├── about/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── templates/
│   ├── tests.py
│   └── views.py
├── blogs/
├── contact/
├── course/
├── main/
├── price/
├── teacher/
└── templates/
    ├── 404.html
    ├── 500.html
    └── base.html

frontend/
├── *.html
├── css/
├── js/
└── assets/

specs/
└── 007-academy-backend-cms/
```

**Structure Decision**: Keep the current monolithic Django project rooted at the repository, implement feature work inside the existing `apps/*` packages, and treat `frontend/` plus the existing app templates as locked UI reference material. No new `backend/src` split is needed because the repo is already a Django application with domain-oriented apps.

## Phase 0 Research Focus

- Confirm the concrete backend stack, persistence choice, and testing approach from the existing repo baseline.
- Resolve model-pattern decisions that are implicit in the spec: singleton handling, shared base fields, slug generation, safe foreign-key deletion policy, and media handling.
- Define how client-side FAQ/category filtering and page-level query budgets will work without introducing a separate API surface.
- Decide the minimum rich-text strategy that supports legal pages, blog content, and long-form content blocks without expanding scope into a full editorial platform.

## Phase 1 Design Focus

- Normalize the spec into app-bounded model groups with explicit ownership and cross-app relationships.
- Document the public route contract and the template-context contract so implementation can preserve the locked templates.
- Define implementation sequencing around shared primitives first: site settings, subjects, CTA blocks, partners, testimonials, FAQs, and singleton page settings.
- Establish quickstart steps that cover migrations, admin bootstrap, media configuration, initial seeding, and smoke verification.

## Complexity Tracking

No constitution violations are currently required by this design.
