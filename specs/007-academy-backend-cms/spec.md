# Feature Specification: Academy Backend CMS

**Feature Branch**: `007-academy-backend-cms`  
**Created**: 2026-04-02  
**Status**: Draft  
**Input**: Convert the existing Sana Academy frontend into a fully manageable Django-backed website with models, admin, views, and queries supporting every frontend page and section.

---

## Non-Negotiable Frontend Preservation Rule

The existing frontend templates are **locked presentation contracts**. The backend must satisfy them. This means:

- No existing frontend section is to be removed
- No existing frontend option is to be dropped
- No CTA block is to be ignored
- No teacher/profile/course/blog/FAQ/contact/pricing/trust/statistics/testimonial/material/partner section is to be left unsupported
- Every designed frontend detail must receive appropriate backend support
- The backend adapts to the frontend, not the other way around

---

## Feature Summary

Sana Academy has a complete, production-quality Arabic RTL frontend with 10+ pages and 100+ distinct content sections. All content is currently hardcoded in HTML templates. This backend phase converts that static frontend into a fully dynamic, admin-managed Django CMS without altering the frontend design.

**Problem**: All website content (teachers, courses, pricing, blog posts, FAQs, testimonials, team members, stats, partner logos, contact info) is hardcoded in HTML. Any content change requires a developer to edit template files. There is no admin panel, no content management, and no structured data.

**Opportunity**: By building Django models, admin interfaces, views, and template integration for every frontend section, the site owner can manage all content through Django admin without developer involvement.

## Goals

1. Every frontend section becomes admin-manageable
2. Structured data models for all content types (teachers, courses, blogs, FAQs, pricing, testimonials, team, partners, stats, subjects)
3. Publish/draft states for content that should be reviewable before going live
4. Ordering control for lists, cards, and grids
5. SEO/meta fields for all public-facing pages
6. Clean query patterns feeding existing templates
7. Contact form submissions stored and viewable in admin
8. Slug-based URLs for teachers, blog posts, and subjects

## Non-Goals

1. User registration/authentication system (future phase)
2. Payment processing or e-commerce
3. Real-time chat or messaging
4. Mobile app API endpoints
5. Multi-language/i18n support (Arabic-only for now)
6. Advanced search engine (simple filtering only)
7. Email notification system
8. Analytics/reporting dashboards

---

## Existing Frontend Alignment

### Pages Identified (10 public pages + 2 legal pages)

| Page | Template Location | Sections Count |
| ---- | ----------------- | -------------- |
| Homepage | `apps/main/templates/index.html` | 15 sections |
| About | `apps/about/templates/about.html` | 9 sections |
| Teachers Listing | `apps/teacher/templates/teachers.html` | 6 sections |
| Teacher Profile | `apps/teacher/templates/teacher-profile.html` | 11 sections |
| How It Works | `apps/about/templates/how-it-works.html` | 6 sections |
| Pricing | `apps/price/templates/pricing.html` | 6 sections |
| Blog Listing | `apps/blogs/templates/blog.html` | 6 sections |
| Blog Post Detail | `apps/blogs/templates/blog-post.html` | 6 sections |
| FAQ | (needs template in appropriate app) | 7 sections |
| Contact | `apps/contact/templates/contact.html` | 9 sections |
| Privacy Policy | `apps/main/templates/privacy.html` | 1 section |
| Terms of Service | `apps/main/templates/terms.html` | 1 section |

### Current Django App Alignment

| App | Responsibility |
| --- | -------------- |
| `main` | Homepage content, shared site settings, global content blocks, stats, partners, hero, subjects, app promo, legal pages |
| `about` | About page (mission, vision, story, team, achievements), How It Works page (process steps, why-us features, parent monitoring) |
| `teacher` | Teacher profiles, teacher listing, subjects/specializations, reviews, availability |
| `course` | Subjects/courses catalog, educational levels, educational services |
| `blogs` | Blog categories, blog posts, authors |
| `contact` | Contact info, contact form submissions, inquiry types, operating hours |
| `price` | Pricing plans, plan features, comparison table, pricing FAQ |

---

## Page-by-Page Backend Support Mapping

### Page 1: Homepage (`apps/main/templates/index.html`)

#### Section 1.1: Hero Section
- **Content**: Headline, subheading, description text, 2 CTA buttons (Browse Courses, Open Account), hero image
- **Data type**: Semi-static (admin-editable singleton)
- **Model**: `main.HeroSection` (singleton)
- **Fields**: `headline` (CharField 200), `subheading` (CharField 300), `description` (TextField), `primary_cta_text` (CharField 50), `primary_cta_url` (CharField 200), `secondary_cta_text` (CharField 50), `secondary_cta_url` (CharField 200), `hero_image` (ImageField)
- **Admin editable**: Yes
- **Ordering**: N/A (singleton)
- **SEO/meta**: Homepage-level meta handled by `main.PageMeta`

#### Section 1.2: Trust Statistics Bar
- **Content**: 4 stats (10,000+ students, 500+ teachers, 50,000+ sessions, 98% satisfaction) each with number, label, description
- **Data type**: Admin-editable collection
- **Model**: `main.TrustStat`
- **Fields**: `number` (CharField 20 - supports "+10,000" format), `label` (CharField 100), `description` (CharField 200), `icon` (CharField 50 - icon name reference), `order` (PositiveIntegerField)
- **Admin editable**: Yes
- **Ordering**: `order` field
- **Featured**: N/A

#### Section 1.3: Educational Services Grid (3 cards)
- **Content**: 3 service cards (Private Tutoring, Aptitude/Achievement Tests, Curricula) each with title, description, feature list, image, CTA
- **Data type**: Admin-editable collection
- **Model**: `main.EducationalService`
- **Fields**: `title` (CharField 100), `description` (TextField), `icon` (CharField 50), `image` (ImageField, optional), `cta_text` (CharField 50), `cta_url` (CharField 200), `order` (PositiveIntegerField), `is_active` (BooleanField default True)
- **Related model**: `main.ServiceFeature` - `service` (FK), `text` (CharField 200), `order` (PositiveIntegerField)
- **Admin editable**: Yes, with inline ServiceFeature
- **Ordering**: `order` field

#### Section 1.4: Partners/Trust Logos (8 logos)
- **Content**: 8 partner logos (King Saud University, Ministry of Education, etc.)
- **Data type**: Admin-editable collection
- **Model**: `main.Partner`
- **Fields**: `name` (CharField 100), `logo` (ImageField/SVGField), `url` (URLField, optional), `order` (PositiveIntegerField), `is_active` (BooleanField default True)
- **Admin editable**: Yes
- **Ordering**: `order` field

#### Section 1.5: Private Tutoring Feature Section
- **Content**: Heading, description, 6 feature bullet points, illustration image
- **Data type**: Semi-static (admin-editable singleton)
- **Model**: `main.FeatureBlock` (reusable, with `slug` identifier like `private-tutoring`)
- **Fields**: `slug` (SlugField unique), `title` (CharField 200), `description` (TextField), `image` (ImageField, optional), `order` (PositiveIntegerField), `is_active` (BooleanField)
- **Related model**: `main.FeaturePoint` - `feature_block` (FK), `text` (CharField 300), `order` (PositiveIntegerField)
- **Admin editable**: Yes, with inline FeaturePoint

#### Section 1.6: Aptitude/Assessment Tests Feature Section
- **Content**: Heading, 3 tabs (Quantitative, Verbal, Achievement), 6 feature points per tab
- **Data type**: Admin-editable
- **Model**: Reuses `main.FeatureBlock` with slug `aptitude-tests`
- **Related model**: `main.FeatureTab` - `feature_block` (FK), `title` (CharField 100), `order` (PositiveIntegerField)
- **Related model**: `main.FeatureTabPoint` - `tab` (FK to FeatureTab), `text` (CharField 300), `order` (PositiveIntegerField)
- **Admin editable**: Yes, with nested inlines

#### Section 1.7: Subjects Grid (8 subject cards)
- **Content**: 8 subject cards (Mathematics, Physics, Chemistry, English, Arabic, Biology, Aptitude, Achievement) each with name, description, icon
- **Data type**: Fully dynamic
- **Model**: `course.Subject`
- **Fields**: `name` (CharField 100), `slug` (SlugField unique), `description` (CharField 200), `icon` (CharField 50), `order` (PositiveIntegerField), `is_active` (BooleanField default True)
- **Admin editable**: Yes
- **Ordering**: `order` field

