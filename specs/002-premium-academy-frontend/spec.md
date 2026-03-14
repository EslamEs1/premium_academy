# Feature Specification: Sana Academy Frontend Website

**Feature Branch**: `002-Sana-academy-frontend`  
**Created**: 2026-03-13  
**Status**: Draft  
**Input**: User description: "Design and implement a highly professional public-facing frontend website for a Sana educational academy using only HTML, CSS, Tailwind CSS, and native JavaScript. The website must be original, conversion-oriented, future-ready for marketplace expansion, and benchmarked against leading tutoring platforms like Preply."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Prospective Student Discovers the Academy (Priority: P1)

A prospective student or parent visits the homepage for the first time. They immediately understand what the academy offers, perceive it as Sana and trustworthy, and are guided toward a clear next step (booking a trial or exploring teachers). The homepage communicates value within seconds through strong visual hierarchy, trust signals, and compelling CTAs.

**Why this priority**: The homepage is the single most important page for conversion. If a first-time visitor cannot quickly understand the value proposition and take action, no other page matters. This is the foundation of the entire website.

**Independent Test**: Can be fully tested by loading the homepage on desktop and mobile, verifying all sections render correctly, CTAs are visible and clickable, and the page communicates trust and value within 5 seconds of viewing.

**Acceptance Scenarios**:

1. **Given** a visitor lands on the homepage, **When** they view the hero section, **Then** they see a clear value proposition, a primary CTA (e.g., "Book a Free Trial"), and a secondary CTA (e.g., "Browse Teachers") within the first viewport.
2. **Given** a visitor scrolls through the homepage, **When** they reach the trust section, **Then** they see quantified credibility metrics (student count, teacher count, satisfaction rate, lesson count).
3. **Given** a visitor on mobile, **When** they tap the mobile menu icon, **Then** a full-screen navigation overlay opens with all primary links and CTA buttons accessible.
4. **Given** a visitor views the homepage, **When** they reach the featured teachers section, **Then** they see teacher cards with photo, name, subject, rating, price indicator, and a CTA linking to the teacher profile page.
5. **Given** a visitor reaches the footer, **When** they view it, **Then** they see organized navigation groups, contact information, legal links, and a newsletter signup form.

---

### User Story 2 - Student Browses and Evaluates Teachers (Priority: P1)

A student navigates to the teachers listing page to find the right instructor. They can browse teacher cards that display key decision-making information (subject, rating, price, experience), use filter/sort UI controls to narrow results, and click through to a detailed teacher profile page. The profile page provides comprehensive information to support a booking decision.

**Why this priority**: Teacher discovery and evaluation is the core marketplace behavior the site must support. Without compelling teacher presentation, the academy cannot convert visitors into students.

**Independent Test**: Can be fully tested by navigating from homepage to teachers listing, viewing teacher cards, applying filter/sort controls, clicking a teacher card, and verifying the profile page displays all required information sections with a sticky booking CTA.

**Acceptance Scenarios**:

1. **Given** a visitor is on the teachers listing page, **When** they view the page, **Then** they see a grid of teacher cards with photo, name, headline, subjects, rating, review count, price indicator, and a CTA button.
2. **Given** a visitor is on the teachers listing page, **When** they interact with the filter sidebar, **Then** they can filter by subject, availability format, and experience level (UI only, no backend filtering required).
3. **Given** a visitor clicks a teacher card, **When** the teacher profile page loads, **Then** they see a teacher intro section, qualifications, subjects taught, teaching style description, student reviews, available lesson formats, pricing information, and a prominent trial CTA.
4. **Given** a visitor is on a teacher profile on desktop, **When** they scroll past the intro section, **Then** a sticky sidebar with booking/trial CTA remains visible in the viewport.
5. **Given** a visitor is on a teacher profile on mobile, **When** they scroll the page, **Then** a fixed bottom CTA bar remains visible for booking.

---

### User Story 3 - Student Explores Programs and Courses (Priority: P2)

A student or parent visits the programs/courses listing to understand the academy's structured offerings. They see categorized course cards with clear descriptions, and can click through to a detailed course page that explains what is included, who it is for, expected outcomes, and the instructor.

