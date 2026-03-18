<!--
  Sync Impact Report
  ==================
  Version change: 2.0.0 → 3.0.0 (MAJOR — structural rewrite to 15 sections)

  Bump rationale: The constitution has been incompatibly restructured
  from a 10-principle + supporting-sections format to a mandatory
  15-section format as required by the user. All principles have been
  revised, expanded, or reorganized. Section hierarchy has changed.
  This constitutes a backward-incompatible governance redefinition
  requiring a MAJOR bump.

  Modified principles (old → new / reorganized):
    I.   Arabic-First, RTL-Native Design → Section 3 (expanded)
    II.  Premium Arabic Typography & Visual Identity → Section 4 + 5
    III. Trust-Heavy Educational Marketing Structure → Section 8
    IV.  Conversion-First CTA Hierarchy → Section 9
    V.   High Section Richness & Content Depth → Section 6 + 7
    VI.  Premium Mobile Experience → Section 10
    VII. Saudi Audience & Cultural Authenticity → Section 11
    VIII. SEO-Aware Semantic Structure → Section 13 (merged into code)
    IX.  Accessibility, Readability & RTL Correctness → Section 9 + 12
    X.   Commercial Production Quality → Section 15

  Added sections:
    - Section 1: Project Identity (new)
    - Section 2: Product Intent (new)
    - Section 5: Color & Emotional Design Direction (new, expanded)
    - Section 12: Component Consistency Rules (new)
    - Section 14: Non-Goals for This Phase (reorganized from inline)
    - Section 15: Definition of Success (new)

  Removed sections:
    - "Originality & Inspiration Boundaries" merged into Section 2
    - "Technology Constraints" merged into Section 13
    - "Design Language, Quality Gates & Production Standards" split
      across Sections 9, 12, 13, 15

  Templates requiring updates:
    - .specify/templates/plan-template.md       ✅ compatible (generic)
    - .specify/templates/spec-template.md        ✅ compatible (generic)
    - .specify/templates/tasks-template.md       ✅ compatible (generic)

  Follow-up TODOs:
    - AGENTS.md still references Google Fonts (Inter + Playfair Display).
      These MUST be replaced with Arabic-appropriate fonts when the next
      feature plan is generated. The constitution now mandates specific
      Arabic font families.
-->

# Premium Academy Frontend Constitution

This constitution is the authoritative, non-negotiable source of
design principles, implementation rules, and quality standards for
the Premium Academy Frontend project. Every spec, plan, task list,
and implementation MUST comply with this document. Violations MUST
be explicitly justified in a Complexity Tracking table.

---

## Section 1: Project Identity

**Project Name**: Premium Academy (أكاديمية بريميوم)

**Project Type**: Arabic-first premium online education platform
frontend — a complete, commercially credible marketing and
enrollment website for a Saudi-market private tutoring academy.

**Market Position**: A premium Arabic educational services platform
targeting Saudi families (parents and students) seeking private
tutoring, exam preparation (القدرات, التحصيلي, IELTS, STEP),
and curriculum-aligned academic support across all grade levels.

**Brand Character**: Confident, modern, warm, trustworthy,
educationally serious, and commercially polished. The brand MUST
feel like an established Saudi edtech company — not a startup
experiment, student project, or generic template deployment.

**Language**: Arabic is the sole interface language. All user-facing
text, navigation, CTAs, form labels, error messages, metadata,
and content MUST be in Arabic. English appears ONLY where
contextually mandatory (international brand names, certifications
like IELTS/IGCSE, technical terms without Arabic equivalents).

**Layout Direction**: Right-to-left (RTL) is the default and only
supported direction. The entire visual and structural design
originates from RTL assumptions.

---

## Section 2: Product Intent

### What This Product MUST Be

A complete, section-rich, trust-heavy Arabic education platform
frontend that:

- Converts Saudi families into enrolled students through
  deliberate educational marketing and CTA hierarchy
- Demonstrates the depth, polish, and content richness of
  established Arabic edtech market leaders
- Serves as a fully functional marketing and enrollment frontend
  that could credibly launch as a real business website
- Contains enough content depth, section variety, and trust
  signals that a Saudi parent browsing on their phone would
  believe this is a real, operational academy

### What This Product MUST NOT Be

- A thin landing page with a hero and a footer
- A UI component demo or design system showcase
- A template-looking website with generic sections
- A translated English website with RTL applied as afterthought
- A prototype or wireframe-quality implementation
- A single-page marketing site without navigational depth

### Originality & Inspiration Boundaries

The design direction is inspired by the visual mood, UX depth,
premium color sensibility, and trust-heavy structure of leading
Arabic edtech platforms (including the general spirit of platforms
like Abwaab Saudi, Noon Academy, and comparable regional leaders).

**Non-negotiable boundaries:**

- The implementation MUST be entirely original. No HTML, CSS, JS,
  or asset may be copied from any existing platform.