#### Section 1.8: Teachers Showcase Grid (8 teacher cards)
- **Content**: 8 teacher cards with initials, name, subject, experience years, rating, student count, profile link
- **Data type**: Fully dynamic (pulls from teacher app)
- **Model**: `teacher.Teacher` (featured teachers query)
- **Query**: `Teacher.objects.filter(is_active=True, is_featured=True).select_related('primary_subject').order_by('order')[:8]`
- **Admin editable**: Via teacher admin
- **Ordering**: `order` field on Teacher
- **Featured flag**: `is_featured` boolean on Teacher

#### Section 1.9: Testimonials Carousel (4 items)
- **Content**: 4 testimonial cards with student initials, name, level/subject, rating, quote text
- **Data type**: Fully dynamic
- **Model**: `main.Testimonial`
- **Fields**: `student_name` (CharField 100), `student_initials` (CharField 10), `level` (CharField 100 - e.g., "Second-year Secondary"), `subject` (CharField 100 - e.g., "Mathematics"), `rating` (PositiveSmallIntegerField 1-5), `quote` (TextField), `order` (PositiveIntegerField), `is_active` (BooleanField default True), `is_featured` (BooleanField default False), `page` (CharField 50 - which page to show on: "homepage", "teachers", "pricing")
- **Admin editable**: Yes
- **Ordering**: `order` field
- **Featured**: `is_featured` for homepage carousel

#### Section 1.10: How to Start Steps (4 steps)
- **Content**: 4 numbered process steps with title, description, icon
- **Data type**: Admin-editable collection
- **Model**: `main.ProcessStep`
- **Fields**: `step_number` (PositiveSmallIntegerField), `title` (CharField 100), `description` (TextField), `icon` (CharField 50), `order` (PositiveIntegerField), `is_active` (BooleanField default True)
- **Admin editable**: Yes
- **Ordering**: `order` field

#### Section 1.11: FAQ Section (10 accordion items)
- **Content**: 10 expandable Q&A items covering registration, teacher switching, payments, scheduling, etc.
- **Data type**: Fully dynamic (pulls from FAQ model, filtered for homepage)
- **Model**: `main.FAQ`
- **Fields**: `question` (CharField 300), `answer` (TextField), `category` (CharField 50 choices: general/pricing/teachers/scheduling/platform), `order` (PositiveIntegerField), `is_active` (BooleanField), `show_on_homepage` (BooleanField default False)
- **Admin editable**: Yes
- **Ordering**: `order` field
- **Query**: `FAQ.objects.filter(is_active=True, show_on_homepage=True).order_by('order')[:10]`

#### Section 1.12: Mobile App Promo Section
- **Content**: Heading, subheading, description, app preview dashboard mockup, 2 store badges (Google Play, App Store)
- **Data type**: Semi-static singleton
- **Model**: `main.AppPromoSection` (singleton)
- **Fields**: `title` (CharField 200), `subtitle` (CharField 200), `description` (TextField), `preview_image` (ImageField), `google_play_url` (URLField, optional), `app_store_url` (URLField, optional), `is_active` (BooleanField default True)
- **Admin editable**: Yes

#### Section 1.13: Final CTA Section
- **Content**: Heading, subheading, body text, 2 CTA buttons, social proof text ("10,000+ students")
- **Data type**: Semi-static singleton
- **Model**: `main.CTABlock` (reusable, slug-identified)
- **Fields**: `slug` (SlugField unique), `heading` (CharField 200), `subheading` (CharField 200), `body_text` (TextField, optional), `primary_cta_text` (CharField 50), `primary_cta_url` (CharField 200), `secondary_cta_text` (CharField 50, optional), `secondary_cta_url` (CharField 200, optional), `social_proof_text` (CharField 200, optional), `is_active` (BooleanField default True)
- **Admin editable**: Yes

#### Section 1.14: Footer
- **Content**: Logo, description, 6 social links, 4 navigation columns (More, Legal, Support, Accreditation), accreditation badge, WhatsApp/email contact, copyright
- **Data type**: Semi-static (site-wide settings)
- **Model**: `main.SiteSettings` (singleton) for social links, contact info, copyright
- **Fields**: `site_name` (CharField 100), `site_description` (TextField), `logo` (ImageField), `logo_white` (ImageField), `phone` (CharField 20), `email` (EmailField), `whatsapp` (CharField 20), `address` (CharField 200), `google_maps_url` (URLField, optional), `copyright_text` (CharField 200), `accreditation_text` (TextField), `accreditation_badge` (ImageField)
- **Related model**: `main.SocialLink` - `platform` (CharField 30 choices), `url` (URLField), `order` (PositiveIntegerField), `is_active` (BooleanField)
- **Admin editable**: Yes

---

### Page 2: About Page (`apps/about/templates/about.html`)

#### Section 2.1: Page Header
- **Content**: "Who Are We" heading, subtitle, icon
- **Model**: `about.PageContent` (singleton, slug `about`)
- **Fields**: `title` (CharField 200), `subtitle` (TextField), `header_icon` (ImageField, optional), `meta_title` (CharField 200), `meta_description` (TextField)
- **Admin editable**: Yes
- **SEO/meta**: Yes

#### Section 2.2: Mission Section
- **Content**: Icon, heading "Our Mission", 2 paragraphs
- **Model**: `about.ContentBlock` with slug `mission`
- **Fields**: `slug` (SlugField unique), `title` (CharField 200), `content` (TextField - rich text), `icon` (ImageField, optional), `order` (PositiveIntegerField), `is_active` (BooleanField)
- **Admin editable**: Yes

#### Section 2.3: Vision Section
- **Content**: Icon, heading "Our Vision", 2 paragraphs
- **Model**: Reuses `about.ContentBlock` with slug `vision`
- **Admin editable**: Yes

#### Section 2.4: Our Story Section
- **Content**: Heading "Our Story", 4 paragraphs of narrative text
- **Model**: Reuses `about.ContentBlock` with slug `our-story`
- **Admin editable**: Yes (rich text for multi-paragraph content)

#### Section 2.5: Statistics Block (4 stats)
- **Content**: 4 stats (Founded 2021, 500+ Teachers, 10,000+ Students, 98% Satisfaction)
- **Model**: `about.Statistic`
- **Fields**: `number` (CharField 20), `label` (CharField 100), `icon` (CharField 50), `order` (PositiveIntegerField), `is_active` (BooleanField)
- **Admin editable**: Yes
- **Ordering**: `order` field

#### Section 2.6: Leadership Team (6 members)
- **Content**: 6 team member cards with name, title, description, avatar
- **Model**: `about.TeamMember`
- **Fields**: `name` (CharField 100), `title` (CharField 100), `description` (TextField), `photo` (ImageField, optional), `order` (PositiveIntegerField), `is_active` (BooleanField default True)
- **Admin editable**: Yes
- **Ordering**: `order` field

#### Section 2.7: Achievements Section (4 stats)
- **Content**: 4 achievement stats with icons (500+ teachers, 10,000+ students, 50,000+ sessions, 98% satisfaction)
- **Model**: `about.Achievement`
- **Fields**: `number` (CharField 20), `label` (CharField 100), `icon` (CharField 50), `order` (PositiveIntegerField), `is_active` (BooleanField)
- **Admin editable**: Yes
- **Ordering**: `order` field

#### Section 2.8: Partners & Accreditation (8 logos + badge)
- **Content**: 8 partner logos + accreditation badge with text
- **Data type**: Reuses `main.Partner` model (shared across pages)
- **Query**: `Partner.objects.filter(is_active=True).order_by('order')`
- **Admin editable**: Via main app partner admin

#### Section 2.9: CTA Section
- **Content**: "Join Sana Academy Family" heading, subheading, 2 CTAs, social proof
- **Model**: Reuses `main.CTABlock` with slug `about-cta`
- **Admin editable**: Yes

---

### Page 3: Teachers Listing Page (`apps/teacher/templates/teachers.html`)

#### Section 3.1: Page Hero
- **Content**: Heading, subheading about teacher qualifications, 3 stats (500+ teachers, 4.8 avg rating, 50,000+ sessions)
- **Model**: Part of `teacher.TeacherPageSettings` (singleton)
- **Fields**: `hero_title` (CharField 200), `hero_subtitle` (TextField), `meta_title` (CharField 200), `meta_description` (TextField)
- **Admin editable**: Yes
- **SEO/meta**: Yes