**Why this priority**: Programs represent the academy's structured educational offerings, which differentiate it from a pure marketplace. This supports the business's positioning as a Sana academy, not just a tutor directory.

**Independent Test**: Can be fully tested by navigating to the programs listing, viewing course cards across categories, clicking a course card, and verifying the detail page includes all required sections (overview, audience, inclusions, outcomes, instructor, CTA, FAQ).

**Acceptance Scenarios**:

1. **Given** a visitor is on the programs listing page, **When** they view the page, **Then** they see course cards organized by category with title, description summary, level indicator, duration, and a CTA.
2. **Given** a visitor clicks a course card, **When** the course detail page loads, **Then** they see an overview, target audience section, inclusions list, learning outcomes, instructor summary, enrollment CTA, and FAQ section.
3. **Given** a visitor is on a course detail page, **When** they view the CTA block, **Then** they see a clear enrollment/inquiry action with pricing or "Contact Us" information.

---

### User Story 4 - Visitor Understands the Academy Process (Priority: P2)

A prospective student or parent wants to understand how the academy works before committing. They visit the "How It Works" page and see a clear step-by-step explanation of the student journey, from choosing a teacher or program, through booking/enrollment, to what happens after signup. Trust and support messaging reinforces their confidence.

**Why this priority**: Process clarity reduces friction and increases conversion. Visitors who understand the next steps are more likely to take action. This page also appears as a homepage section preview.

**Independent Test**: Can be fully tested by navigating to the How It Works page and verifying the step-by-step flow is clear, complete, and includes trust messaging.

**Acceptance Scenarios**:

1. **Given** a visitor is on the How It Works page, **When** they view the steps, **Then** they see at least 3-4 clearly labeled steps explaining the student journey from discovery to first lesson.
2. **Given** a visitor reads the process steps, **When** they reach the end, **Then** they see a CTA encouraging them to start the process (e.g., "Find Your Teacher" or "Book a Free Trial").
3. **Given** a visitor views the page, **When** they look for trust signals, **Then** they find support messaging (e.g., "Personal guidance from our team," "Satisfaction guaranteed").

---

### User Story 5 - Visitor Learns About the Academy (Priority: P3)

A visitor who is evaluating the academy's credibility navigates to the About page. They read the academy's story, mission, teaching philosophy, and reasons to choose this academy. Trust indicators and a CTA reinforce the brand.

**Why this priority**: The About page builds deeper trust for visitors who are seriously evaluating the academy. It is important but typically viewed by a smaller, more committed audience.

**Independent Test**: Can be fully tested by loading the About page and verifying all sections are present, content tone is Sana, and the CTA is visible.

**Acceptance Scenarios**:

1. **Given** a visitor is on the About page, **When** they scroll through it, **Then** they see the academy story, mission/vision statement, teaching philosophy, "Why Choose Us" section, and trust indicators.
2. **Given** a visitor finishes reading the About page, **When** they reach the bottom, **Then** they see a CTA encouraging them to explore teachers or programs.

---

### User Story 6 - Visitor Contacts the Academy (Priority: P3)

A visitor with questions or a specific inquiry navigates to the Contact page. They see a Sana contact form, alternative contact methods (email, phone, address), an FAQ prompt for common questions, and professional business presentation.

**Why this priority**: Contact is essential for lead generation and converting hesitant visitors. It supports the business directly but is lower priority than the core discovery pages.

**Independent Test**: Can be fully tested by loading the Contact page, filling in the form fields, verifying form validation behavior, and checking that contact methods and FAQ links are present.

**Acceptance Scenarios**:

1. **Given** a visitor is on the Contact page, **When** they view the form, **Then** they see fields for name, email, subject/topic, and message with proper labels and validation indicators.
2. **Given** a visitor submits the contact form with empty required fields, **When** validation triggers, **Then** they see clear, non-intrusive error messages indicating which fields need attention.
3. **Given** a visitor views the Contact page, **When** they look for alternatives, **Then** they find email address, phone number, and a link to the FAQ page.

---

### User Story 7 - Visitor Reads FAQ (Priority: P3)

A visitor looking for answers navigates to the FAQ page. They see questions organized into categories with a smooth accordion interface. Questions cover common student/parent concerns about the academy, lessons, pricing, and process.

