<!--
  Sync Impact Report
  ==================
  Version change: N/A → 1.0.0 (initial ratification)

  Principles established:
    I.   Premium Over Decorative
    II.  Conversion-First UX
    III. Clear Visual Hierarchy
    IV.  Strong Trust Signals
    V.   Mobile-First and Responsive
    VI.  SEO-Aware Frontend Structure
    VII. Accessibility and Readability

  Added sections:
    - Technology Constraints
    - Design Language & Quality Standards
    - Governance

  Removed sections: N/A (initial version)

  Templates requiring updates:
    - .specify/templates/plan-template.md       ✅ compatible (no conflicts)
    - .specify/templates/spec-template.md        ✅ compatible (no conflicts)
    - .specify/templates/tasks-template.md       ✅ compatible (no conflicts)

  Follow-up TODOs: None
-->

# Premium Academy Frontend Constitution

## Core Principles

### I. Premium Over Decorative

The interface MUST use a clean, modern, premium design language.

- Layouts MUST avoid noise, excessive gradients, childish education
  visuals, and visual clutter.
- The target aesthetic is polished, international, elegant, and light
  but confident.
- Template-looking layouts, generic Bootstrap feel, crowded card grids,
  weak spacing, overuse of shadows, over-rounded childish UI,
  inconsistent section spacing, and random typography are prohibited.
- Interactions MUST feel restrained and premium: smooth hover states,
  subtle transitions, elegant dropdowns, polished tabs/accordions/modals.
- Flashy animations and visual gimmicks are prohibited.
- Asset placeholders MUST support a premium visual concept using
  high-quality tutor/student imagery, modern education visuals, clean
  avatars, and professional icons. Cheap stock-photo feeling and
  cartoon-heavy education style are prohibited.

**Rationale**: The website represents a high-paying commercial client.
Every visual element MUST reinforce credibility and professionalism.

### II. Conversion-First UX

Every important page MUST clearly guide the user toward a business
action.

- Primary conversion goals: exploring teachers, booking a trial,
  contacting the academy, understanding the offer, trusting the
  platform.
- The homepage is a strategic conversion page: it MUST contain a
  premium hero, strong value proposition, search/CTA block, featured
  teachers, categories, how-it-works, testimonials, trust blocks,
  benefits, trial CTA, FAQ preview, and final CTA.
- Mock content MUST be realistic and premium. Lorem ipsum in important
  sections is prohibited.
- Copy MUST sound clear, confident, premium, simple, and trustworthy.
  Exaggerated marketing hype, awkward filler text, and generic low-trust
  language are prohibited.

**Rationale**: The frontend exists to convert visitors into leads and
students. UX decisions MUST serve measurable business outcomes.

### III. Clear Visual Hierarchy

The user MUST always understand where they are, what the main action is,
what the academy offers, and why they should trust it.

- Every page MUST use a consistent spacing system, consistent grid
  behavior, consistent section rhythm, and premium typography hierarchy.
- CTA styling, card systems, icon treatment, and form styling MUST be
  consistent across all pages.
- No rough, rushed, or placeholder-like sections may remain in the
  delivered frontend.

**Rationale**: Unclear hierarchy causes users to abandon pages. Visual
consistency is a trust signal and usability requirement.

### IV. Strong Trust Signals

The frontend MUST naturally support trust-building elements.

- Required trust patterns: testimonials, student counts, teacher quality
  messaging, ratings/reviews, featured categories, institution trust
  blocks, FAQ clarity, transparent process explanation.
- Teacher marketplace readiness MUST include: professional teacher
  cards, filtering/sorting layout readiness, teacher profile pages,
  ratings and review presentation, subjects/specializations display,
  pricing display, availability display, and CTA patterns such as
  "Book trial" or "View profile."

**Rationale**: Paid education services require high trust thresholds.
Social proof and transparency directly impact conversion rates.

### V. Mobile-First and Responsive

The design MUST be intentionally designed for each breakpoint, not
merely "responsive enough."

- Target breakpoints: mobile, tablet, desktop, large desktop.
- Each breakpoint MUST receive deliberate layout and interaction design.
- Mobile experience MUST include a usable mobile menu, clear filters,
  and touch-friendly interactions.