- No page layout may directly reproduce another platform's page
  structure. Inspiration means adopting the market standard of
  quality, depth, and Arabic UX maturity — not cloning specific
  layouts.
- Brand identity (colors, logo treatment, naming, typography
  pairing) MUST be unique to this project.
- The goal is to meet or exceed the quality bar set by Saudi
  market leaders, using original design and implementation.

---

## Section 3: Arabic-First & RTL-First Requirements

The entire frontend MUST be designed Arabic-first with native
right-to-left (RTL) layout as the sole default.

### Mandatory RTL Rules

- The `<html>` element MUST declare `dir="rtl"` and `lang="ar"`.
- All layouts, grids, flexbox directions, margins, paddings,
  border radii, and icon placements MUST be authored RTL-first.
  LTR MUST be treated as the rare exception, not the adaptation
  target.
- Navigation flows, reading order, card arrangements, form field
  order, breadcrumbs, pagination, and progress indicators MUST
  follow Arabic right-to-left reading conventions.
- Tailwind CSS logical utilities and RTL-aware utilities (`rtl:`,
  `ltr:`) MUST be used where directional overrides are needed.
  Hard-coded `left`/`right` values without logical equivalents
  are prohibited unless explicitly justified.
- Icons with inherent directionality (arrows, chevrons, progress
  bars, navigation indicators) MUST be mirrored for RTL context.
- No component, section, or page may exhibit LTR leakage — where
  elements visually or structurally default to left-to-right flow.
- Bidirectional text content (Arabic with embedded English terms)
  MUST render correctly using appropriate `dir` attributes on
  mixed-content elements.

### RTL Testing Mandate

Every page MUST be visually verified for:

- No mirrored logos or brand marks
- No incorrectly reversed icons (e.g., clocks, globes)
- No misaligned absolutely-positioned elements
- No broken flexbox or grid layouts under RTL
- Correct text alignment in all form inputs
- Correct dropdown and menu positioning

**Rationale**: The Saudi educational market expects native Arabic
interfaces. RTL-as-afterthought produces subtle alignment errors,
broken reading flow, and low perceived quality that erode trust
with Saudi families making education purchasing decisions.

---

## Section 4: Visual Language Principles

The visual identity MUST convey a premium, modern, Arabic-native
educational brand — not a translated English template.

### Typography

- Primary typefaces MUST be high-quality Arabic web fonts. Required
  options: IBM Plex Arabic, Tajawal, Cairo, Noto Kufi Arabic, or
  Dubai. Latin-only fonts as primary typefaces are prohibited.
- Typography hierarchy MUST include at minimum: hero/display size
  (40–54px desktop), section heading size (28–36px), card heading
  size (18–22px), body text size (16–18px), caption size (14px),
  and CTA text size (16–20px) — all tuned for Arabic readability.
- Arabic body text MUST use line-height of 1.7–2.0 to ensure
  diacritics and letter stacking render cleanly.
- Arabic body text MUST use a minimum font size of 16px. Dense
  Arabic text without adequate spacing is prohibited.
- Font weight hierarchy MUST include at least: bold (700) for
  headings, medium (500–600) for CTAs and emphasis, regular (400)
  for body text, and light (300) for descriptive/supporting text.

### Visual Rhythm & Spacing

- Generous section spacing MUST be applied: minimum 40px between
  sections on mobile, minimum 80–112px between major sections on
  desktop.
- Maximum content width MUST be constrained (1280–1500px) with
  centered layout and comfortable horizontal padding (16px mobile,
  32–64px desktop).
- Card and component spacing MUST be consistent and deliberate.
  Crowded layouts with insufficient breathing room are prohibited.
- Rounded corners MUST be generous and consistent: 16–24px for
  cards and feature containers, 12px for buttons, full rounding
  for pills and tags.

### Decorative Elements

- Decorative elements MUST be restrained and modern. Overuse of
  geometric Islamic patterns, heavy ornamentation, or cliched
  cultural motifs is prohibited. The aesthetic is contemporary
  Arab premium, not traditional.
- Subtle scroll-triggered entrance animations (fade-in, slide-in)
  MUST be implemented for content sections. Flashy, gimmicky, or
  distracting animations are prohibited.
- SVG illustrations and decorative icons SHOULD use brand-palette
  colors and complement the educational theme.

### Imagery Direction

- Visual assets MUST reflect Arabic/Middle Eastern educational
  context: imagery featuring Arab students and educators, Arabic
  text in mockups, regionally appropriate settings. Generic
  Western stock photography as primary imagery is prohibited.
- High-quality placeholder images MUST be used where photography
  is needed. Broken image icons, empty gray boxes, and visible
  placeholder artifacts are prohibited.
- Teacher profile images MUST use professional avatar placeholders
  that feel authentic and regionally appropriate.

**Rationale**: Premium Arabic edtech platforms invest heavily in
typographic quality and culturally resonant visual identity. A
translated-looking interface signals low investment and reduces
Saudi audience trust immediately.

---