#### Section 3.2: Filter/Category Tabs (9 categories)
- **Content**: Filter tabs: All, Mathematics, Physics, Chemistry, English, Arabic, Biology, Aptitude, Achievement
- **Data type**: Dynamic, derived from `course.Subject`
- **Query**: `Subject.objects.filter(is_active=True).order_by('order')`
- **Admin editable**: Via Subject admin

#### Section 3.3: Teacher Cards Grid (8 cards)
- **Content**: 8 teacher cards with initials, name, subject, experience years, rating, student count, "View Profile" CTA
- **Model**: `teacher.Teacher`
- **Fields**: `name` (CharField 100), `slug` (SlugField unique), `initials` (CharField 10), `primary_subject` (FK to `course.Subject`), `experience_years` (PositiveSmallIntegerField), `experience_description` (CharField 200 - e.g., "middle and secondary"), `rating` (DecimalField 2,1), `student_count` (PositiveIntegerField), `photo` (ImageField, optional), `is_active` (BooleanField default True), `is_featured` (BooleanField default False), `order` (PositiveIntegerField)
- **Admin editable**: Yes
- **Ordering**: `order` field (or by rating, configurable)
- **Featured**: `is_featured` for homepage display

#### Section 3.4: Statistics Section (4 stats)
- **Content**: 4 stats (500+ certified teachers, 4.8/5 rating, 50,000+ sessions, 98% satisfaction)
- **Model**: `teacher.TeacherStat`
- **Fields**: `number` (CharField 20), `label` (CharField 100), `description` (CharField 200), `icon` (CharField 50), `order` (PositiveIntegerField), `is_active` (BooleanField)
- **Admin editable**: Yes
- **Ordering**: `order` field

#### Section 3.5: Student Testimonials (4 testimonials)
- **Content**: 4 testimonial cards with student initials, name, level/subject, 5-star rating, quote
- **Model**: Reuses `main.Testimonial` filtered by `page='teachers'`
- **Query**: `Testimonial.objects.filter(is_active=True, page='teachers').order_by('order')[:4]`
- **Admin editable**: Via Testimonial admin with page filter

#### Section 3.6: CTA Section
- **Content**: "Start Now" heading, subheading, 2 CTAs, social proof
- **Model**: Reuses `main.CTABlock` with slug `teachers-cta`

---

### Page 4: Teacher Profile Page (`apps/teacher/templates/teacher-profile.html`)

#### Section 4.1: Breadcrumb Navigation
- **Content**: Home > Teachers > Teacher Name
- **Data type**: Auto-generated from teacher data
- **No model needed**: Built from URL and teacher name

#### Section 4.2: Teacher Header
- **Content**: Name, title/specialization, subjects list, experience years, session rate (SAR), star rating, 2 CTAs (Book Session, WhatsApp)
- **Model**: `teacher.Teacher` (extended fields)
- **Additional fields**: `title` (CharField 200 - e.g., "Mathematics specialist teacher"), `session_rate` (DecimalField - starting price in SAR), `whatsapp_number` (CharField 20, optional)
- **Admin editable**: Yes

#### Section 4.3: Key Statistics Bar (4 stats)
- **Content**: Rating, Active Students, Completed Sessions, Experience Years
- **Data type**: Derived from Teacher model fields
- **Fields on Teacher**: `rating`, `student_count`, `completed_sessions` (PositiveIntegerField), `experience_years`

#### Section 4.4: Teacher Bio Section
- **Content**: Multi-paragraph bio, qualifications (Bachelor's, Master's), teaching philosophy
- **Model**: `teacher.Teacher`
- **Fields**: `bio` (TextField - rich text), `qualifications` (TextField - rich text or structured)

#### Section 4.5: Key Features (3 checkmarks)
- **Content**: "Recorded sessions available", "Weekly progress reports", "Schedule flexibility"
- **Model**: `teacher.TeacherFeature`
- **Fields**: `teacher` (FK to Teacher), `text` (CharField 200), `order` (PositiveIntegerField), `is_active` (BooleanField)
- **Admin editable**: Yes, inline on Teacher

#### Section 4.6: Specializations Section
- **Content**: Subjects organized by educational level (e.g., Mathematics - Middle School: Grades 1-3, Mathematics - Secondary: Grades 1-3)
- **Model**: `teacher.TeacherSpecialization`
- **Fields**: `teacher` (FK to Teacher), `subject` (FK to `course.Subject`), `level` (CharField 100 - e.g., "Middle School"), `grades` (CharField 200 - e.g., "Grades 1-3"), `order` (PositiveIntegerField)
- **Admin editable**: Yes, inline on Teacher

#### Section 4.7: Student Reviews (4 reviews)
- **Content**: 4 review cards with student name, level/subject, 5-star rating, quote text, date
- **Model**: `teacher.TeacherReview`
- **Fields**: `teacher` (FK to Teacher), `student_name` (CharField 100), `student_initials` (CharField 10), `level` (CharField 100), `subject` (CharField 100), `rating` (PositiveSmallIntegerField 1-5), `review_text` (TextField), `review_date` (DateField), `is_active` (BooleanField default True), `order` (PositiveIntegerField)
- **Admin editable**: Yes, inline on Teacher
- **Ordering**: `order` field or `-review_date`

#### Section 4.8: Performance Metrics Dashboard
- **Content**: 4 metrics (1,500+ sessions, 230 students, 4.9 rating, 3 years on platform)
- **Data type**: Derived from Teacher model fields
- **Fields on Teacher**: `completed_sessions`, `student_count`, `rating`, `platform_years` (PositiveSmallIntegerField)

#### Section 4.9: Availability Schedule
- **Content**: Daily availability (Saturday-Tuesday, 4 PM - 10 PM), note about scheduling
- **Model**: `teacher.TeacherAvailability`
- **Fields**: `teacher` (FK to Teacher), `days` (CharField 200 - e.g., "Saturday-Tuesday"), `start_time` (TimeField), `end_time` (TimeField), `note` (CharField 300, optional), `order` (PositiveIntegerField)
- **Admin editable**: Yes, inline on Teacher

#### Section 4.10: Similar Teachers (4 cards)
- **Content**: 4 teacher cards of related teachers (same or similar subjects)
- **Data type**: Dynamic query
- **Query**: `Teacher.objects.filter(is_active=True, primary_subject=teacher.primary_subject).exclude(pk=teacher.pk).order_by('order')[:4]`
- **Fallback**: If fewer than 4, fill with other active teachers

#### Section 4.11: Final Booking CTA
- **Content**: Heading, description, 2 CTAs (Book First Session, WhatsApp), trial session note
- **Model**: Reuses `main.CTABlock` with slug `teacher-profile-cta`

---

### Page 5: How It Works Page (`apps/about/templates/how-it-works.html`)

#### Section 5.1: Hero Section
- **Content**: Heading, subheading description, 2 CTAs (Start Now, Contact Us)
- **Model**: `about.PageContent` with slug `how-it-works`
- **Fields**: Same as about PageContent + CTA fields
- **SEO/meta**: Yes

#### Section 5.2: Six-Step Process Flow (6 steps)
- **Content**: 6 sequential steps with number, title, description, icon
- **Model**: `about.HowItWorksStep`
- **Fields**: `step_number` (PositiveSmallIntegerField), `title` (CharField 100), `description` (TextField), `icon` (CharField 50), `order` (PositiveIntegerField), `is_active` (BooleanField)
- **Admin editable**: Yes
- **Ordering**: `order` field

#### Section 5.3: "Why Us" Features Grid (6 features)
- **Content**: 6 feature highlight cards with icon, title, description
- **Model**: `about.WhyUsFeature`
- **Fields**: `title` (CharField 100), `description` (TextField), `icon` (CharField 50), `order` (PositiveIntegerField), `is_active` (BooleanField)
- **Admin editable**: Yes
- **Ordering**: `order` field

#### Section 5.4: Success Stories / Testimonials (3 items)
- **Content**: 3 testimonial cards with name, grade/subject, rating, quote
- **Model**: Reuses `main.Testimonial` filtered by `page='how-it-works'`
- **Query**: `Testimonial.objects.filter(is_active=True, page='how-it-works').order_by('order')[:3]`

#### Section 5.5: Parent Monitoring Features
- **Content**: Heading, description, 3 core features with titles/descriptions, 4 monitoring capability bullet points
- **Model**: `about.ParentFeature`
- **Fields**: `title` (CharField 100), `description` (TextField), `icon` (CharField 50), `order` (PositiveIntegerField), `is_active` (BooleanField), `feature_type` (CharField 20 choices: 'core'/'capability')
- **Admin editable**: Yes
- **Ordering**: `order` field, grouped by `feature_type`