**Rationale**: A significant share of educational platform traffic
originates from mobile devices. Poor mobile UX directly reduces
conversions.

### VI. SEO-Aware Frontend Structure

Pages MUST be structured for search engine discoverability.

- Required: semantic headings, clean content sections, crawlable links,
  metadata-ready templates, scalable landing page structure.
- The information architecture MUST anticipate page families: Homepage,
  About, Teachers listing, Teacher profile, Courses/Programs listing,
  Program detail, How it works, Pricing, Trial booking, Contact, FAQ,
  Blog/Articles, Legal pages.
- Even pages not implemented immediately MUST be anticipated in the
  frontend architecture.

**Rationale**: Organic search is a primary acquisition channel for
educational platforms. SEO-hostile structure creates long-term growth
debt.

### VII. Accessibility and Readability

The frontend MUST use semantic HTML and meet baseline accessibility
standards.

- Required: semantic HTML elements, accessible contrast ratios,
  keyboard-friendly interactions where practical, readable spacing,
  readable font sizing.
- Clear states for hover, focus, active, and error MUST be implemented.

**Rationale**: Accessibility is both a legal consideration and a quality
indicator. Semantic HTML also reinforces SEO goals (Principle VI).

## Technology Constraints

The frontend implementation is strictly constrained to prevent framework
complexity.

**Allowed technologies**:
- HTML
- CSS
- Tailwind CSS
- Native JavaScript

**Prohibited technologies**:
- React, Vue, Angular, Next.js, Nuxt, Svelte, Alpine, jQuery,
  Bootstrap, and any frontend SPA or meta-framework.

**Reusability patterns** (when needed):
- Reusable HTML partial philosophy
- Consistent class conventions
- Clean CSS utilities/components
- Native JS modules where necessary

**Rationale**: The client and developer MUST be able to inspect,
maintain, and deploy the frontend easily from static page sources and
GitHub without framework build complexity.

**Non-goals for this phase** (MUST NOT be implemented but frontend MUST
be designed for future integration):
- Backend logic
- Full booking engine
- Student/teacher dashboards
- Payment system implementation
- API integration
- Admin system implementation

## Design Language & Quality Standards

### Code Quality

Generated frontend code MUST be:
- Clean and well-structured
- Commented only when useful (no comment clutter)
- Easy to navigate and maintain manually
- Split logically by page/section/component if applicable

HTML MUST be semantic. Tailwind usage MUST remain organized and not
chaotic. Native JS MUST be modular and minimal. Unnecessary complexity
is prohibited.

### UI Quality Gates

Every page MUST pass these quality gates before delivery:
- Consistent spacing system applied
- Consistent grid behavior verified
- Consistent section rhythm maintained
- Premium typography hierarchy enforced
- CTA styling consistent
- Card system consistent
- Icon treatment consistent
- Form styling consistent
- No placeholder-like or rough sections remaining

### Future Integration Readiness

The frontend MUST support future expansion into:
- Teacher profiles and marketplace flows
- Student onboarding
- Course discovery and booking flows
- Trial lesson flows
- Dashboard/system integration
- Multilingual content
- SEO content pages

Frontend pages MUST be designed so these features can be integrated
later without major redesign.

## Governance

This constitution is the authoritative source of design and
implementation principles for the Premium Academy Frontend project.

- **Supremacy**: This constitution supersedes all other style guides,
  conventions, or ad-hoc decisions. Conflicts MUST be resolved in favor
  of constitution principles.
- **Amendments**: Any change to this constitution MUST be documented
  with a version increment, rationale, and sync impact report. Changes
  to principles require MINOR or MAJOR version bumps.
- **Versioning**: MAJOR for principle removals or incompatible
  redefinitions, MINOR for new principles or material expansions, PATCH
  for clarifications and wording fixes.
- **Compliance**: Every spec, plan, and task list MUST reference and
  pass a Constitution Check before implementation begins. Violations
  MUST be justified in a Complexity Tracking table.

**Version**: 1.0.0 | **Ratified**: 2026-03-13 | **Last Amended**: 2026-03-13