## Section 5: Color & Emotional Design Direction

The color palette MUST evoke a premium educational mood that feels
confident, trustworthy, modern, and warm — inspired by the color
energy of leading Arabic edtech platforms.

### Primary Color Family: Deep Blue

- The dominant brand color MUST be a confident, saturated blue in
  the range of `#2563EB` to `#2767E3` (blue-600 family).
- Blue MUST be used for: primary CTA buttons, header accents,
  active states, link text, feature section gradient backgrounds,
  and brand identity elements.
- The blue MUST feel confident and institutional — not pastel,
  not neon, not baby-blue. It MUST convey educational authority.
- A blue gradient (e.g., from `#2563EB` to `#3B82F6`, ~260-degree
  angle) MUST be used for major feature highlight sections to
  create visual depth and premium presentation.

### Accent Color: Warm Yellow

- A warm, confident yellow in the range of `#FACC15` to `#FBD53D`
  (yellow-400 family) MUST serve as the primary accent color.
- Yellow MUST be used for: secondary/exploratory CTA buttons,
  feature tags/pills, bullet point icons, highlighted labels,
  and attention-drawing elements.
- Yellow CTAs MUST use dark text (slate-900 / `#0F172A`) for
  high contrast readability.

### Neutral Foundation

- Primary text color: slate-900 (`#0F172A`) for headings and
  body text — confident and high-contrast.
- Secondary text: slate-500 to slate-700 for supporting and
  descriptive content.
- Primary background: clean white (`#FFFFFF`) for body and
  content areas.
- Subtle warm gray: slate-50 (`#F8FAFC`) for alternating section
  backgrounds, FAQ items, and subtle content separation.
- Light blue: blue-50 (`#EFF6FF`) for footer background and
  supporting surface areas.

### Emotional Palette Rules

- The palette MUST create a feeling of: trust (blue), energy
  (yellow), clarity (white), and warmth (slate warm tones).
- Harsh neons, childish primary colors, generic Bootstrap-blue,
  cold grays, and dark/moody themes are all prohibited.
- Multi-color teacher card accents (warm gradients in red, orange,
  amber, yellow families) MAY be used to add visual variety to
  card grids, but MUST remain within a warm, educational tone.
- Social proof and trust elements MAY use subtle green for
  positive indicators (ratings, success rates) but green MUST
  NOT compete with the primary blue-yellow palette.

### Color Consistency Mandate

- Color usage MUST be systematic and consistent. Every color
  choice MUST map to a defined role (primary, accent, text,
  background, surface, success, warning).
- Random or inconsistent color application across sections is
  prohibited. The entire website MUST feel like a single,
  cohesive brand experience.

**Rationale**: The blue-yellow-white palette creates the specific
premium educational mood observed in successful Saudi edtech
platforms — institutional confidence (blue), accessible energy
(yellow), and clean modernity (white). This combination builds
trust while maintaining approachability for Saudi families.

---

## Section 6: Homepage Richness Expectations

The homepage is the primary conversion and trust-building page.
It MUST contain a minimum of 10–14 distinct, substantive content
sections. A homepage that feels thin, empty, or section-poor is
a delivery failure.

### Mandatory Homepage Sections (Minimum)

1. **Hero Section**: Full-width hero with compelling Arabic value
   proposition headline, supporting description, primary + secondary
   CTA buttons, and a trust indicator (accreditation badge, student
   count, or download stat). Hero MUST include visual elements
   (educational imagery or illustrations) alongside text content.

2. **Quick-Stats Trust Bar**: A compact section displaying key
   platform statistics with Arabic-formatted numbers — e.g.,
   "+٥٠٠ معلم", "+١٠٬٠٠٠ طالب", "+٥٠٬٠٠٠ حصة". Numbers MUST
   feel realistic and impressive.

3. **Services/Products Overview**: Cards or visual blocks
   showcasing the main service categories (private tutoring,
   exam preparation courses, curriculum-aligned content). Each
   card MUST have a heading, description, and visual element.

4. **Partner/Trust Logos**: A carousel or grid of institutional
   partner logos (universities, government bodies, corporate
   sponsors). Minimum 6–8 logos. Auto-scrolling carousel
   preferred for visual dynamism.

5. **Featured Service Deep-Dive #1**: A detailed section for the
   primary service (e.g., private tutoring) with gradient
   background, bullet-point features, category tags, and a
   dedicated CTA button. MUST include supporting imagery.

6. **Featured Service Deep-Dive #2**: A second detailed section
   for another key service (e.g., exam preparation or curriculum
   content) with equivalent depth and visual treatment.

7. **Subject/Category Browser**: Interactive browsable display of
   available subjects using realistic Saudi curriculum subjects
   and grade levels.

8. **Teacher Showcase**: Grid of featured teacher cards (minimum
   4–8 teachers) displaying name, photo, subject, credentials,
   and a link to learn more.

9. **Student Testimonials**: Social proof section with student
   reviews, video testimonials, or success stories. Testimonials
   MUST include Arabic names, profile context, and realistic
   Arabic review text.