#### Section 5.6: CTA Footer Section
- **Content**: Heading, subheading, 2 CTAs, free trial note
- **Model**: Reuses `main.CTABlock` with slug `how-it-works-cta`

---

### Page 6: Pricing Page (`apps/price/templates/pricing.html`)

#### Section 6.1: Hero Section
- **Content**: "Flexible Plans" heading, description
- **Model**: `price.PricingPageSettings` (singleton)
- **Fields**: `hero_title` (CharField 200), `hero_subtitle` (TextField), `meta_title` (CharField 200), `meta_description` (TextField)
- **Admin editable**: Yes
- **SEO/meta**: Yes

#### Section 6.2: Three Pricing Tiers (3 plans)
- **Content**: 3 pricing cards (Basic 150 SAR, Premium 200 SAR, Professional 300 SAR) each with name, price, tagline, feature list with included/excluded indicators, CTA, optional "Most Requested" badge
- **Model**: `price.PricingPlan`
- **Fields**: `name` (CharField 100), `slug` (SlugField unique), `price` (DecimalField), `price_unit` (CharField 50 - "per session"), `tagline` (CharField 200), `cta_text` (CharField 50), `cta_url` (CharField 200), `is_popular` (BooleanField default False - for "Most Requested" badge), `order` (PositiveIntegerField), `is_active` (BooleanField default True)
- **Related model**: `price.PlanFeature` - `plan` (FK), `text` (CharField 200), `is_included` (BooleanField - True=checkmark, False=X), `order` (PositiveIntegerField)
- **Admin editable**: Yes, with inline PlanFeature
- **Ordering**: `order` field

#### Section 6.3: Features Comparison Table (9 features x 3 plans)
- **Content**: Comparison table with feature rows and plan columns showing checkmarks, dashes, or text values
- **Model**: `price.ComparisonFeature`
- **Fields**: `feature_name` (CharField 100), `basic_value` (CharField 100 - supports text or "yes"/"no"), `premium_value` (CharField 100), `professional_value` (CharField 100), `order` (PositiveIntegerField), `is_active` (BooleanField)
- **Admin editable**: Yes
- **Ordering**: `order` field

#### Section 6.4: Payment & Subscription FAQ (5 questions)
- **Content**: 5 expandable Q&A items about payment methods, refunds, discounts, free trial, upgrades
- **Model**: `price.PricingFAQ`
- **Fields**: `question` (CharField 300), `answer` (TextField), `order` (PositiveIntegerField), `is_active` (BooleanField)
- **Admin editable**: Yes
- **Ordering**: `order` field

#### Section 6.5: Student Testimonials (3 items)
- **Content**: 3 testimonials from students about pricing value
- **Model**: Reuses `main.Testimonial` filtered by `page='pricing'`
- **Query**: `Testimonial.objects.filter(is_active=True, page='pricing').order_by('order')[:3]`

#### Section 6.6: Final CTA Section
- **Content**: "Book Your Free Trial" heading, subheading, 2 CTAs, trust text
- **Model**: Reuses `main.CTABlock` with slug `pricing-cta`

---

### Page 7: Blog Listing Page (`apps/blogs/templates/blog.html`)

#### Section 7.1: Page Title
- **Content**: "Blog" heading, description
- **Model**: Part of blog view context or `blogs.BlogPageSettings` (singleton)
- **Fields**: `title` (CharField 200), `subtitle` (TextField), `meta_title` (CharField 200), `meta_description` (TextField)
- **SEO/meta**: Yes

#### Section 7.2: Featured Article (1 highlighted post)
- **Content**: 1 featured post with icon, title, category, excerpt, author, date, read time, CTA
- **Model**: `blogs.BlogPost` with `is_featured=True`
- **Query**: `BlogPost.objects.filter(status='published', is_featured=True).select_related('category', 'author').first()`

#### Section 7.3: Latest Articles Grid (6 posts)
- **Content**: 6 blog cards with icon, category, title, author, date
- **Model**: `blogs.BlogPost`
- **Fields**: `title` (CharField 200), `slug` (SlugField unique), `excerpt` (TextField), `content` (TextField - rich text), `category` (FK to `blogs.Category`), `author` (FK to `blogs.Author`), `icon` (CharField 50 - category icon), `featured_image` (ImageField, optional), `read_time_minutes` (PositiveSmallIntegerField), `status` (CharField choices: 'draft'/'published'), `is_featured` (BooleanField default False), `published_date` (DateTimeField), `created_at` (DateTimeField auto_now_add), `updated_at` (DateTimeField auto_now), `meta_title` (CharField 200, optional), `meta_description` (TextField, optional)
- **Admin editable**: Yes
- **Ordering**: `-published_date`
- **SEO/meta**: Yes per post

#### Section 7.4: Category Filter (5 categories)
- **Content**: Filter tabs: All, Education, Study Tips, Aptitude & Achievement, Platform News
- **Model**: `blogs.Category`
- **Fields**: `name` (CharField 100), `slug` (SlugField unique), `order` (PositiveIntegerField), `is_active` (BooleanField)
- **Admin editable**: Yes
- **Ordering**: `order` field

#### Section 7.5: Pagination (Load More)
- **Data type**: View logic
- **Implementation**: Paginated queryset or AJAX load-more pattern

#### Section 7.6: CTA Section
- **Model**: Reuses `main.CTABlock` with slug `blog-cta`

---

### Page 8: Blog Post Detail Page (`apps/blogs/templates/blog-post.html`)

#### Section 8.1: Breadcrumb Navigation
- **Content**: Home > Blog > Post Title
- **Data type**: Auto-generated from post data

#### Section 8.2: Article Header
- **Content**: Category badge, title, author name/title/initials, date, read time
- **Model**: `blogs.BlogPost` fields + related `Author`

#### Section 8.3: Article Body
- **Content**: Multi-section article with headings, paragraphs, pull quotes, bulleted lists
- **Model**: `blogs.BlogPost.content` field (rich text / TextField with markdown or HTML)
- **Admin editable**: Yes (rich text editor recommended)

#### Section 8.4: Author Bio Section
- **Content**: Author name, title, bio description, avatar
- **Model**: `blogs.Author`
- **Fields**: `name` (CharField 100), `slug` (SlugField unique), `title` (CharField 200 - e.g., "Manager of Educational Content"), `bio` (TextField), `initials` (CharField 10), `photo` (ImageField, optional), `is_active` (BooleanField)
- **Admin editable**: Yes

#### Section 8.5: Related Articles (3 posts)
- **Content**: 3 related post cards with category, title, author, date
- **Data type**: Dynamic query
- **Query**: `BlogPost.objects.filter(status='published', category=post.category).exclude(pk=post.pk).order_by('-published_date')[:3]`

#### Section 8.6: CTA Section
- **Model**: Reuses `main.CTABlock` with slug `blog-post-cta`

---

### Page 9: FAQ Page (needs template placement)

**Note**: The FAQ page template exists in `frontend/faq.html` but does not yet have a Django app template. It should be placed in `apps/main/templates/faq.html` or a dedicated FAQ section within the `main` app since FAQs are shared across the site.

#### Section 9.1: Page Header
- **Content**: "Frequently Asked Questions" heading, subtitle
- **Model**: Part of FAQ page view context
- **SEO/meta**: Yes via `main.PageMeta`

#### Section 9.2: Search Functionality
- **Content**: Search input to filter FAQ items
- **Data type**: Client-side JS filtering (already exists in frontend JS)

#### Section 9.3: Category Filter (6 categories)
- **Content**: Filter tabs: All, General, Pricing, Teachers, Scheduling, Platform
- **Data type**: Derived from `main.FAQ.category` choices
- **No separate model needed**: Categories are CharField choices on FAQ model

#### Section 9.4: FAQ Content (16+ questions across 5 categories)
- **Content**: Accordion Q&A grouped by category
  - General (3 questions): Registration, teacher switching, covered subjects
  - Pricing (3 questions): Session prices, package discounts, refund policy
  - Teachers (3 questions): Selection criteria, choosing specific teacher, qualifications
  - Scheduling (3 questions): Available times, rescheduling, session duration
  - Platform (4 questions): Online sessions, recordings, parent monitoring
- **Model**: `main.FAQ` (same model used for homepage FAQ section)
- **Query**: `FAQ.objects.filter(is_active=True).order_by('category', 'order')`
- **Admin editable**: Yes

#### Section 9.5: Help CTA (WhatsApp + Email)
- **Content**: "Didn't find your answer?" heading, WhatsApp button, email link
- **Data type**: Pulls from `main.SiteSettings` for WhatsApp/email

