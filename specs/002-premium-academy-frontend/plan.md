# Implementation Plan: Sana Academy Frontend Website

**Branch**: `002-Sana-academy-frontend` | **Date**: 2026-03-14 | **Spec**: [spec.md](./spec.md)
**Input**: Feature specification from `/specs/002-Sana-academy-frontend/spec.md`

## Summary

Build a Sana, conversion-oriented public website for an educational academy using only HTML, CSS, Tailwind CSS, and native JavaScript. The website comprises 13 static pages (Homepage, About, Teachers Listing, Teacher Profile, Programs Listing, Program Detail, How It Works, Contact, FAQ, Blog Listing, Blog Detail, Privacy Policy, Terms of Service) with a consistent visual design system, interactive components (accordion, mobile menu, sticky header, form validation, announcement bar dismiss), responsive layouts across 4 breakpoints, and realistic Sana demo content. No backend, no frameworks, no SPA patterns.

## Technical Context

**Language/Version**: HTML5, CSS3, JavaScript ES2020+  
**Primary Dependencies**: Tailwind CSS v3 (CDN), Google Fonts (Inter + Playfair Display), Heroicons (inline SVGs)  
**Storage**: N/A (static files, no persistence)  
**Testing**: Manual browser testing, Lighthouse audits, W3C HTML validation  
**Target Platform**: Modern browsers (Chrome, Firefox, Safari, Edge - last 2 versions), static file hosting (GitHub Pages compatible)  
**Project Type**: Static multi-page website (no build step required)  
**Performance Goals**: Above-the-fold content renders within 4 seconds on 3G; Lighthouse accessibility score 90+  
**Constraints**: No JavaScript frameworks, no CSS frameworks other than Tailwind, no SPA patterns, no build tools required, total page weight target <2MB per page  
**Scale/Scope**: 13 pages, 8+ teacher demo profiles, 6+ course demo entries, 6+ blog demo articles, ~15 reusable component patterns

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| # | Principle | Status | Evidence |
|---|-----------|--------|----------|
| I | Sana Over Decorative | PASS | Design system uses clean typography (Inter + Playfair Display), restrained color palette, generous spacing, no gradients/shadows abuse, no Bootstrap feel. Constitution prohibitions (crowded grids, random typography, cheap stock photos) addressed in visual system design. |
| II | Conversion-First UX | PASS | Homepage specified with full conversion structure: hero + CTA, featured teachers, categories, how-it-works, testimonials, trust metrics, FAQ preview, final CTA band. All pages guide toward business actions. Realistic Sana demo content required (no lorem ipsum). |
| III | Clear Visual Hierarchy | PASS | Consistent spacing scale, typography hierarchy (H1-H4, body, small), button hierarchy (primary/secondary/tertiary), card system, consistent section rhythm enforced across all pages via Tailwind config. |
| IV | Strong Trust Signals | PASS | Trust metrics section, testimonials, teacher ratings/reviews, student counts, quality messaging, process explanation, FAQ all specified. Teacher cards include all marketplace-ready fields. |
| V | Mobile-First and Responsive | PASS | Four explicit breakpoints defined (320px+, 768px+, 1024px+, 1280px+). Deliberate mobile menu, collapsible filters, card stacking, fixed mobile CTAs all specified. |
| VI | SEO-Aware Frontend Structure | PASS | Semantic HTML5, proper heading hierarchy, unique titles/meta per page, Open Graph tags, descriptive anchor text, blog structure for content marketing. All 13 page types from constitution anticipated. |
| VII | Accessibility and Readability | PASS | Semantic markup, visible focus states, alt text, form labels, keyboard navigation, sufficient contrast all specified as functional requirements. |
| Tech | Technology Constraints | PASS | Strictly HTML + CSS + Tailwind + native JS. No prohibited frameworks. Reusable HTML partial philosophy via shared CSS classes and JS modules. |
| Quality | UI Quality Gates | PASS | Consistent spacing, grid, section rhythm, typography, CTAs, cards, icons, forms enforced via design system tokens in Tailwind config. |
| Future | Future Integration Readiness | PASS | Pages structured for future teacher marketplace, booking, courses, dashboards, multilingual content. CTAs link to contact page or coming-soon modal as interim. |

**Gate Result**: ALL PASS. No violations. Proceeding to Phase 0.

## Project Structure

### Documentation (this feature)

```text
specs/002-Sana-academy-frontend/
├── plan.md              # This file
├── research.md          # Phase 0 output
├── data-model.md        # Phase 1 output
├── quickstart.md        # Phase 1 output
└── tasks.md             # Phase 2 output (/speckit.tasks command)
```

### Source Code (repository root)

```text
src/
├── css/
│   └── custom.css           # Custom CSS beyond Tailwind (transitions, animations, overrides)
├── js/
│   ├── main.js              # Shared: mobile menu, sticky header, announcement bar
│   ├── accordion.js         # FAQ accordion behavior
│   ├── filters.js           # Teachers listing filter/sort UI interactions
│   └── forms.js             # Contact form validation
├── images/                  # Placeholder images and SVG icons
├── index.html               # Homepage
├── about.html               # About page
├── teachers.html            # Teachers listing page
├── teacher-profile.html     # Teacher profile page (demo: single teacher)
├── programs.html            # Programs/courses listing page
├── program-detail.html      # Program detail page (demo: single program)
├── how-it-works.html        # How It Works page
├── contact.html             # Contact page
├── faq.html                 # FAQ page
├── blog.html                # Blog listing page
├── blog-post.html           # Blog detail page (demo: single article)
├── privacy-policy.html      # Privacy Policy page
└── terms-of-service.html    # Terms of Service page
```

**Structure Decision**: Flat static site structure. All HTML pages at `src/` root for simple navigation and hosting. CSS and JS separated by responsibility in subdirectories. No build step. Tailwind via CDN with inline config. This matches the constitution's requirement for inspectable, maintainable static files deployable from GitHub.

## Complexity Tracking

> No Constitution Check violations. Table intentionally empty.

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| *(none)*  | —          | —                                   |
