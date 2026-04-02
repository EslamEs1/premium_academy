# Data Model: Academy Backend CMS

## Design Rules

- All user-visible collection models use `is_active` and, where ordering matters, `order`.
- All singleton/page settings models are enforced in admin and retrieved with `.first()` or slug lookup.
- Publicly routed content uses unique slugs with admin-editable overrides.
- Cross-domain references that must not disappear from rendered pages use `on_delete=PROTECT`.
- Inline-owned children use `CASCADE` to keep parent-owned records tidy.

## Shared Base Patterns

| Pattern | Fields / Behavior | Applied To |
| --- | --- | --- |
| `ActiveOrdered` | `is_active`, `order` | stats, partners, testimonials, steps, FAQs, plans, team, operating hours, related links, similar collections |
| `SeoFields` | `meta_title`, `meta_description` | page settings, teacher, blog post, legal page, page meta |
| `SluggedContent` | unique `slug`, optional auto-generation | teacher, blog post, subject, category, pricing plan, legal page, reusable content blocks |
| Singleton admin | one record only, changelist redirects to edit form | site settings, hero/app promo/page settings models |

## `main` App

| Model | Key Fields | Relationships | Validation / Notes |
| --- | --- | --- | --- |
| `SiteSettings` | `site_name`, `site_description`, `logo`, `logo_white`, `phone`, `email`, `whatsapp`, `address`, `google_maps_url`, `copyright_text`, `accreditation_text`, `accreditation_badge` | one-to-many with `SocialLink` | singleton; delivered to every page through a context processor |
| `SocialLink` | `platform`, `url`, `order`, `is_active` | FK to `SiteSettings` | ordered footer/header social items |
| `HeroSection` | `headline`, `subheading`, `description`, primary/secondary CTA text+URL, `hero_image` | none | homepage singleton |
| `TrustStat` | `number`, `label`, `description`, `icon`, `order`, `is_active` | none | homepage trust bar |
| `EducationalService` | `title`, `description`, `icon`, `image`, CTA fields, `order`, `is_active` | one-to-many with `ServiceFeature` | homepage services grid |
| `ServiceFeature` | `text`, `order` | FK to `EducationalService` | inline-owned list |
| `Partner` | `name`, `logo`, `url`, `order`, `is_active` | none | shared homepage/about logos |
| `FeatureBlock` | `slug`, `title`, `description`, `image`, `order`, `is_active` | one-to-many with `FeaturePoint`; one-to-many with `FeatureTab` | reusable sections like `private-tutoring`, `aptitude-tests` |
| `FeaturePoint` | `text`, `order` | FK to `FeatureBlock` | inline-owned bullet list |
| `FeatureTab` | `title`, `order` | FK to `FeatureBlock`; one-to-many with `FeatureTabPoint` | used for aptitude tabs |
| `FeatureTabPoint` | `text`, `order` | FK to `FeatureTab` | inline-owned tab bullets |
| `Testimonial` | `student_name`, `student_initials`, `level`, `subject`, `rating`, `quote`, `page`, `order`, `is_active`, `is_featured` | none | `rating` constrained to 1-5; page-targeted shared content |
| `ProcessStep` | `step_number`, `title`, `description`, `icon`, `order`, `is_active` | none | homepage process section |
| `FAQ` | `question`, `answer`, `category`, `order`, `is_active`, `show_on_homepage` | none | shared FAQ pool; category drives FAQ-page grouping |
| `AppPromoSection` | `title`, `subtitle`, `description`, `preview_image`, store URLs, `is_active` | none | homepage singleton |
| `CTABlock` | `slug`, `heading`, `subheading`, `body_text`, CTA fields, `social_proof_text`, `is_active` | none | shared CTA contract across multiple pages |
| `RelatedLink` | `title`, `description`, `url`, `order`, `is_active` | none | FAQ help/resources section |
| `PageMeta` | `slug`, `meta_title`, `meta_description`, `is_active` | none | pages without dedicated settings model like home/faq |
| `LegalPage` | `title`, `slug`, `content`, `meta_title`, `meta_description`, `updated_at` | none | rich-text-like long-form content for privacy/terms |

## `course` App