#### Section 9.6: Related Links (3 resource cards)
- **Content**: 3 cards linking to How It Works, Pricing, Contact
- **Model**: `main.RelatedLink`
- **Fields**: `title` (CharField 100), `url` (CharField 200), `icon` (CharField 50), `page` (CharField 50 - which page to show on), `order` (PositiveIntegerField), `is_active` (BooleanField)
- **Admin editable**: Yes

---

### Page 10: Contact Page (`apps/contact/templates/contact.html`)

#### Section 10.1: Hero Section
- **Content**: Contact page heading, "We're here to help" subheading
- **Model**: `contact.ContactPageSettings` (singleton)
- **Fields**: `hero_title` (CharField 200), `hero_subtitle` (TextField), `meta_title` (CharField 200), `meta_description` (TextField)
- **SEO/meta**: Yes

#### Section 10.2: Contact Form (5 fields)
- **Content**: Form with Full Name (required), Email (required), Phone (+966 prefix, optional), Subject dropdown (General inquiry, Book session, Complaint, Suggestion, Other), Message (required), Submit button
- **Model**: `contact.ContactSubmission`
- **Fields**: `full_name` (CharField 100), `email` (EmailField), `phone` (CharField 20, optional), `subject` (CharField 50 choices: inquiry/booking/complaint/suggestion/other), `message` (TextField), `is_read` (BooleanField default False), `created_at` (DateTimeField auto_now_add)
- **Admin editable**: View-only in admin (list display with filters and read status)

#### Section 10.3: Why Choose SanaAcademy (5 points)
- **Content**: 5 checkmark feature points about academy benefits
- **Model**: `contact.WhyChoosePoint`
- **Fields**: `text` (CharField 300), `order` (PositiveIntegerField), `is_active` (BooleanField)
- **Admin editable**: Yes

#### Section 10.4: WhatsApp CTA
- **Content**: "Contact via WhatsApp" button
- **Data type**: Pulls WhatsApp number from `main.SiteSettings`

#### Section 10.5: Contact Information (4 methods)
- **Content**: Phone (+966 11 400 0000), Email (info@premiumacademy.sa), WhatsApp (direct link), Address (Riyadh, Saudi Arabia), 6 social media icons
- **Data type**: Pulls from `main.SiteSettings` and `main.SocialLink`

#### Section 10.6: Operating Hours
- **Content**: Saturday-Thursday: 8 AM - 10 PM, Friday: Closed, note about platform booking
- **Model**: `contact.OperatingHours`
- **Fields**: `days` (CharField 100 - e.g., "Saturday-Thursday"), `hours` (CharField 100 - e.g., "8 AM - 10 PM"), `note` (CharField 300, optional), `order` (PositiveIntegerField), `is_active` (BooleanField)
- **Admin editable**: Yes

#### Section 10.7: Contact Page FAQ (5 questions)
- **Content**: 5 Q&A items about quick contact, support hours, office visit, reply time, free consultation
- **Model**: `contact.ContactFAQ`
- **Fields**: `question` (CharField 300), `answer` (TextField), `order` (PositiveIntegerField), `is_active` (BooleanField)
- **Admin editable**: Yes

#### Section 10.8: Location Section
- **Content**: "Our Location" heading, description, "Open in Google Maps" CTA, address display
- **Model**: Part of `main.SiteSettings` (`address`, `google_maps_url` URLField)

#### Section 10.9: CTA Section
- **Model**: Reuses `main.CTABlock` with slug `contact-cta` (if applicable)

---

### Pages 11-12: Privacy Policy & Terms of Service

- **Content**: Legal text pages
- **Model**: `main.LegalPage`
- **Fields**: `title` (CharField 200), `slug` (SlugField unique), `content` (TextField - rich text), `meta_title` (CharField 200), `meta_description` (TextField), `updated_at` (DateTimeField auto_now)
- **Admin editable**: Yes (rich text editor)
- **SEO/meta**: Yes

---

## User Scenarios & Testing

### User Story 1 - Admin Manages Homepage Content (Priority: P1)

A site administrator logs into Django admin and edits any homepage section (hero text, stats, services, testimonials, FAQ items, process steps, app promo) without touching any template code. Changes appear immediately on the public site.

**Why this priority**: The homepage is the primary traffic entry point. Making it admin-manageable is the highest-value deliverable.

**Independent Test**: Admin can change hero headline text via Django admin and see the updated text on the homepage without any code deployment.

**Acceptance Scenarios**:

1. **Given** an admin is logged into Django admin, **When** they edit the hero headline text and save, **Then** the homepage displays the new headline immediately
2. **Given** an admin creates a new Testimonial with `page='homepage'`, **When** they set `is_active=True` and save, **Then** the testimonial appears in the homepage carousel
3. **Given** an admin reorders FAQ items by changing `order` values, **When** they save, **Then** the homepage FAQ section reflects the new order

---

### User Story 2 - Admin Manages Teachers (Priority: P1)

A site administrator creates, edits, and manages teacher profiles including bio, specializations, reviews, availability, and featured status. Teachers appear on both the listing page and their individual profile pages.

**Why this priority**: Teachers are the core product. Their profiles drive conversion and must be fully manageable.

**Independent Test**: Admin creates a new teacher profile with all fields, and the teacher appears on the listing page and has a working profile page with all sections populated.

**Acceptance Scenarios**:

1. **Given** an admin creates a Teacher with `is_active=True`, **When** the teachers page loads, **Then** the teacher appears in the grid
2. **Given** an admin marks a teacher as `is_featured=True`, **When** the homepage loads, **Then** the teacher appears in the homepage teacher showcase
3. **Given** an admin adds reviews, specializations, and availability to a teacher, **When** the teacher profile page loads, **Then** all sections are populated with the admin-entered data

---

### User Story 3 - Admin Publishes Blog Posts (Priority: P2)

A site administrator creates blog posts with title, content, category, author, and featured status. Posts flow to the blog listing page and individual post pages with working category filtering and related posts.

**Why this priority**: Blog content drives SEO and organic traffic. It must be manageable independently of developers.

**Independent Test**: Admin creates a blog post with `status='published'`, and it appears on the blog listing page with correct category, author, and date.

**Acceptance Scenarios**:

1. **Given** an admin creates a BlogPost with `status='published'`, **When** the blog listing page loads, **Then** the post appears in the latest articles grid
2. **Given** an admin sets `is_featured=True` on a post, **When** the blog listing page loads, **Then** the post appears in the featured article section
3. **Given** a blog post has `status='draft'`, **When** the blog listing page loads, **Then** the post does NOT appear publicly

---

### User Story 4 - Admin Manages Pricing Plans (Priority: P2)

A site administrator edits pricing plans, plan features, comparison table, and pricing FAQ. Changes appear on the pricing page without code changes.

**Why this priority**: Pricing is directly tied to revenue and must be updateable quickly for promotions and plan changes.

**Independent Test**: Admin updates a plan price and features, and the pricing page shows the updated information.

**Acceptance Scenarios**:

1. **Given** an admin changes the Premium plan price from 200 to 180 SAR, **When** the pricing page loads, **Then** the displayed price shows 180 SAR
2. **Given** an admin marks a plan as `is_popular=True`, **When** the pricing page loads, **Then** that plan displays the "Most Requested" badge
3. **Given** an admin edits the comparison table features, **When** the pricing page loads, **Then** the table reflects the updated values

---

### User Story 5 - Visitors Submit Contact Forms (Priority: P2)

A site visitor fills out the contact form with name, email, phone, subject, and message. The submission is stored in the database and appears in Django admin for staff review.

**Why this priority**: Contact form is the primary conversion mechanism for prospective students and parents.

**Independent Test**: A visitor fills out and submits the contact form, and the submission appears in Django admin with all fields.

**Acceptance Scenarios**:

1. **Given** a visitor fills in all required contact form fields, **When** they click Submit, **Then** the submission is saved and a success message is displayed
2. **Given** a new contact submission arrives, **When** an admin opens Django admin ContactSubmission list, **Then** the submission appears with `is_read=False`
3. **Given** a visitor submits a form with invalid email, **When** they click Submit, **Then** the form shows a validation error and is NOT submitted

---

### User Story 6 - Admin Manages About & How It Works Pages (Priority: P3)

A site administrator edits mission, vision, story content, team members, process steps, and "Why Us" features for the about and how-it-works pages.

**Why this priority**: These pages change less frequently but must still be manageable for team updates and content refreshes.