**Why this priority**: FAQ reduces support burden and answers objections that might prevent conversion. It is supporting content that improves overall site effectiveness.

**Independent Test**: Can be fully tested by loading the FAQ page, clicking accordion items to expand/collapse answers, and verifying category organization.

**Acceptance Scenarios**:

1. **Given** a visitor is on the FAQ page, **When** they view the categories, **Then** they see at least 3 categories (e.g., "Getting Started," "Lessons & Teachers," "Pricing & Payments").
2. **Given** a visitor clicks a FAQ question, **When** the accordion expands, **Then** the answer appears with a smooth transition and only one item is expanded at a time within each category.
3. **Given** a visitor is on the FAQ page on mobile, **When** they interact with accordions, **Then** the touch targets are large enough and the expand/collapse behavior is responsive.

---

### User Story 8 - Visitor Reads Blog Content (Priority: P3)

A visitor discovers the academy through search or browses educational articles. The blog listing page shows article cards with clean hierarchy and category/tag indicators. Clicking an article opens a detail page with readable typography, share options, and related content suggestions.

**Why this priority**: Blog content supports SEO and positions the academy as a thought leader. It drives organic traffic but is lower priority than the core commercial pages.

**Independent Test**: Can be fully tested by loading the blog listing, viewing article cards, clicking an article, and verifying the detail page has proper typography, share links, and related content.

**Acceptance Scenarios**:

1. **Given** a visitor is on the blog listing page, **When** they view the page, **Then** they see article cards with featured image, title, excerpt, author, date, and category tags.
2. **Given** a visitor clicks an article card, **When** the blog detail page loads, **Then** they see the article with readable typography (proper line length, spacing, heading hierarchy), share buttons, and a "Read Next" or related articles section.
3. **Given** a visitor finishes reading an article, **When** they reach the end, **Then** they see a CTA encouraging further engagement (e.g., "Book a Free Trial," "Explore Our Teachers").

---

### User Story 9 - Visitor Reviews Legal Information (Priority: P4)

A visitor checks the academy's legal pages (Privacy Policy, Terms of Service) to evaluate trustworthiness. These pages have clean, readable layouts with proper heading structure.

**Why this priority**: Legal pages are required for business credibility and compliance but are rarely the focus of user engagement. They must exist and be accessible but do not need rich interaction design.

**Independent Test**: Can be fully tested by navigating to legal pages from the footer and verifying they load with proper heading structure and readable content.

**Acceptance Scenarios**:

1. **Given** a visitor clicks "Privacy Policy" in the footer, **When** the page loads, **Then** they see a properly structured legal document with headings, last-updated date, and readable formatting.
2. **Given** a visitor clicks "Terms of Service" in the footer, **When** the page loads, **Then** they see a properly structured terms document with clear sections.

---

### Edge Cases

- What happens when images fail to load? Placeholder images or background colors must prevent layout breakage.
- What happens when a user navigates to a teacher or course page that does not yet have content populated? A clean placeholder state with a message like "Coming soon" or "Profile being updated" must be shown.
- How does the mobile menu behave when the viewport changes orientation? The menu must close on orientation change or adapt gracefully.
- What happens when a user clicks a CTA that leads to a future feature (booking, enrollment)? The CTA must link to the Contact page or a "Coming Soon" modal explaining next steps.
- How does the site behave with JavaScript disabled? Core content and navigation links must remain accessible; only interactive enhancements (accordion, mobile menu toggle) degrade.
- What happens when the contact form is submitted? A client-side success message must appear since no backend exists yet. The form data is not sent anywhere.
- How do pages behave with very long content (e.g., a teacher with 50 reviews)? Content must be paginated or truncated with a "Show More" pattern.

## Requirements *(mandatory)*

### Functional Requirements

