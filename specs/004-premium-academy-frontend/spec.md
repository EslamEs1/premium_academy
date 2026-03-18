# Feature Specification: Premium Arabic Academy Website Frontend

**Feature Branch**: `004-premium-academy-frontend`
**Created**: 2026-03-18
**Status**: Draft
**Input**: User description: "Premium Arabic academy website frontend — a complete,
section-rich, trust-heavy, commercially credible marketing and enrollment website
for a Saudi-market private tutoring academy. Arabic-first, RTL-default, built
with HTML + CSS + Tailwind CSS + native JavaScript only. Inspired by the depth,
polish, and premium educational confidence of leading Arabic edtech platforms."

---

## User Scenarios & Testing _(mandatory)_

### User Story 1 — Saudi Parent Discovers the Academy Homepage (Priority: P1)

A Saudi parent searching for private tutoring options lands on the academy
homepage. They scroll through the entire page, absorbing the value
proposition, service offerings, teacher showcase, trust signals, student
testimonials, FAQ, and closing CTA. By the end, they feel confident
this is a real, premium educational platform and click "سجّل الآن"
(Register Now) or "احجز حصة تجريبية" (Book a Trial Lesson).

**Why this priority**: The homepage is the primary conversion page.
80%+ of first-time visitors will form their trust impression here.
Without a compelling, section-rich, trust-heavy homepage, no other
page matters.

**Independent Test**: Open the homepage on both mobile (375px) and
desktop (1440px). Scroll from top to bottom. Verify that every
required section is present, content is in natural Arabic, RTL
layout is flawless, CTAs are prominent, and the overall impression
passes the "Saudi parent test" — would a parent believe this is a
real academy?

**Acceptance Scenarios**:

1. **Given** a visitor loads the homepage on desktop, **When** they
   scroll from top to bottom, **Then** they encounter a minimum of
   12 distinct content sections including hero, stats bar, services
   overview, partner logos, service deep-dives, teacher showcase,
   testimonials, how-it-works, FAQ, and closing CTA.

2. **Given** a visitor loads the homepage on mobile (375px width),
   **When** they scroll through the page, **Then** all sections are
   fully visible, no horizontal overflow exists, touch targets meet
   44x44px minimum, and CTAs are prominent and tap-friendly.

3. **Given** the homepage is loaded, **When** a visitor inspects any
   visible text, **Then** all content is in natural Arabic with no
   Lorem Ipsum, no English placeholder text, and no machine
   translation artifacts.

4. **Given** the homepage hero section is visible, **When** a visitor
   reads the hero, **Then** they see a compelling Arabic headline,
   a supporting description, a primary CTA button, a secondary CTA
   button, and at least one trust indicator (stat badge or
   accreditation mark).

---

### User Story 2 — Parent Explores Teachers and Subjects (Priority: P2)

A Saudi parent who was impressed by the homepage navigates to the
Teachers page to browse available tutors. They filter or browse by
subject and grade level, view teacher cards with credentials, and
click into a teacher profile to read their biography, see reviews,
and find a booking CTA.

**Why this priority**: Teacher credibility is the second-highest
trust factor after the homepage impression. Parents need to see
qualified, experienced teachers before committing.

**Independent Test**: Navigate to the Teachers listing page. Verify
that a grid of teacher cards is displayed with complete data fields
(name, photo, subject, experience, rating, CTA). Click a teacher
card and verify the profile page loads with biography, reviews,
subjects, and booking CTA.

**Acceptance Scenarios**:

1. **Given** a visitor navigates to the Teachers page, **When** the
   page loads, **Then** they see a hero section, a grid of minimum
   8 teacher cards, subject filter/browse capability, and a trust
   stats section.

2. **Given** a teacher card is displayed, **When** a visitor
   inspects it, **Then** it shows: Arabic name, profile photo,
   primary subject, experience years, star rating, student count,
   and a "عرض الملف" (View Profile) CTA.

3. **Given** a visitor clicks a teacher card, **When** the teacher
   profile page loads, **Then** it contains: header with photo and
   name, biography section, subjects taught list, student reviews
   with Arabic text, availability preview, booking CTA, and
   related teachers section.

---

### User Story 3 — Parent Learns How It Works and Reads FAQ (Priority: P3)

A parent interested but not yet convinced visits the How It Works
page and the FAQ page to understand the enrollment process and
get answers to their concerns about online tutoring quality,
pricing, scheduling, and teacher qualifications.

**Why this priority**: Process clarity and concern resolution are
the final trust barriers before conversion. Parents who understand
the process and have concerns addressed are significantly more
likely to register.

**Independent Test**: Navigate to the How It Works page and verify
it contains a step-by-step visual process. Navigate to the FAQ page
and verify it contains categorized, expandable questions with
substantive Arabic answers.

**Acceptance Scenarios**:

1. **Given** a visitor opens the How It Works page, **When** they
   scroll through, **Then** they see a hero section, a 4–6 step
   visual process (browse → book → learn → succeed), a benefits
   section, testimonials, and a registration CTA.

2. **Given** a visitor opens the FAQ page, **When** they view the
   accordion, **Then** they see minimum 12 questions organized by
   category (general, pricing, teachers, scheduling, platform),
   each expandable with a substantive Arabic answer.

3. **Given** a visitor clicks an FAQ question, **When** the
   accordion expands, **Then** the answer animates smoothly open
   with Arabic text that directly addresses the question with
   specific, helpful information.

---

### User Story 4 — Parent Reviews About Page and Contact (Priority: P4)

A parent who wants to verify the academy's legitimacy visits the
About page to understand the mission, team, and credentials, then
navigates to the Contact page to find communication channels.

