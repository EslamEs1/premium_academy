# Tasks: Premium Arabic Academy Website Frontend

**Input**: Design documents from `/specs/004-premium-academy-frontend/`
**Prerequisites**: plan.md (required), spec.md (required), research.md, data-model.md, quickstart.md

**Tests**: No automated tests requested. Quality validation is manual per the spec acceptance criteria.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Static frontend**: `frontend/` at repository root
- HTML pages: `frontend/*.html`
- Custom CSS: `frontend/css/custom.css`
- JavaScript modules: `frontend/js/*.js`
- Assets: `frontend/assets/{images,icons,logos}/`

---

## Phase 1: Setup (Project Structure & Design System)

**Purpose**: Create the project directory structure, design system foundation (custom CSS, Tailwind config, fonts, icons, logos), and all shared assets that every page depends on.

- [x] T001 Create project directory structure: `frontend/`, `frontend/css/`, `frontend/js/`, `frontend/assets/images/`, `frontend/assets/icons/`, `frontend/assets/logos/` per plan.md
- [x] T002 Create `frontend/css/custom.css` with all custom CSS: scroll-triggered animation classes (`.animate-on-scroll`, `.animate-on-scroll.visible`, `.slide-left`, `.slide-right`), floating keyframe animations (`@keyframes float1/float2/float3`), marquee keyframe (`@keyframes scroll-marquee`), blue gradient utility class (`.bg-brand-gradient`), custom focus styles for accessibility, smooth scroll behavior, and RTL-aware base styles
- [x] T003 [P] Create `frontend/assets/icons/` with complete inline SVG icon library (20+ icons): subject icons (calculator, flask, atom, book, pen, brain, globe, graduation-cap), navigation icons (menu-hamburger, close-x, chevron-right, chevron-left, arrow-right, arrow-left), social media icons (instagram, twitter-x, tiktok, linkedin, youtube, facebook), utility icons (checkmark-circle, star-filled, star-half, phone, email, whatsapp, location-pin, clock, user, search, plus, minus), and educational icons (lightbulb, trophy, chart-up, shield-check). Each icon as a standalone `.svg` file with consistent 24x24 viewBox and `currentColor` fill.
- [x] T004 [P] Create `frontend/assets/logos/brand-logo.svg` — Arabic text-based brand logo "أكاديمية بريميوم" in blue (#2563EB) with clean, modern Arabic typography. Also create `frontend/assets/logos/brand-logo-white.svg` (white version for dark/gradient backgrounds).
- [x] T005 [P] Create 8 partner logo SVG placeholders in `frontend/assets/logos/`: `partner-1.svg` through `partner-8.svg`. Each a clean rounded rectangle with Arabic institution name text (جامعة الملك سعود, وزارة التعليم, جامعة الملك عبدالله, مؤسسة الراجحي, شركة جرير, المؤسسة الوطنية, هيئة التعليم, الصندوق التعليمي). Dimensions: 150x60px each.
- [x] T006 [P] Create `frontend/assets/logos/accreditation-badge.svg` — accreditation/certification badge SVG with Arabic text "معتمد" and institutional styling.
- [x] T007 [P] Create `frontend/assets/images/` placeholder system: CSS gradient-based teacher avatar templates (8 distinct warm gradient combinations — red #F51140, orange #FF8A2C, yellow #FFDE05, amber #F59E0B, teal #14B8A6, indigo #6366F1, pink #EC4899, blue #3B82F6) documented as Tailwind class combinations in a reference comment within `custom.css`.

**Checkpoint**: All directories, CSS, icons, logos, and assets exist. Any HTML page can be started.

---

## Phase 2: Foundational (Global Shell — Header, Footer, Mobile Menu, Shared JS)

**Purpose**: Build the global navigation shell (sticky header, 4-column footer, RTL mobile slide-out menu) and shared JavaScript modules that EVERY page requires. Create a reusable page template structure.

**⚠️ CRITICAL**: No page (user story) work can begin until this phase is complete.

- [x] T008 Create `frontend/js/main.js` — shared initialization module: DOMContentLoaded listener that initializes navigation, animations, and any page-specific modules. Import pattern using deferred script loading (no ES modules — use global function namespace for static HTML compatibility).
- [x] T009 Create `frontend/js/navigation.js` — sticky header behavior: scroll-based shadow toggle (add `shadow-md` class on scroll > 10px), active page highlighting in nav links (compare `window.location.pathname` with link `href`), hamburger menu toggle (open/close mobile sidebar, body scroll lock via `overflow-hidden` on `<body>`, backdrop click to close, Escape key to close). All RTL-aware with `transform: translateX()` sliding from the correct direction.
- [x] T010 Create `frontend/js/animations.js` — Intersection Observer module: observe all elements with `.animate-on-scroll` class, add `.visible` class when element enters viewport (threshold: 0.1), unobserve after triggering. Support `.slide-left` and `.slide-right` variants with corresponding CSS transitions defined in T002.
- [x] T011 Create the global page template by building `frontend/index.html` with ONLY the shared shell (no page-specific content yet). This template includes: complete `<head>` (charset, viewport, Arabic title, meta description in Arabic, Google Fonts preconnect + IBM Plex Sans Arabic CDN link, Tailwind CDN script with custom config extending fontFamily/colors, custom.css link), `<body class="font-arabic bg-white text-slate-900 leading-relaxed">`, complete sticky `<header>` (fixed, z-50, white bg, max-w-[1500px], 3-zone RTL layout: right=logo, center=6 nav links desktop-only, left=2 CTA buttons desktop-only + hamburger mobile-only), mobile slide-out `<aside>` (fixed, full-height, RTL slide from right, all nav links + CTAs + contact info + social icons), complete `<footer>` (blue-50 bg, rounded-t-3xl, max-w-[1500px], row 1: logo + 6 social icons, row 2: 4-column link grid with المزيد/القانونية/الدعم/الاعتماد columns, copyright line), and `<script defer>` tags for main.js, navigation.js, animations.js. `<html dir="rtl" lang="ar">`. `<main class="pt-[64px] md:pt-[80px]">` with empty content placeholder. All navigation links point to correct `.html` files. Footer links include all 12 pages + external links. Mobile menu includes all links + WhatsApp CTA.

**Checkpoint**: Opening `frontend/index.html` shows a working header, footer, and mobile menu. The shell is ready to be copied to all other pages. Navigation links exist (even if target pages don't yet).

---

## Phase 3: User Story 1 — Homepage (Priority: P1) 🎯 MVP

**Goal**: Build the complete 13-section homepage — the primary conversion and trust-building page that establishes all reusable component patterns.

**Independent Test**: Open `frontend/index.html` on mobile (375px) and desktop (1440px). Scroll top-to-bottom. Verify 13 distinct sections, all Arabic content, flawless RTL, prominent CTAs, trust signals distributed throughout, and ~5,500px scroll depth on desktop.

### Implementation for User Story 1

- [x] T012 [US1] Build homepage Section 1 (Hero) in `frontend/index.html`: two-column layout (lg:flex-row, stacked on mobile). Right column (RTL): H1 headline in Arabic (text-[22px] mobile / text-[48px] md / text-[54px] lg, font-bold), supporting paragraph, primary CTA button "سجّل الآن" (bg-blue-600, text-white, h-12, rounded-xl, text-xl), secondary CTA "احجز حصة تجريبية" (white bg, blue border, same dimensions), trust badge below CTAs (accreditation logo + "معتمدين من" text). Left column (RTL): hero educational illustration placeholder (CSS gradient or SVG) with 4-6 floating decorative SVG icon circles using float animation keyframes from custom.css. Minimum height 500px mobile, 600px desktop. Apply `.animate-on-scroll` to both columns.
- [x] T013 [US1] Build homepage Section 2 (Quick-Stats Trust Bar) in `frontend/index.html`: horizontal bar with bg-slate-50, 4 stat items in flex row (2x2 grid on mobile via grid-cols-2, 4 inline on md). Each stat: SVG icon (from assets/icons), bold Arabic number (+٥٠٠ معلم, +١٠,٠٠٠ طالب, +٥٠,٠٠٠ حصة, ٩٨٪ رضا), label text. Apply `.animate-on-scroll`.
- [x] T014 [US1] Build homepage Section 3 (Services Overview) in `frontend/index.html`: heading "خدماتنا التعليمية" centered, 3 service cards in horizontal scrollable row (flex, overflow-x-auto, xl:justify-center). Each card: w-[310px] h-[364px] md:w-[370px] md:h-[389px], bg-blue-500, rounded-3xl, white text, service title (font-bold), description paragraph (font-light), illustrative gradient/SVG image positioned at bottom. Cards: الدروس الخصوصية, دورات القدرات والتحصيلي, المناهج الدراسية. Apply `.animate-on-scroll`.
- [x] T015 [US1] Build homepage Section 4 (Partner Logos Carousel) in `frontend/index.html` and create `frontend/js/carousel.js`: heading "شركاؤنا في النجاح" centered. Logo track: flex row with 16 logo images (8 unique from assets/logos duplicated for seamless loop), each w-[150px] h-[60px]. CSS animation using `scroll-marquee` keyframe from custom.css (16s linear infinite, translateX -50%). Container: overflow-hidden. Apply `.animate-on-scroll` on heading.
- [x] T016 [US1] Build homepage Section 5 (Private Tutoring Deep-Dive) in `frontend/index.html`: outer heading "ادرس مع معلمك الخصوصي" + subheading. Large rounded card (rounded-[20px] md:rounded-[40px]) with blue gradient background (.bg-brand-gradient from custom.css). Two-column layout inside: right column (RTL) = inner heading (white, bold), 2 yellow pill tags (rounded-full, bg-yellow-400, text-slate-900: "المنهاج الوطني", "IB/IGCSE"), 6 bullet points with yellow checkmark SVG icon (from assets/icons) and white font-light text, yellow CTA button "اعرف أكثر عن الدروس الخصوصية" (bg-yellow-400, text-slate-900, rounded-xl, h-[48px] md:h-[56px]). Left column (RTL) = feature illustration placeholder. Apply `.slide-right`.
- [x] T017 [US1] Build homepage Section 6 (Exam Prep Deep-Dive) in `frontend/index.html`: same visual pattern as Section 5 but with distinct content. Heading "تغلب على اختبارات القدرات والتحصيلي". Tags: "القدرات الكمي", "القدرات اللفظي", "التحصيلي". 6 bullet points covering exam-specific features. Yellow CTA "اكتشف دورات القدرات والتحصيلي". Different illustration. Apply `.slide-left`.
- [x] T018 [US1] Build homepage Section 7 (Subject Browser) in `frontend/index.html`: heading "استكشف المواد الدراسية" centered. Grid of 8 subject cards (grid-cols-2 sm:grid-cols-3 lg:grid-cols-4 gap-4). Each card: rounded-2xl, bg-white, shadow-md hover:shadow-lg transition, subject SVG icon (from assets/icons), Arabic subject name (font-bold), grade level text (text-sm, text-slate-500). Subjects: الرياضيات, الفيزياء, الكيمياء, اللغة الإنجليزية, اللغة العربية, الأحياء, القدرات, التحصيلي. Apply `.animate-on-scroll`.
- [x] T019 [US1] Build homepage Section 8 (Teacher Showcase) in `frontend/index.html`: heading "تعرّف على معلمينا" centered. Grid of 8 teacher cards (grid-cols-2 sm:grid-cols-3 lg:grid-cols-4 gap-2 lg:gap-6). Each teacher card: rounded-2xl overflow-hidden, photo container with warm gradient background (unique per card from the 8 gradient colors in T007), Arabic name (font-bold, text-base md:text-lg), primary subject (text-slate-500, text-sm), experience years, star rating with filled star icon, student count, CTA link "عرض الملف" → teacher-profile.html. Group hover: name turns blue-600. All 8 teachers from data-model.md with complete data. "عرض جميع المعلمين" link at bottom → teachers.html. Apply `.animate-on-scroll`.
- [x] T020 [US1] Build homepage Section 9 (Student Testimonials) in `frontend/index.html`: heading "ماذا يقول طلابنا" centered. Horizontal scrollable row (flex, overflow-x-auto, gap-4 lg:gap-6). 6 testimonial cards: w-[280px] md:w-[340px], bg-white, rounded-2xl, shadow-md, p-6. Each card: gradient avatar circle with initials, student name (font-bold), grade level + subject (text-sm, text-slate-500), star rating (5 filled stars), review text (2-3 Arabic sentences, text-base, leading-relaxed). All 6 testimonials from data-model.md with realistic Arabic names and reviews. Apply `.animate-on-scroll`.
- [x] T021 [US1] Build homepage Section 10 (How It Works Preview) in `frontend/index.html`: heading "كيف تبدأ رحلتك التعليمية" centered. 4 steps in horizontal row (flex, gap-8, stacked on mobile). Each step: numbered circle (w-12 h-12, bg-blue-600, text-white, rounded-full, font-bold), SVG icon below, Arabic title (font-bold), short description (text-slate-500). Steps: ١. اختر المادة, ٢. اختر المعلم, ٣. احجز الحصة, ٤. ابدأ التعلم. Visual connector lines between steps (RTL direction — dashed border or SVG). CTA "ابدأ الآن" button at bottom (blue primary). Apply `.animate-on-scroll`.
- [x] T022 [US1] Build homepage Section 11 (FAQ Preview) in `frontend/index.html` and create `frontend/js/accordion.js`: heading "الأسئلة الشائعة" centered. Accordion with 10 FAQ items from data-model.md (selecting 2 from each of the 5 categories). Each item: bg-slate-50, rounded-[20px], mt-3, cursor-pointer. Question bar: flex justify-between, py-7 px-5, question text (font-bold, text-base lg:text-[22px]), toggle "+" icon (text-[40px], font-thin, leading-none). Answer panel: hidden by default, bg-slate-50, rounded-b-[20px], px-8 pb-8, text-base lg:text-xl font-medium. JS: single-open behavior (clicking one closes others), smooth max-height transition (300ms ease), keyboard support (Enter/Space), aria-expanded toggle. "عرض جميع الأسئلة" link at bottom → faq.html. Apply `.animate-on-scroll` on the accordion container.
- [x] T023 [US1] Build homepage Section 12 (Platform Promotion) in `frontend/index.html`: large rounded card with blue gradient background (.bg-brand-gradient), rounded-[20px] lg:rounded-[40px]. Two-column layout: right column (RTL) = heading "معك في كل مكان" (white, bold, text-[34px]), subheading (white), two app store badge images (Google Play + App Store SVG badges, dir="ltr", w-[205px] each, side by side). Left column (RTL) = device mockup placeholder (phone outline SVG or gradient container showing "platform screenshot" concept). Apply `.animate-on-scroll`.
- [x] T024 [US1] Build homepage Section 13 (Closing CTA) in `frontend/index.html`: bg-slate-50, full-width, py-20. Centered content: compelling Arabic headline "لا تفوّت فرصة التفوق الدراسي" (text-[28px] md:text-4xl, font-bold), supporting paragraph, primary CTA "سجّل الآن" (blue, large, h-14, text-xl), optional WhatsApp CTA button (bg-[#25D366], white text, WhatsApp icon, "تواصل عبر الواتساب"). Small trust text below: "انضم إلى أكثر من ١٠,٠٠٠ طالب". Apply `.animate-on-scroll`.

**Checkpoint**: Homepage is complete with 13 sections. Open on mobile and desktop. All Arabic content present. All interactive elements work (accordion, carousel, animations, mobile menu). The Saudi Parent Test passes.

---

## Phase 4: User Story 2 — Teachers Pages (Priority: P2)

**Goal**: Build the Teachers listing page and Teacher profile page — the second-highest trust factor after the homepage.

**Independent Test**: Navigate to `frontend/teachers.html`. Verify 8 teacher cards with complete data. Click a card. Verify `frontend/teacher-profile.html` has 8 sections with biography, reviews, and booking CTA.

### Implementation for User Story 2

- [x] T025 [US2] Build `frontend/teachers.html` — copy the global shell from `index.html` (header, footer, mobile menu, all head includes). Update `<title>` and meta description to Arabic teachers page text. Update nav active state to highlight المعلمون. Set `<main>` content.
- [x] T026 [US2] Build teachers.html Section 1 (Hero): H1 "المعلمون" (centered, bold, hero size), subtitle describing teacher quality, trust stat badges inline ("+٥٠٠ معلم معتمد", "٤.٨ تقييم متوسط"). Background: white with subtle decorative element.
- [x] T027 [US2] Build teachers.html Section 2 (Subject Filter Bar): horizontal scrollable row of pill buttons (rounded-full, bg-slate-50 default, bg-blue-600 text-white active). Pills: الكل, الرياضيات, الفيزياء, الكيمياء, الإنجليزية, العربية, الأحياء, القدرات, التحصيلي. JS filter behavior: clicking a pill filters teacher cards by `data-subject` attribute. "الكل" shows all. Add filter logic to `frontend/js/main.js` (or a new inline script block).
- [x] T028 [US2] Build teachers.html Section 3 (Teacher Grid): grid-cols-2 sm:grid-cols-3 lg:grid-cols-4 gap-4 lg:gap-6. 8 teacher cards — IDENTICAL HTML/class structure to homepage teacher cards (T019) for consistency. Each card has `data-subject` attribute for filtering. All 8 teachers with complete data from data-model.md. Each card links to `teacher-profile.html`.
- [x] T029 [US2] Build teachers.html Sections 4-6: Section 4 = Trust stats (total teachers, average rating, total sessions — large bold numbers, bg-slate-50). Section 5 = Testimonials (reuse exact card pattern from homepage T020, show 4 testimonials). Section 6 = Registration CTA (reuse pattern from homepage T024 closing CTA).
- [x] T030 [US2] Build `frontend/teacher-profile.html` — copy global shell from index.html. Update title/meta to teacher name. Add breadcrumb: الرئيسية > المعلمون > [اسم المعلم].
- [x] T031 [US2] Build teacher-profile.html Section 1 (Profile Header): large layout with teacher photo placeholder (128px circle with gradient background and Arabic initials), teacher Arabic name (H1, text-3xl, font-bold), title/honorific, subjects taught as pills (rounded-full, bg-blue-100, text-blue-700), experience badge ("١٠ سنوات خبرة", bg-yellow-100, text-yellow-800, rounded-full), star rating, student count, price "يبدأ من ١٥٠ ر.س/الحصة". Primary CTA "احجز حصة" (blue, prominent).
- [x] T032 [US2] Build teacher-profile.html Sections 2-4: Section 2 = Biography (2-3 paragraphs of realistic Arabic text about teaching philosophy, qualifications, university degree, years of experience, teaching approach). Section 3 = Subjects & Grades (grid of subject+grade pill combinations, e.g., "الرياضيات — ثانوي", "الفيزياء — متوسط"). Section 4 = Student Reviews (4-6 review cards with student name, rating, date "١٥ مارس ٢٠٢٦", Arabic review text 2-3 sentences — unique content per review).
- [x] T033 [US2] Build teacher-profile.html Sections 5-8: Section 5 = Teaching Stats (4-item stats bar: حصص مكتملة, عدد الطلاب, التقييم, سنوات في المنصة). Section 6 = Availability Preview (styled weekly grid showing available slots or "تواصل معنا لحجز موعد مناسب" message). Section 7 = Related Teachers (3-4 teacher cards using same card pattern, different teachers from same subject). Section 8 = Booking CTA section (gradient bg, "احجز حصتك الأولى الآن", blue CTA, WhatsApp CTA).

**Checkpoint**: Teachers listing shows 8 cards with filter. Teacher profile has 8 complete sections. All Arabic content. All components consistent with homepage.

---

## Phase 5: User Story 3 — How It Works, Pricing, FAQ (Priority: P3)

**Goal**: Build the process clarity (How It Works), pricing transparency (Pricing), and concern resolution (FAQ) pages — the final trust barriers before conversion.

**Independent Test**: Open each of the 3 pages. Verify section counts (6, 5+, 5). Verify step flow is RTL. Verify pricing tiers differentiate clearly. Verify FAQ accordion works with 15+ categorized questions.

### Implementation for User Story 3

- [x] T034 [US3] Build `frontend/how-it-works.html` — copy global shell, update title/meta, set nav active state. Build Section 1 (Hero): H1 "كيف يعمل", subtitle "ابدأ رحلتك التعليمية في خطوات بسيطة", supportive illustration placeholder.
- [x] T035 [US3] Build how-it-works.html Section 2 (Step-by-Step Process): 4-6 numbered steps in responsive layout (horizontal on lg, vertical on mobile). Each step: numbered circle (w-16 h-16, bg-blue-600, text-white, text-2xl, rounded-full), large SVG icon, Arabic title (font-bold, text-xl), description paragraph (text-slate-500). Steps flow RTL with dashed connector lines (border-dashed, border-blue-200). Steps: ١. اختر المادة والمرحلة, ٢. تصفح المعلمين واختر الأنسب, ٣. حدد الموعد المناسب, ٤. احضر الحصة أونلاين, ٥. تابع تقدمك مع التقارير, ٦. حقق التفوق الدراسي.
- [x] T036 [US3] Build how-it-works.html Sections 3-6: Section 3 = Platform Benefits (6 benefit cards in grid-cols-2 lg:grid-cols-3: معلمون معتمدون, مواعيد مرنة, تقارير دورية, حصص مسجلة, دعم متواصل, مناهج محدثة — each with icon, title, description). Section 4 = Student Success Stories (2-3 testimonial cards, reuse pattern). Section 5 = Parent Section (content addressing parents: how to monitor progress, communication channels, reporting frequency — 2-3 paragraphs). Section 6 = Getting Started CTA (blue CTA + trial lesson CTA).
- [x] T037 [US3] Build `frontend/pricing.html` — copy global shell, update title/meta, set nav active. Build Section 1 (Hero): H1 "الأسعار والباقات", subtitle "خطط مرنة تناسب احتياجاتك".
- [x] T038 [US3] Build pricing.html Section 2 (Pricing Tiers): 3 pricing cards in flex row (stacked on mobile). Each card: rounded-2xl, bg-white, shadow-lg, p-8. Card fields: plan name Arabic (font-bold, text-2xl), price "١٥٠ ر.س / الحصة" (text-4xl, font-bold, text-blue-600), feature list (8 items with checkmark/x icons), CTA button. Plans: الباقة الأساسية (150 SAR, basic features), الباقة المميزة (isPopular=true, 200 SAR, yellow accent border or blue gradient bg, "الأكثر طلبًا" badge), الباقة الاحترافية (300 SAR, all features). Popular plan visually distinct (scale-105, ring-2 ring-yellow-400 or bg-gradient).
- [x] T039 [US3] Build pricing.html Sections 3-6: Section 3 = Feature Comparison (table or grid comparing the 3 plans across 8-10 features with checkmarks). Section 4 = Billing FAQ (5 pricing-specific questions using accordion pattern from T022: payment methods, refund policy, discounts, trial lessons, package upgrades). Section 5 = Testimonials (reuse pattern). Section 6 = Registration CTA.
- [x] T040 [US3] Build `frontend/faq.html` — copy global shell, update title/meta, set nav active. Build Section 1 (Hero): H1 "الأسئلة الشائعة", subtitle, decorative search input (styled but non-functional — no backend).
- [x] T041 [US3] Build faq.html Section 2 (Category Tabs): horizontal scrollable tab bar (flex, overflow-x-auto on mobile). 5 tabs: الكل, عام, الأسعار, المعلمون, الجدولة/المنصة. Each tab: rounded-full, px-6 py-2, bg-slate-100 default, bg-blue-600 text-white active. JS: clicking tab filters FAQ items by `data-category` attribute. "الكل" shows all. Add tab logic to main.js or inline script.
- [x] T042 [US3] Build faq.html Section 3 (Full Accordion): all 15 FAQ questions from data-model.md spec, each with `data-category` attribute matching its category. Use identical accordion HTML/class structure from homepage (T022) for consistency. Each question has a substantive Arabic answer (3-5 sentences). Reuse `accordion.js` module. Questions organized: 3 عام, 3 الأسعار, 3 المعلمون, 3 الجدولة, 3 المنصة.
- [x] T043 [US3] Build faq.html Sections 4-5: Section 4 = Contact CTA ("لم تجد إجابتك؟ تواصل معنا" with WhatsApp button bg-[#25D366] and email link). Section 5 = Related Quick Links (3 cards linking to How It Works, Pricing, Contact — each with icon, title, short description).

**Checkpoint**: How It Works has 6 sections with RTL step flow. Pricing has 3 differentiated tiers. FAQ has 15 categorized questions with working tabs and accordion. All Arabic content present.

---

## Phase 6: User Story 4 — About & Contact Pages (Priority: P4)

**Goal**: Build the institutional credibility (About) and accessibility (Contact) pages that complete the trust picture for parents performing due diligence.

**Independent Test**: Open About page — verify 7 sections including team and stats. Open Contact page — verify form with Arabic validation, contact info cards, and mini FAQ.

### Implementation for User Story 4

- [x] T044 [US4] Build `frontend/about.html` — copy global shell, update title/meta, set nav active. Build Section 1 (Hero): H1 "من نحن", subtitle about the academy's mission, bg-slate-50 or illustration.
- [x] T045 [US4] Build about.html Section 2 (Mission & Vision): two-column layout (stacked on mobile). رسالتنا: icon + 2-3 sentences about mission. رؤيتنا: icon + 2-3 sentences about vision. Each in a card with bg-white, rounded-2xl, shadow-sm, p-8.
- [x] T046 [US4] Build about.html Section 3 (Our Story): narrative section with 3-4 paragraphs of Arabic text about founding, growth, commitment to Saudi education. Include milestones (تأسيس ٢٠٢١, +١٠,٠٠٠ طالب في ٢٠٢٤, etc.) in a timeline or narrative format.
- [x] T047 [US4] Build about.html Sections 4-7: Section 4 = Team (4-6 team member cards in grid-cols-2 lg:grid-cols-3: gradient avatar + Arabic name + title + 1-sentence bio, from data-model.md). Section 5 = Platform Statistics (4 large bold numbers in horizontal bar, reuse stats pattern). Section 6 = Partners & Accreditation (partner logo grid + accreditation badge, reuse logos from assets/). Section 7 = Join CTA "انضم إلى عائلة أكاديمية بريميوم" (blue CTA).
- [x] T048 [US4] Build `frontend/contact.html` — copy global shell, update title/meta, set nav active. Build Section 1 (Hero): H1 "تواصل معنا", subtitle "نسعد بتواصلك معنا".
- [x] T049 [US4] Build contact.html Section 2 (Contact Form) and create `frontend/js/forms.js`: RTL-aligned form with `novalidate` attribute. Fields: الاسم الكامل (text, required), البريد الإلكتروني (email, required), رقم الجوال (tel, +966 prefix, dir="ltr" on input), الموضوع (select dropdown with 5 Arabic options), الرسالة (textarea, required, min 20 chars). Submit button "أرسل الرسالة" (blue primary). `forms.js`: prevent default submit, validate each field, show Arabic error messages below fields in red (text-red-500), show success modal/message "تم إرسال رسالتك بنجاح" on valid submission. All labels, placeholders, and error messages in Arabic.
- [x] T050 [US4] Build contact.html Sections 3-6: Section 3 = Contact Info Cards (grid-cols-2 lg:grid-cols-4: هاتف card with phone icon + +966-11-XXX-XXXX, بريد إلكتروني card with email icon + info@premiumacademy.sa, واتساب card with WhatsApp icon + green "تواصل الآن" button, العنوان card with location icon + الرياض, المملكة العربية السعودية). Section 4 = Operating Hours (أوقات العمل: السبت–الخميس ٨ صباحًا – ١٠ مساءً, الجمعة: مغلق). Section 5 = Mini FAQ (4-5 contact-related questions using accordion: "كيف أتواصل بسرعة؟", "ما هي أوقات الدعم الفني؟", "هل يمكنني زيارة المقر؟", "كم يستغرق الرد على الرسائل؟"). Section 6 = Map placeholder (decorative gradient area with Saudi Arabia outline or location pin illustration).

**Checkpoint**: About page has 7 sections with team and stats. Contact page has working form with Arabic validation. All trust elements present.

---

## Phase 7: User Story 5 — Blog & Legal Pages (Priority: P5)

**Goal**: Build the blog listing, blog article, Terms of Service, and Privacy Policy pages — content marketing and legal compliance foundation.

**Independent Test**: Open blog listing — verify 6 article cards. Open blog article — verify full Arabic content. Open Terms and Privacy — verify structured legal content.

### Implementation for User Story 5

- [x] T051 [P] [US5] Build `frontend/blog.html` — copy global shell, update title/meta. Build Sections 1-2: Hero (H1 "المدونة", subtitle) + Featured article (large card: full-width, gradient thumbnail, large title, excerpt, author, date, "اقرأ المزيد" CTA → blog-post.html).
- [x] T052 [US5] Build blog.html Sections 3-5: Section 3 = Article Grid (6 article cards in grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6. Each card: gradient thumbnail, Arabic title (font-bold), 2-line excerpt, author name, date "١٥ مارس ٢٠٢٦", category tag pill. All 6 articles from data-model.md with realistic Arabic educational titles and excerpts). Section 4 = Category filter bar (pills: الكل, تعليم, نصائح دراسية, القدرات والتحصيلي, أخبار المنصة). Section 5 = "تحميل المزيد" button (decorative — disabled state, bg-slate-100).
- [x] T053 [P] [US5] Build `frontend/blog-post.html` — copy global shell, update title/meta. Section 1 = Article header: H1 Arabic title (font-bold, text-3xl lg:text-4xl), breadcrumb (الرئيسية > المدونة > [عنوان المقال]), meta row (author + date + category tag + "٥ دقائق قراءة"). Section 2 = Article body: 4-5 paragraphs of realistic Arabic educational content about a topic like "نصائح للتفوق في اختبار القدرات" with H2/H3 subheadings, bullet lists, blockquote, proper line-height (leading-relaxed) and paragraph spacing. Section 3 = Author bio card (gradient avatar, name, title, 2-sentence bio). Section 4 = Related articles (3 article cards from the blog grid). Section 5 = Registration CTA.
- [x] T054 [P] [US5] Build `frontend/terms.html` — copy global shell, update title/meta. Hero: H1 "الشروط والأحكام", "آخر تحديث: ١ يناير ٢٠٢٦". Body: 8+ numbered sections with Arabic legal content. Sections: ١. نطاق الاستخدام, ٢. إنشاء الحسابات, ٣. الرسوم والمدفوعات, ٤. سياسة الاسترداد, ٥. حقوق الملكية الفكرية, ٦. الخصوصية والبيانات, ٧. إنهاء الخدمة, ٨. التعديلات, ٩. القانون المطبق, ١٠. التواصل. Each section: H2 heading, 2-3 Arabic paragraphs with realistic legal content. Use proper `<ol>`, `<ul>`, and heading hierarchy.
- [x] T055 [P] [US5] Build `frontend/privacy.html` — copy global shell, update title/meta. Hero: H1 "سياسة الخصوصية", "آخر تحديث: ١ يناير ٢٠٢٦". Body: 8+ sections: ١. البيانات التي نجمعها, ٢. كيف نستخدم بياناتك, ٣. مشاركة البيانات, ٤. ملفات تعريف الارتباط, ٥. أمان البيانات, ٦. حقوقك, ٧. خصوصية الأطفال, ٨. التعديلات على السياسة, ٩. التواصل. Each section: H2 heading, 2-3 Arabic paragraphs. Realistic Saudi-context privacy policy content.

**Checkpoint**: Blog listing shows 6 articles. Blog post has full Arabic content. Terms and Privacy have structured legal content. All pages have consistent header/footer.

---

## Phase 8: User Story 6 — Cross-Page QA, Navigation Consistency & Polish (Priority: P6)

**Goal**: Comprehensive quality assurance pass across all 12 pages. Verify constitution quality gates, cross-page consistency, responsive behavior, and the Saudi Parent Test on every page.

**Independent Test**: Navigate between all 12 pages using header, footer, and internal links. Verify everything works at 375px, 768px, 1440px, and 1920px.

### Implementation for User Story 6

- [x] T056 [US6] Cross-page header/footer consistency audit: verify the sticky header and 4-column footer are IDENTICAL in HTML structure, link targets, and styling across all 12 HTML pages. Fix any discrepancies. Verify active page highlighting works correctly on each page (the current page's nav link should have distinct styling).
- [x] T057 [US6] Cross-page internal link verification: click every link in every header, footer, mobile menu, breadcrumb, and inline CTA across all 12 pages. Verify all links resolve to the correct page. Fix any broken or incorrect links. Verify all "عرض جميع المعلمين", "عرض جميع الأسئلة", "اقرأ المزيد", and similar cross-page CTAs link correctly.
- [x] T058 [US6] Mobile menu verification on all 12 pages: open the mobile menu on each page at 375px viewport. Verify it slides in from the correct RTL direction, shows all nav links, shows CTAs, closes on backdrop click, closes on Escape key, locks body scroll. Fix any page where the menu behaves differently.
- [x] T059 [US6] RTL correctness audit across all 12 pages: systematically check every page at 1440px for LTR leakage — misaligned elements, wrong text alignment, incorrect icon direction, broken flex/grid under RTL. Specific checks: form inputs right-aligned, breadcrumbs flow RTL, step connectors point RTL, card grids flow RTL, footer columns ordered correctly. Fix all issues.
- [x] T060 [US6] Responsive breakpoint audit at 375px (mobile): check every page for horizontal overflow (none permitted), touch target sizing (minimum 44x44px on all buttons and links), font sizes (minimum 14px), CTA visibility (no hidden/tiny CTAs), image overflow, and content readability. Fix all issues.
- [x] T061 [US6] Responsive breakpoint audit at 768px (tablet) and 1920px (large desktop): verify card grids adapt correctly (2→3 cols on tablet), hero layouts transition properly, content stays centered within max-w-[1500px] on large displays (no edge-to-edge stretching), footer columns display correctly. Fix all issues.
- [x] T062 [US6] Interactive elements verification: test ALL accordions (homepage FAQ, pricing FAQ, contact FAQ, full FAQ page) — verify single-open behavior, smooth animation, keyboard support. Test ALL scroll-triggered animations — verify they fire once on scroll into view. Test partner logo marquee — verify seamless loop. Test teacher subject filter — verify it filters correctly. Test FAQ category tabs — verify they filter correctly. Test contact form — verify Arabic validation messages. Fix any broken interactions.
- [x] T063 [US6] Arabic content proofread across all 12 pages: review every visible Arabic text element for naturalness, fluency, and cultural appropriateness. Check: no Lorem Ipsum, no English placeholders, no machine translation artifacts, consistent terminology (same Arabic term for same concept across pages), consistent numeral style, correct curriculum terms (القدرات, التحصيلي), correct currency (ر.س). Fix any content issues.
- [x] T064 [US6] Trust signal density verification: confirm every page has trust elements distributed throughout (not concentrated in one section). Homepage: 6+ trust layers. Teachers: credentials on every card. About: stats + team + partners. Contact: accessibility signals. FAQ: proactive concern resolution. Footer (every page): accreditation + legal links + social presence. Add missing trust elements where needed.
- [x] T065 [US6] Section count verification against spec minimums: Homepage ≥13, Teachers ≥5, Teacher Profile ≥7, About ≥7, How It Works ≥6, Pricing ≥5, Contact ≥5, FAQ ≥5, Blog Listing ≥4, Blog Article ≥5. Count sections on each page. Add missing sections where any page falls short.
- [x] T066 [US6] Accessibility final pass: verify all `<img>` tags have Arabic `alt` text, all icon-only buttons have `aria-label` in Arabic, all interactive elements are keyboard-accessible with visible focus states (focus:ring-2 focus:ring-blue-500), color contrast meets WCAG 2.1 AA on all text elements. Add `loading="lazy"` to all below-fold images. Fix all issues.
- [x] T067 [US6] Saudi Parent Test: open every page on a 375px mobile viewport. For each page, answer: "Would a Saudi parent browsing this page at 10pm believe this is a real academy?" If any page fails, identify specific deficiencies (thin sections, weak content, missing trust signals, broken layout) and fix them.

**Checkpoint**: ALL 12 pages pass all quality gates. The site feels like a cohesive, premium, commercially credible Arabic education platform.

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies — start immediately
- **Foundational (Phase 2)**: Depends on Phase 1 — BLOCKS all user stories
- **US1 Homepage (Phase 3)**: Depends on Phase 2 — establishes all component patterns
- **US2 Teachers (Phase 4)**: Depends on Phase 3 (teacher card, testimonial, CTA patterns)
- **US3 How It Works / Pricing / FAQ (Phase 5)**: Depends on Phase 3 (accordion, CTA, benefit card patterns)
- **US4 About / Contact (Phase 6)**: Depends on Phase 3 (stats bar, partner logos, CTA patterns)
- **US5 Blog / Legal (Phase 7)**: Depends on Phase 2 (needs only global shell, not homepage components)
- **US6 QA & Polish (Phase 8)**: Depends on ALL previous phases

### User Story Dependencies

- **US1 (P1)**: Can start after Phase 2. No dependencies on other stories.
- **US2 (P2)**: Can start after US1 (reuses teacher card and testimonial patterns).
- **US3 (P3)**: Can start after US1 (reuses accordion, CTA, and card patterns).
- **US4 (P4)**: Can start after US1 (reuses stats bar, partner logos, and CTA patterns).
- **US5 (P5)**: Can start after Phase 2 (only needs global shell; blog/legal don't reuse homepage component patterns heavily). Could run in parallel with US2-US4.
- **US6 (P6)**: Must wait for ALL stories to complete.

### Within Each User Story

- Copy global shell first (header/footer from index.html)
- Build hero section first (establishes page identity)
- Build content sections in visual order (top to bottom)
- Content-heavy sections before interactive sections
- Each story complete before moving to next priority

### Parallel Opportunities

- Phase 1: T003, T004, T005, T006, T007 can all run in parallel (different files)
- Phase 7: T051, T053, T054, T055 can run in parallel (different HTML files)
- After US1 completes: US2, US3, US4 could run in parallel if staffed
- US5 (Blog/Legal) could run in parallel with US2-US4

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup (T001–T007)
2. Complete Phase 2: Foundational (T008–T011)
3. Complete Phase 3: User Story 1 / Homepage (T012–T024)
4. **STOP and VALIDATE**: Open homepage on mobile and desktop
5. The homepage alone is a deployable, demonstrable MVP

### Incremental Delivery

1. Setup + Foundational → Foundation ready
2. Add Homepage (US1) → Test → Deploy/Demo (MVP!)
3. Add Teachers (US2) → Test → Deploy/Demo
4. Add How It Works + Pricing + FAQ (US3) → Test → Deploy/Demo
5. Add About + Contact (US4) → Test → Deploy/Demo
6. Add Blog + Legal (US5) → Test → Deploy/Demo
7. Cross-page QA (US6) → Final polish → Deploy

### Parallel Team Strategy

With multiple developers after US1:

- Developer A: US2 (Teachers)
- Developer B: US3 (How It Works / Pricing / FAQ)
- Developer C: US4 (About / Contact) + US5 (Blog / Legal)
- All developers: US6 (QA) — each reviews the others' pages

---

## Notes

- [P] tasks = different files, no dependencies on incomplete tasks
- [Story] label maps task to specific user story for traceability
- Each user story is independently completable and testable
- Global shell (header/footer) is copy-pasted across pages — no server-side includes
- Commit after each completed task or logical group of tasks
- Stop at any checkpoint to validate story independently
- Arabic content quality is as important as visual quality — proofread continuously
- The "Saudi Parent Test" is the ultimate quality gate for every page