| Model | Key Fields | Relationships | Validation / Notes |
| --- | --- | --- | --- |
| `Subject` | `name`, `slug`, `description`, `icon`, `order`, `is_active` | referenced by `Teacher.primary_subject`; referenced by `TeacherSpecialization.subject` | slug unique; deletion protected where linked from teachers |

## `teacher` App

| Model | Key Fields | Relationships | Validation / Notes |
| --- | --- | --- | --- |
| `TeacherPageSettings` | `title`, `subtitle`, `hero_image`, `meta_title`, `meta_description` | none | singleton for teachers listing page |
| `TeacherStat` | `number`, `label`, `icon`, `order`, `is_active` | none | teachers page statistics strip |
| `Teacher` | `name`, `slug`, `primary_subject`, `title`, `short_bio`, `full_bio`, `experience_years`, `rating`, `student_count`, `sessions_count`, `success_rate`, `photo`, booking CTA fields, `is_active`, `is_featured`, `order`, `meta_title`, `meta_description` | FK to `course.Subject`; one-to-many with `TeacherFeature`, `TeacherSpecialization`, `TeacherReview`, `TeacherAvailability` | slug unique and editable; `rating` 1-5; `primary_subject` uses `PROTECT` |
| `TeacherFeature` | `text`, `order` | FK to `Teacher` | teacher profile checkmarks |
| `TeacherSpecialization` | optional `subject`, `label`, `grade_level`, `order` | FK to `Teacher`; FK to `course.Subject` | specialization rows and grade mappings |
| `TeacherReview` | `student_name`, `rating`, `quote`, `review_date`, `order`, `is_active` | FK to `Teacher` | `rating` 1-5; stacked inline in admin |
| `TeacherAvailability` | `day_of_week`, `start_time`, `end_time`, `order`, `is_active` | FK to `Teacher` | ordered availability rows |

## `about` App

| Model | Key Fields | Relationships | Validation / Notes |
| --- | --- | --- | --- |
| `PageContent` | `slug`, `title`, `subtitle`, `header_icon`, `meta_title`, `meta_description` | none | singleton-like records for `about` and `how-it-works` pages |
| `ContentBlock` | `slug`, `title`, `content`, `icon`, `order`, `is_active` | none | reusable long-form blocks for mission, vision, story |
| `Statistic` | `number`, `label`, `icon`, `order`, `is_active` | none | about-page stats |
| `TeamMember` | `name`, `title`, `description`, `photo`, `order`, `is_active` | none | leadership section |
| `Achievement` | `number`, `label`, `icon`, `order`, `is_active` | none | about-page achievements |
| `HowItWorksStep` | `step_number`, `title`, `description`, `icon`, `order`, `is_active` | none | how-it-works process flow |
| `WhyUsFeature` | `title`, `description`, `icon`, `order`, `is_active` | none | why-us feature cards |
| `ParentFeature` | `title`, `description`, `feature_type`, `icon`, `order`, `is_active` | none | parent monitoring capabilities; `feature_type` supports grouping |

## `price` App

| Model | Key Fields | Relationships | Validation / Notes |
| --- | --- | --- | --- |
| `PricingPageSettings` | `title`, `subtitle`, `description`, `meta_title`, `meta_description` | none | singleton |
| `PricingPlan` | `name`, `slug`, `price`, `billing_period`, `description`, CTA fields, `is_popular`, `is_active`, `order` | one-to-many with `PlanFeature` | positive decimal price; slug retained for internal linking/SEO |
| `PlanFeature` | `text`, `is_included`, `order` | FK to `PricingPlan` | inline-owned feature rows |
| `ComparisonFeature` | `label`, per-plan value fields, `order`, `is_active` | none | comparison-table rows keyed to plan names/order |
| `PricingFAQ` | `question`, `answer`, `order`, `is_active` | none | pricing-page FAQ only |

## `blogs` App

| Model | Key Fields | Relationships | Validation / Notes |
| --- | --- | --- | --- |
| `BlogPageSettings` | `title`, `subtitle`, `description`, `meta_title`, `meta_description` | none | singleton for listing page |
| `Category` | `name`, `slug`, `description`, `order`, `is_active` | one-to-many with `BlogPost` | slug unique; used in filter query string |
| `Author` | `name`, `title`, `bio`, `photo`, `is_active`, `order` | one-to-many with `BlogPost` | author bio block on post page |
| `BlogPost` | `title`, `slug`, `excerpt`, `content`, `featured_image`, `category`, `author`, `status`, `is_featured`, `published_date`, `reading_time`, `meta_title`, `meta_description` | FK to `Category`; FK to `Author` | `status` transitions from `draft` to `published`; slug unique; public queries only expose `published` |