**Why this priority**: About and Contact pages complete the trust
picture. They are lower-traffic than the homepage but critical
for parents performing due diligence before financial commitment.

**Independent Test**: Open the About page — verify mission,
vision, team, stats, partners, and CTA sections. Open the Contact
page — verify contact form, contact info, WhatsApp link, and FAQ.

**Acceptance Scenarios**:

1. **Given** a visitor opens the About page, **When** they scroll
   through, **Then** they see: hero, mission/vision, team section,
   platform statistics, partner logos, accreditation, and CTA.

2. **Given** a visitor opens the Contact page, **When** they view
   the page, **Then** they see: a contact form with Arabic labels
   and RTL input, phone number, email, WhatsApp link, office
   address, operating hours, and a mini FAQ section.

---

### User Story 5 — Visitor Browses Pricing and Blog (Priority: P5)

A visitor evaluating options checks the Pricing page for cost
clarity and browses the Blog for educational content, building
further trust in the academy's expertise.

**Why this priority**: Pricing transparency aids conversion
decisions. Blog content supports SEO and positions the academy as
a thought leader. Both are important but rely on the core pages
(homepage, teachers, FAQ) being solid first.

**Independent Test**: Open the Pricing page — verify pricing
tiers, comparison features, FAQ, and CTA. Open the Blog listing
page — verify article cards with titles, excerpts, and categories.

**Acceptance Scenarios**:

1. **Given** a visitor opens the Pricing page, **When** they view
   the content, **Then** they see: hero, pricing tiers (minimum 2–3
   plans), feature comparison, FAQ about billing, testimonials, and
   registration CTA.

2. **Given** a visitor opens the Blog page, **When** the page loads,
   **Then** they see: hero section, grid of article cards with Arabic
   titles, excerpts, author, date, and category tags.

---

### User Story 6 — Cross-Page Navigation and Global Elements (Priority: P6)

A visitor navigates between multiple pages using the sticky header
navigation, footer links, and internal CTAs. The global header,
footer, and navigation feel consistent, polished, and complete
across every page.

**Why this priority**: Navigation consistency and footer depth are
baseline quality indicators. Broken or inconsistent navigation
destroys trust even if individual pages are well-designed.

**Independent Test**: Navigate between all implemented pages using
both header and footer links. Verify header stays fixed, footer is
identical across pages, mobile menu works on all pages, and all
internal links resolve correctly.

**Acceptance Scenarios**:

1. **Given** a visitor is on any page, **When** they look at the
   header, **Then** they see: a fixed sticky header with logo,
   primary CTA (registration), secondary CTA (sign-in), and
   navigation links — all consistent across every page.

2. **Given** a visitor scrolls to the footer of any page, **When**
   they inspect the footer, **Then** they see: minimum 4 columns
   (company links, legal/policies, support, accreditation), social
   media icons, accreditation logos, and consistent styling.

3. **Given** a visitor is on mobile, **When** they tap the menu
   icon, **Then** a full-featured RTL slide-out menu opens with
   smooth animation, showing all navigation links, CTAs, and
   contact information.

---

### Edge Cases

- What happens when a visitor loads the site on an ultra-wide
  display (> 2560px)? Content MUST remain constrained to max-width
  and centered — no edge-to-edge stretching.

- What happens when Arabic text contains embedded English terms
  (e.g., "IELTS", "IGCSE")? Bidirectional text MUST render
  correctly without breaking line flow.

- What happens when a visitor has JavaScript disabled? All content
  MUST be visible and readable. Interactive elements (accordions,
  carousels) degrade gracefully — content is accessible even if
  animations do not run.

- What happens on very slow connections? Images MUST have proper
  `alt` text in Arabic. The page structure MUST be usable before
  images fully load.

- What happens when a visitor uses keyboard navigation? All
  interactive elements MUST be keyboard-accessible with visible
  focus states.

---

## Requirements _(mandatory)_

### 1. Sitemap / Page Architecture

The website MUST implement the following page hierarchy:

**Primary pages (MUST implement in this phase)**:

- **الرئيسية** (Homepage) — `index.html`
- **من نحن** (About) — `about.html`
- **المعلمون** (Teachers listing) — `teachers.html`
- **ملف المعلم** (Teacher profile) — `teacher-profile.html`
- **كيف يعمل** (How It Works) — `how-it-works.html`
- **الأسعار** (Pricing) — `pricing.html`
- **تواصل معنا** (Contact) — `contact.html`
- **الأسئلة الشائعة** (FAQ) — `faq.html`
- **المدونة** (Blog listing) — `blog.html`
- **مقال المدونة** (Blog article) — `blog-post.html`

**Secondary pages (MUST implement in this phase)**:

- **الشروط والأحكام** (Terms of Service) — `terms.html`
- **سياسة الخصوصية** (Privacy Policy) — `privacy.html`

**Anticipated but NOT implemented this phase** (MUST appear in
navigation as disabled links or "قريبًا" indicators):

- **المواد** (Subjects listing)
- **تفاصيل المادة** (Subject detail)
- **احجز حصة تجريبية** (Trial booking form)
- **لوحة تحكم الطالب** (Student dashboard)
- **لوحة تحكم المعلم** (Teacher dashboard)

### 2. Homepage Section-by-Section Structure

The homepage MUST contain a minimum of 13 distinct sections in the
following order (minor reordering permitted if trust-building arc
is preserved):

**Section 1 — Hero**

- Full-width hero with blue gradient or white background
- Compelling Arabic H1 headline (40–54px desktop, 22–28px mobile)
- Supporting description paragraph (16–18px)
- Primary CTA button: "سجّل الآن" or "ابدأ رحلتك التعليمية"
  (blue, prominent, h-12)