**Independent Test**: Admin edits a team member's title and bio, and the about page reflects the change.

**Acceptance Scenarios**:

1. **Given** an admin edits a TeamMember name, **When** the about page loads, **Then** the updated name appears in the leadership team section
2. **Given** an admin adds a 7th HowItWorksStep, **When** the how-it-works page loads, **Then** all 7 steps are displayed in order

---

### User Story 7 - Admin Manages FAQs Across Pages (Priority: P3)

A site administrator creates, edits, and categorizes FAQ items. FAQs appear on the FAQ page grouped by category, and selected FAQs appear on the homepage.

**Why this priority**: FAQ content reduces support burden and must be maintainable as new questions emerge.

**Independent Test**: Admin creates an FAQ with `show_on_homepage=True`, and it appears on both the FAQ page and homepage FAQ section.

**Acceptance Scenarios**:

1. **Given** an admin creates an FAQ in category 'general', **When** the FAQ page loads with 'General' filter, **Then** the question appears
2. **Given** an admin sets `show_on_homepage=True` on an FAQ, **When** the homepage loads, **Then** the FAQ appears in the homepage FAQ section

---

### Edge Cases

- What happens when no featured blog post exists? The featured section should hide gracefully or show the most recent post.
- What happens when a teacher has no reviews? The reviews section should display a "No reviews yet" placeholder.
- What happens when all testimonials for a page are inactive? The testimonials section should not render.
- What happens when an admin deletes a Subject that teachers are linked to? Foreign key protection should prevent deletion if teachers reference it.
- What happens when the contact form subject dropdown has no options? There must always be at least a default "General Inquiry" choice.

---

## Requirements

### Functional Requirements

- **FR-001**: System MUST support singleton models for page-level settings (homepage hero, pricing page settings, contact page settings) ensuring exactly one instance per page
- **FR-002**: System MUST support `is_active` boolean on all content models to allow hiding content without deleting it
- **FR-003**: System MUST support `order` field on all list/grid models to control display sequence
- **FR-004**: System MUST support `is_featured` boolean on teachers and blog posts for homepage/highlight placement
- **FR-005**: System MUST support publish/draft status on blog posts via `status` field with choices `draft`/`published`
- **FR-006**: System MUST store contact form submissions with `is_read` tracking for admin workflow
- **FR-007**: System MUST support slug fields on teachers, blog posts, subjects, categories, pricing plans, and legal pages for SEO-friendly URLs
- **FR-008**: System MUST support SEO meta fields (`meta_title`, `meta_description`) on all public page-level models
- **FR-009**: System MUST support image/media uploads for teachers (photos), blog posts (featured images), team members (photos), partners (logos), and hero section (images)
- **FR-010**: System MUST support rich text content for blog post bodies, teacher bios, legal pages, about page content blocks, and FAQ answers
- **FR-011**: System MUST support the `page` field on Testimonial model to control which page(s) a testimonial appears on
- **FR-012**: System MUST support inline editing in admin for related models (PlanFeature on PricingPlan, TeacherReview on Teacher, ServiceFeature on EducationalService, etc.)
- **FR-013**: System MUST serve the FAQ page with client-side category filtering (categories derived from FAQ model `category` choices)
- **FR-014**: System MUST protect against cascading deletes on foreign keys where content would be lost (use `PROTECT` on Subject FK from Teacher)
- **FR-015**: System MUST support a shared `SiteSettings` singleton for global content (site name, contact info, social links, copyright, accreditation)
- **FR-016**: System MUST support reusable `CTABlock` model identified by slug for CTA sections across multiple pages
- **FR-017**: System MUST support blog post category filtering on the blog listing page
- **FR-018**: System MUST generate related/similar items (similar teachers by subject, related blog posts by category)

### Key Entities

- **SiteSettings**: Global configuration (name, contact info, social links, copyright, accreditation). Singleton. Used by footer/header on every page.
- **SocialLink**: Social media platform links. Related to SiteSettings. Ordered.
- **HeroSection**: Homepage hero content. Singleton. Headline, image, CTAs.
- **TrustStat**: Homepage trust statistics bar. 4+ items with number/label/icon. Ordered.
- **EducationalService**: Homepage services grid cards (3). Title, description, features list. Ordered.
- **ServiceFeature**: Feature bullet points within an EducationalService. FK to EducationalService. Ordered.
- **Partner**: Partner/accreditation logos. Shared across homepage and about page. Ordered.
- **FeatureBlock**: Reusable feature content blocks identified by slug. Used for Private Tutoring and Aptitude sections.
- **FeaturePoint**: Bullet points within a FeatureBlock. FK to FeatureBlock. Ordered.
- **FeatureTab**: Tabs within a FeatureBlock (for Aptitude section). FK to FeatureBlock. Ordered.
- **FeatureTabPoint**: Points within a FeatureTab. FK to FeatureTab. Ordered.
- **Subject**: Academic subjects (8). Name, slug, icon. Used in teacher filters and subjects grid. Belongs to `course` app.
- **Teacher**: Teacher profiles. Name, slug, subject, experience, rating, bio, photo, featured status. Core entity in `teacher` app.
- **TeacherFeature**: Teacher-specific feature checkmarks (e.g., "Recorded sessions"). FK to Teacher.
- **TeacherSpecialization**: Teacher subject-level-grade mappings. FK to Teacher and Subject.
- **TeacherReview**: Student reviews for a teacher. FK to Teacher. With date, rating, quote.
- **TeacherAvailability**: Teacher schedule slots. FK to Teacher. Days and time range.
- **Testimonial**: Student testimonials with page targeting. Shared across homepage, teachers, pricing, how-it-works pages.
- **ProcessStep**: Homepage "How to Start" steps (4). Numbered, titled, described.
- **FAQ**: Shared FAQ items with category and homepage flag. Used on FAQ page and homepage.
- **AppPromoSection**: Homepage mobile app promo block. Singleton.
- **CTABlock**: Reusable CTA sections identified by slug. Used across 6+ pages.
- **PageContent**: About page content blocks (mission, vision, story). Slug-identified.
- **ContentBlock**: Reusable content blocks in about app. Slug-identified.
- **Statistic**: About page statistics. Ordered.
- **TeamMember**: Leadership team members for about page. 6 members. Ordered.
- **Achievement**: About page achievements/stats. Ordered.
- **HowItWorksStep**: Process steps for how-it-works page (6 steps). Ordered.
- **WhyUsFeature**: "Why Us" feature highlights for how-it-works page (6). Ordered.
- **ParentFeature**: Parent monitoring features for how-it-works page. Typed (core/capability). Ordered.
- **PricingPlan**: Pricing tiers (3). Name, price, features, popular badge. Ordered.
- **PlanFeature**: Feature items within a PricingPlan. FK to PricingPlan. Included/excluded flag. Ordered.
- **ComparisonFeature**: Pricing comparison table rows. Values per plan. Ordered.
- **PricingFAQ**: Pricing-specific FAQ items (5). Ordered.
- **BlogPost**: Blog articles. Title, slug, content, category, author, status, featured flag, SEO fields.
- **Category**: Blog categories (4). Name, slug. Ordered.
- **Author**: Blog post authors. Name, title, bio, photo.
- **ContactSubmission**: Contact form entries. Name, email, phone, subject, message, read status.
- **ContactPageSettings**: Contact page hero/settings. Singleton.
- **WhyChoosePoint**: Contact page benefit points (5). Ordered.
- **OperatingHours**: Business hours for contact page. Ordered.
- **ContactFAQ**: Contact-page-specific FAQ items (5). Ordered.
- **LegalPage**: Privacy policy and terms of service. Slug-identified. Rich text content.
- **PageMeta**: SEO metadata for pages without dedicated settings models.
- **RelatedLink**: Resource/related page links for FAQ help section.

---

## Success Criteria

### Measurable Outcomes

- **SC-001**: 100% of visible frontend sections are backed by admin-editable data -- no hardcoded content remains in templates for any section that has a corresponding model
- **SC-002**: Admin can update any text, image, or ordering on any page and see the change reflected on the public site within one page refresh
- **SC-003**: All public pages load with at most 5 database queries per page (using `select_related` and `prefetch_related` where applicable)
- **SC-004**: Contact form submissions are stored with 100% reliability and are viewable/filterable in Django admin
- **SC-005**: Blog posts support draft/published workflow -- draft posts are invisible to public visitors
- **SC-006**: All slug-based URLs resolve correctly (teacher profiles, blog posts, categories)
- **SC-007**: All pages render correctly with the existing frontend templates after backend integration (visual regression: zero layout or content breaks)

