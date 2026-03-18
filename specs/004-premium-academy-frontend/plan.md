# Implementation Plan: Premium Arabic Academy Website Frontend

**Branch**: `004-premium-academy-frontend` | **Date**: 2026-03-18 | **Spec**: [spec.md](spec.md)
**Input**: Feature specification from `/specs/004-premium-academy-frontend/spec.md`

## Summary

Build a complete, section-rich, trust-heavy Arabic-first educational
platform frontend for the Saudi tutoring market. The project delivers
12 HTML pages with a shared design system, global header/footer shell,
and premium interactive elements — all using HTML5 + Tailwind CSS (CDN)

- native JavaScript with zero framework dependencies. The implementation
  is inspired by the depth and polish of leading Arabic edtech platforms
  but is entirely original in design, content, and code.

## Technical Context

**Language/Version**: HTML5, CSS3, JavaScript ES2020+
**Primary Dependencies**: Tailwind CSS v3 (CDN), IBM Plex Sans Arabic (Google Fonts CDN)
**Storage**: N/A (static frontend, no database)
**Testing**: Manual browser testing across 4 breakpoints (375px, 768px, 1440px, 1920px)
**Target Platform**: Static web deployment (GitHub Pages, Netlify, Vercel, any HTTP server, or file:// protocol)
**Project Type**: Static multi-page website (frontend only)
**Performance Goals**: Full page render under 3 seconds on broadband; all content visible without JS execution
**Constraints**: Zero build tooling required; zero backend dependencies; works via file:// protocol
**Scale/Scope**: 12 HTML pages, ~28 reusable component patterns, ~6 JS modules, 1 custom CSS file

## Constitution Check

_GATE: Must pass before Phase 0 research. Re-check after Phase 1 design._

| #   | Constitution Section     | Gate                                                                       | Status |
| --- | ------------------------ | -------------------------------------------------------------------------- | ------ |
| 1   | Project Identity         | Arabic-first, Saudi-market educational platform                            | PASS   |
| 2   | Product Intent           | Complete frontend, not thin landing page, not clone                        | PASS   |
| 3   | Arabic-First & RTL-First | `dir="rtl"` + `lang="ar"` on all pages, RTL-native design                  | PASS   |
| 4   | Visual Language          | IBM Plex Sans Arabic, 6-level type scale, generous spacing                 | PASS   |
| 5   | Color Direction          | Blue (#2563EB) primary, yellow (#FACC15) accent, slate neutrals            | PASS   |
| 6   | Homepage Richness        | 13 sections specified (meets 10–14 minimum)                                | PASS   |
| 7   | Section Depth            | All pages meet minimum section counts per constitution                     | PASS   |
| 8   | Trust-Building           | Multi-layer trust: hero, stats, logos, teachers, testimonials, FAQ, footer | PASS   |
| 9   | UX Quality Bar           | 3-tier CTA hierarchy, polished interactions, comprehensive nav             | PASS   |
| 10  | Responsive               | 4 breakpoints, mobile-first, slide-out menu, 44px touch targets            | PASS   |
| 11  | Content Tone             | Modern Standard Arabic, confident/warm, Saudi MOE terminology              | PASS   |
| 12  | Component Consistency    | 28 components defined with consistent styling rules                        | PASS   |
| 13  | Frontend Code Rules      | HTML5 + CSS3 + Tailwind CDN + native JS only. Zero frameworks.             | PASS   |
| 14  | Non-Goals                | No backend, no auth, no payments, no CMS. Frontend-only scope.             | PASS   |
| 15  | Definition of Success    | Saudi Parent Test + 14 quality gates defined                               | PASS   |

**Post-design re-check**: All gates remain PASS. No constitution violations.

## Project Structure

### Documentation (this feature)

```text
specs/004-premium-academy-frontend/
├── plan.md              # This file
├── research.md          # Phase 0 output — tech decisions
├── data-model.md        # Phase 1 output — content entities
├── quickstart.md        # Phase 1 output — getting started guide
└── tasks.md             # Phase 2 output (created by /speckit.tasks)
```

### Source Code (repository root)

```text
frontend/
├── index.html                # Homepage (13 sections)
├── about.html                # About page (7 sections)
├── teachers.html             # Teachers listing (5+ sections)
├── teacher-profile.html      # Teacher profile (7+ sections)
├── how-it-works.html         # How It Works (6 sections)
├── pricing.html              # Pricing (5+ sections)
├── contact.html              # Contact (5+ sections)
├── faq.html                  # FAQ (5 sections)
├── blog.html                 # Blog listing (4+ sections)
├── blog-post.html            # Blog article (5 sections)
├── terms.html                # Terms of Service
├── privacy.html              # Privacy Policy
├── css/
│   └── custom.css            # Custom animations, marquee, gradients
├── js/
│   ├── main.js               # Entry point, shared initialization
│   ├── navigation.js         # Sticky header, mobile menu
│   ├── accordion.js          # FAQ accordion component
│   ├── carousel.js           # Logo marquee, testimonial scroll
│   ├── animations.js         # Intersection Observer scroll animations
│   └── forms.js              # Contact form validation (Arabic)
└── assets/
    ├── images/               # Placeholder images (CSS gradients)
    ├── icons/                # Inline SVG icon collection
    └── logos/                # Brand logo, partner logo placeholders
```

**Structure Decision**: Flat static site structure within `frontend/`.
No nested routing, no build pipeline, no component framework. Each
HTML page is self-contained with shared `<head>` includes (Tailwind CDN,
Google Fonts, custom CSS) and shared `<script>` includes (JS modules
with `defer`). The global header and footer HTML are duplicated across
pages (no server-side includes in static HTML).

---

## Implementation Phases

### Phase 1: Design System Foundation & Project Setup

**Objective**: Establish the complete visual foundation that every
subsequent page will build upon. Define the Tailwind configuration,
load Arabic fonts, create the custom CSS file with animations and
reusable patterns, and create the SVG icon library.

**Outputs**:

- `frontend/css/custom.css` — All custom CSS: animations
  (fade-in, slide-left, slide-right, float), marquee keyframes,
  blue gradient utility, scroll-behavior, custom focus styles
- Tailwind CDN configuration block (shared across all pages) with
  custom font-family, brand colors, and extended utilities
- `frontend/assets/icons/` — Complete SVG icon library (20+ icons):
  educational subject icons, navigation icons (menu, close, chevron,
  arrow), social media icons, checkmark, star, phone, email,
  WhatsApp, location, clock, user, book, graduation cap
- `frontend/assets/logos/` — Brand logo SVG (Arabic text-based),
  8 partner logo SVG placeholders
- `frontend/assets/images/` — Teacher avatar gradient templates,
  educational illustration SVG placeholders

**Dependencies**: None — this is the foundation phase.

**Why this order**: Every page requires the font, colors, animations,
icons, and brand assets. Building these first prevents inconsistency
and rework. If the design system is wrong, every page built on it
is wrong.

**Major UX risks**:

- Arabic font failing to load from CDN → fallback sans-serif looks
  generic. **Mitigation**: Include fallback font-family chain and
  `font-display: swap`.
- Tailwind CDN failing → no styles at all. **Mitigation**: Test
  offline behavior; ensure the page is still readable without
  Tailwind (semantic HTML provides basic structure).
- Icon inconsistency across pages. **Mitigation**: Build complete
  icon library upfront; document sizing and color conventions.

**Quality focus**: Font rendering quality at all sizes (16px body
to 54px hero). Arabic letter stacking, diacritics spacing, line-
height validation. Color contrast ratios meeting WCAG 2.1 AA.

---

### Phase 2: Global Shell (Header, Footer, Mobile Menu)

**Objective**: Build the persistent navigation shell that wraps every
page. This includes the sticky header, the 4-column footer, and the
mobile slide-out menu. Create a "page template" HTML structure that
all subsequent pages will copy.

**Outputs**:

- Sticky header HTML + responsive behavior (desktop nav + mobile
  hamburger)
- Mobile slide-out menu (RTL) with JS toggle, backdrop, scroll lock
- 4-column footer with social icons, link grid, accreditation,
  copyright
- `frontend/js/navigation.js` — Menu open/close, active page
  highlighting, scroll-based header shadow
- `frontend/js/main.js` — Shared initialization (font loading,
  navigation init, animation init)
- Page template structure: `<html>` → `<head>` → `<body>` →
  `<header>` → `<main>` → `<footer>` → `<script>` tags

**Dependencies**: Phase 1 (design system, icons, logos).

**Why this order**: The header and footer appear on EVERY page.
Building them second (after the design system) means every subsequent
page starts with a complete, consistent shell. If the shell is built
late, early pages ship with incomplete navigation and footer, requiring
expensive rework.

**Major UX risks**:

- Mobile menu not sliding from the correct direction in RTL.
  **Mitigation**: Test with `dir="rtl"` from the start; use
  `transform: translateX()` with RTL-aware direction.
- Footer column reordering breaking on certain breakpoints.
  **Mitigation**: Use Tailwind `order-*` classes with explicit
  mobile and desktop ordering.
- Header height causing content overlap. **Mitigation**: Apply
  matching `pt-[64px] md:pt-[80px]` on `<main>` element.

**Quality focus**: Header stickiness across all scroll depths.
Footer consistency verification (visual diff between pages).
Mobile menu animation smoothness (60fps). RTL correctness in
all navigation elements.

---

### Phase 3: Homepage

**Objective**: Build the complete 13-section homepage — the most
critical page on the entire site. This is the primary conversion
and trust-building page. It MUST feel rich, deep, and commercially
credible.

**Outputs**:

- `frontend/index.html` — Complete homepage with all 13 sections:
  1. Hero (headline, CTAs, trust badge, illustration, floating elements)
  2. Quick-Stats Trust Bar (4 statistics with icons)
  3. Services Overview (3 blue cards, horizontal scroll on mobile)
  4. Partner Logos Carousel (8+ logos, infinite CSS marquee)
  5. Private Tutoring Deep-Dive (gradient card, features, CTA)
  6. Exam Prep Deep-Dive (gradient card, features, CTA)
  7. Subject Browser (8 subject cards in grid)
  8. Teacher Showcase (8 teacher cards in responsive grid)
  9. Student Testimonials (4–6 scrollable cards)
  10. How It Works Preview (4-step process)
  11. FAQ Preview (10 accordion items)
  12. Platform Promotion (gradient card, app badges, mockup)
  13. Closing CTA (compelling headline, primary CTA, WhatsApp)
- `frontend/js/accordion.js` — FAQ accordion with single-open behavior
- `frontend/js/carousel.js` — Logo marquee + testimonial horizontal scroll
- `frontend/js/animations.js` — Intersection Observer for scroll-triggered
  entrance animations (fade-in, slide-left, slide-right)

**Dependencies**: Phase 1 (design system) + Phase 2 (header/footer shell).

**Why this order**: The homepage is the highest-impact page. It
establishes the visual rhythm, section patterns, and component
library that all other pages reuse. Teacher cards, testimonial cards,
FAQ accordion, stats bar, service deep-dive cards, and CTA sections
built here become the templates for every subsequent page.

**Major UX risks**:

- Homepage feeling thin or section-poor. **Mitigation**: Constitution
  mandates minimum 13 sections. Count sections during development.
  Target ~5,500px scroll depth on desktop.
- Marquee animation janking or leaving gaps. **Mitigation**: Duplicate
  logo track and use `-50%` translateX for seamless loop. Test at
  various screen widths.
- FAQ accordion JS conflicting with other page accordions later.
  **Mitigation**: Write accordion.js as a generic, reusable module
  that initializes on any container with the right data attributes.
- Hero section looking weak on mobile. **Mitigation**: Design
  mobile hero separately — stacked layout, full-width CTAs,
  trust badge above the fold.

**Quality focus**: Section-by-section visual audit against spec.
Scroll depth measurement. CTA prominence at every scroll position.
Trust element distribution (not concentrated in one section).
Mobile experience as a first-class product — not just "doesn't
break." Arabic content fluency check on every visible text element.

---

### Phase 4: Teachers Pages (Listing + Profile)

**Objective**: Build the Teachers listing page and the Teacher
profile page — the second-highest trust factor after the homepage.

**Outputs**:

- `frontend/teachers.html` — Teachers listing with:
  1. Hero section ("المعلمون" heading, subtitle, stats)
  2. Subject filter bar (horizontal scrollable pills)
  3. Teacher card grid (8 cards, 2→3→4 column responsive)
  4. Trust stats section (total teachers, average rating)
  5. Testimonials section (reuse component from homepage)
  6. Registration CTA section
- `frontend/teacher-profile.html` — Teacher profile with:
  1. Profile header (large photo, name, subjects, experience badge)
  2. Biography section (2–3 Arabic paragraphs)
  3. Subjects & grades (pill grid)
  4. Student reviews (4–6 review cards)
  5. Teaching stats (sessions, students, rating, years)
  6. Availability preview (weekly grid or contact message)
  7. Related teachers (3–4 teacher cards, reuse component)
  8. Booking CTA section

**Dependencies**: Phase 3 (teacher card component, testimonial
component, CTA section, stats bar from homepage).

**Why this order**: Teachers are the second-most visited pages
after the homepage. The teacher card component is already built
in Phase 3 (homepage teacher showcase). The profile page extends
the teacher entity with biography, reviews, and availability.
Building teachers before other informational pages ensures the
high-trust content is complete early.

**Major UX risks**:

- Teacher cards looking inconsistent between homepage and listing
  page. **Mitigation**: Reuse identical HTML/Tailwind class patterns.
  Constitution Section 12 mandates card consistency.
- Profile page feeling thin. **Mitigation**: Enforce minimum 7
  sections. Ensure biography has real Arabic content, reviews
  have realistic text.
- Subject filter not working without JS. **Mitigation**: Show all
  teachers by default. Filter is progressive enhancement.

**Quality focus**: Teacher card data completeness (all 7 fields
present on every card). Profile biography Arabic fluency.
Review text realism. Card gradient color variety across the grid.

---

### Phase 5: How It Works + Pricing

**Objective**: Build the process clarity and pricing transparency
pages — the final trust barriers before conversion.

**Outputs**:

- `frontend/how-it-works.html` — How It Works with:
  1. Hero section
  2. Step-by-step process (4–6 steps with icons and connectors)
  3. Platform benefits (6 benefit cards in grid)
  4. Student success stories (testimonial cards)
  5. Parent section (monitoring, reports, communication)
  6. Getting started CTA
- `frontend/pricing.html` — Pricing with:
  1. Hero section
  2. Pricing tiers (3 plan cards with feature lists)
  3. Feature comparison table or grid
  4. Billing FAQ (5 pricing-specific questions, reuse accordion)
  5. Testimonials section (reuse)
  6. Registration CTA

**Dependencies**: Phase 3 (CTA section, testimonial component,
benefit card pattern, FAQ accordion).

**Why this order**: How It Works and Pricing are conversion-support
pages. They answer "how does this work?" and "how much does it
cost?" — questions that arise after homepage and teacher browsing.
Building them after the core pages ensures all reusable components
are available.

**Major UX risks**:

- Step-by-step process reading left-to-right instead of RTL.
  **Mitigation**: Connector arrows must point RTL. Number sequence
  flows right-to-left. Test visually.
- Pricing cards being too similar and not differentiating tiers.
  **Mitigation**: Highlight the "popular" plan with distinct color
  treatment (yellow accent or blue gradient). Use clear visual
  hierarchy.
- Pricing page feeling generic. **Mitigation**: Include real
  subject examples, session duration details, and "what's included"
  specifics in Arabic.

**Quality focus**: Step flow direction in RTL. Pricing card
comparison clarity. CTA prominence on pricing page. Arabic content
quality in benefit descriptions and FAQ answers.

---

### Phase 6: About + Contact

**Objective**: Build the institutional credibility and accessibility
pages that complete the trust picture for parents performing due
diligence.

**Outputs**:

- `frontend/about.html` — About page with:
  1. Hero section ("من نحن")
  2. Mission & Vision (two-column or stacked)
  3. Our Story (timeline or narrative, 3–4 paragraphs)
  4. Team section (4–6 member cards in grid)
  5. Platform statistics (large bold numbers)
  6. Partners & Accreditation (logo grid, badge)
  7. Join CTA
- `frontend/contact.html` — Contact page with:
  1. Hero section ("تواصل معنا")
  2. Contact form (RTL, Arabic labels, validation)
  3. Contact info cards (phone, email, WhatsApp, address)
  4. Operating hours
  5. Mini FAQ (4–5 contact questions)
  6. Map placeholder
- `frontend/js/forms.js` — Contact form validation with Arabic
  error messages, RTL input styling, success feedback

**Dependencies**: Phase 3 (CTA section, stats bar, FAQ accordion,
partner logos). Phase 1 (icon library for contact cards).

**Why this order**: About and Contact are due-diligence pages.
Parents visit them after being impressed by the homepage and
teachers. They are lower-traffic but essential for conversion.
Building them after core pages ensures all shared components and
the form validation module are ready.

**Major UX risks**:

- Contact form inputs aligning LTR. **Mitigation**: RTL is
  default via `dir="rtl"`. Test every input type (text, email,
  tel, select, textarea) for correct alignment.
- About page feeling corporate/generic. **Mitigation**: Include
  specific Arabic narrative content, realistic team member photos
  (gradient placeholders with Arabic initials), and concrete
  statistics.
- Phone input with +966 prefix breaking RTL. **Mitigation**: Use
  `dir="ltr"` on the phone input specifically, with RTL label.

**Quality focus**: Form validation Arabic error messages. Contact
info completeness. Team section photo/name/title consistency.
Mission/vision Arabic content fluency. Operating hours formatting.

---

### Phase 7: FAQ Page

**Objective**: Build the full FAQ page with categorized questions,
search UI, and comprehensive answers — the primary concern-resolution
tool for hesitant parents.

**Outputs**:

- `frontend/faq.html` — Full FAQ page with:
  1. Hero section ("الأسئلة الشائعة", decorative search input)
  2. Category tabs (عام, الأسعار, المعلمون, الجدولة, المنصة)
  3. Accordion with 15+ questions (3+ per category)
  4. Contact CTA ("لم تجد إجابتك؟")
  5. Related quick links (How It Works, Pricing, Contact)
- Tab/filter behavior in JS (show/hide questions by category)

**Dependencies**: Phase 3 (accordion.js from homepage FAQ preview).
Phase 6 (contact page link for "لم تجد إجابتك؟" CTA).

**Why this order**: The FAQ page extends the homepage FAQ preview
with full categorization and all 15 questions. The accordion JS
module is already built. Category tabs add the only new JS behavior.
Building after Contact means the "contact us" CTA can link to a
real page.

**Major UX risks**:

- Category tabs not fitting on mobile. **Mitigation**: Horizontal
  scrollable tab bar on mobile.
- Answer text being too short/generic. **Mitigation**: Each answer
  MUST be 3–5 sentences of specific, helpful Arabic content.
  Constitution prohibits placeholder answers.
- Tab filtering breaking accordion state. **Mitigation**: Close
  all open accordions when switching categories.

**Quality focus**: Answer depth and helpfulness. Tab responsiveness.
Category distribution (3+ questions per category). Arabic content
proofread. "لم تجد إجابتك؟" CTA prominence.

---

### Phase 8: Blog Pages (Listing + Article)

**Objective**: Build the blog listing page and a sample blog article
page — content marketing and SEO foundation pages.

**Outputs**:

- `frontend/blog.html` — Blog listing with:
  1. Hero section ("المدونة")
  2. Featured article (large card)
  3. Article card grid (6+ cards, 2→3 column responsive)
  4. Category filter bar
  5. Pagination or "تحميل المزيد" button
- `frontend/blog-post.html` — Blog article with:
  1. Article header (title, author, date, category, reading time)
  2. Article body (4–5 paragraphs of Arabic educational content)
  3. Author bio card
  4. Related articles (3 article cards)
  5. Registration CTA

**Dependencies**: Phase 1 (design system). Phase 2 (header/footer).
Phase 3 (CTA section pattern).

**Why this order**: Blog pages are lower-priority than core
conversion pages. They support SEO and thought leadership but are
not on the primary conversion path. Building them late ensures
all component patterns are stable and the article card can follow
established card conventions.

**Major UX risks**:

- Article body text rendering poorly in RTL. **Mitigation**: Test
  long-form Arabic content with headings, lists, and blockquotes.
  Ensure line-height and paragraph spacing are comfortable for
  extended reading.
- Blog cards feeling generic. **Mitigation**: Include realistic
  Arabic titles, meaningful excerpts, and category-specific
  gradient thumbnails.

**Quality focus**: Long-form Arabic readability (line-height,
paragraph spacing, heading hierarchy). Article content substance.
Card consistency with other card types on the site.

---

### Phase 9: Legal Pages (Terms + Privacy)

**Objective**: Build the Terms of Service and Privacy Policy pages
— professional legal presence that completes the trust picture.

**Outputs**:

- `frontend/terms.html` — Terms of Service with:
  1. Hero section ("الشروط والأحكام")
  2. 8+ numbered legal sections in Arabic (scope, accounts,
     payments, refunds, IP, privacy reference, termination,
     modifications, contact)
  3. Last updated date
- `frontend/privacy.html` — Privacy Policy with:
  1. Hero section ("سياسة الخصوصية")
  2. 8+ sections in Arabic (data collection, usage, sharing,
     cookies, security, user rights, children's privacy, contact)
  3. Last updated date

**Dependencies**: Phase 2 (header/footer shell).

**Why this order**: Legal pages are the lowest-priority content
pages but are required for commercial credibility. They use the
simplest layout (hero + long-form text) and can be built quickly
late in the project without blocking anything.

**Major UX risks**:

- Legal text looking like a wall of unstyled text. **Mitigation**:
  Use proper heading hierarchy, numbered lists, and consistent
  section spacing. Apply the same section rhythm as other pages.
- Arabic legal terminology being awkward. **Mitigation**: Use
  standard Saudi legal phrasing for terms of service and privacy
  policies. Reference existing Saudi platform legal pages for
  terminology conventions.

**Quality focus**: Heading hierarchy. Section numbering. Arabic
legal terminology accuracy. Last-updated date formatting.

---

### Phase 10: Cross-Page QA, Responsiveness & Polish

**Objective**: Comprehensive quality assurance pass across all 12
pages. Verify every constitution quality gate, fix RTL issues,
ensure responsive behavior at all breakpoints, and polish
interactions.

**Outputs**:

- All RTL issues fixed across all pages
- All responsive breakpoint issues fixed (375px, 768px, 1440px, 1920px)
- All horizontal overflow eliminated
- All scroll-triggered animations verified
- All interactive elements verified (accordions, mobile menu,
  carousels, hover states, form validation)
- Consistent header/footer verified across all pages
- Internal links verified (all cross-page links work)
- Active page highlighting in navigation verified
- Arabic content proofread for fluency and naturalness
- Trust signal distribution verified on every page
- Section count verification against spec minimums
- The Saudi Parent Test applied to every page
- `alt` text in Arabic verified on all images
- Keyboard accessibility verified on all interactive elements
- Focus state visibility verified

**Dependencies**: All previous phases (1–9).

**Why this order**: QA is the final phase because it requires all
pages to be complete. Cross-page consistency, navigation verification,
and the Saudi Parent Test can only be performed when every page exists.
Earlier phases do per-page QA during development, but this phase does
holistic, site-wide quality verification.

**Major UX risks**:

- Discovering systemic RTL issues that require rework on all pages.
  **Mitigation**: Each phase tests RTL on its own pages. Phase 10
  catches cross-page inconsistencies only.
- Mobile experience passing individual page tests but feeling
  inconsistent across pages. **Mitigation**: Check spacing, font
  sizes, and CTA patterns are identical on every page.
- Performance degradation from accumulated animations and images.
  **Mitigation**: Verify `loading="lazy"` on below-fold images.
  Check animation performance on mobile devices.

**Quality focus**: The 14 quality gates from Constitution Section 15.
The Saudi Parent Test on every page. Cross-page consistency. Mobile
experience as a holistic product, not individual pages in isolation.

---

## Phase Dependency Graph

```
Phase 1: Design System Foundation
    ↓
Phase 2: Global Shell (Header/Footer/Menu)
    ↓
Phase 3: Homepage (13 sections) ← builds ALL reusable components
    ↓
    ├── Phase 4: Teachers (Listing + Profile)
    ├── Phase 5: How It Works + Pricing
    ├── Phase 6: About + Contact
    ↓
Phase 7: FAQ (full page, extends homepage preview)
    ↓
Phase 8: Blog (Listing + Article)
    ↓
Phase 9: Legal (Terms + Privacy)
    ↓
Phase 10: Cross-Page QA & Polish
```

**Notes on parallelism**: Phases 4, 5, and 6 can be built in
parallel after Phase 3 since they reuse components from the
homepage. However, sequential execution is recommended to maintain
component consistency and allow learnings from each page to
improve subsequent pages.

---

## Complexity Tracking

> No constitution violations detected. No complexity justifications needed.

| Violation | Why Needed | Simpler Alternative Rejected Because |
| --------- | ---------- | ------------------------------------ |
| (none)    | —          | —                                    |