- Secondary CTA button: "احجز حصة تجريبية" or "تعرّف على المعلمين"
  (white with blue border)
- Trust indicator: accreditation badge, "المنصة الأكثر ثقة" badge,
  or student count floating badge
- Right side (RTL context): educational illustration or photography
  with floating decorative SVG elements and subtle animation
- Minimum height: 500px mobile, 600px desktop

**Section 2 — Quick-Stats Trust Bar**

- Compact horizontal bar with 4 key statistics
- Statistics: teacher count (+٥٠٠ معلم), student count (+١٠٬٠٠٠
  طالب), lesson count (+٥٠٬٠٠٠ حصة), satisfaction rate (٩٨٪ رضا)
- Arabic-formatted numbers, bold typography
- Subtle background differentiation (slate-50 or light border)
- Each stat with an icon and a label

**Section 3 — Services Overview**

- 3 service category cards in a horizontal row (scrollable on
  mobile, centered on desktop)
- Card 1: الدروس الخصوصية (Private Tutoring)
- Card 2: دورات القدرات والتحصيلي (Exam Preparation)
- Card 3: المناهج الدراسية (Curriculum Content)
- Each card: blue background (rounded-3xl), white text, heading,
  description, illustrative image at bottom
- Card dimensions: ~310x364px mobile, ~370x389px desktop

**Section 4 — Partner/Trust Logos Carousel**

- Heading: "شركاؤنا في النجاح" or similar
- Auto-scrolling infinite marquee of 8+ institutional logos
- Logos: universities, government bodies, corporate partners
  (use realistic placeholder names and clean SVG/image logos)
- Seamless loop animation (16s linear infinite)
- Clean, minimal visual treatment

**Section 5 — Featured Service: Private Tutoring Deep-Dive**