#### Site Structure & Navigation
- **FR-001**: Website MUST include all 13 required pages: Homepage, About, Teachers Listing, Teacher Profile, Programs Listing, Program Detail, How It Works, Contact, FAQ, Blog Listing, Blog Detail, Privacy Policy, and Terms of Service.
- **FR-002**: Website MUST include a consistent global header on every page with navigation links to Home, Teachers, Programs, How It Works, About, Blog, and Contact.
- **FR-003**: Header MUST include a prominent CTA button (e.g., "Book a Free Trial" or "Get Started") visible on all pages.
- **FR-004**: Website MUST include a consistent global footer on every page with navigation groups, contact details, legal links, and newsletter signup form.
- **FR-005**: Website MUST include a mobile navigation menu that opens as a full-screen or slide-in overlay with all primary links and CTA.
- **FR-006**: Mobile menu MUST be dismissible by tapping a close button, tapping outside the menu area, or pressing the Escape key.

#### Homepage
- **FR-007**: Homepage MUST include an announcement bar or utility strip at the top of the page (dismissible).
- **FR-008**: Homepage MUST include a hero section with a value proposition headline, supporting text, a primary CTA button, and a secondary CTA link.
- **FR-009**: Homepage MUST include a featured teachers section displaying at least 4 teacher cards with photo, name, subject, rating, and CTA.
- **FR-010**: Homepage MUST include a subjects/categories section displaying at least 8 subject categories as clickable cards or pills.
- **FR-011**: Homepage MUST include a "How It Works" preview section with 3-4 numbered steps.
- **FR-012**: Homepage MUST include a value proposition section highlighting benefits for students and parents (at least 3 value blocks).
- **FR-013**: Homepage MUST include a testimonials section with at least 3 student/parent review cards.
- **FR-014**: Homepage MUST include a trust metrics section displaying quantified credibility indicators (e.g., student count, teacher count, satisfaction percentage, lessons delivered).
- **FR-015**: Homepage MUST include a FAQ preview section with 4-5 expandable accordion items.
- **FR-016**: Homepage MUST include a final CTA band section encouraging visitor action before the footer.

#### Teachers Listing
- **FR-017**: Teachers listing page MUST display teacher cards in a responsive grid layout.
- **FR-018**: Each teacher card MUST display: profile photo, full name, headline/tagline, primary subject(s), star rating with review count, price indicator, and a CTA button.
- **FR-019**: Teachers listing page MUST include a filter sidebar (or collapsible filter panel on mobile) with controls for subject, format (online/in-person), and experience level.
- **FR-020**: Teachers listing page MUST include a sorting dropdown with options (e.g., "Recommended," "Highest Rated," "Price: Low to High," "Price: High to Low").
- **FR-021**: Filter and sort controls MUST visually respond to user interaction (active states, selected indicators) even without backend data filtering.

#### Teacher Profile
- **FR-022**: Teacher profile page MUST include a hero/intro section with large photo, name, headline, subjects, rating, and key stats.
- **FR-023**: Teacher profile page MUST include sections for qualifications, subjects taught, teaching style/experience, student reviews, available lesson formats, and pricing/trial CTA.
- **FR-024**: Teacher profile page MUST include a sticky sidebar on desktop (or fixed bottom bar on mobile) with a booking/trial CTA that remains visible during scrolling.
- **FR-025**: Student reviews section MUST display individual review cards with reviewer name, rating, date, and review text.

#### Programs / Courses
- **FR-026**: Programs listing page MUST display course cards with title, description summary, category, level indicator, duration, and CTA.
- **FR-027**: Programs listing page MUST organize courses by category with visible category headers or filter tabs.
- **FR-028**: Program detail page MUST include sections for overview, target audience ("Who It's For"), inclusions ("What's Included"), learning outcomes, instructor summary, enrollment CTA, and FAQ.

#### Supporting Pages
- **FR-029**: How It Works page MUST present a step-by-step process (at least 3 steps) explaining the student journey from discovery to first lesson.
- **FR-030**: About page MUST include academy story, mission/vision, teaching philosophy, "Why Choose Us" section, trust indicators, and a CTA.
- **FR-031**: Contact page MUST include a form with fields for name, email, subject, and message, with client-side validation for required fields and email format.
- **FR-032**: Contact page MUST display alternative contact methods (email address, phone number) and a link to the FAQ page.
- **FR-033**: FAQ page MUST display questions organized into at least 3 categories with an accordion interface where only one item expands at a time per category.
- **FR-034**: Blog listing page MUST display article cards with featured image, title, excerpt, author, publication date, and category/tag indicators.
- **FR-035**: Blog detail page MUST include the article body with proper typography, share buttons (social share links), author bio, and a related articles or "Read Next" section.
- **FR-036**: Privacy Policy and Terms of Service pages MUST present structured legal content with proper heading hierarchy and a last-updated date.

