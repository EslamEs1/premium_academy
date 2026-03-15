# Tasks: Sana Academy Frontend Website

**Input**: Design documents from `/specs/002-Sana-academy-frontend/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, quickstart.md

**Tests**: No automated tests requested. Verification is via manual browser testing, Lighthouse audits, and W3C validation as described in success criteria.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story. Each user story phase produces a complete, viewable increment of the website.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

All source files live under `src/` at repository root per plan.md:

- HTML pages: `src/*.html`
- CSS: `src/css/custom.css`
- JavaScript: `src/js/*.js`
- Images: `src/images/`

---

## Phase 1: Setup (Project Initialization)

**Purpose**: Create project skeleton, configure Tailwind design system, and establish shared conventions

- [x] T001 Create directory structure: `src/css/`, `src/js/`, `src/images/` per plan.md project structure
- [x] T002 Create Tailwind config file with complete design system (colors, typography, spacing, shadows, radii) from research.md in `src/js/tailwind-config.js`
- [x] T003 [P] Create custom CSS file with base styles, transitions, animations, scroll-behavior, focus styles, and reserved header/footer placeholder heights in `src/css/custom.css`

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Build shared components (header, footer, mobile menu, sticky header) that ALL pages depend on. No page can be built until these are complete.

**CRITICAL**: Every HTML page depends on the header/footer JS injection and the shared Tailwind config from Phase 1.

- [x] T004 Implement global header injection with desktop navigation (7 nav links + CTA button), logo placeholder, and active page highlighting via JS in `src/js/main.js`
- [x] T005 Implement mobile menu (full-screen overlay with nav links + CTA, close on button/outside click/Escape, prevent background scroll, smooth animation) in `src/js/main.js`
- [x] T006 Implement sticky header behavior (fixed on scroll, reduced height, shadow enhancement, hide-on-scroll-down/show-on-scroll-up) in `src/js/main.js`
- [x] T007 Implement global footer injection with 4 navigation groups (Explore, Learn, Support, Legal), contact details, newsletter signup form, social links, copyright, and legal links in `src/js/main.js`
- [x] T008 Implement announcement bar component (dismissible, session-persistent via sessionStorage, close button) in `src/js/main.js`
- [x] T009 Implement FAQ accordion behavior (expand/collapse with smooth CSS transitions, single-item-open per category, data-attribute driven, keyboard accessible) in `src/js/accordion.js`

**Checkpoint**: Shared infrastructure ready. Opening any HTML page that includes `main.js` will render a consistent header, footer, mobile menu, and sticky behavior. The accordion module is ready for any page that needs it.

---

## Phase 3: User Story 1 - Prospective Student Discovers the Academy (Priority: P1) MVP

**Goal**: A visitor landing on the homepage immediately understands the academy's value, sees trust signals, featured teachers, subject categories, testimonials, and is guided toward a primary CTA. The homepage functions as the complete conversion landing experience.

**Independent Test**: Load `src/index.html` on desktop (1280px+) and mobile (375px). Verify: hero section with value proposition and CTAs visible in first viewport; all 10 sections render with realistic Sana content; announcement bar is dismissible; FAQ preview accordion works; mobile menu opens/closes; footer newsletter form is present; no horizontal scroll at 320px.

### Implementation for User Story 1

- [x] T010 [US1] Create homepage HTML skeleton with semantic structure (announcement bar, header placeholder, main with 10 sections, footer placeholder), meta tags, OG tags, JSON-LD EducationalOrganization, and CDN includes in `src/index.html`
- [x] T011 [US1] Build hero section with display heading, supporting paragraph, primary CTA button ("Book a Free Trial"), secondary CTA link ("Browse Teachers"), and hero image/visual in `src/index.html`
- [x] T012 [US1] Build trust metrics section with 4 metric cards (15,000+ Students, 200+ Teachers, 98% Satisfaction, 500,000+ Lessons) using inline SVG icons in `src/index.html`
- [x] T013 [US1] Build featured teachers section with 4 teacher cards (photo from randomuser.me, name, headline, subjects as pills, star rating with review count, price indicator, "View Profile" CTA linking to teacher-profile.html) in `src/index.html`
- [x] T014 [US1] Build subjects/categories section with 8+ subject cards (Mathematics, Science, English, Business, Technology, Music, Languages, Test Prep) each with inline SVG icon, name, teacher count, and link in `src/index.html`
- [x] T015 [US1] Build "How It Works" preview section with 4 numbered steps (Browse Teachers, Book a Trial, Start Learning, Track Progress) with icons and descriptions in `src/index.html`
- [x] T016 [US1] Build value proposition section with 3 benefit blocks for students/parents (Expert Teachers, Flexible Learning, Proven Results) with icons, headings, and descriptions in `src/index.html`
- [x] T017 [US1] Build testimonials section with 3 review cards (reviewer photo, name, role, star rating, review text, date) using carousel or grid layout in `src/index.html`
- [x] T018 [US1] Build FAQ preview section with 4-5 accordion items using data-accordion attributes (wired to accordion.js) with realistic Q&A content in `src/index.html`
- [x] T019 [US1] Build final CTA band section with compelling heading, supporting text, and primary + secondary CTA buttons in `src/index.html`
- [x] T020 [US1] Verify homepage responsive behavior at all 4 breakpoints (320px, 768px, 1024px, 1280px): card stacking, section spacing adjustments, hero layout changes, category grid reflow, mobile-appropriate font sizes

**Checkpoint**: Homepage is fully functional and viewable. A visitor can see the complete Sana landing experience, interact with mobile menu, dismiss announcement bar, expand FAQ items, and navigate to other pages (which will be empty shells until their phases complete).

---

## Phase 4: User Story 2 - Student Browses and Evaluates Teachers (Priority: P1)

**Goal**: A visitor navigates to the teachers listing, browses 8+ teacher cards with all decision-making information, uses filter/sort UI controls, and clicks through to a detailed teacher profile with sticky booking CTA, qualifications, reviews, and lesson formats.

**Independent Test**: Navigate from homepage "Browse Teachers" CTA to `src/teachers.html`. Verify: 8 teacher cards display with all required fields; filter sidebar toggles on mobile; sort dropdown shows options; clicking a card goes to `src/teacher-profile.html`; profile page shows all sections with 4+ reviews; sticky sidebar visible on desktop scroll; fixed bottom CTA bar visible on mobile scroll.

### Implementation for User Story 2

- [x] T021 [US2] Implement filter/sort UI interaction logic (checkbox active states, dropdown selection visual feedback, collapsible filter panel on mobile, clear filters button) in `src/js/filters.js`
- [x] T022 [US2] Create teachers listing page with semantic structure, meta tags, OG tags, breadcrumb, and CDN includes in `src/teachers.html`
- [x] T023 [US2] Build filter sidebar with subject checkboxes (8 subjects), format radio buttons (Online/In-Person/Both), experience level checkboxes (Senior/Experienced/New), and "Clear All" reset in `src/teachers.html`
- [x] T024 [US2] Build sorting bar with results count, sort dropdown (Recommended, Highest Rated, Price Low-High, Price High-Low), and grid/list view toggle in `src/teachers.html`
- [x] T025 [US2] Build 8 teacher cards with data from data-model.md Teacher entity (photo from randomuser.me, name, headline, subject pills, star rating with count, experience badge, price indicator, "View Profile" CTA button) in responsive grid layout in `src/teachers.html`
- [x] T026 [US2] Build collapsible mobile filter panel (slide-down with toggle button, overlay, apply/clear buttons) for teachers listing mobile view in `src/teachers.html`
- [x] T027 [US2] Create teacher profile page with semantic structure, meta tags, OG tags, JSON-LD Person, breadcrumb, and CDN includes in `src/teacher-profile.html`
- [x] T028 [US2] Build teacher profile hero/intro section with large photo, name, headline, subject pills, star rating, key stats (Students, Lessons, Experience, Response Time), and availability badge in `src/teacher-profile.html`
- [x] T029 [US2] Build teacher profile content sections: About Me (biography), Qualifications (credential list), Subjects Taught (with descriptions), Teaching Style, Available Lesson Formats (1-on-1, Group, In-Person with pricing per format) in `src/teacher-profile.html`
- [x] T030 [US2] Build teacher profile reviews section with 4+ individual review cards (reviewer name, photo, rating, date, review text), overall rating summary, and "Show More" truncation pattern in `src/teacher-profile.html`
- [x] T031 [US2] Build sticky sidebar on desktop (position: sticky with booking CTA, price summary, "Book a Free Trial" button, availability indicator) and fixed bottom CTA bar on mobile in `src/teacher-profile.html`
- [x] T032 [US2] Verify teachers listing and profile responsive behavior at all 4 breakpoints: filter sidebar collapses on mobile, card grid reflows (4→2→1 columns), profile layout switches from 2-column to single-column, sticky sidebar becomes fixed bottom bar

**Checkpoint**: Teacher discovery flow is complete. Visitor can browse, filter (visually), sort, view cards, and explore a detailed teacher profile with booking CTA — the core marketplace UX.

---

## Phase 5: User Story 3 - Student Explores Programs and Courses (Priority: P2)

**Goal**: A visitor browses categorized course cards on the programs listing and clicks through to a detailed course page with overview, audience, inclusions, outcomes, instructor, and enrollment CTA.

**Independent Test**: Navigate to `src/programs.html`. Verify: 6+ course cards across 3 categories; category tabs/headers visible; cards show all required fields; clicking a card goes to `src/program-detail.html`; detail page shows all sections including FAQ accordion; enrollment CTA is prominent.

### Implementation for User Story 3

- [x] T033 [P] [US3] Create programs listing page with semantic structure, meta tags, OG tags, breadcrumb, and CDN includes in `src/programs.html`
- [x] T034 [US3] Build category filter tabs (All, Mathematics, Science, Languages, Business, Test Prep) with active state styling and visual filtering in `src/programs.html`
- [x] T035 [US3] Build 6+ course cards with data from data-model.md Program entity (title, description excerpt, category badge, level indicator, duration, price indicator, "Learn More" CTA) in responsive grid in `src/programs.html`
- [x] T036 [P] [US3] Create program detail page with semantic structure, meta tags, OG tags, JSON-LD Course, breadcrumb, and CDN includes in `src/program-detail.html`
- [x] T037 [US3] Build program detail hero section with title, category badge, level, duration, price indicator, and hero image in `src/program-detail.html`
- [x] T038 [US3] Build program detail content sections: Overview, Who It's For (target audience), What's Included (inclusions checklist with checkmark icons), Learning Outcomes (numbered list), and Instructor summary card (referencing a Teacher entity) in `src/program-detail.html`
- [x] T039 [US3] Build program detail enrollment CTA block (prominent button, price, "Contact Us" alternative, trust messaging) and FAQ section with 3-4 accordion items in `src/program-detail.html`
- [x] T040 [US3] Verify programs listing and detail responsive behavior at all 4 breakpoints: category tabs scroll horizontally on mobile, card grid reflows, detail page sections stack vertically

**Checkpoint**: Program discovery flow is complete. Visitor can browse courses by category and view detailed information to support enrollment decisions.

---

## Phase 6: User Story 4 - Visitor Understands the Academy Process (Priority: P2)

**Goal**: A visitor sees a clear step-by-step explanation of the student journey with trust and support messaging, encouraging them to take the first step.

**Independent Test**: Navigate to `src/how-it-works.html`. Verify: 4 clearly labeled steps visible with icons and descriptions; CTA at bottom; trust/support messaging present; responsive layout adjusts step arrangement at each breakpoint.

### Implementation for User Story 4

- [x] T041 [US4] Create How It Works page with semantic structure, meta tags, OG tags, breadcrumb, and CDN includes in `src/how-it-works.html`
- [x] T042 [US4] Build step-by-step process section with 4 numbered steps (1. Browse & Discover, 2. Book a Trial, 3. Start Learning, 4. Track & Grow) each with large icon, heading, description, and connecting visual line/arrow in `src/how-it-works.html`
- [x] T043 [US4] Build trust and support messaging section (Personal guidance, Satisfaction guarantee, Flexible scheduling, 24/7 support) with icons and descriptions in `src/how-it-works.html`
- [x] T044 [US4] Build bottom CTA section with heading, supporting text, and "Find Your Teacher" / "Browse Programs" buttons in `src/how-it-works.html`
- [x] T045 [US4] Verify How It Works responsive behavior: steps layout switches from horizontal timeline to vertical on mobile, icons resize, CTA remains prominent

**Checkpoint**: Process explanation page is complete. Visitor understands the journey from discovery to first lesson.

---

## Phase 7: User Story 5 - Visitor Learns About the Academy (Priority: P3)

**Goal**: A visitor evaluating the academy reads the story, mission, philosophy, and trust indicators to build confidence.

**Independent Test**: Navigate to `src/about.html`. Verify: academy story, mission/vision, teaching philosophy, "Why Choose Us" section, trust indicators, and CTA are all present with Sana content.

### Implementation for User Story 5

- [x] T046 [P] [US5] Create About page with semantic structure, meta tags, OG tags, breadcrumb, and CDN includes in `src/about.html`
- [x] T047 [US5] Build About page sections: Academy Story (with image), Mission & Vision (with highlight block), Teaching Philosophy (with 3 philosophy pillars), Why Choose Us (4 benefit cards with icons), Trust Indicators (partner logos or credential badges), and bottom CTA in `src/about.html`
- [x] T048 [US5] Verify About page responsive behavior at all 4 breakpoints: image/text layout switches, philosophy pillars stack, benefit cards reflow

**Checkpoint**: About page builds deep trust for evaluating visitors.

---

## Phase 8: User Story 6 - Visitor Contacts the Academy (Priority: P3)

**Goal**: A visitor submits an inquiry via a Sana contact form with client-side validation, sees alternative contact methods, and is prompted to check FAQ.

**Independent Test**: Navigate to `src/contact.html`. Verify: form displays 4 fields with labels; submitting empty form shows inline errors; valid email format required; successful submission shows client-side confirmation; email, phone, and FAQ link visible.

### Implementation for User Story 6

- [x] T049 [US6] Implement contact form validation logic (required fields, email format, inline error display, success message on valid submit) with data-validate attribute pattern in `src/js/forms.js`
- [x] T050 [P] [US6] Create Contact page with semantic structure, meta tags, OG tags, breadcrumb, and CDN includes in `src/contact.html`
- [x] T051 [US6] Build contact form section with name, email, subject dropdown, and message textarea fields, each with labels, placeholder text, and validation attributes, plus "Send Message" primary button in `src/contact.html`
- [x] T052 [US6] Build contact information section with email address, phone number, business hours, and office address, plus "Check our FAQ" prompt linking to faq.html in `src/contact.html`
- [x] T053 [US6] Build form success state (client-side only: hide form, show confirmation message with checkmark icon and "We'll get back to you within 24 hours" text) in `src/contact.html`
- [x] T054 [US6] Verify Contact page responsive behavior at all 4 breakpoints: form and contact info stack vertically on mobile, form fields full-width on small screens

**Checkpoint**: Contact/lead generation flow is complete with form validation and success feedback.

---

## Phase 9: User Story 7 - Visitor Reads FAQ (Priority: P3)

**Goal**: A visitor finds answers organized into categories with a smooth accordion interface covering common student/parent concerns.

**Independent Test**: Navigate to `src/faq.html`. Verify: 3+ categories visible; 12+ total FAQ items; clicking expands one item at a time per category; smooth transitions; touch-friendly on mobile.

### Implementation for User Story 7

- [x] T055 [P] [US7] Create FAQ page with semantic structure, meta tags, OG tags, JSON-LD FAQPage, breadcrumb, and CDN includes in `src/faq.html`
- [x] T056 [US7] Build FAQ content with 3 categories (Getting Started: 4 items, Lessons & Teachers: 4 items, Pricing & Payments: 4 items) using data-accordion attributes, realistic Sana Q&A content in `src/faq.html`
- [x] T057 [US7] Build FAQ page header with search-like text (decorative, non-functional) and bottom CTA section ("Still have questions? Contact us") in `src/faq.html`
- [x] T058 [US7] Verify FAQ page responsive behavior at all 4 breakpoints: accordion touch targets minimum 48px, category spacing adjusts, text remains readable

**Checkpoint**: FAQ page answers visitor objections and reduces support burden.

---

## Phase 10: User Story 8 - Visitor Reads Blog Content (Priority: P3)

**Goal**: A visitor browses educational articles with clean hierarchy, clicks through to a readable article with share options and related content.

**Independent Test**: Navigate to `src/blog.html`. Verify: 6+ article cards with all required fields; clicking a card goes to `src/blog-post.html`; article has readable typography (prose class), share buttons, author bio, related articles section, and engagement CTA.

### Implementation for User Story 8

- [x] T059 [P] [US8] Create blog listing page with semantic structure, meta tags, OG tags, breadcrumb, and CDN includes in `src/blog.html`
- [x] T060 [US8] Build 6+ article cards with data from data-model.md Blog Article entity (featured image from Unsplash, title, excerpt, author, date, category tag, read time) in responsive grid with featured article highlight in `src/blog.html`
- [x] T061 [US8] Build blog listing sidebar or category filter bar with category tags (Study Tips, Teaching Methods, Student Success, Education News, Exam Prep) in `src/blog.html`
- [x] T062 [P] [US8] Create blog detail page with semantic structure, meta tags, OG tags, JSON-LD Article, breadcrumb, and CDN includes in `src/blog-post.html`
- [x] T063 [US8] Build blog article header with title, author byline (photo, name, date), category tag, read time, and featured image in `src/blog-post.html`
- [x] T064 [US8] Build blog article body with Tailwind Typography `prose` class styling, proper heading hierarchy (H2, H3), paragraphs, lists, blockquotes, and inline images in `src/blog-post.html`
- [x] T065 [US8] Build blog article footer with share buttons (Twitter, Facebook, LinkedIn, Copy Link), author bio card, and "Read Next" related articles section (3 cards) in `src/blog-post.html`
- [x] T066 [US8] Build blog article engagement CTA band ("Ready to start learning? Book a Free Trial") between article body and footer in `src/blog-post.html`
- [x] T067 [US8] Verify blog listing and detail responsive behavior at all 4 breakpoints: article grid reflows, sidebar becomes horizontal on mobile, prose max-width controls line length, share buttons reposition

**Checkpoint**: Blog content system is complete, supporting SEO and thought leadership positioning.

---

## Phase 11: User Story 9 - Visitor Reviews Legal Information (Priority: P4)

**Goal**: Privacy Policy and Terms of Service pages exist with proper heading structure, readable formatting, and last-updated dates.

**Independent Test**: Click "Privacy Policy" and "Terms of Service" in footer. Verify: pages load with proper heading hierarchy, readable content, last-updated date, and consistent styling.

### Implementation for User Story 9

- [x] T068 [P] [US9] Create Privacy Policy page with semantic structure, meta tags, breadcrumb, structured legal content (10+ sections: Information Collection, Data Usage, Cookies, Third Parties, Data Security, Children's Privacy, User Rights, Data Retention, Changes, Contact), and last-updated date in `src/privacy-policy.html`
- [x] T069 [P] [US9] Create Terms of Service page with semantic structure, meta tags, breadcrumb, structured legal content (10+ sections: Acceptance, Services, Accounts, Payments, Intellectual Property, User Conduct, Disclaimers, Limitation of Liability, Termination, Governing Law, Contact), and last-updated date in `src/terms-of-service.html`

**Checkpoint**: Legal pages complete. All required pages are now implemented.

---

## Phase 12: Polish & Cross-Cutting Concerns

**Purpose**: Final quality pass across all pages for consistency, accessibility, SEO, and edge cases

- [x] T070 Audit all 13 pages for visual consistency: verify same color palette, typography scale, spacing rhythm, card styles, button hierarchy, section padding, and container widths across every page
- [x] T071 Audit all 13 pages for accessibility: verify focus states on all interactive elements, alt text on all images, form labels, ARIA attributes on accordion/menu, sufficient color contrast, keyboard operability (Tab/Enter/Escape)
- [x] T072 [P] Audit all 13 pages for SEO: verify unique title tags, unique meta descriptions, OG tags, canonical links, heading hierarchy (one H1 per page), descriptive anchor text, JSON-LD structured data on applicable pages
- [x] T073 [P] Implement edge case handling: image fallback backgrounds (CSS background-color on image containers), "Coming Soon" modal for future-feature CTAs, graceful JS-disabled degradation (noscript content for mobile menu, visible nav links without JS)
- [x] T074 Verify cross-page navigation: test every internal link from header, footer, and in-page CTAs across all 13 pages to confirm correct href targets and no broken links
- [ ] T075 Final responsive audit: test all 13 pages at 320px, 375px, 768px, 1024px, 1280px, and 1440px viewports — verify no horizontal scroll, no overlapping elements, all CTAs tappable, readable typography at every size
- [ ] T076 Run W3C HTML validation on all 13 pages, fix any errors (warnings acceptable for Tailwind utility classes)
- [ ] T077 [P] Run Lighthouse audits on all 13 pages: verify accessibility score >= 90 (SC-004), test homepage above-the-fold render < 4 seconds on simulated 3G throttling (SC-003), and confirm total page weight < 2MB per page (plan.md constraint). Document results and fix any critical failures.

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies — start immediately
- **Foundational (Phase 2)**: Depends on Phase 1 completion — BLOCKS all page implementation
- **US1 Homepage (Phase 3)**: Depends on Phase 2 — establishes all component patterns (MVP)
- **US2 Teachers (Phase 4)**: Depends on Phase 2 — can run in parallel with US1 but benefits from US1's component patterns
- **US3 Programs (Phase 5)**: Depends on Phase 2 — independent of other stories
- **US4 How It Works (Phase 6)**: Depends on Phase 2 — independent of other stories
- **US5 About (Phase 7)**: Depends on Phase 2 — independent of other stories
- **US6 Contact (Phase 8)**: Depends on Phase 2 — independent of other stories
- **US7 FAQ (Phase 9)**: Depends on Phase 2 (accordion.js) — independent of other stories
- **US8 Blog (Phase 10)**: Depends on Phase 2 — independent of other stories
- **US9 Legal (Phase 11)**: Depends on Phase 2 — independent of other stories, can run in parallel with anything
- **Polish (Phase 12)**: Depends on ALL user story phases being complete

### User Story Dependencies

- **US1 (P1 - Homepage)**: Start first — establishes visual patterns for all other pages. Recommended to complete before other stories.
- **US2 (P1 - Teachers)**: Can start after Phase 2. Benefits from US1 component patterns (teacher cards, star ratings). Highest value after homepage.
- **US3 (P2 - Programs)**: Independent. Reuses card patterns established in US1/US2.
- **US4 (P2 - How It Works)**: Independent. Simple page, quick to implement.
- **US5 (P3 - About)**: Independent. Content-heavy, no interactive complexity.
- **US6 (P3 - Contact)**: Independent. Requires `forms.js` (built within this phase).
- **US7 (P3 - FAQ)**: Independent. Reuses `accordion.js` from Phase 2.
- **US8 (P3 - Blog)**: Independent. Requires Tailwind Typography plugin (included via CDN).
- **US9 (P4 - Legal)**: Independent. Simplest pages — parallel with anything.

### Within Each User Story

1. Create HTML page skeleton with meta/CDN includes first
2. Build sections top-to-bottom in page order
3. Page-specific JS (if any) before the sections that use it
4. Responsive verification as final task in each phase

### Parallel Opportunities

- **Phase 1**: T003 [P] can run in parallel with T001/T002
- **Phase 2**: T004-T009 are sequential (each builds on main.js state), except T009 (accordion.js) [implied P]
- **Phase 3 (US1)**: Tasks are sequential (building sections into one file)
- **Phase 4 (US2)**: T021 (filters.js) can run in parallel with T022-T026 (listing page)
- **Phase 5 (US3)**: T033 and T036 [P] (page skeletons can be created in parallel)
- **Phase 7 (US5)**: T046 [P] (page skeleton independent)
- **Phase 8 (US6)**: T049 (forms.js) and T050 [P] (page skeleton in parallel)
- **Phase 9 (US7)**: T055 [P] (page skeleton independent)
- **Phase 10 (US8)**: T059 and T062 [P] (both page skeletons in parallel)
- **Phase 11 (US9)**: T068 and T069 [P] (both legal pages in parallel)
- **Phase 12**: T072 and T073 [P] (different concerns, different files)
- **Cross-phase**: After Phase 2, US3-US9 can all proceed in parallel if team capacity allows

---

## Parallel Example: User Story 2

```text
# First, build the JS module in parallel with the listing page skeleton:
Task T021: "Implement filter/sort UI interaction logic in src/js/filters.js"    [parallel]
Task T022: "Create teachers listing page skeleton in src/teachers.html"         [parallel]

# Then build listing page sections sequentially (same file):
Task T023: "Build filter sidebar in src/teachers.html"
Task T024: "Build sorting bar in src/teachers.html"
Task T025: "Build 8 teacher cards in src/teachers.html"
Task T026: "Build collapsible mobile filter panel in src/teachers.html"

# Profile page can start as soon as T022 is done (different file):
Task T027: "Create teacher profile page skeleton in src/teacher-profile.html"   [parallel with T023-T026]
```

---

## Implementation Strategy

### MVP First (Homepage Only — Phases 1-3)

1. Complete Phase 1: Setup (Tailwind config, custom CSS, directory structure)
2. Complete Phase 2: Foundational (header/footer injection, mobile menu, sticky header, accordion)
3. Complete Phase 3: User Story 1 — Homepage
4. **STOP and VALIDATE**: Open `src/index.html` — homepage should be a fully functional Sana landing page with all 10 sections, working mobile menu, dismissible announcement bar, FAQ accordion, and responsive layout
5. This alone is a deliverable, demonstrable increment

### Incremental Delivery

1. **Setup + Foundational** → Shared infrastructure ready
2. **+ US1 (Homepage)** → MVP deliverable: complete Sana landing page
3. **+ US2 (Teachers)** → Core marketplace UX: teacher listing + profile
4. **+ US3 (Programs)** → Structured offerings: course listing + detail
5. **+ US4 (How It Works)** → Process clarity page
6. **+ US5-US7 (About, Contact, FAQ)** → Supporting pages for trust and leads
7. **+ US8 (Blog)** → SEO/content marketing pages
8. **+ US9 (Legal)** → Compliance pages
9. **+ Polish** → Final consistency, accessibility, SEO, edge cases

### Single Developer Strategy (Recommended)

Execute phases sequentially in priority order: 1 → 2 → 3 → 4 → 5 → 6 → 7 → 8 → 9 → 10 → 11 → 12. Each phase completion is a demonstrable increment.

---

## Notes

- [P] tasks = different files, no dependencies on incomplete tasks in the same phase
- [Story] label maps every page-building task to its user story for traceability
- Each user story produces viewable, navigable pages that work independently
- All pages share the same header/footer/mobile-menu from main.js — changes propagate automatically
- Realistic Sana demo content is required for every section (no lorem ipsum, no "placeholder text here")
- Commit after each completed phase for clean git history
- All interactive behaviors must be keyboard-accessible (Tab, Enter, Escape)