- Large rounded card (rounded-[20px] md:rounded-[40px])
- Blue gradient background (linear-gradient ~260deg,
  #2563EB to #3B82F6)
- Two-column layout: text content + feature image
- Inner heading in white bold text
- 2–3 yellow pill tags (e.g., "المنهاج الوطني", "IB/IGCSE")
- 6 bullet points with yellow checkmark icons describing features
- Yellow CTA button: "اعرف أكثر عن الدروس الخصوصية"
- Feature image: educational illustration on the left side (RTL)

**Section 6 — Featured Service: Exam Preparation Deep-Dive**

- Same visual pattern as Section 5 but with distinct content
- Focus on القدرات (Qudurat) and التحصيلي (Tahsili) exam prep
- 6 bullet points covering exam-specific features
- Yellow CTA: "اكتشف دورات القدرات والتحصيلي"
- Feature image: different illustration from Section 5
- Background: same blue gradient for visual consistency

**Section 7 — Subject/Category Browser**

- Heading: "استكشف المواد الدراسية"
- Grid or horizontal scroll of subject category cards
- Minimum 8 subjects: الرياضيات, الفيزياء, الكيمياء,
  اللغة الإنجليزية, اللغة العربية, الأحياء, القدرات, التحصيلي
- Each card: subject icon, Arabic name, grade level indicator
- Cards link to subject detail (or disabled with "قريبًا" for
  unimplemented subjects)

**Section 8 — Teacher Showcase**

- Heading: "تعرّف على معلمينا"
- Grid of 8 featured teacher cards (2 cols mobile, 3 cols tablet,
  4 cols desktop)
- Each card: teacher photo with colored gradient overlay, Arabic
  name (bold), primary subject, experience years, star rating
- Cards link to teacher profile page
- "عرض جميع المعلمين" link/button at bottom linking to
  teachers.html

**Section 9 — Student Testimonials**

- Heading: "ماذا يقول طلابنا"
- Horizontal scrollable row of 4–6 testimonial cards
- Each card: student name (Arabic), grade level, subject,
  star rating, review text (2–3 Arabic sentences), profile
  photo placeholder
- Cards styled with white background, rounded-2xl, subtle shadow
- Alternatively: video testimonial placeholders (blue rounded
  cards with play button overlay)

**Section 10 — How It Works Preview**

- Heading: "كيف تبدأ رحلتك التعليمية"
- 4-step visual process in a horizontal row
- Steps: ١. اختر المادة → ٢. اختر المعلم → ٣. احجز الحصة →
  ٤. ابدأ التعلم
- Each step: numbered circle, icon, Arabic title, short description
- Visual connector lines or arrows between steps (RTL direction)
- CTA button at bottom: "ابدأ الآن"

**Section 11 — FAQ Preview**

- Heading: "الأسئلة الشائعة"
- Accordion with minimum 10 questions covering:
  - Account creation and registration
  - Pricing and payment methods
  - Trial lessons
  - Teacher qualifications
  - Session scheduling and flexibility
  - Curriculum alignment
  - Session recording
  - Refund policy
  - Technical requirements
  - Parent progress reports
- Each question: slate-50 background, rounded-[20px], bold text,
  "+" toggle icon, expandable answer
- "عرض جميع الأسئلة" link to full FAQ page

**Section 12 — App/Platform Promotion**

- Blue gradient card (same gradient pattern)
- Heading: "معك في كل مكان" or similar
- Sub-heading about platform accessibility
- App store badges (Google Play + App Store) or platform feature
  showcase
- Device mockup image (phone/tablet showing the platform)

**Section 13 — Closing CTA**

- Full-width section with compelling Arabic headline
- "لا تفوّت فرصة التفوق الدراسي" or similar
- Primary CTA button (large, blue, prominent)
- Optional: WhatsApp contact CTA (green button)
- Trust reinforcement: small stat or guarantee text

### 3. Global Header Requirements

- Fixed/sticky header, `position: fixed`, `z-index: 50+`,
  white background
- Maximum content width: 1500px, centered with auto margins
- Three-zone layout:
  - Right zone (RTL visual): Logo (30px mobile, 44px desktop)
  - Center zone: Navigation links (desktop only):
    الرئيسية, المعلمون, المواد, كيف يعمل, الأسعار, تواصل معنا
  - Left zone (RTL visual): Primary CTA "سجّل الآن" (blue) +
    Secondary CTA "تسجيل الدخول" (outlined)
- Mobile: Logo + hamburger menu icon. CTAs hidden.
- Mobile menu: Full-featured RTL slide-out sidebar with all
  navigation links, CTAs, contact info, social links, smooth
  open/close animation (300ms ease)
- Header height: ~64px mobile, ~80px desktop
- Page content MUST have top padding matching header height

### 4. Global Footer Requirements

- Background: blue-50 (#EFF6FF) with rounded-t-3xl top corners
- Maximum content width: 1500px, centered
- Footer row 1: Logo (larger version, ~188px) + 6 social media
  icons (Instagram, Twitter/X, TikTok, LinkedIn, YouTube,
  Facebook) in circular white buttons with blue icon color
- Footer row 2: 4-column link grid (responsive: stacks on mobile)
  - Column 1 — "المزيد" (More): عن الأكاديمية, المعلمون,
    المدونة, وظائف, تواصل معنا, مركز المساعدة (6–7 links)
  - Column 2 — "القانونية" (Legal): شروط الاستخدام, سياسة
    الخصوصية, سياسة ملفات تعريف الارتباط, سياسة الاسترداد,
    النزاهة الأكاديمية (5–6 links)
  - Column 3 — "الدعم" (Support): الأسئلة الشائعة, تواصل معنا,
    واتساب (with icon), هاتف (with number) (4–5 links)
  - Column 4 — "الاعتماد" (Accreditation): Accreditation logo +
    "عرض شهادة الاعتماد" link + decorative Saudi educational
    context element
- Column headings: blue-600 text, bold, text-[22px]
- Link styling: slate-700 text, hover:text-blue-500, text-base to
  text-lg, whitespace-nowrap, mb-4 spacing
- Mobile column reordering: Accreditation first (visual priority),
  then More, Legal, Support
- Copyright line at bottom: "© ٢٠٢٦ أكاديمية بريميوم. جميع
  الحقوق محفوظة."

### 5. Trust Sections

Trust elements MUST be distributed across the entire site, not
concentrated in a single section:

**Homepage trust layer**:

- Hero: Accreditation badge + student count floating element
- Stats bar: 4 quantitative metrics
- Partner logos carousel: 8+ institutional logos
- Teacher showcase: Credentials on every card
- Testimonials: Named student reviews with context
- FAQ: Proactive concern resolution

**Teacher page trust layer**:

- Total teacher count stat
- Average rating stat
- Credential display on every card
- Student review excerpts

**About page trust layer**:

- Platform statistics (large, bold numbers)
- Team section with photos and titles
- Partner logos (repeated)
- Accreditation display (repeated)
- Mission/vision establishing institutional presence

**Footer trust layer (every page)**:

- Accreditation logo and certificate link
- Legal policy links (demonstrates professionalism)
- Social media presence (demonstrates activity)
- Contact channels (demonstrates accessibility)

### 6. Featured Teachers / Programs Presentation Rules

**Teacher Card (Listing Page)**:

- Profile photo/avatar in rounded container with colored gradient
  background (warm gradients: red, orange, amber, yellow families)
- Arabic name in bold (text-base to text-lg)
- Primary subject taught
- Experience years (e.g., "١٠ سنوات خبرة")
- Star rating (e.g., "٤.٩ ★")
- Student count (e.g., "٢٣٠ طالب")
- Price indicator: "يبدأ من ١٥٠ ر.س/الحصة"
- CTA: "عرض الملف" or "احجز حصة"
- Hover: Name changes to blue-600, subtle shadow increase
- Grid: 2 cols mobile, 3 cols tablet, 4 cols desktop

**Teacher Profile Page** (minimum 7 sections):

1. Header: Large photo, name, title, subjects, experience badge
2. Biography: 2–3 paragraphs of Arabic text about teaching
   philosophy, qualifications, and approach
3. Subjects & Grades: Grid of subject pills with grade levels
4. Student Reviews: 4–6 review cards with student name, rating,
   date, and Arabic review text
5. Teaching Stats: Sessions completed, student count, average
   rating, years on platform
6. Availability Preview: Weekly schedule grid or "contact to
   schedule" messaging
7. Related Teachers: 3–4 teacher cards for similar subjects
8. Booking CTA: Prominent blue CTA section at bottom

**Program/Course Cards** (if displayed):

- Course title in Arabic
- Teacher name
- Duration (e.g., "١٢ حصة")
- Schedule indicator
- Price
- Level indicator (مبتدئ, متوسط, متقدم)
- Gradient background matching teacher card style

### 7. FAQ Experience

**Full FAQ Page** (minimum 5 sections):

1. Hero: Heading "الأسئلة الشائعة", subtitle, search-style
   input (decorative — no backend)
2. Category tabs/filters: عام, الأسعار, المعلمون, الجدولة,
   المنصة
3. Accordion: Minimum 15 questions total (3+ per category)
4. Contact CTA: "لم تجد إجابتك؟ تواصل معنا" with WhatsApp
   and email links
5. Related quick links: Links to How It Works, Pricing, Contact

**FAQ Accordion Behavior**:

- Each item: slate-50 background, rounded-[20px], cursor pointer
- Question: bold text (text-base mobile, text-[22px] desktop),
  slate-900 color
- Toggle icon: "+" character (text-[40px], font-thin), rotates or
  changes to "−" on expand
- Answer panel: slides open with smooth animation (300ms ease),
  text in text-base to text-xl, font-medium, slate-900
- Only one question open at a time (accordion behavior)
- Answer padding: px-8 pb-8

**FAQ Content Requirements** (minimum 15 questions):

- كيف أسجل في المنصة؟
- ما هي تكلفة الحصص الخصوصية؟
- هل يمكنني حجز حصة تجريبية مجانية؟
- كيف يتم اختيار المعلمين؟
- ما هي مؤهلات المعلمين؟
- هل يمكنني تغيير المعلم بعد البدء؟
- ما هي المواد المتوفرة؟
- هل تغطون مناهج القدرات والتحصيلي؟
- كيف أحجز موعد الحصة؟
- هل يمكنني إلغاء أو إعادة جدولة الحصة؟
- هل يتم تسجيل الحصص؟
- ما هي طرق الدفع المتاحة؟
- هل هناك سياسة استرداد؟
- هل يمكن للوالدين متابعة تقدم أبنائهم؟
- ما هي المتطلبات التقنية لحضور الحصص؟

### 8. About Page Structure

Minimum 7 sections:

1. **Hero**: "من نحن" heading, compelling subtitle about the
   academy's mission, background image or illustration
2. **Mission & Vision**: Two-column or stacked layout with
   mission statement (رسالتنا) and vision statement (رؤيتنا),
   each with an icon and 2–3 sentences of Arabic text
3. **Our Story**: Timeline or narrative section telling the
   academy's founding story, growth milestones, and commitment
   to Saudi education (3–4 paragraphs)
4. **Team Section**: Grid of 4–6 team member cards with photo,
   Arabic name, title, and 1-sentence bio
5. **Platform Statistics**: Large bold numbers section:
   +٥٠٠ معلم, +١٠٬٠٠٠ طالب, +٥٠٬٠٠٠ حصة, +٥ سنوات خبرة
6. **Partners & Accreditation**: Partner logo grid + accreditation
   badge (repeated from homepage for trust reinforcement)
7. **Join CTA**: "انضم إلى عائلة أكاديمية بريميوم" with
   registration CTA button

### 9. How-It-Works Page Structure

Minimum 6 sections:

1. **Hero**: "كيف يعمل" heading, subtitle explaining the
   simplicity of the process, supportive illustration
2. **Step-by-Step Process**: 4–6 numbered steps with icons,
   Arabic titles, and descriptions. Visual flow connectors.
   Steps: اختر المادة → اختر المعلم → حدد الموعد →
   احضر الحصة → تابع تقدمك → حقق التفوق
3. **Platform Benefits**: Grid of 6 benefit cards with icons:
   معلمون معتمدون, مواعيد مرنة, تقارير دورية, حصص مسجلة,
   دعم متواصل, مناهج محدثة
4. **Student Success Stories**: 2–3 testimonial cards with
   before/after narrative
5. **Parent Section**: Content addressing parents directly:
   how they can monitor progress, communication channels,
   reporting frequency
6. **Getting Started CTA**: "ابدأ رحلتك الآن" with primary
   registration CTA and trial lesson CTA

### 10. Contact Page Structure

Minimum 5 sections:

1. **Hero**: "تواصل معنا" heading, subtitle welcoming inquiries
2. **Contact Form**: RTL-aligned form with Arabic labels:
   - الاسم الكامل (Full Name) — text input
   - البريد الإلكتروني (Email) — email input
   - رقم الجوال (Mobile) — tel input with +966 prefix
   - الموضوع (Subject) — select dropdown
   - الرسالة (Message) — textarea
   - Submit button: "أرسل الرسالة" (blue primary CTA)
   - All labels in Arabic, placeholders in Arabic, validation
     messages in Arabic
3. **Contact Information Cards**: Grid of 3–4 cards:
   - هاتف: +966-XX-XXX-XXXX
   - بريد إلكتروني: info@premiumacademy.sa
   - واتساب: رابط مباشر (with green WhatsApp icon)
   - العنوان: الرياض, المملكة العربية السعودية
4. **Operating Hours**: أوقات العمل section with daily schedule
5. **Mini FAQ**: 4–5 contact-related questions in accordion
6. **Map placeholder**: Decorative map section or office
   location visual

### 11. Blog and Legal Page Structure

**Blog Listing Page** (minimum 4 sections):

1. Hero: "المدونة" heading, subtitle
2. Featured article: Large card with image, title, excerpt, date
3. Article grid: 6+ article cards (2 cols mobile, 3 cols desktop)
   with: thumbnail image, Arabic title (bold), excerpt (2 lines),
   author name, date, category tag
4. Categories sidebar or filter bar: تعليم, نصائح دراسية,
   القدرات والتحصيلي, أخبار المنصة
5. Pagination or "تحميل المزيد" button

**Blog Article Page** (minimum 5 sections):

1. Article header: Title (H1), author, date, category, reading
   time estimate, share buttons
2. Article body: Rich Arabic content with headings, paragraphs,
   bullet lists, blockquotes (minimum 4–5 paragraphs of realistic
   Arabic educational content)
3. Author bio card: Photo, name, title, short bio
4. Related articles: 3 article cards
5. CTA: Registration or newsletter signup

**Terms of Service Page**:

- Hero with "الشروط والأحكام" heading
- Structured legal content with Arabic headings and numbered
  sections covering: scope, accounts, payments, refunds,
  intellectual property, privacy reference, termination,
  modifications, contact
- Last updated date
- Minimum 8 legal sections with substantive Arabic text

**Privacy Policy Page**:

- Same structure as Terms but focused on: data collection, data
  usage, data sharing, cookies, security measures, user rights,
  contact for privacy concerns
- Minimum 8 sections with substantive Arabic text

### 12. Visual System Expectations

**Color Palette**:

- Primary: Deep blue #2563EB (blue-600) for CTAs, links, headers
- Primary gradient: linear-gradient(260.66deg, #2563EB 23.6%,
  #3B82F6 78.5%) for feature sections
- Accent: Warm yellow #FACC15 (yellow-400) for secondary CTAs,
  tags, highlights
- Text primary: slate-900 (#0F172A)
- Text secondary: slate-500 to slate-700
- Background primary: white (#FFFFFF)
- Background alternate: slate-50 (#F8FAFC)
- Footer background: blue-50 (#EFF6FF)
- Success/positive: emerald-500 (ratings, checkmarks)
- WhatsApp: #25D366

**Spacing System**:

- Section vertical spacing: mt-10 (40px) mobile, mt-20 to mt-28
  (80–112px) desktop
- Section padding: px-4 mobile, px-6 tablet, px-16 desktop
- Max content width: max-w-[1500px] mx-auto
- Card gap: gap-2 mobile, gap-4 tablet, gap-6 desktop

**Border Radius System**:

- Feature cards: rounded-[20px] mobile, rounded-[40px] desktop
- Standard cards: rounded-2xl (16px) to rounded-3xl (24px)
- Buttons: rounded-md (6px) to rounded-xl (12px)
- Pills/tags: rounded-full
- FAQ items: rounded-[20px]
- Footer: rounded-t-3xl (top only)

**Shadow System**:

- Cards: shadow-md to shadow-lg
- Floating elements: box-shadow with wide spread and low opacity
- Buttons: no shadow (flat design with color contrast)

**Animation System**:

- Scroll-triggered entrance: fade-in (opacity 0→1, translateY
  20px→0, 600ms ease-out)
- Slide-left and slide-right for alternating content
- Partner logo marquee: continuous horizontal scroll (16s linear
  infinite)
- Floating hero elements: gentle vertical bob (3–5s infinite)
- Accordion: height transition (300ms ease)
- Hover transitions: 200–300ms on all interactive elements
- Mobile menu: slide-in from right (RTL), 300ms ease

### 13. Arabic Typography and RTL Behavior Requirements

**Font Stack**:

- Primary: "IBM Plex Arabic", "Tajawal", "Cairo", sans-serif
  (load via Google Fonts CDN)
- Load weights: 300 (light), 400 (regular), 500 (medium),
  600 (semibold), 700 (bold)

**Typography Scale**:

- Hero H1: text-[22px] mobile → text-[48px] md → text-[54px] lg
- Section headings: text-[22px] mobile → text-[28px] md →
  text-4xl lg
- Card headings: text-base to text-lg
- Body text: text-base (16px) as minimum
- Section descriptions: text-[22px] for prominent descriptions
- CTA text: text-lg to text-xl
- Caption/meta: text-sm (14px)
- FAQ toggle icon: text-[40px]

**Font Weights by Context**:

- Headings: font-bold (700)
- CTA buttons: font-medium (500)
- Body text: font-normal (400)
- Supporting text: font-light (300)
- FAQ questions: font-bold (700)
- FAQ answers: font-medium (500)

**Line Height**:

- Body text: leading-relaxed (1.75) minimum
- Headings: leading-tight (1.25) to leading-snug (1.375)
- FAQ toggle: leading-none (for the "+" icon)

**RTL Rules**:

- `<html dir="rtl" lang="ar">` on every page
- All Tailwind flex/grid flows respect RTL automatically via
  `dir="rtl"`
- Directional icons (arrows, chevrons) MUST be mirrored
- `dir="ltr"` used only for: app store badges, specific English
  brand elements
- Form inputs: text-align right by default
- No hard-coded `left`/`right` without RTL consideration
- Bidirectional text: use `dir` attributes on mixed-content spans

### 14. Responsive Rules

**Breakpoints**:

- Base: < 640px (mobile-first default)
- sm: 640px+ (large mobile / small tablet)
- md: 768px+ (tablet)
- lg: 1024px+ (desktop)
- xl: 1280px+ (large desktop)

**Layout Adaptations**:

- Card grids: 1 col → 2 col (sm) → 3 col (lg) → 4 col (xl)
- Hero: stacked (mobile) → side-by-side (lg)
- Service deep-dive: stacked (mobile) → two-column (lg)
- Stats bar: 2x2 grid (mobile) → 4 inline (md)
- Footer: stacked columns (mobile) → 4-column grid (md)
- FAQ: full-width on all breakpoints
- Teacher cards: 2 col (mobile) → 3 col (md) → 4 col (lg)

**Mobile-Specific Rules**:

- Hero CTAs: full-width stacked buttons
- Navigation: slide-out sidebar menu (not dropdown)
- Carousels: horizontal scroll with momentum
- Cards in service overview: horizontal scroll
- All touch targets: minimum 44x44px
- No horizontal overflow on any viewport
- Font sizes MUST NOT drop below 14px for any visible text

### 15. Component Inventory

The following reusable components MUST be designed and implemented
consistently across all pages:

**Navigation Components**:

- `StickyHeader` — fixed header with logo, nav, CTAs
- `MobileMenu` — RTL slide-out sidebar
- `Footer` — 4-column footer with social, legal, accreditation
- `Breadcrumb` — RTL breadcrumb trail (for inner pages)

**Card Components**:

- `TeacherCard` — photo, name, subject, stats, CTA
- `ServiceCard` — icon/image, title, description (blue bg)
- `TestimonialCard` — photo, name, rating, review text
- `ArticleCard` — thumbnail, title, excerpt, meta
- `SubjectCard` — icon, subject name, grade indicator
- `TeamMemberCard` — photo, name, title, bio excerpt
- `StatCard` — icon, number, label (for stats sections)
- `PricingCard` — plan name, price, features list, CTA
- `StepCard` — number, icon, title, description (how-it-works)
- `BenefitCard` — icon, title, description

**Section Components**:

- `HeroSection` — reusable hero with heading, description, CTAs
- `StatsBar` — horizontal stats display
- `LogoCarousel` — auto-scrolling partner logos
- `ServiceDeepDive` — blue gradient card with features + image
- `FAQAccordion` — expandable question/answer list
- `CTASection` — closing conversion section
- `TestimonialSlider` — horizontal scrollable testimonials

**Form Components**:

- `TextInput` — RTL text input with Arabic label
- `EmailInput` — email input with Arabic validation
- `PhoneInput` — phone input with +966 prefix
- `SelectDropdown` — RTL dropdown with Arabic options
- `TextArea` — RTL textarea with Arabic placeholder
- `SubmitButton` — form submission CTA

**Interactive Components**:

- `Accordion` — expandable panel (FAQ, collapsible sections)
- `Carousel` — horizontal scroll with optional auto-play
- `Modal` — centered overlay (for future use)
- `Tabs` — horizontal tab navigation (for FAQ categories)
- `ScrollAnimation` — Intersection Observer fade/slide trigger

### 16. Content Tone Rules in Arabic

**Voice**: The academy speaks as a confident, warm educational
authority. Not corporate. Not casual. Premium professional with
a personal touch.

**Headline Style**:

- Direct, compelling, action-oriented
- Examples: "ابدأ رحلتك مع أفضل المعلمين", "تفوّق مع
  أكاديمية بريميوم", "نجاحك يبدأ من هنا"
- Avoid: vague promises, overly formal diction, English loanwords
  where Arabic alternatives exist

**CTA Text Style**:

- Arabic imperative verbs: ابدأ, سجّل, احجز, تعرّف, اكتشف
- Confident and direct: "سجّل الآن", "احجز حصتك", "ابدأ مجانًا"
- Avoid: passive voice, weak language, "click here" equivalents

**Body Copy Style**:

- Modern Standard Arabic (فصحى حديثة)
- Short sentences (15–25 words)
- Active voice preferred
- Address both students and parents
- Educational terminology aligned with Saudi MOE conventions

**Number Formatting**:

- Use Arabic-European numerals (0123456789) for statistics and
  prices — more commonly used in Saudi digital contexts
- Thousands separator: comma (١٠,٠٠٠ or 10,000)
- Currency: ر.س (before or after the number)

**Prohibited Content Patterns**:

- Lorem Ipsum in any visible section
- English placeholder text
- Machine translation artifacts
- Generic "Student A" testimonials
- Empty "coming soon" blocks in shipped sections
- Transliteration inconsistency (same concept in Arabic in one
  place and English in another)

### 17. SEO-Ready Structure

**Per-Page Requirements**:

- Unique `<title>` tag in Arabic (50–60 characters)
- Unique `<meta name="description">` in Arabic (150–160 chars)
- `<meta property="og:title">` and `og:description` in Arabic
- `<meta property="og:image">` with appropriate social image
- `<html lang="ar" dir="rtl">` on every page
- Single `<h1>` per page, sequential heading hierarchy
- Semantic HTML5: `<header>`, `<nav>`, `<main>`, `<section>`,
  `<article>`, `<aside>`, `<footer>`
- `alt` attributes in Arabic on all `<img>` tags
- Internal links with descriptive Arabic anchor text
- Clean URL structure: `/teachers.html`, `/about.html`, etc.

**Structured Data Readiness**:

- Clean heading hierarchy supports future Schema.org markup
- Teacher cards structured for future Person/EducationalOrganization
  schema
- FAQ markup ready for future FAQPage schema
- Article pages structured for future Article schema

**Performance Considerations**:

- Images: use `loading="lazy"` on below-fold images
- Fonts: preconnect to Google Fonts CDN
- Tailwind: CDN or single compiled CSS file
- Minimal JavaScript: loaded defer or at end of body

### 18. Acceptance Criteria

Every delivered page MUST pass ALL of the following criteria:

**Content Completeness**:

- [ ] All visible text is in natural, fluent Arabic
- [ ] No Lorem Ipsum, placeholder text, or "coming soon" blocks
- [ ] All statistics use realistic numbers
- [ ] All teacher profiles have complete data
- [ ] All testimonials have Arabic names and realistic reviews
- [ ] FAQ answers are substantive and helpful

**RTL Correctness**:

- [ ] `dir="rtl"` and `lang="ar"` on every page's `<html>` tag
- [ ] No LTR leakage in any layout element
- [ ] All directional icons properly mirrored
- [ ] Form inputs right-aligned with Arabic labels
- [ ] Navigation flows right-to-left
- [ ] Bidirectional text renders correctly

**Visual Quality**:

- [ ] Typography hierarchy correctly applied (6 size levels)
- [ ] Color palette consistent (blue primary, yellow accent)
- [ ] Section backgrounds alternate rhythmically
- [ ] Rounded corners consistent per component type
- [ ] Scroll-triggered animations implemented
- [ ] Hover states on all interactive elements

**Section Density**:

- [ ] Homepage: minimum 13 sections
- [ ] Teachers page: minimum 5 sections
- [ ] Teacher profile: minimum 7 sections
- [ ] About page: minimum 7 sections
- [ ] How It Works: minimum 6 sections
- [ ] FAQ page: minimum 5 sections
- [ ] Contact page: minimum 5 sections
- [ ] Blog listing: minimum 4 sections
- [ ] Blog article: minimum 5 sections
- [ ] Pricing: minimum 5 sections

**Trust Signals**:

- [ ] Stats bar on homepage with 4 metrics
- [ ] Partner logos carousel with 8+ logos
- [ ] Accreditation badge in hero and footer
- [ ] Teacher credentials on every teacher card
- [ ] Student testimonials with Arabic names and reviews
- [ ] FAQ addressing real parent concerns

**Responsive Quality**:

- [ ] Mobile (375px): all content visible, no horizontal overflow
- [ ] Tablet (768px): appropriate grid adaptations
- [ ] Desktop (1440px): full layout with side-by-side sections
- [ ] Large desktop (1920px): content centered, not stretched
- [ ] Touch targets: minimum 44x44px on mobile
- [ ] Mobile menu: full-featured RTL slide-out

**Navigation & Footer**:

- [ ] Sticky header consistent across all pages
- [ ] Mobile menu functional with smooth animation
- [ ] Footer 4-column layout consistent across all pages
- [ ] All internal links functional
- [ ] Active page highlighted in navigation

**Code Quality**:

- [ ] Semantic HTML5 elements used throughout
- [ ] Single H1 per page, sequential heading hierarchy
- [ ] Tailwind classes organized by concern
- [ ] JavaScript modular and minimal
- [ ] No framework dependencies
- [ ] Pages function when opened directly from filesystem

**The Saudi Parent Test**:

- [ ] A Saudi parent browsing on their phone at 10pm would believe
      this is a real, operational academy where they can enroll
      their child

---

## Assumptions

- The academy name "أكاديمية بريميوم" (Premium Academy) is used
  as a working title. The actual brand name can be changed later
  without structural impact.

- Teacher data, testimonials, statistics, and FAQ answers use
  realistic but fictional content. All content is authored
  specifically for this project — not copied from any existing
  platform.

- Partner logos and accreditation badges use clean placeholder
  designs (SVG rectangles with institution names) until real
  partner agreements are established.

- Pricing displayed is illustrative (e.g., "يبدأ من ١٥٠ ر.س")
  and can be updated when real pricing is finalized.

- The site targets Saudi Arabia as the primary market. Currency
  is SAR, academic terms follow Saudi MOE conventions, cultural
  context is Saudi/Gulf.

- All forms are frontend-only (no backend submission). Forms
  display Arabic validation messages but do not process data.
  Form structure supports future backend integration.

- Blog articles contain realistic educational content written
  for demonstration purposes. Content establishes the tone and
  depth expected from real articles.

---

## Key Entities

- **Teacher**: Arabic name, profile photo, biography, subjects
  taught (list), grade levels (list), experience years, student
  count, star rating, price range, availability status

- **Subject**: Arabic name, icon, description, grade levels
  covered, related teachers (list), curriculum alignment indicator

- **Testimonial**: Student Arabic name, grade level, subject
  studied, star rating, review text in Arabic, profile photo

- **Article**: Arabic title, Arabic body content, author,
  publication date, category, thumbnail image, reading time

- **FAQ Item**: Arabic question text, Arabic answer text, category
  (general/pricing/teachers/scheduling/platform)

- **Service**: Arabic name, Arabic description, feature list,
  illustration image, CTA text, CTA link

- **Team Member**: Arabic name, title, photo, short biography

- **Partner**: Institution name, logo image, website URL

---

## Success Criteria _(mandatory)_

### Measurable Outcomes

- **SC-001**: Every page loads completely and is fully scrollable
  within 3 seconds on a standard broadband connection, with all
  content visible without waiting for JavaScript execution.

- **SC-002**: 100% of visible text across all pages is in natural,
  fluent Arabic with zero English placeholders, zero Lorem Ipsum,
  and zero machine translation artifacts.

- **SC-003**: The homepage contains a minimum of 13 distinct
  content sections, each with substantive Arabic content, as
  verified by manual scroll-through on both mobile and desktop.

- **SC-004**: Every teacher card across the site displays all
  required fields (name, photo, subject, experience, rating,
  student count, CTA) with no missing or placeholder data.

- **SC-005**: The FAQ section contains a minimum of 15 questions
  with substantive Arabic answers, each addressing a genuine
  parent/student concern about online tutoring.

- **SC-006**: Zero horizontal scroll overflow on any page at any
  viewport width from 320px to 2560px.

- **SC-007**: The site passes WCAG 2.1 AA color contrast ratios
  on all text elements as verified by automated contrast checking.

- **SC-008**: 100% of interactive elements (buttons, links, form
  inputs, accordion triggers, menu toggles) are keyboard-
  accessible with visible focus states.

- **SC-009**: All pages function correctly when opened directly
  from the filesystem (file:// protocol) without requiring a
  server, confirming zero backend dependencies.

- **SC-010**: A review by a native Arabic speaker confirms that
  all Arabic content reads naturally, uses appropriate educational
  terminology, and contains no awkward phrasing or cultural
  misalignment.

- **SC-011**: The footer appears identically on all pages with
  minimum 4 link columns, social media icons, and accreditation
  elements — verified by visual comparison.

- **SC-012**: Mobile navigation (slide-out menu) opens and closes
  with smooth animation, contains all navigation links, and is
  functional on all pages — verified on a 375px viewport.