#### Interactive Behaviors
- **FR-037**: FAQ accordion items MUST expand and collapse with smooth CSS transitions when clicked.
- **FR-038**: Mobile navigation MUST toggle open/close with smooth animation and prevent background scrolling when open.
- **FR-039**: Header MUST support a sticky/fixed behavior on scroll, reducing in height or adjusting styling as the user scrolls down.
- **FR-040**: Contact form MUST validate fields on submission and display inline error messages for invalid inputs without page reload.
- **FR-041**: Announcement bar MUST be dismissible with a close button, and once dismissed, it remains hidden for the session.

#### Visual & Responsive
- **FR-042**: Website MUST be fully responsive across mobile (320px+), tablet (768px+), laptop (1024px+), and desktop (1280px+) breakpoints.
- **FR-043**: All interactive elements MUST have visible focus states for keyboard navigation.
- **FR-044**: All pages MUST use semantic HTML5 elements (header, nav, main, section, article, aside, footer) for accessibility and SEO.
- **FR-045**: All images MUST include alt text attributes (placeholder text acceptable for demo content).
- **FR-046**: Typography MUST follow a consistent hierarchy: one font family for headings, one for body text, with defined sizes for H1 through H4, body, small text, and captions.
- **FR-047**: Website MUST use a consistent color palette with primary, secondary, accent, neutral, success, and error colors defined as CSS custom properties or Tailwind config values.
- **FR-048**: All CTA buttons MUST follow a defined hierarchy: primary (solid, high contrast), secondary (outline or muted), and tertiary (text link style).

#### Content & SEO
- **FR-049**: Every page MUST have a unique, descriptive title tag structure and meta description placeholder.
- **FR-050**: All pages MUST include proper Open Graph meta tag placeholders for social sharing.
- **FR-051**: Internal links between pages MUST use descriptive anchor text (not "click here").
- **FR-052**: Heading hierarchy on every page MUST follow logical order (one H1 per page, H2s for sections, H3s for subsections).

### Key Entities

- **Teacher**: Represents an instructor on the platform. Key attributes: name, photo, headline, biography, qualifications, subjects taught, teaching style description, experience level, lesson formats offered, rating, review count, pricing indicator, availability status.
- **Subject/Category**: Represents an academic or skill area offered. Key attributes: name, icon/illustration reference, description, number of available teachers.
- **Program/Course**: Represents a structured learning offering. Key attributes: title, description, category, level (beginner/intermediate/advanced), duration, inclusions list, target audience description, learning outcomes, instructor reference, price/inquiry indicator.
- **Testimonial/Review**: Represents social proof content. Key attributes: reviewer name, reviewer role (student/parent), rating, review text, date, associated teacher or program reference.
- **Blog Article**: Represents educational content. Key attributes: title, excerpt, body content, featured image, author, publication date, category, tags, estimated read time.
- **Trust Metric**: Represents a quantified credibility indicator. Key attributes: label (e.g., "Active Students"), value (e.g., "15,000+"), icon reference.
- **FAQ Item**: Represents a frequently asked question. Key attributes: question text, answer text, category.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: First-time visitors can identify the academy's value proposition and locate the primary CTA within 5 seconds of landing on the homepage.
- **SC-002**: A visitor can navigate from the homepage to any required page within 2 clicks using the global navigation.
- **SC-003**: The homepage loads and renders all above-the-fold content on a standard mobile connection (3G simulated) within 4 seconds.
- **SC-004**: All pages score 90+ on a Lighthouse accessibility audit when evaluated with demo content.
- **SC-005**: The website is fully usable on screens as small as 320px wide with no horizontal scrolling, no overlapping elements, and all CTAs tappable.
- **SC-006**: Every interactive element (accordion, menu, form) is operable using keyboard-only navigation (Tab, Enter, Escape).
- **SC-007**: A visitor can complete the contact form submission flow (fill fields, submit, see confirmation) in under 60 seconds.
- **SC-008**: All 13 required pages are implemented with complete section structure and demo content that reads as Sana and professional.
- **SC-009**: The visual design is consistent across all pages: same color palette, typography scale, spacing rhythm, card styles, and button hierarchy with zero visual inconsistencies.
- **SC-010**: A non-technical reviewer assesses the website as "Sana and commercially credible" suitable for a real academy business launch.
- **SC-011**: The codebase contains zero dependencies on JavaScript frameworks, CSS frameworks other than Tailwind, or SPA patterns; all files are plain HTML, CSS, Tailwind CSS, and vanilla JavaScript.
- **SC-012**: Teacher listing page displays at least 8 teacher cards with all required information fields populated with realistic demo data.
- **SC-013**: All pages pass W3C HTML validation with no errors (warnings acceptable for Tailwind utility classes).

