# Research: Academy Backend CMS

## Decision 1: Build on the existing Django monolith and keep domain boundaries at the app level

**Decision**: Use the current `config/` Django project plus the existing `apps/about`, `apps/blogs`, `apps/contact`, `apps/course`, `apps/main`, `apps/price`, and `apps/teacher` packages as the implementation boundary.

**Rationale**: The repository already contains the target app layout and locked templates inside those apps. Preserving that structure minimizes routing churn, keeps template ownership aligned with the current frontend mapping, and avoids introducing an unnecessary service split for a server-rendered CMS.

**Alternatives considered**:
- Introduce a new `backend/src` layout: rejected because it conflicts with the current repo shape and creates avoidable migration overhead.
- Collapse everything into a single content app: rejected because the feature spec is explicitly organized by domain app responsibility.

## Decision 2: Use normalized shared model patterns rather than one-off page models everywhere

**Decision**: Standardize on a few repeatable patterns:
- singleton models for page/global settings
- ordered collection models for grids and lists
- inline-owned child models for features, reviews, availability, and comparison rows
- reusable slug-identified blocks for CTA, feature, content, legal, and page-meta records

**Rationale**: The frontend has many repeated section types across pages. Reusable patterns reduce admin inconsistency, keep query logic predictable, and lower migration complexity while still preserving each section's content contract.

**Alternatives considered**:
- A fully generic CMS schema with polymorphic content blocks: rejected because it would make the locked templates harder to feed predictably.
- Separate bespoke models for every section: rejected because it would duplicate behavior and increase admin/configuration cost without adding user value.

## Decision 3: Keep rich text simple for Phase 1

**Decision**: Model long-form content with `TextField` and use Django admin widgets initially, leaving richer editor integration as a follow-up if content-authoring needs exceed plain multiline editing.

**Rationale**: The repo does not yet define an editorial package or dependency manifest beyond stock Django. The immediate requirement is to make existing content manageable, not to launch a WYSIWYG-heavy publishing platform. `TextField` satisfies legal pages, blog bodies, teacher bios, FAQ answers, and about-page narrative content without adding integration risk.

**Alternatives considered**:
- Add Wagtail or a full CMS package: rejected as out of scope and structurally invasive.
- Add CKEditor/TinyMCE immediately: deferred because it adds dependency and sanitization decisions before the basic CMS surface exists.

## Decision 4: Use Django default media handling now, but keep storage swappable

**Decision**: Configure local media upload support for development and keep all image fields on standard `ImageField`/file storage abstractions.

**Rationale**: The feature explicitly needs admin-managed logos, photos, hero imagery, and badges. Django's default storage is enough for the current implementation phase and can later be swapped to S3-compatible storage without changing model contracts.

**Alternatives considered**:
- Hardcode static asset paths only: rejected because it fails the admin-manageable requirement.
- Introduce cloud storage immediately: rejected because deployment infrastructure is not part of this feature.

## Decision 5: Enforce query budgets with context shaping, not a new API layer

**Decision**: Keep the application server-rendered and meet the page contracts with carefully composed querysets using `select_related`, `prefetch_related`, and a shared `site_settings` context processor.

**Rationale**: The locked frontend already exists as Django templates. A JSON API would add a second contract and more moving parts without helping the immediate objective. Query shaping directly in views keeps the implementation aligned with the templates while satisfying the spec's query-count goal.

**Alternatives considered**:
- Build REST endpoints and have templates call them: rejected as unnecessary architectural expansion.
- Accept naive ORM access in templates: rejected because it would break the query-budget success criteria.

## Decision 6: Favor `PROTECT` for cross-domain content references and `CASCADE` only for owned child rows

**Decision**: Use `PROTECT` where deleting a referenced parent would silently break visible content, such as `Teacher.primary_subject` and similar cross-domain links. Use `CASCADE` only for tightly owned rows like plan features, service features, reviews, and availability records.

**Rationale**: The frontend preservation rule makes accidental content loss especially costly. This split protects public content integrity while keeping inline-owned child cleanup automatic and predictable.

**Alternatives considered**:
- Broad `CASCADE`: rejected because it risks deleting visible site content unexpectedly.
- Broad `SET_NULL`: rejected because many templates depend on required relationships and would need extra null-fallback logic.

## Decision 7: Implement filtering at the page level with server-rendered data and light client behavior

**Decision**: Blog category filtering and teacher subject filtering remain queryset-driven, while FAQ page category selection/search stays client-side over server-rendered FAQ data.

**Rationale**: That matches the current frontend behavior, avoids live-search backend complexity, and keeps the FAQ page fast and resilient without additional endpoints.

**Alternatives considered**:
- Server round-trips for each FAQ filter/search interaction: rejected as unnecessary for static-size content.
- Pure client-side data blobs for every page: rejected because core page content still needs normal server-rendered SEO and slug routing.