10. **How It Works**: Step-by-step visual process explaining how
    the platform works (browse → book → learn → succeed or
    similar flow).

11. **FAQ Preview**: Collapsible accordion with minimum 8–15
    real questions addressing genuine parent/student concerns
    about online Arabic tutoring.

12. **App/Platform Promotion**: Section promoting mobile app
    download or platform capabilities with app store badges
    and device mockup imagery.

13. **Closing CTA**: Strong conversion section with compelling
    Arabic headline and prominent registration/trial CTA.

### Section Ordering

Sections MUST be ordered to maximize trust-building and conversion:
hook (hero) → credibility (stats, logos) → value (services) →
proof (teachers, testimonials) → clarity (how it works, FAQ) →
convert (closing CTA). The exact order MAY vary but MUST follow
this general trust-building arc.

**Rationale**: Saudi families making education purchasing decisions
require high trust thresholds. Leading Arabic edtech platforms
maintain 10+ homepage sections with ~5,000–6,000px of scroll
depth. Matching this density is a baseline requirement.

---

## Section 7: Section Depth Expectations

Every page beyond the homepage MUST demonstrate substantive
content depth. No page may consist of only a hero and a footer.

### Minimum Section Counts

- **Homepage**: 10–14 sections (see Section 6)
- **Teachers listing page**: Minimum 5–8 sections (hero/filter,
  teacher grid, subject categories, trust stats, testimonials,
  CTA)
- **Teacher profile page**: Minimum 6–8 sections (header/photo,
  bio, subjects, reviews, availability preview, booking CTA,
  related teachers)
- **Subject detail page**: Minimum 5–7 sections (hero, subject
  overview, related teachers, curriculum info, FAQ, CTA)
- **About page**: Minimum 5–7 sections (hero, mission, team,
  stats, partners, CTA)
- **Pricing page**: Minimum 5–7 sections (hero, pricing tiers,
  comparison, FAQ, testimonials, CTA)
- **Contact page**: Minimum 4–6 sections (hero, contact form,
  contact info, FAQ, map/location)
- **FAQ page**: Minimum 3–5 sections (hero, categorized FAQ
  accordion, contact CTA)

### Content Depth Rules

- Every visible section MUST contain real, substantive Arabic
  content — not placeholder text, Lorem Ipsum, or skeleton blocks.
- Subject categories MUST use realistic Saudi curriculum subjects
  (الرياضيات، الفيزياء، الكيمياء، اللغة الإنجليزية، القدرات،
  التحصيلي) and grade levels (ابتدائي، متوسط، ثانوي).
- Teacher profiles MUST include realistic Arabic biographies,
  teaching philosophies, credentials, and student reviews.
- Statistics MUST use realistic numbers with Arabic-Indic or
  Arabic-European numerals used consistently within each context.
- FAQ content MUST address real parent/student concerns: pricing,
  trial lessons, teacher qualifications, scheduling, curriculum
  alignment, session recording, payment methods.
- Testimonials MUST include Arabic names, profile photos, grade
  levels, subjects, and realistic Arabic review text. Generic
  "Student A says great things" placeholders are prohibited.

### Page Architecture

The information architecture MUST anticipate the full page family:

- الرئيسية (Homepage)
- من نحن (About)
- المعلمون (Teachers listing)
- ملف المعلم (Teacher profile)
- المواد (Subjects listing)
- تفاصيل المادة (Subject detail)
- كيف يعمل (How it works)
- الأسعار (Pricing)
- احجز حصة تجريبية (Trial booking)
- تواصل معنا (Contact)
- الأسئلة الشائعة (FAQ)
- المدونة (Blog/Articles)
- الشروط والأحكام (Legal pages)

Even pages not implemented in the current phase MUST be
anticipated in navigation and site architecture through
proper internal linking.

**Rationale**: Thin pages with placeholder content signal a demo
project. Saudi audiences expect content depth matching established
regional platforms. Every page MUST justify the time investment
of a busy Saudi parent evaluating educational options.

---

## Section 8: Trust-Building Requirements

Trust is the primary conversion driver in Saudi educational
purchasing decisions. Every page MUST incorporate deliberate,
multi-layered trust signals.

### Required Trust Elements