## Assumptions

- **Academy Brand**: The academy brand name is "Sana Academy" or a placeholder to be replaced. Color palette and logo will use Sana placeholder values that can be swapped.
- **Demo Content**: All content (teacher bios, course descriptions, blog articles, testimonials) will use realistic, high-quality placeholder text that reflects the Sana tone, not lorem ipsum.
- **Images**: Placeholder images will use professional stock photo services (referenced via URL) or solid-color placeholder blocks with appropriate dimensions.
- **No Backend**: No server-side logic, API calls, or data persistence exists. All data is hardcoded in the HTML. Filter/sort interactions provide visual feedback only.
- **Future CTAs**: CTAs like "Book a Free Trial" or "Enroll Now" will link to the Contact page or display a lightweight modal explaining the feature is coming soon, since no booking system exists yet.
- **Single Language**: The website is in English only. RTL or internationalization is not in scope.
- **Hosting**: The site will be hosted as static files, served directly from a file server or GitHub Pages-compatible environment.
- **Tailwind Delivery**: Tailwind CSS will be included via CDN link for simplicity, with a Tailwind config for custom theme values. No build step is required.
- **Icon System**: Icons will use an inline SVG approach or a lightweight icon library (e.g., Heroicons via CDN) consistent with Tailwind's ecosystem.
- **Newsletter Form**: The newsletter signup in the footer captures visual input only; no email service integration exists.

## Scope Boundaries

### In Scope
- All 13 required pages with complete section structure and demo content
- Global header with desktop and mobile navigation
- Global footer with all required elements
- All interactive behaviors (accordion, mobile menu, sticky header, form validation, announcement bar dismiss)
- Responsive design across all specified breakpoints
- Consistent visual design system (typography, colors, spacing, components)
- SEO-ready semantic HTML structure
- Accessibility fundamentals (focus states, semantic markup, alt text, form labels)
- Realistic Sana demo content

### Out of Scope
- Backend logic, APIs, or server-side rendering
- User authentication or account creation
- Real booking/scheduling functionality
- Payment processing
- Real-time teacher availability
- Database or data persistence
- Email sending (contact form, newsletter)
- Search functionality with actual filtering/sorting logic
- CMS integration
- Analytics integration
- Third-party chat widgets
- Multi-language support
- Optional pages (Trial Landing, Success Stories, Pricing, Become a Teacher) unless explicitly added later

### Anticipated Future Pages (Constitution Principle VI)
Per the constitution's SEO-Aware Frontend Structure principle, the following page families are anticipated in the architecture even though they are not implemented in this phase. Future-feature CTAs (e.g., "Book a Trial," pricing links) MUST route to the Contact page or display a "Coming Soon" modal, establishing link placeholders that can be swapped for real pages later without architectural changes:
- **Pricing**: Dedicated pricing/plans page
- **Trial Booking**: Dedicated trial lesson booking flow

## Dependencies

- **Tailwind CSS CDN**: Requires access to the Tailwind CSS CDN for styling
- **Placeholder Images**: Requires access to a placeholder image service or pre-selected stock image URLs
- **Icon Library**: Requires access to an icon set (Heroicons CDN or inline SVGs)
- **Web Fonts**: Requires access to Google Fonts or equivalent for Sana typography (e.g., Inter for body, a serif or display font for headings)