## `contact` App

| Model | Key Fields | Relationships | Validation / Notes |
| --- | --- | --- | --- |
| `ContactPageSettings` | `title`, `subtitle`, `description`, CTA text, `meta_title`, `meta_description` | none | singleton |
| `ContactSubmission` | `full_name`, `email`, `phone`, `subject`, `message`, `is_read`, `created_at` | none | subject required; email validated; message min length 10; admin mostly read-only except read-status toggle |
| `WhyChoosePoint` | `title`, `description`, `icon`, `order`, `is_active` | none | contact-page trust bullets |
| `OperatingHours` | `day_label`, `time_range`, `order`, `is_active` | none | ordered operating-hours rows |
| `ContactFAQ` | `question`, `answer`, `order`, `is_active` | none | contact-page FAQ subset |

## Cross-App Read Models

| Page | Primary Records | Shared Records |
| --- | --- | --- |
| Homepage | `HeroSection`, `TrustStat`, `EducationalService`, `FeatureBlock`, `ProcessStep`, `AppPromoSection` | `Subject`, featured `Teacher`, homepage `Testimonial`, homepage `FAQ`, `Partner`, `CTABlock`, `SiteSettings`, `PageMeta` |
| About | `PageContent(slug='about')`, `ContentBlock`, `Statistic`, `TeamMember`, `Achievement` | `Partner`, `CTABlock`, `SiteSettings` |
| Teachers | `TeacherPageSettings`, `Teacher`, `TeacherStat` | `Subject`, teachers `Testimonial`, `CTABlock`, `SiteSettings` |
| Teacher Profile | `Teacher` plus owned child rows | similar `Teacher`, `CTABlock`, `SiteSettings` |
| How It Works | `PageContent(slug='how-it-works')`, `HowItWorksStep`, `WhyUsFeature`, `ParentFeature` | how-it-works `Testimonial`, `CTABlock`, `SiteSettings` |
| Pricing | `PricingPageSettings`, `PricingPlan`, `ComparisonFeature`, `PricingFAQ` | pricing `Testimonial`, `CTABlock`, `SiteSettings` |
| Blog Listing | `BlogPageSettings`, `BlogPost`, `Category` | `CTABlock`, `SiteSettings` |
| Blog Detail | `BlogPost`, related `BlogPost`, `Author` | `CTABlock`, `SiteSettings` |
| FAQ | `FAQ`, `RelatedLink`, `PageMeta(slug='faq')` | `SiteSettings` |
| Contact | `ContactPageSettings`, `WhyChoosePoint`, `OperatingHours`, `ContactFAQ`, `ContactSubmission` form | `SiteSettings`, shared CTA if kept in template |
| Legal | `LegalPage` | `SiteSettings` |

## Validation Rules

- All slug fields are unique and admin-editable after auto-generation.
- Rating fields are integers constrained to 1-5.
- Order fields are non-negative integers.
- Price fields are positive decimals with two decimal places at most.
- URL and email fields use Django validators.
- Image uploads accept site-approved image formats only.
- Contact submission form requires `full_name`, `email`, `subject`, and `message`; `message` must be at least 10 characters.

## State Transitions

| Model | States | Transition Rules |
| --- | --- | --- |
| `BlogPost` | `draft` -> `published` | only `published` posts appear publicly; demotion back to `draft` removes the post from public routes without deleting it |
| Most content models | `is_active=False/True` | inactive records stay in admin but are excluded from public querysets |
| `ContactSubmission` | unread -> read | created with `is_read=False`; staff may mark as read in admin |

## Deletion Rules

- Use `PROTECT` for `Teacher.primary_subject` and other cross-domain required references.
- Use `CASCADE` for inline-owned children such as service features, teacher reviews, teacher availability, plan features, and feature-tab points.
- Prefer soft visibility control through `is_active` over deleting records that map to locked frontend sections.