1. **Quantitative Trust**: Platform statistics displayed
   prominently — student counts, teacher counts, lesson counts,
   satisfaction percentages, years of operation. Numbers MUST
   be formatted in Arabic and feel realistic (e.g., "+١٠٬٠٠٠
   طالب", "+٥٠٠ معلم", "٩٨٪ رضا").

2. **Institutional Trust**: Partner and accreditation logos from
   recognizable Saudi/Gulf institutions (ministries, universities,
   corporate sponsors). Minimum 6–8 logos displayed in a
   professional carousel or grid.

3. **Social Proof**: Student and parent testimonials with real
   Arabic names, profile context, and detailed review text.
   Video testimonials embedded from YouTube or similar are
   strongly encouraged.

4. **Credential Trust**: Teacher cards MUST display qualifications,
   experience years, student counts, ratings, and subjects taught.
   Skeleton teacher cards with missing credential fields are
   prohibited.

5. **Process Trust**: Clear "how it works" content that demystifies
   the enrollment and learning process.

6. **Policy Trust**: Visible links to terms of service, privacy
   policy, refund policy, and academic integrity policies in
   the footer.

7. **Accessibility Trust**: Help center links, contact information,
   WhatsApp/phone support indicators, and FAQ sections that
   proactively address concerns.

### Trust Element Distribution

Trust elements MUST NOT be concentrated in a single section.
They MUST appear naturally throughout every page:

- Hero sections MUST contain at least one trust indicator
- Mid-page sections MUST reinforce trust through stats or logos
- Near-CTA sections MUST include social proof or guarantees
- Footer MUST contain comprehensive trust links and accreditation

### Teacher Card Trust Requirements

Teacher cards MUST display at minimum:

- Full name in Arabic
- Professional profile photo/avatar
- Subjects taught
- Experience years
- Student rating (stars or numerical)
- Student count
- Price indicator (if applicable)
- Clear booking/profile CTA

**Rationale**: Saudi families commit significant financial
resources to education. The trust threshold for online education
is particularly high. Every missing trust signal is a potential
conversion loss.

---

## Section 9: UX Quality Bar

### CTA Hierarchy

Every page MUST implement a deliberate, multi-tier call-to-action
hierarchy that guides visitors toward conversion.

- Primary conversion goals: exploring teachers by subject, booking
  a trial lesson, registering an account, contacting the academy.
- Each page MUST have a primary CTA (most prominent), one or more
  secondary CTAs (supporting actions), and contextual micro-CTAs
  embedded within content sections.
- CTA buttons MUST use Arabic action verbs that are direct,
  confident, and culturally appropriate (e.g., "ابدأ مجانًا",
  "احجز حصتك", "تعرّف على المعلمين", "سجّل الآن").
- CTA visual hierarchy MUST be enforced through size, color
  contrast, spacing, and positioning:
  - **Primary CTAs**: Blue background (`bg-blue-600`), white text,
    prominent sizing (h-12, text-lg/xl), used for registration
    and primary conversion actions.
  - **Secondary CTAs**: White background with blue border and
    text, used for sign-in and alternative actions.
  - **Exploratory CTAs**: Yellow background (`bg-yellow-400`),
    dark text, used for section-specific "learn more" actions.
- Sticky or repeated CTAs MUST appear at strategic scroll points
  on long pages. A single CTA at page bottom is insufficient.

### Interaction Quality

- All interactive elements MUST feel polished: smooth hover
  transitions (200–300ms), subtle entrance animations on scroll
  (600ms ease-out), elegant dropdowns, polished accordion/tab/
  modal behaviors.
- Button hover states MUST be implemented on all clickable
  elements. Un-hovered, flat-looking buttons are prohibited.
- Form interactions MUST include Arabic field labels, RTL input
  alignment, appropriate validation messages in Arabic, and
  frictionless input flow.
- Loading states, empty states, and error states MUST all be
  designed and presented in Arabic with correct RTL alignment.

### Navigation Quality

- Header navigation MUST be fixed/sticky, containing logo
  (centered or RTL-positioned), primary auth CTAs (registration
  - sign-in), and contextual navigation elements.
- Mobile navigation MUST be a full-featured Arabic RTL slide-out
  menu with smooth transitions — not a minimal hamburger dropdown.
- Footer navigation MUST be comprehensive: minimum 3–4 columns
  with categorized links (company info, legal/policies, support,
  regional/accreditation). Footer MUST include social media icons,
  accreditation logos, and a distinct visual treatment (e.g.,
  light blue background, rounded top corners).
- Internal linking with Arabic anchor text MUST be implemented
  across all pages for both UX and SEO benefit.

### Accessibility Baseline

- Required: semantic HTML5 elements, WCAG 2.1 AA contrast ratios,
  keyboard-navigable interactive elements, visible focus states,
  `aria-label` attributes in Arabic for icon-only buttons.
- Form validation messages, error states, empty states, and
  loading states MUST all be in Arabic with correct RTL alignment.

**Rationale**: The frontend exists to convert Saudi families into
enrolled students. Every UX decision MUST serve this commercial
conversion objective with Arabic-native interaction patterns.

---

## Section 10: Responsive Expectations

The mobile experience MUST be treated as a first-class product
with deliberate design at every breakpoint.

### Target Breakpoints

- **Mobile**: < 640px (base/default styles)
- **Tablet**: 640px–1024px (`sm:` and `md:` prefixes)
- **Desktop**: 1024px–1280px (`lg:` prefix)
- **Large Desktop**: > 1280px (`xl:` prefix)

### Breakpoint-Specific Rules

- Each breakpoint MUST receive intentional layout decisions — not
  just content reflow. Section order, CTA placement, navigation
  patterns, and content density MUST be optimized per breakpoint.
- Mobile hero sections MUST be compelling and complete — not
  truncated desktop heroes. Mobile-specific CTA positioning and
  sizing MUST be implemented.
- Card grids MUST adapt meaningfully: 1-column on mobile (or
  horizontal scroll), 2–3 columns on tablet, 3–4 columns on
  desktop.
- Mobile navigation MUST use a full-featured slide-out sidebar
  menu, not a minimal dropdown.
- Touch targets MUST meet minimum 44x44px sizing. Form inputs,
  buttons, and interactive elements MUST be comfortable for
  thumb-zone interaction.

### Prohibited Mobile Behaviors

- Horizontal scroll on any viewport is prohibited (except
  intentional carousels with proper scroll indicators).
- Content overflow artifacts on mobile are prohibited.
- Text that is readable on desktop but too small on mobile is
  prohibited.
- CTAs that are prominent on desktop but hidden or tiny on
  mobile are prohibited.
- Full-width images without mobile-optimized aspect ratios are
  prohibited.

### Maximum Content Width

- Content MUST be constrained to a maximum width of 1280–1500px
  with auto margins for centering.
- On large displays (> 1500px), content MUST remain centered with
  comfortable side margins — not stretched edge-to-edge.

**Rationale**: Saudi mobile internet penetration exceeds 95%.
The majority of prospective students and parents will first
encounter the platform on a mobile device. A degraded mobile
experience directly reduces enrollment conversion.

---

## Section 11: Content Tone Rules in Arabic

All user-facing content MUST be written in natural, fluent Modern
Standard Arabic (فصحى حديثة) appropriate for Saudi educational
marketing.

### Tone Characteristics

- **Confident**: The academy speaks with authority about education.
  Hedging language and uncertain phrasing are prohibited.
- **Warm**: The tone addresses Saudi families with respect and
  warmth. Cold, corporate, or overly formal language is prohibited.
- **Professional**: Marketing copy MUST sound like it was written
  by a native Arabic-speaking marketing professional — not
  machine-translated or awkwardly phrased.
- **Direct**: CTA text and calls to action MUST use clear Arabic
  imperatives. Passive or vague CTAs are prohibited.
- **Parent-aware**: Content MUST speak to both students and their
  parents. Parental concerns (quality, safety, results, value)
  MUST be addressed.

### Arabic Content Rules

- All visible Arabic text MUST read naturally and fluently to a
  native Saudi Arabic reader.
- Machine translation artifacts, awkward phrasing, and Lorem
  Ipsum in any visible section are prohibited.
- Technical educational terms MUST use established Arabic
  translations where they exist.
- Inconsistent transliteration (mixing Arabic and English for
  the same concept in different places) is prohibited.
- Arabic numerals (٨٢٣ or 123) MUST be used consistently within
  each context. Random mixing is prohibited.
- Currency references MUST use Saudi Riyal (ر.س / SAR).
- Academic terminology MUST align with Saudi Ministry of Education
  conventions: grade level names, examination types (القدرات,
  التحصيلي, IELTS, STEP), and curriculum references.

### Cultural Authenticity

- Imagery MUST reflect Saudi/Gulf cultural context without
  stereotyping. Modern educational settings, diverse student
  representations, and professional educator imagery are required.
- Privacy and conservative design sensibility MUST be maintained.
  Content MUST be family-appropriate and respectful of Saudi
  cultural norms.
- Seasonal and academic calendar references MUST align with the
  Saudi academic year structure.

**Rationale**: Cultural and linguistic misalignment is immediately
detected by Saudi audiences and irreparably damages platform
credibility. Authenticity is a prerequisite for trust in Saudi
edtech.

---

## Section 12: Component Consistency Rules

All UI components MUST follow strict consistency rules to maintain
a cohesive, professional visual system across every page.

### Card System

- **Teacher cards**: MUST always display the same field set (name,
  photo, subject, credentials, rating, CTA) with identical layout
  and spacing wherever they appear.
- **Subject/category cards**: MUST use consistent sizing, border
  radius (rounded-2xl to rounded-3xl), color treatment, and
  typography hierarchy.
- **Service/feature cards**: MUST use consistent background
  treatment (solid color or gradient), consistent padding, and
  consistent CTA button placement.
- Card dimensions MUST be defined and reused. Random card sizing
  across different pages is prohibited.

### Button System

- **Primary buttons**: Blue background, white text, consistent
  height (h-12 or equivalent), consistent border radius
  (rounded-md to rounded-xl), hover state darkening.
- **Secondary buttons**: White background, blue border, blue text,
  same dimensions as primary.
- **Accent buttons**: Yellow background, dark text, same height
  consistency, used for section-specific CTAs.
- **Button text**: MUST use `font-medium` weight, consistent
  font size (text-lg or text-xl), and Arabic action verbs.
- Button dimensions and padding MUST be identical for buttons
  of the same tier across the entire site.

### Spacing System

- Section vertical padding MUST be consistent: a defined rhythm
  of padding-top and padding-bottom applied uniformly.
- Section backgrounds MUST alternate in a deliberate rhythm
  (white → slate-50 → white → gradient → white) to create
  visual section separation.
- Component internal spacing (card padding, form field margins,
  list item gaps) MUST use a consistent spacing scale.

### Icon System

- All icons MUST come from a single consistent source (inline
  SVGs with consistent sizing, stroke width, and color treatment).
- Icon sizing MUST be consistent within each context (navigation
  icons same size, card icons same size, feature icons same size).
- Directional icons MUST be RTL-appropriate.

### Section Header Pattern

- Section headings MUST follow a consistent pattern: centered
  bold heading (defined size per breakpoint) + optional centered
  subtitle in secondary text color + consistent bottom spacing
  before section content.

**Rationale**: Component inconsistency is the most visible sign
of an unpolished, template-assembled website. Saudi families
accustomed to polished edtech platforms will immediately notice
inconsistent card sizes, button styles, or spacing rhythms.

---

## Section 13: Frontend Code Rules

### Technology Constraints

**Allowed technologies**:

- HTML5 (semantic elements required)
- CSS3
- Tailwind CSS (v3, CDN or build)
- Native JavaScript (ES2020+)

**Prohibited technologies**:

- React, Vue, Angular, Next.js, Nuxt, Svelte, Alpine.js, jQuery,
  Bootstrap, Foundation, and any frontend SPA framework, meta-
  framework, or CSS framework beyond Tailwind.

### HTML Rules

- Pages MUST use semantic HTML5 elements: `<header>`, `<nav>`,
  `<main>`, `<section>`, `<article>`, `<aside>`, `<footer>`.
- Each page MUST have exactly one `<h1>` element.
- Heading hierarchy MUST be sequential (h1 → h2 → h3) with no
  skipped levels.
- The `<html>` tag MUST include `lang="ar"` and `dir="rtl"`.
- Page titles, meta descriptions, and Open Graph tags MUST be
  in Arabic and contain relevant Saudi educational keywords.

### Tailwind CSS Rules

- Tailwind class usage MUST be organized and consistent:
  grouped by concern (layout → spacing → typography → color →
  effects → responsive).
- Utility class chains MUST NOT exceed reasonable length. When
  a pattern repeats across 3+ elements, extract to a shared
  class or document the pattern.
- Responsive prefixes (`sm:`, `md:`, `lg:`, `xl:`) MUST be
  applied deliberately, not scattered randomly.
- Custom colors extending the Tailwind palette MUST be defined
  if the default palette is insufficient.

### JavaScript Rules

- Native JS MUST be modular and minimal — used only for
  interactive behaviors (menus, tabs, accordions, modals,
  carousels, scroll animations, form validation).
- JS MUST NOT be used for layout or styling that CSS/Tailwind
  can handle.
- JS modules MUST be cleanly organized by feature (navigation.js,
  accordion.js, carousel.js, animations.js, etc.).
- Unnecessary complexity, over-engineering, and premature
  abstraction are prohibited.

### Code Organization

- Generated frontend code MUST be clean, well-structured, and
  logically organized.
- Comments MUST add genuine value — no clutter, no stating the
  obvious.
- Code MUST be navigable by a developer unfamiliar with the
  project.
- Pages MUST be split logically, with shared components and
  patterns clearly identified.

### Reusability Patterns

- Reusable HTML partial philosophy with consistent structure.
- Consistent Tailwind class conventions and component patterns.
- Clean CSS utilities for repeated patterns.
- Native JS modules for interactivity.

### SEO Requirements

- Crawlable internal linking structure with Arabic anchor text
  MUST be implemented across all pages.
- Descriptive `<meta>` tags with Arabic content on every page.
- Clean URL structure anticipating the full page architecture.

### Deployment Target

Static files servable directly from GitHub Pages, Netlify,
Vercel static, or any static file server. No build step is
required beyond optional Tailwind CSS compilation. The frontend
MUST function correctly when opened directly in a browser from
the file system.

**Rationale**: The project MUST remain inspectable, maintainable,
and deployable without framework complexity. Static deployment
ensures maximum hosting flexibility and eliminates runtime
dependencies.

---

## Section 14: Non-Goals for This Phase

The following capabilities MUST NOT be implemented in the current
phase, but the frontend MUST be architectured so they can be
integrated later without requiring major structural redesign:

- Backend logic or API integration
- Full booking/scheduling engine
- Student/teacher authentication dashboards
- Payment system implementation (Stripe, Tamara, STC Pay, etc.)
- Real-time chat or video integration
- Admin panel or CMS
- Multi-language support (English version)
- Email notification system
- Analytics dashboard
- Student progress tracking UI
- Real-time availability calendars

### Future Integration Readiness

The frontend MUST support future expansion into:

- Teacher profiles and marketplace flows
- Student onboarding and registration
- Course/subject discovery and booking flows
- Trial lesson scheduling
- Student and teacher dashboards
- Full Arabic + English bilingual support
- SEO content pages and blog
- Payment gateway integration
- Mobile app promotion and deep linking

Frontend pages MUST be designed so these features can be
integrated later without major structural redesign. Forms MUST
have proper `name` attributes and logical structure. Navigation
MUST anticipate future pages. Data display patterns MUST be
ready for dynamic data injection.

**Rationale**: Scope discipline ensures delivery quality. Building
a polished, trust-worthy frontend is more valuable than a
half-implemented full-stack prototype. The frontend investment
retains its value when backend integration begins.

---

## Section 15: Definition of Success

### The Saudi Parent Test

Every delivered page MUST pass this test: **Would a Saudi parent
browsing this page on their phone at 10pm believe this is a real,
operational academy where they can enroll their child?**

If the answer is "no" or "maybe" — the page is not ready for
delivery.

### Quality Gates

Every page MUST pass ALL of the following gates before delivery:

1. **RTL Correctness**: Layout verified on all viewports with no
   LTR leakage, no misaligned elements, no broken flex/grid.
2. **Arabic Typography**: Typography hierarchy correctly applied
   with proper font family, sizes, weights, and line-heights.
3. **Spacing Consistency**: Consistent spacing system applied at
   section, card, and element levels.
4. **Grid Behavior**: Consistent grid behavior verified across
   all four breakpoints (mobile, tablet, desktop, large desktop).
5. **Section Rhythm**: Alternating backgrounds and consistent
   padding creating visual section separation.
6. **CTA Hierarchy**: Primary, secondary, and accent CTAs
   implemented and visually verified at every scroll depth.
7. **Card Consistency**: All card types (teacher, subject, service)
   consistent in layout, fields, and styling.
8. **Icon Treatment**: Consistent and RTL-appropriate across the
   entire page.
9. **Form Styling**: RTL input alignment, Arabic labels, proper
   validation states.
10. **Content Completeness**: No placeholder text, no "coming
    soon" blocks, no empty sections, no Lorem Ipsum.
11. **Mobile Verification**: Mobile experience manually verified
    as a first-class product — not just "doesn't break."
12. **Arabic Proofread**: All Arabic content proofread for
    naturalness, fluency, and cultural appropriateness.
13. **Interactive Polish**: All menus, tabs, accordions, modals,
    and carousels functional with smooth transitions.
14. **Trust Signal Density**: Trust elements distributed naturally
    throughout the page — not concentrated in one section.

### Prohibited Delivery States

The following states constitute delivery failures and MUST be
rejected:

- Generic, template-looking layouts
- Thin pages with insufficient section count
- Section-poor pages with weak scroll depth
- Weak Arabic typography (wrong fonts, small sizes, tight spacing)
- LTR-leaking layouts
- Low-trust pages missing social proof and credentials
- Visually flat designs without depth, gradients, or shadows
- Broken or inconsistent card systems
- Missing or weak mobile experience
- Placeholder content in any visible section
- "Demo quality" output that would not convince a Saudi parent
- Inconsistent spacing, random typography mixing, or crowded
  layouts
- Shallow landing-page behavior where a page looks acceptable
  at first glance but has no depth or real information

### Commercial Readiness Standard

Every page MUST look and feel like a real, commercially
operational Arabic education platform. The quality bar is set
by established Saudi edtech market leaders. Meeting this bar
with original design and implementation is the definition of
success for this project.

---

## Governance

This constitution is the authoritative source of design and
implementation principles for the Premium Academy Frontend project.

- **Supremacy**: This constitution supersedes all other style
  guides, conventions, or ad-hoc decisions. Conflicts MUST be
  resolved in favor of constitution principles.
- **Amendments**: Any change to this constitution MUST be
  documented with a version increment, rationale, and sync
  impact report. Changes to principles require MINOR or MAJOR
  version bumps.
- **Versioning**: MAJOR for section removals or incompatible
  redefinitions, MINOR for new sections or material expansions,
  PATCH for clarifications and wording fixes.
- **Compliance**: Every spec, plan, and task list MUST reference
  and pass a Constitution Check before implementation begins.
  Violations MUST be justified in a Complexity Tracking table.
- **Arabic-First Enforcement**: Any deliverable that defaults to
  English text, LTR layout, or Western-centric UX patterns
  without explicit RTL/Arabic adaptation is a constitution
  violation and MUST be rejected.
- **Section Completeness Enforcement**: Any deliverable that
  fails to meet the minimum section counts defined in Sections
  6 and 7 is a constitution violation and MUST be rejected.
- **Trust Density Enforcement**: Any deliverable that lacks the
  trust elements defined in Section 8 is a constitution
  violation and MUST be rejected.

**Version**: 3.0.0 | **Ratified**: 2026-03-13 | **Last Amended**: 2026-03-17