---

## Per-App Responsibility Summary

### `main` App
- SiteSettings (singleton) + SocialLink
- HeroSection (singleton)
- TrustStat (collection)
- EducationalService + ServiceFeature
- Partner (shared)
- FeatureBlock + FeaturePoint + FeatureTab + FeatureTabPoint
- Testimonial (shared, page-targeted)
- ProcessStep
- FAQ (shared, category-based)
- AppPromoSection (singleton)
- CTABlock (shared, slug-identified)
- RelatedLink
- PageMeta
- LegalPage

### `about` App
- PageContent (about + how-it-works page settings)
- ContentBlock (mission, vision, story)
- Statistic
- TeamMember
- Achievement
- HowItWorksStep
- WhyUsFeature
- ParentFeature

### `teacher` App
- Teacher
- TeacherFeature
- TeacherSpecialization
- TeacherReview
- TeacherAvailability
- TeacherPageSettings (singleton)
- TeacherStat

### `course` App
- Subject

### `blogs` App
- BlogPost
- Category
- Author
- BlogPageSettings (singleton)

### `contact` App
- ContactSubmission
- ContactPageSettings (singleton)
- WhyChoosePoint
- OperatingHours
- ContactFAQ

### `price` App
- PricingPlan + PlanFeature
- ComparisonFeature
- PricingFAQ
- PricingPageSettings (singleton)

---

## Admin/CMS Requirements

### Singleton Models Admin Pattern
All singleton models (HeroSection, SiteSettings, AppPromoSection, PageSettings models) should use a custom admin that:
- Redirects the changelist to the single instance's change form
- Disables "Add" button if instance exists
- Pre-creates the instance on first admin access

### Inline Admin Patterns
| Parent Model | Inline Model | Type |
| ------------ | ------------ | ---- |
| EducationalService | ServiceFeature | TabularInline |
| FeatureBlock | FeaturePoint | TabularInline |
| FeatureTab | FeatureTabPoint | TabularInline |
| PricingPlan | PlanFeature | TabularInline |
| Teacher | TeacherFeature | TabularInline |
| Teacher | TeacherSpecialization | TabularInline |
| Teacher | TeacherReview | StackedInline |
| Teacher | TeacherAvailability | TabularInline |

### Admin List Display Recommendations
| Model | list_display | list_filter | search_fields |
| ----- | ------------ | ----------- | ------------- |
| Teacher | name, primary_subject, rating, is_active, is_featured, order | is_active, is_featured, primary_subject | name |
| BlogPost | title, category, author, status, is_featured, published_date | status, category, is_featured | title, content |
| ContactSubmission | full_name, email, subject, is_read, created_at | is_read, subject, created_at | full_name, email, message |
| FAQ | question (truncated), category, is_active, show_on_homepage, order | category, is_active, show_on_homepage | question, answer |
| Testimonial | student_name, page, is_active, order | page, is_active | student_name, quote |
| PricingPlan | name, price, is_popular, is_active, order | is_active, is_popular | name |
| Partner | name, is_active, order | is_active | name |
| TeamMember | name, title, is_active, order | is_active | name, title |

### Admin Permissions
- All content models: full CRUD for staff users
- ContactSubmission: read-only (no edit/delete in admin), with `is_read` toggle

---

## Query and Retrieval Requirements

### Homepage View Query Plan
```
hero = HeroSection.objects.first()
stats = TrustStat.objects.filter(is_active=True).order_by('order')
services = EducationalService.objects.filter(is_active=True).prefetch_related('features').order_by('order')
partners = Partner.objects.filter(is_active=True).order_by('order')
tutoring_block = FeatureBlock.objects.prefetch_related('points').get(slug='private-tutoring')
aptitude_block = FeatureBlock.objects.prefetch_related('tabs__points').get(slug='aptitude-tests')
subjects = Subject.objects.filter(is_active=True).order_by('order')
teachers = Teacher.objects.filter(is_active=True, is_featured=True).select_related('primary_subject').order_by('order')[:8]
testimonials = Testimonial.objects.filter(is_active=True, page='homepage').order_by('order')[:4]
steps = ProcessStep.objects.filter(is_active=True).order_by('order')
faqs = FAQ.objects.filter(is_active=True, show_on_homepage=True).order_by('order')[:10]
app_promo = AppPromoSection.objects.first()
cta = CTABlock.objects.get(slug='homepage-cta')
site_settings = SiteSettings.objects.prefetch_related('social_links').first()
```

### Teachers Listing View Query Plan
```
page_settings = TeacherPageSettings.objects.first()
subjects = Subject.objects.filter(is_active=True).order_by('order')  # for filter tabs
teachers = Teacher.objects.filter(is_active=True).select_related('primary_subject').order_by('order')
# Optional subject filter: .filter(primary_subject__slug=request.GET.get('subject'))
stats = TeacherStat.objects.filter(is_active=True).order_by('order')
testimonials = Testimonial.objects.filter(is_active=True, page='teachers').order_by('order')[:4]
cta = CTABlock.objects.get(slug='teachers-cta')
```

### Teacher Profile View Query Plan
```
teacher = Teacher.objects.select_related('primary_subject').prefetch_related(
    'features', 'specializations__subject', 'reviews', 'availability'
).get(slug=slug, is_active=True)
similar_teachers = Teacher.objects.filter(
    is_active=True, primary_subject=teacher.primary_subject
).exclude(pk=teacher.pk).select_related('primary_subject').order_by('order')[:4]
cta = CTABlock.objects.get(slug='teacher-profile-cta')
```

### Blog Listing View Query Plan
```
page_settings = BlogPageSettings.objects.first()
featured_post = BlogPost.objects.filter(status='published', is_featured=True).select_related('category', 'author').first()
categories = Category.objects.filter(is_active=True).order_by('order')
posts = BlogPost.objects.filter(status='published').select_related('category', 'author').order_by('-published_date')
# Optional category filter: .filter(category__slug=request.GET.get('category'))
# Paginate posts
```

### Blog Post Detail View Query Plan
```
post = BlogPost.objects.select_related('category', 'author').get(slug=slug, status='published')
related_posts = BlogPost.objects.filter(
    status='published', category=post.category
).exclude(pk=post.pk).select_related('category', 'author').order_by('-published_date')[:3]
```

### N+1 Prevention Rules
- Always use `select_related` for FK fields rendered in templates (e.g., `teacher.primary_subject`, `post.category`, `post.author`)
- Always use `prefetch_related` for reverse FK sets rendered in templates (e.g., `service.features`, `plan.features`, `teacher.reviews`)
- Singleton queries (HeroSection, SiteSettings, PageSettings) are single queries with no N+1 risk
- SiteSettings with social_links should use `prefetch_related('social_links')` since it's used on every page via context processor

### Context Processor for Shared Data
Create a context processor for data needed on every page:
- `site_settings`: SiteSettings singleton with social_links prefetched
- This avoids repeating the SiteSettings query in every view

---

## Slug / SEO / Publication-State Requirements

### Slug Fields
| Model | Slug Field | Auto-generated From | URL Pattern |
| ----- | ---------- | ------------------- | ----------- |
| Teacher | `slug` | `name` | `/teachers/<slug>/` |
| BlogPost | `slug` | `title` | `/blog/<slug>/` |
| Category | `slug` | `name` | `/blog/?category=<slug>` |
| Subject | `slug` | `name` | `/teachers/?subject=<slug>` |
| PricingPlan | `slug` | `name` | N/A (display only) |
| LegalPage | `slug` | `title` | `/pages/<slug>/` |
| CTABlock | `slug` | Manual entry | N/A (internal lookup) |
| FeatureBlock | `slug` | Manual entry | N/A (internal lookup) |
| ContentBlock | `slug` | Manual entry | N/A (internal lookup) |

### SEO Meta Fields
Pages with dedicated meta fields:
- Homepage: via `PageMeta` with slug `home`
- About: via `about.PageContent` slug `about`
- How It Works: via `about.PageContent` slug `how-it-works`
- Teachers Listing: via `teacher.TeacherPageSettings`
- Teacher Profile: via `Teacher.meta_title` / `Teacher.meta_description` (add these fields)
- Pricing: via `price.PricingPageSettings`
- Blog Listing: via `blogs.BlogPageSettings`
- Blog Post: via `BlogPost.meta_title` / `BlogPost.meta_description`
- FAQ: via `PageMeta` with slug `faq`
- Contact: via `contact.ContactPageSettings`

### Publication States
| Model | State Field | States | Default |
| ----- | ----------- | ------ | ------- |
| BlogPost | `status` | draft, published | draft |
| All other models | `is_active` | True/False | True |

---

## Validation Requirements

- **Contact form**: `full_name` required, max 100 chars. `email` required, valid email format. `phone` optional, max 20 chars. `subject` required, must be one of defined choices. `message` required, min 10 chars.
- **Teacher slug**: Unique, auto-generated, editable in admin
- **BlogPost slug**: Unique, auto-generated from title, editable in admin
- **Rating fields**: 1-5 integer range validation
- **Order fields**: Non-negative integers
- **Image fields**: Validate file type (JPEG, PNG, SVG, WebP)
- **URL fields**: Valid URL format
- **Email fields**: Valid email format
- **Price fields**: Positive decimal, max 2 decimal places

---

## Ordering / Featured / Visibility Logic

### Ordering
All collection models with `order` field default to `order_by('order')`. Admin should display drag-to-reorder or numeric order input.

### Featured Flags
| Model | Field | Purpose |
| ----- | ----- | ------- |
| Teacher | `is_featured` | Show on homepage teacher showcase |
| BlogPost | `is_featured` | Show in blog listing featured section |
| PricingPlan | `is_popular` | Show "Most Requested" badge |
| FAQ | `show_on_homepage` | Include in homepage FAQ section |

### Visibility
All content models use `is_active` boolean. Views filter by `is_active=True`. BlogPost additionally uses `status='published'` filter.

---

## Shared Content/Settings Requirements

### SiteSettings Singleton
Used on every page via context processor. Contains:
- Site name, description, logo (normal + white variant)
- Phone, email, WhatsApp number, address
- Copyright text
- Accreditation text and badge image
- Google Maps URL
- Related SocialLink entries

### CTABlock Reusable Pattern
Used on 6+ pages. Each CTA section is a CTABlock identified by slug:
- `homepage-cta`, `about-cta`, `teachers-cta`, `teacher-profile-cta`, `how-it-works-cta`, `pricing-cta`, `blog-cta`, `blog-post-cta`

### Testimonial Page Targeting
Testimonials are centrally managed but appear on multiple pages. The `page` field (choices: homepage, teachers, pricing, how-it-works) controls placement. A testimonial can appear on one page at a time (use multiple entries if the same testimonial should appear on multiple pages).

### Partner Logos
Shared between homepage and about page. Single queryset, no page targeting needed.

---

## Future-Readiness Notes

1. **User authentication**: Models are designed to NOT depend on User FK. When auth is added, Teacher and Author models can optionally link to User.
2. **Multi-language**: CharField/TextField are used without translation framework. When i18n is needed, django-modeltranslation or similar can wrap existing fields.
3. **API endpoints**: Models are clean and serializer-friendly. DRF or similar can expose them without model changes.
4. **Search**: Subject/teacher filtering uses simple queryset filters. Full-text search can be added later via django-watson or similar.
5. **Media storage**: ImageField uses default storage. Can be swapped to S3/cloud storage via Django storage backends.
6. **Caching**: Singleton models and rarely-changing content (partners, services, steps) are excellent cache candidates. Template fragment caching can be added per-section.

---

## Phased Implementation Recommendation

### Phase 1: Foundation (Milestone 1)
1. Register all apps in `INSTALLED_APPS`
2. Create `main` app models: SiteSettings, SocialLink, PageMeta
3. Create `course` app model: Subject
4. Create context processor for SiteSettings
5. Create base URL routing for all apps
6. Run migrations
7. **Deliverable**: Admin can manage site settings, and base template pulls dynamic footer/header data

### Phase 2: Homepage Core (Milestone 2)
1. Create remaining `main` models: HeroSection, TrustStat, EducationalService, ServiceFeature, Partner, FeatureBlock, FeaturePoint, FeatureTab, FeatureTabPoint, ProcessStep, FAQ, AppPromoSection, CTABlock, Testimonial
2. Create homepage view with all queries
3. Update `index.html` template to use template variables
4. **Deliverable**: Fully dynamic homepage

### Phase 3: Teachers (Milestone 3)
1. Create `teacher` models: Teacher, TeacherFeature, TeacherSpecialization, TeacherReview, TeacherAvailability, TeacherPageSettings, TeacherStat
2. Create teacher listing view and teacher profile view
3. Update teacher templates
4. **Deliverable**: Fully dynamic teacher listing and profile pages

### Phase 4: Blog (Milestone 4)
1. Create `blogs` models: BlogPost, Category, Author, BlogPageSettings
2. Create blog listing view and blog post detail view
3. Update blog templates
4. **Deliverable**: Fully dynamic blog with publish/draft workflow

### Phase 5: Pricing (Milestone 5)
1. Create `price` models: PricingPlan, PlanFeature, ComparisonFeature, PricingFAQ, PricingPageSettings
2. Create pricing view
3. Update pricing template
4. **Deliverable**: Fully dynamic pricing page

### Phase 6: Contact & FAQ (Milestone 6)
1. Create `contact` models: ContactSubmission, ContactPageSettings, WhyChoosePoint, OperatingHours, ContactFAQ
2. Create contact view with form handling
3. Create FAQ page view
4. Update contact and FAQ templates
5. **Deliverable**: Working contact form + fully dynamic FAQ page

### Phase 7: About & How It Works (Milestone 7)
1. Create `about` models: PageContent, ContentBlock, Statistic, TeamMember, Achievement, HowItWorksStep, WhyUsFeature, ParentFeature
2. Create about and how-it-works views
3. Update about and how-it-works templates
4. **Deliverable**: Fully dynamic about and how-it-works pages

### Phase 8: Legal Pages & Polish (Milestone 8)
1. Create `main` model: LegalPage, RelatedLink
2. Create legal page views
3. Update privacy and terms templates
4. Create 404/500 error page content
5. Final admin polish, data seeding
6. **Deliverable**: Complete CMS with all pages dynamic

### Recommended Model Creation Order
1. SiteSettings + SocialLink (needed by every page)
2. Subject (needed by Teacher FK)
3. CTABlock (reused by many pages)
4. Partner (shared across pages)
5. Testimonial (shared across pages)
6. FAQ (shared across pages)
7. HeroSection, TrustStat, EducationalService, ServiceFeature, FeatureBlock, FeaturePoint, FeatureTab, FeatureTabPoint, ProcessStep, AppPromoSection (homepage)
8. Teacher, TeacherFeature, TeacherSpecialization, TeacherReview, TeacherAvailability, TeacherPageSettings, TeacherStat
9. BlogPost, Category, Author, BlogPageSettings
10. PricingPlan, PlanFeature, ComparisonFeature, PricingFAQ, PricingPageSettings
11. ContactSubmission, ContactPageSettings, WhyChoosePoint, OperatingHours, ContactFAQ
12. PageContent, ContentBlock, Statistic, TeamMember, Achievement, HowItWorksStep, WhyUsFeature, ParentFeature
13. LegalPage, RelatedLink, PageMeta

### Recommended Dynamic-Conversion Order by Page
1. Base template (footer/header via SiteSettings context processor)
2. Homepage
3. Teachers listing + Teacher profile
4. Blog listing + Blog post detail
5. Pricing
6. Contact + FAQ
7. About + How It Works
8. Privacy + Terms

---

## Acceptance Criteria for Backend Phase

1. **All 7 Django apps are registered** in `INSTALLED_APPS` and have working migrations
2. **Every model defined in this spec exists** with all specified fields, relationships, and constraints
3. **Every frontend section has a corresponding data source** -- no hardcoded content remains in templates for sections that have backend models
4. **Django admin is fully configured** with proper list_display, list_filter, search_fields, inlines, and singleton patterns for every model
5. **All views are implemented** with clean querysets using `select_related` and `prefetch_related` where applicable
6. **URL routing is complete** for all pages including slug-based URLs for teachers and blog posts
7. **Contact form submission works** end-to-end: form renders, validates, saves to database, shows success message, appears in admin
8. **Blog draft/published workflow works**: draft posts are not visible to public visitors
9. **Featured/ordering/active flags work correctly** across all models
10. **SEO meta fields render** in `<head>` for all public pages
11. **Context processor delivers SiteSettings** to every template
12. **Existing frontend design is preserved** -- zero visual regressions after backend integration
13. **All templates extend `base.html`** and use Django template tags to render dynamic content
14. **Initial data is seeded** matching the current frontend content (all current hardcoded content migrated to database records)
