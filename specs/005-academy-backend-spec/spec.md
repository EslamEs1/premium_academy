# Feature Specification: Academy Backend — Django Data Layer & CMS

**Feature Branch**: `005-academy-backend-spec`
**Created**: 2026-03-28
**Status**: Draft
**Input**: Backend specification for SanaAcademy Django platform — supporting existing Arabic RTL frontend with dynamic content, teacher profiles, courses, blogs, FAQ, contact submissions, and phased platform growth.

---

## 1. Feature Summary

Build the Django backend data layer and admin CMS that powers the existing SanaAcademy public website. The backend converts the current static HTML frontend into a dynamic, admin-managed website. It covers: homepage sections, teacher profiles, course/program listings, blog articles, FAQ, contact form submissions, pricing packages, testimonials, site settings, and SEO metadata — all manageable through Django admin without code changes.

The backend is designed in two layers:
- **Layer 1 (Current Phase)**: Public website data models, Django admin CMS, and template integration to make all frontend content dynamic and editable.
- **Layer 2 (Future Phase)**: Student/teacher accounts, bookings, sessions, payments, dashboards — foundations are laid now but not fully built.

---

## 2. Problem / Opportunity

The SanaAcademy frontend is fully designed and implemented as static HTML/CSS/JS with 12 templates across 6 Django apps. However:

- All content is hardcoded in templates — every text change requires developer intervention
- No database models exist — all `models.py` files are empty
- Apps are not registered in `INSTALLED_APPS`
- No URL routing exists beyond `/admin/`
- No admin interface is configured for content management
- Contact form submissions have no backend processing
- Teacher profiles, courses, blog posts cannot be added/edited without code changes
- SEO metadata is static and cannot be managed per-page

This specification defines the backend needed to make the website fully dynamic, admin-managed, and ready for phased platform expansion.

---

## 3. Goals

1. **Dynamic Content**: Make all public website content editable through Django admin
2. **Teacher Management**: Admin can create, edit, publish, and order teacher profiles
3. **Course/Program Management**: Admin can manage courses, programs, subjects, and pricing packages
4. **Blog System**: Admin can publish, categorize, and manage blog articles
5. **FAQ Management**: Admin can manage FAQ entries by category with ordering
6. **Contact Processing**: Store contact form submissions with status tracking and admin notifications
7. **Site Settings**: Centralized admin-managed site settings (phone, email, social links, statistics)
8. **SEO Control**: Per-page and per-entity SEO metadata management
9. **Publication Workflow**: Draft/published/archived states with featured flags and ordering
10. **Frontend Alignment**: Backend models map directly to current frontend page structure and content blocks
11. **Future Readiness**: Model structure supports future accounts, bookings, and platform features without polluting current phase

---

## 4. Non-Goals

- Student registration or authentication system (Layer 2)
- Teacher login or dashboard (Layer 2)
- Online booking or scheduling system (Layer 2)
- Payment processing or invoicing (Layer 2)
- Live session infrastructure (Layer 2)
- Notification system (Layer 2)
- REST API or mobile API endpoints (Layer 2)
- Multi-language support beyond Arabic (not needed now)
- Advanced analytics or reporting dashboards (Layer 2)
- Wallet or payout systems (Layer 2)
- Full role-based access control beyond Django admin groups (Layer 2)

---

## Clarifications

### Session 2026-03-28

- Q: Should we create a custom User model now or use Django's default `auth.User`? → A: Create minimal custom User model now (`accounts` app, extends `AbstractUser`, no extra fields yet) — zero-cost future-proofing for Layer 2 accounts.
- Q: What spam protection should the contact form have? → A: Honeypot field (hidden field that bots fill, humans don't) — simple, no external dependency.
- Q: Should teacher rating be manually set or auto-computed from reviews? → A: Admin-managed — rating is a manually set field, independent of reviews. Auto-computation deferred to Layer 2 when real student reviews exist.

---

## 5. Current Frontend Alignment

The backend must serve data to these existing frontend pages:

| Frontend Page | Template Location | Backend Data Source |
| --- | --- | --- |
| Homepage | `main/index.html` | HeroSection, Statistics, Service, Partner, FeaturedTeacher, Testimonial, HowItWorksStep, FAQ (top 10), SiteSettings |
| About | `about/about.html` | AboutPage (mission, vision, story), TeamMember, Partner, Statistics |
| Teachers Listing | `teacher/teachers.html` | Teacher (filtered by subject), Subject categories, Statistics |
| Teacher Profile | `teacher/teacher-profile.html` | Teacher (full profile), TeacherReview, Subject, Availability |
| How It Works | `main/how-it-works.html` | HowItWorksStep, Feature, Testimonial, ParentFeature |
| Pricing | `main/pricing.html` | PricingPackage, PackageFeature, PaymentMethod |
| Blog Listing | `blogs/blog.html` | BlogPost (listing), BlogCategory, featured post |
| Blog Detail | `blogs/blog-post.html` | BlogPost (detail), Author info, RelatedPosts |
| FAQ | `main/faq.html` | FAQ entries by FAQCategory |
| Contact | `contact/contact.html` | ContactInfo (from SiteSettings), ContactSubmission (form processing) |
| Privacy Policy | `main/privacy.html` | StaticPage (or remain static initially) |
| Terms | `main/terms.html` | StaticPage (or remain static initially) |

---

## 6. Proposed Backend Architecture Direction

- **Framework**: Django 6.0.3 (already installed)
- **Database**: SQLite3 for development, PostgreSQL for production
- **Admin**: Django admin with customized list views, filters, and fieldsets
- **Templates**: Django template engine rendering existing HTML with template tags replacing hardcoded content
- **Static Files**: Existing static structure maintained; media uploads via `MEDIA_ROOT` for admin-uploaded images
- **Image Handling**: Pillow for image processing and thumbnails
- **Rich Text**: Rich text editor for blog content and static page content fields
- **Slugs**: Auto-generated from Arabic titles with custom slug generation
- **No API layer in this phase** — server-side rendering only

---

## 7. Proposed Django App Responsibilities

### Existing Apps (Keep and Extend)

| App | Responsibility |
| --- | --- |
| `main` | Homepage sections, HowItWorks steps, pricing packages, FAQ, site settings, static pages, statistics, partner logos, testimonials |
| `teacher` | Teacher model, teacher reviews, availability, subject specializations |
| `courses` | Subject model, course/program tracks, grade levels |
| `blogs` | BlogPost, BlogCategory, Author profile (inline on User or standalone) |
| `about` | AboutPage singleton, team members |
| `contact` | ContactSubmission model, contact form processing |

### New App

| App | Justification |
| --- | --- |
| `accounts` | Minimal custom User model extending `AbstractUser` with no extra fields yet. Required because Django makes it extremely difficult to swap the User model after migrations are applied, and Layer 2 will need student/teacher/parent accounts. Must be created before first migration. |

Shared abstract models (TimeStampedModel, SEOModel, PublishableModel) will reside in `main/abstract_models.py` and be imported across apps.

---

## 8. Data Model Scope for Current Phase

### Abstract Base Models (`main/abstract_models.py`)

#### TimeStampedModel (Abstract)
- `created_at`: auto-set on creation
- `updated_at`: auto-set on every save

#### SEOModel (Abstract)
- `meta_title`: up to 120 characters, optional
- `meta_description`: up to 320 characters, optional
- `meta_keywords`: up to 255 characters, optional

#### PublishableModel (Abstract)
- `status`: one of draft, published, archived (default: draft)
- `is_featured`: boolean (default: false)
- `order`: positive integer for sorting (default: 0)
- `published_at`: optional datetime, auto-set when status changes to published

---

### `main` App Models

#### SiteSettings (Singleton)
- `site_name`: academy name in Arabic
- `site_name_en`: academy name in English (optional)
- `tagline`: site tagline
- `logo`: uploaded image
- `logo_white`: white variant of logo (optional)
- `phone`: contact phone number
- `email`: contact email
- `whatsapp`: WhatsApp number
- `address`: physical address (optional)
- `working_hours`: business hours display text
- `working_hours_friday`: Friday-specific hours (optional)
- Social media URLs: Instagram, Twitter/X, TikTok, LinkedIn, YouTube, Facebook (all optional)
- App store URLs: Google Play, App Store (all optional)
- `footer_text`: footer description (optional)
- `copyright_text`: copyright line (optional)

**Admin**: Single-object edit (no add/delete), organized in fieldsets (General, Contact, Social, App Links, Footer).

#### HeroSection
- Inherits: TimeStampedModel, PublishableModel
- `title`: headline text
- `subtitle`: supporting description
- `primary_cta_text`: primary button text
- `primary_cta_url`: primary button link
- `secondary_cta_text`: secondary button text (optional)
- `secondary_cta_url`: secondary button link (optional)
- `image`: hero image (optional)
- `social_proof_text`: e.g. "10k+ students" (optional)

#### Statistic
- Inherits: TimeStampedModel
- `label`: metric label — e.g. "Active Students"
- `value`: display value — e.g. "+10,000"
- `icon`: icon identifier (optional)
- `description`: supporting text (optional)
- `order`: sort position

#### Service
- Inherits: TimeStampedModel, PublishableModel
- `title`: service name
- `subtitle`: short description (optional)
- `description`: full description
- `image`: service image (optional)
- `icon`: icon identifier (optional)
- `features`: feature list (one per line, rendered as list items)

Maps to: Homepage services section (Private Tutoring, Aptitude Exams, Curriculum Studies)

#### Partner
- Inherits: TimeStampedModel
- `name`: partner organization name
- `logo`: partner logo image
- `url`: partner website (optional)
- `order`: sort position
- `is_active`: visibility flag (default: true)

#### Testimonial
- Inherits: TimeStampedModel, PublishableModel
- `student_name`: reviewer name
- `subject`: subject area (optional) — e.g. "Mathematics"
- `grade_level`: grade/level (optional) — e.g. "Grade 3 Secondary"
- `title`: testimonial headline
- `content`: testimonial text
- `rating`: 1-5 stars (default: 5)
- `image`: reviewer photo (optional)
- `testimonial_type`: student or parent (default: student)

#### HowItWorksStep
- Inherits: TimeStampedModel
- `step_number`: unique step order
- `title`: step title
- `description`: step description
- `icon`: icon identifier (optional)

#### Feature
- Inherits: TimeStampedModel
- `title`: feature name
- `description`: feature description (optional)
- `icon`: icon identifier (optional)
- `order`: sort position
- `page`: which page this feature belongs to — how_it_works, parent_features, or why_us

Maps to: "Why Us" features, parent monitoring features on How It Works page

#### PricingPackage
- Inherits: TimeStampedModel, PublishableModel, SEOModel
- `name`: package name — e.g. "Basic", "Premium", "Professional"
- `slug`: unique URL-safe identifier
- `subtitle`: short pitch (optional)
- `price`: price amount (decimal)
- `currency`: currency code (default: "SAR")
- `unit`: billing unit display — e.g. "per session"
- `session_duration_minutes`: session length (default: 60)
- `description`: full description (optional)
- `badge_text`: highlight label (optional) — e.g. "Most Requested"
- `cta_text`: button text (default: "Start Now")
- `cta_url`: button link (optional)

#### PackageFeature
- Inherits: TimeStampedModel
- `package`: belongs to a PricingPackage
- `feature_text`: feature description
- `is_included`: whether included in this package (default: true)
- `order`: sort position

#### FAQ
- Inherits: TimeStampedModel, PublishableModel
- `category`: belongs to an FAQCategory (optional, nullable)
- `question`: question text
- `answer`: answer text
- `show_on_homepage`: flag for homepage display (default: false)

#### FAQCategory
- Inherits: TimeStampedModel
- `name`: category name (unique) — e.g. "General", "Pricing", "Teachers", "Scheduling", "Platform"
- `slug`: unique URL-safe identifier
- `order`: sort position

#### StaticPage
- Inherits: TimeStampedModel, SEOModel
- `slug`: unique URL-safe identifier — e.g. "privacy", "terms"
- `title`: page title
- `content`: rich text body
- `is_active`: visibility flag (default: true)

---

### `teacher` App Models

#### Teacher
- Inherits: TimeStampedModel, PublishableModel, SEOModel
- `name`: teacher full name
- `title`: professional title — e.g. "specialized math instructor"
- `slug`: unique URL-safe identifier
- `initials`: 2-5 character display for avatar — e.g. "أ.ع"
- `bio`: biography text
- `image`: teacher photo (optional)
- `subjects`: many-to-many relationship with Subject (through TeacherSubject)
- `years_of_experience`: number of years
- `rating`: decimal 1.0-5.0 (default: 5.0) — manually set by admin, independent of review ratings (auto-computation deferred to Layer 2)
- `student_count`: number of students (default: 0)
- `total_sessions`: total sessions completed (default: 0)
- `education`: degrees and qualifications (optional)
- `teaching_approach`: methodology description (optional)
- `grade_levels`: grade range text (optional) — e.g. "Grades 7-12"
- `session_rate_min`: minimum session price (optional)
- `availability_notes`: general availability text (optional)

**Admin**: List display with name, subject filter, status, rating, student count. Search by name. Inline editing for subjects, availability, and reviews.

#### TeacherSubject (Through Table)
- `teacher`: belongs to a Teacher
- `subject`: belongs to a Subject
- `is_primary`: whether this is the teacher's primary subject (default: false)
- Unique together: (teacher, subject)

#### TeacherAvailability
- Inherits: TimeStampedModel
- `teacher`: belongs to a Teacher
- `day_of_week`: one of Saturday through Thursday
- `start_time`: session start time
- `end_time`: session end time
- Unique together: (teacher, day_of_week)

#### TeacherReview
- Inherits: TimeStampedModel, PublishableModel
- `teacher`: belongs to a Teacher
- `reviewer_name`: reviewer display name
- `rating`: 1-5 stars
- `content`: review text
- `review_date`: date of review (auto-set on creation)

---

### `courses` App Models

#### Subject
- Inherits: TimeStampedModel
- `name`: subject name (unique) — e.g. "Mathematics"
- `slug`: unique URL-safe identifier
- `icon`: icon identifier (optional)
- `description`: subject description (optional)
- `order`: sort position
- `is_active`: visibility flag (default: true)

#### GradeLevel
- Inherits: TimeStampedModel
- `name`: level name (unique) — e.g. "Elementary", "Middle", "Secondary"
- `slug`: unique URL-safe identifier
- `order`: sort position

#### SubjectLevel
- `subject`: belongs to a Subject
- `grade_level`: belongs to a GradeLevel
- `description`: level-specific description (optional) — e.g. "Intermediate, Secondary"
- Unique together: (subject, grade_level)

Maps to: Subject grid on homepage showing subjects with their available grade levels.

#### ProgramTrack
- Inherits: TimeStampedModel, PublishableModel, SEOModel
- `name`: track name — e.g. "Private Tutoring", "Measurement Exams", "Subject Materials"
- `slug`: unique URL-safe identifier
- `subtitle`: short pitch (optional)
- `description`: full description
- `image`: track image (optional)
- `features`: feature list (one per line)
- `cta_text`: button text (optional)
- `cta_url`: button link (optional)

Maps to: The three main program tracks on the homepage.

---

### `blogs` App Models

#### BlogCategory
- Inherits: TimeStampedModel
- `name`: category name (unique) — e.g. "Study Tips", "Education", "Platform News"
- `slug`: unique URL-safe identifier
- `icon`: icon identifier (optional)
- `order`: sort position

#### BlogPost
- Inherits: TimeStampedModel, PublishableModel, SEOModel
- `title`: article title
- `slug`: unique URL-safe identifier
- `category`: belongs to a BlogCategory (optional, nullable)
- `author_name`: author display name
- `author_title`: author professional title (optional) — e.g. "Educational Content Director"
- `author_bio`: author biography (optional)
- `excerpt`: short summary (up to 500 chars)
- `content`: full article body (rich text)
- `featured_image`: article image (optional)
- `read_time_minutes`: estimated reading time (default: 5)

**Admin**: List display with title, category, status, is_featured, published_at. Filters by category, status. Search by title, content, author.

---

### `about` App Models

#### AboutPage (Singleton)
- Inherits: TimeStampedModel, SEOModel
- `mission`: mission statement
- `vision`: vision statement
- `story`: academy story/history
- `founding_year`: year founded (default: 2021)

#### TeamMember
- Inherits: TimeStampedModel
- `name`: member full name
- `title`: role title — e.g. "Executive Director"
- `image`: member photo (optional)
- `bio`: short biography (optional)
- `order`: sort position
- `is_active`: visibility flag (default: true)

---

### `contact` App Models

#### ContactSubmission
- Inherits: TimeStampedModel
- `full_name`: submitter name
- `email`: submitter email
- `phone`: submitter phone (optional)
- `subject`: inquiry type — one of: general_inquiry, book_session, complaint, suggestion, other
- `message`: message body
- `status`: one of: new, in_progress, resolved, closed (default: new)
- `admin_notes`: internal notes (optional)
- `resolved_at`: resolution timestamp (optional)

**Admin**: List display with name, subject, status, created_at. Filters by status, subject. Form fields (name, email, phone, subject, message) are read-only. Editable: status, admin_notes.

---

## 9. Admin/CMS Requirements

### General Admin Configuration
- Custom admin site title: "SanaAcademy Admin"
- Register all models with customized admin classes
- List displays optimized for content management workflows
- Filters and search on all content models
- Inline editing where appropriate:
  - PackageFeature inline on PricingPackage
  - TeacherSubject inline on Teacher
  - TeacherAvailability inline on Teacher
  - TeacherReview inline on Teacher
  - SubjectLevel inline on Subject

### Singleton Pattern
- SiteSettings and AboutPage use singleton pattern (max one instance, no add/delete)
- Admin redirects list view to change view for singletons

### Image Upload
- Configure `MEDIA_URL` and `MEDIA_ROOT`
- Teacher photos, partner logos, testimonial images, blog featured images, hero images

### Rich Text Fields
- Blog post content
- Static page content (privacy, terms)

### Ordering
- All models with `order` field support admin reordering
- Default ordering: `order` ascending, then `created_at` descending

---

## 10. Public-Site Dynamic Content Requirements

### Homepage (`main/index.html`)
All these sections must become database-driven:

| Section | Data Source | Query |
| --- | --- | --- |
| Hero | HeroSection | First published hero |
| Social proof text | HeroSection.social_proof_text | — |
| Statistics bar | Statistic | All, ordered by `order` |
| Services (3 blocks) | Service | Published, ordered by `order` |
| Partners carousel | Partner | Active, ordered by `order` |
| Featured teachers | Teacher | Published + featured, limit 8, ordered by `order` |
| Program tracks | ProgramTrack | Published, ordered by `order` |
| Subject grid | Subject + SubjectLevel | Active subjects with their levels |
| Testimonials | Testimonial | Published, limit 4, ordered by `order` |
| How it starts | HowItWorksStep | All, ordered by `step_number` |
| FAQ accordion | FAQ | Published + show_on_homepage=True, limit 10 |
| App promotion | SiteSettings | App store URLs |
| Contact info | SiteSettings | Phone, email, WhatsApp |

### Template Context
- A context processor for `SiteSettings` makes it available on all pages
- Each view provides page-specific querysets

---

## 11. Teacher Module Backend Requirements

### Teacher Listing Page
- Filter teachers by Subject (matches frontend filter tabs: All, Mathematics, Physics, Chemistry, English, Arabic, Biology, Aptitude, Achievement)
- Display: name, title, initials, primary subject, years_of_experience, rating, student_count
- Published teachers only, ordered by `order` then `name`
- Statistics bar: total teachers, average rating, total sessions, satisfaction rate

### Teacher Profile Page
- URL pattern: `/teachers/<slug>/`
- Full profile: all Teacher fields
- Subjects and grade levels via TeacherSubject
- Availability schedule via TeacherAvailability
- Published reviews via TeacherReview (ordered by review_date desc)
- Minimum session rate
- CTA: booking/contact links

### Teacher Admin
- Inline: TeacherSubject, TeacherAvailability, TeacherReview
- Bulk actions: publish, unpublish, feature, unfeature

---

## 12. Courses/Programs Module Backend Requirements

### Subject Management
- 8 subjects matching frontend: Mathematics, Physics, Chemistry, English, Arabic, Biology, Aptitude, Achievement
- Each subject has associated grade levels via SubjectLevel
- Subjects displayed on homepage subject grid and teacher filter tabs

### Program Tracks
- 3 tracks matching frontend: Private Tutoring, Measurement Exams, Subject Materials
- Each with description, features list, image, and CTA
- Displayed on homepage as program cards

### Grade Levels
- Pre-defined: Elementary, Middle, Secondary, Tracks (for specialized)
- Linked to subjects via SubjectLevel

### Pricing
- 3 packages matching frontend: Basic (150 SAR), Premium (200 SAR), Professional (300 SAR)
- Each with inline features (included/excluded)
- Pricing page and potential homepage display

---

## 13. Blog Module Backend Requirements

### Blog Listing Page
- URL pattern: `/blog/`
- Filter by BlogCategory (matches frontend: All, Education, Study Tips, Aptitude & Achievement, Platform News)
- Featured post displayed prominently (first published + featured)
- Standard cards: title, category, author_name, published_at, icon
- Pagination or load-more pattern
- Published posts only, ordered by `published_at` descending

### Blog Detail Page
- URL pattern: `/blog/<slug>/`
- Full post: title, category, author info (name, title, bio), published_at, read_time_minutes, content (rich text)
- Related posts: 3 posts from same category, excluding current, published
- CTA section at bottom

### Blog Admin
- Prepopulate slug from title
- Filters: category, status, is_featured, published_at range
- Search: title, content, author_name

---

## 14. FAQ / Contact Backend Requirements

### FAQ Page
- URL pattern: `/faq/`
- Display all published FAQs grouped by FAQCategory
- Category tabs matching frontend: General, Pricing, Teachers, Scheduling, Platform
- Accordion expand/collapse (frontend JS already handles this)
- Ordered by category order, then FAQ order within category

### Contact Page
- URL pattern: `/contact/`
- Form fields: full_name (required), email (required), phone (optional), subject dropdown (required), message (required)
- Server-side validation
- Honeypot field for spam protection (hidden field that bots fill, humans don't — submissions with honeypot filled are silently discarded)
- On success: save ContactSubmission, display success message
- Contact info sidebar populated from SiteSettings
- CSRF protection

### Contact Submission Processing
- New submissions get status "new"
- Admin can update status: new → in_progress → resolved/closed
- Admin can add internal notes
- Future: email notification to admin on new submission (defer to Layer 2)

---

## 15. Shared SEO/Content Management Requirements

### SEO Fields (via SEOModel abstract)
Applied to: Teacher, PricingPackage, ProgramTrack, BlogPost, StaticPage, AboutPage

- `meta_title`: Used in `<title>` tag; falls back to model's title/name if blank
- `meta_description`: Used in `<meta name="description">`; falls back to first 160 chars of description/excerpt
- `meta_keywords`: Used in `<meta name="keywords">` (optional)

### Template Implementation
- Base template reads SEO fields from context
- Each view passes SEO data for the current page/entity
- Default fallbacks so pages always have reasonable meta tags

### Open Graph Tags
- `og:title`, `og:description`, `og:image` derived from SEO fields + featured images
- Applied to blog posts, teacher profiles, and program tracks

---

## 16. URL/Data Slug and Publication-State Requirements

### Slug Rules
- Auto-generated from Arabic titles
- Unique per model (enforced at database level)
- Editable in admin but auto-populated on creation
- Allow Arabic characters, Latin characters, and hyphens

### URL Patterns

| URL | View | Template |
| --- | --- | --- |
| `/` | main:index | main/index.html |
| `/about/` | about:about | about/about.html |
| `/teachers/` | teacher:list | teacher/teachers.html |
| `/teachers/<slug>/` | teacher:profile | teacher/teacher-profile.html |
| `/how-it-works/` | main:how_it_works | main/how-it-works.html |
| `/pricing/` | main:pricing | main/pricing.html |
| `/blog/` | blogs:list | blogs/blog.html |
| `/blog/<slug>/` | blogs:detail | blogs/blog-post.html |
| `/faq/` | main:faq | main/faq.html |
| `/contact/` | contact:contact | contact/contact.html |
| `/privacy/` | main:static_page | main/privacy.html |
| `/terms/` | main:static_page | main/terms.html |

### Publication States

| Status | Behavior |
| --- | --- |
| `draft` | Visible only in admin; not shown on frontend |
| `published` | Visible on frontend; requires `published_at` to be set |
| `archived` | Hidden from frontend listings; direct URL returns 404 |

### Featured Flag
- `is_featured=True` items appear in featured sections (homepage teachers, blog featured post)
- Combined with `status=published` for frontend display

### Ordering
- `order` field: lower numbers appear first
- Ties broken by `created_at` descending (newest first)

---

## 17. Validation Rules

### Contact Form
- `full_name`: required, max 200 chars, strip whitespace
- `email`: required, valid email format
- `phone`: optional, must match Saudi format if provided (+966XXXXXXXXX)
- `subject`: required, must be one of defined choices
- `message`: required, min 10 chars, max 5000 chars

### Teacher Model
- `name`: required, max 200 chars
- `slug`: unique, auto-generated
- `years_of_experience`: positive integer, max 50
- `rating`: decimal 1.0-5.0
- `student_count`: non-negative integer
- At least one subject required

### Blog Post
- `title`: required, max 400 chars
- `slug`: unique, auto-generated from title
- `excerpt`: required, max 500 chars
- `content`: required, min 100 chars
- `published_at`: auto-set when status changes to published (if not already set)

### Pricing Package
- `price`: positive decimal, max 99999.99
- `session_duration_minutes`: positive integer, min 15, max 180
- At least one PackageFeature

### FAQ
- `question`: required, min 10 chars
- `answer`: required, min 20 chars

### General
- All slug fields: unique, max 200 chars, allow Arabic characters and hyphens
- All image fields: max 5MB, accepted formats: JPEG, PNG, SVG, WebP
- All URL fields: valid URL format, max 500 chars

---

## 18. Role and Permission Assumptions

### Current Phase (Layer 1)
- **Superadmin**: Full Django admin access; manages all content, settings, submissions
- **Content Editor** (Django admin group): Can manage blog posts, FAQ, testimonials, static pages; cannot modify site settings or teacher profiles
- **Teacher Manager** (Django admin group): Can manage teacher profiles, reviews, subjects; cannot modify site settings or blog

### Future Phase (Layer 2 — Not Built Now)
- Student accounts with profile and dashboard
- Teacher accounts with self-service profile editing
- Parent/Guardian accounts linked to students
- Supervisor role for teacher quality management

### Preparation for Layer 2
- Use a minimal custom User model (`accounts.User` extending `AbstractUser`, no extra fields) — set `AUTH_USER_MODEL = 'accounts.User'` before first migration
- Teacher model has no foreign key to User yet — add when teacher accounts are built in Layer 2
- The custom User model exists solely to prevent painful migration issues later; no custom fields are added in Layer 1

---

## 19. Phased Backend Rollout Recommendation

### Phase 1A — Foundation (Week 1-2)
**Goal**: Project setup, abstract models, site settings, and basic admin

1. Create `accounts` app with minimal custom User model (`AbstractUser`, no extra fields); set `AUTH_USER_MODEL = 'accounts.User'` in settings
2. Register all apps (including `accounts`) in `INSTALLED_APPS`
3. Create abstract base models (TimeStampedModel, SEOModel, PublishableModel)
4. Implement SiteSettings singleton model + admin
5. Configure MEDIA_URL/MEDIA_ROOT
6. Set up URL routing for all apps
7. Create Statistic model + admin
8. Run initial migrations (custom User model must be in place before this step)
9. Create context processor for SiteSettings

**Milestone**: Admin can edit site settings; base infrastructure is in place.

### Phase 1B — Core Content Models (Week 2-3)
**Goal**: Teacher, Subject, Course models and admin

1. Implement Subject, GradeLevel, SubjectLevel models + admin
2. Implement Teacher, TeacherSubject, TeacherAvailability, TeacherReview models + admin
3. Implement ProgramTrack model + admin
4. Create teacher list and profile views
5. Wire teacher templates to database
6. Seed initial data (8 subjects, 4 grade levels, 8 teachers from frontend)

**Milestone**: Teacher listing and profile pages are fully dynamic.

### Phase 1C — Homepage & Content (Week 3-4)
**Goal**: All homepage sections dynamic

1. Implement HeroSection, Service, Partner, Testimonial, HowItWorksStep, Feature models + admin
2. Implement PricingPackage, PackageFeature models + admin
3. Implement FAQ, FAQCategory models + admin
4. Create homepage view pulling all section data
5. Wire homepage template sections to database
6. Create How It Works, Pricing, FAQ views
7. Seed homepage content from current static data

**Milestone**: Homepage and all main pages are fully dynamic.

### Phase 1D — Blog & Contact (Week 4-5)
**Goal**: Blog system and contact form processing

1. Implement BlogCategory, BlogPost models + admin
2. Implement blog list and detail views with category filtering
3. Implement ContactSubmission model + admin
4. Create contact form with validation and processing
5. Create about page view with AboutPage and TeamMember models
6. Implement StaticPage model for privacy/terms
7. Seed blog categories and sample posts

**Milestone**: All public pages are dynamic. Content is fully admin-managed.

### Phase 1E — Polish & SEO (Week 5-6)
**Goal**: SEO, admin polish, and production readiness

1. Implement SEO meta tags across all templates
2. Add Open Graph tags for social sharing
3. Admin polish: custom list displays, filters, search, fieldsets
4. Admin ordering support
5. Image optimization and thumbnail generation
6. Sitemap generation
7. 404/500 error page template integration
8. Production settings (PostgreSQL, ALLOWED_HOSTS, SECRET_KEY from env)

**Milestone**: Production-ready public website with full CMS capabilities.

---

## User Scenarios & Testing

### User Story 1 — Admin Manages Website Content (Priority: P1)

An academy admin logs into Django admin and updates homepage content: edits the hero section text, reorders featured teachers, adds a new testimonial, and updates site contact information. All changes appear immediately on the public website without any code deployment.

**Why this priority**: This is the core value proposition — making content editable without developer intervention. Every other feature depends on this working.

**Independent Test**: Admin can log in, edit SiteSettings (phone number), save, and see the updated phone on the public homepage footer.

**Acceptance Scenarios**:

1. **Given** an admin is logged into Django admin, **When** they edit the hero section title and save, **Then** the homepage displays the updated title
2. **Given** an admin creates a new Testimonial with status=published, **When** they visit the homepage, **Then** the new testimonial appears in the testimonials section
3. **Given** an admin changes a teacher's status to "archived", **When** a visitor browses the teachers page, **Then** that teacher no longer appears in the listing

---

### User Story 2 — Visitor Browses Teachers and Views Profile (Priority: P1)

A prospective student or parent visits the teachers page, filters by subject (e.g. Mathematics), views teacher cards with ratings and experience, clicks on a teacher, and sees the full profile including bio, qualifications, availability, and reviews.

**Why this priority**: Teacher discovery is a primary conversion path. The frontend already has this flow designed — the backend must power it.

**Independent Test**: Visit `/teachers/`, filter by "Mathematics", click a teacher card, see full profile at `/teachers/<slug>/`.

**Acceptance Scenarios**:

1. **Given** a visitor is on the teachers page, **When** they click the "Mathematics" filter tab, **Then** only teachers with Mathematics as a subject are displayed
2. **Given** a visitor clicks "View Profile" on a teacher card, **When** the profile page loads, **Then** it shows the teacher's bio, education, availability, subjects, rating, and reviews
3. **Given** a teacher has status "draft", **When** a visitor accesses the teachers listing, **Then** that teacher is not visible

---

### User Story 3 — Visitor Reads Blog Articles (Priority: P2)

A visitor navigates to the blog, sees the featured article prominently displayed, browses articles by category, clicks an article to read the full content, and sees related posts at the bottom.

**Why this priority**: Blog content builds SEO authority and trust. It's a key content marketing channel but not as critical as core teacher/course content.

**Independent Test**: Visit `/blog/`, see articles listed by category, click one to read full content with author info and related posts.

**Acceptance Scenarios**:

1. **Given** a visitor is on the blog page, **When** they click the "Study Tips" category filter, **Then** only articles in that category are shown
2. **Given** a blog post is published with is_featured=True, **When** a visitor loads the blog page, **Then** that post appears in the featured position
3. **Given** a visitor reads a blog post, **When** they scroll to the bottom, **Then** they see 3 related posts from the same category

---

### User Story 4 — Visitor Submits Contact Form (Priority: P2)

A visitor goes to the contact page, fills out the form (name, email, subject, message), submits it, and sees a success confirmation. The submission is stored in the database and visible in Django admin.

**Why this priority**: Contact form is a primary lead generation tool. Without backend processing, inquiries are lost.

**Independent Test**: Submit a contact form, see success message, then verify the submission appears in Django admin.

**Acceptance Scenarios**:

1. **Given** a visitor fills out all required contact fields correctly, **When** they click "Send Message", **Then** they see a success confirmation and the submission is stored
2. **Given** a visitor submits an invalid email, **When** they click "Send Message", **Then** they see a validation error and the form is not submitted
3. **Given** an admin views ContactSubmission in admin, **When** they open a submission, **Then** they can see all form data and update the status to "in_progress"

---

### User Story 5 — Admin Manages Blog Posts (Priority: P2)

An admin creates a new blog post with title, category, content, excerpt, and author info. They save it as draft, then publish it. The post appears on the blog listing with correct category and date.

**Why this priority**: Ongoing content publishing is essential for marketing and SEO.

**Independent Test**: Create a blog post in admin with status=draft (not visible on frontend), change to published (appears on blog page).

**Acceptance Scenarios**:

1. **Given** an admin creates a blog post with status "draft", **When** a visitor browses the blog, **Then** the draft post is not visible
2. **Given** an admin changes a blog post status to "published", **When** the post's `published_at` is auto-set, **Then** the post appears on the blog listing ordered by publication date
3. **Given** an admin marks a blog post as featured, **When** a visitor loads the blog page, **Then** that post appears in the featured position

---

### User Story 6 — Visitor Views Pricing Packages (Priority: P3)

A visitor navigates to the pricing page and sees three packages (Basic, Premium, Professional) with prices in SAR, feature comparison, included/excluded features, and CTAs for each tier.

**Why this priority**: Pricing transparency supports conversion but the packages are relatively static.

**Independent Test**: Visit `/pricing/`, see 3 packages with prices and feature lists matching admin-configured data.

**Acceptance Scenarios**:

1. **Given** an admin has configured 3 pricing packages, **When** a visitor views the pricing page, **Then** they see all packages with correct prices, features, and CTAs
2. **Given** a package feature has `is_included=False`, **When** it is displayed, **Then** it appears with a visual indicator showing it is not included

---

### User Story 7 — Visitor Browses FAQ (Priority: P3)

A visitor navigates to the FAQ page, sees questions organized by category tabs, clicks a category, and expands accordion items to read answers.

**Why this priority**: FAQ reduces support load but is lower priority than core content pages.

**Independent Test**: Visit `/faq/`, see questions grouped by category, expand an accordion to read the answer.

**Acceptance Scenarios**:

1. **Given** FAQs exist in multiple categories, **When** a visitor clicks a category tab, **Then** only FAQs in that category are displayed
2. **Given** an FAQ has `show_on_homepage=True`, **When** a visitor views the homepage, **Then** that FAQ appears in the homepage FAQ section

---

### Edge Cases

- What happens when SiteSettings has no instance? → Create default instance on first admin access or via data migration
- What happens when no published teachers exist for a subject filter? → Display "No teachers found" message
- What happens when a visitor accesses a teacher profile slug that doesn't exist? → Return 404 page
- What happens when a blog post has no category? → Display without category label; still appears in "All" filter
- What happens when a contact form is submitted with JavaScript disabled? → Server-side form processing still works
- What happens when an admin deletes a FAQ category? → FAQs with that category get `category=NULL`; still display under "All"
- What happens when two blog posts both have is_featured=True? → First one by `order` then `published_at` takes the featured position
- What happens when an archived teacher's direct URL is accessed? → Return 404 page

---

## Requirements

### Functional Requirements

- **FR-001**: System MUST allow admins to create, edit, and delete all content types through Django admin
- **FR-002**: System MUST support draft/published/archived publication states on Teachers, Blog Posts, Services, Testimonials, Program Tracks, Pricing Packages, and FAQs
- **FR-003**: System MUST display only published content on public-facing pages
- **FR-004**: System MUST provide a singleton SiteSettings model accessible across all templates via context processor
- **FR-005**: System MUST store contact form submissions with validation and display success/error feedback
- **FR-006**: System MUST support filtering teachers by subject on the teachers listing page
- **FR-007**: System MUST support filtering blog posts by category on the blog listing page
- **FR-008**: System MUST support filtering FAQs by category on the FAQ page
- **FR-009**: System MUST auto-generate URL slugs from titles for teachers, blog posts, subjects, FAQ categories, pricing packages, and program tracks
- **FR-010**: System MUST enforce slug uniqueness per model at the database level
- **FR-011**: System MUST support ordering of content items via an `order` field manageable in admin
- **FR-012**: System MUST support `is_featured` flag to highlight specific items in homepage and listing sections
- **FR-013**: System MUST provide SEO meta fields (title, description, keywords) on key content types
- **FR-014**: System MUST render SEO meta tags in HTML head with fallback to default values
- **FR-015**: System MUST support image uploads for teachers, partners, testimonials, blog posts, and hero sections
- **FR-016**: System MUST serve uploaded media files via configured MEDIA_URL
- **FR-017**: System MUST display related blog posts (same category) on blog detail pages
- **FR-018**: System MUST display teacher reviews on teacher profile pages
- **FR-019**: System MUST support rich text editing for blog post content and static pages
- **FR-020**: System MUST support admin permission groups (Content Editor, Teacher Manager)
- **FR-021**: System MUST display FAQ entries marked with `show_on_homepage=True` on the homepage
- **FR-022**: System MUST auto-set `published_at` when a content item's status changes to "published" (if not already set)
- **FR-023**: System MUST validate contact form phone numbers against Saudi format when provided
- **FR-024**: System MUST include a honeypot field on the contact form to prevent automated spam submissions; submissions with the honeypot filled are silently discarded
- **FR-025**: System MUST support inline editing of PackageFeatures within PricingPackage admin, TeacherSubjects within Teacher admin, and TeacherAvailability within Teacher admin

### Key Entities

- **SiteSettings**: Global configuration — contact info, social links, branding, app store URLs
- **HeroSection**: Homepage hero banner — title, subtitle, CTAs, image, social proof
- **Statistic**: Quantified platform metrics — label, value, icon
- **Service**: Academy service offerings — title, description, features, image
- **Partner**: Institutional partners — name, logo, URL
- **Testimonial**: Student/parent testimonials — name, content, rating, type
- **HowItWorksStep**: Process steps — number, title, description
- **Feature**: Platform features — title, description, icon, page assignment
- **PricingPackage**: Pricing tiers — name, price, duration, badge, CTA
- **PackageFeature**: Features per package — text, included/excluded
- **FAQ**: Questions and answers — question, answer, category, homepage flag
- **FAQCategory**: FAQ groupings — name, slug, order
- **StaticPage**: CMS-managed pages — slug, title, rich text content
- **Teacher**: Instructor profiles — name, bio, credentials, rating, statistics, availability
- **TeacherSubject**: Teacher-to-subject mapping — primary flag
- **TeacherAvailability**: Weekly schedule — day, start/end times
- **TeacherReview**: Student reviews — reviewer, rating, content
- **Subject**: Academic subjects — name, icon, description
- **GradeLevel**: Education levels — name, order
- **SubjectLevel**: Subject-to-level mapping — description
- **ProgramTrack**: Program offerings — name, description, features, CTA
- **BlogCategory**: Article categories — name, icon
- **BlogPost**: Blog articles — title, content, author, category, excerpt, SEO
- **AboutPage**: About page content — mission, vision, story
- **TeamMember**: Leadership team — name, title, image
- **ContactSubmission**: Form submissions — name, email, subject, message, status

---

## Success Criteria

### Measurable Outcomes

- **SC-001**: All 12 public-facing pages load with dynamic content from the database within 2 seconds
- **SC-002**: Admin can update any visible text on the homepage and see the change reflected on the public site within one page refresh
- **SC-003**: Admin can publish a new teacher profile and it appears on the teachers listing page without any code changes
- **SC-004**: Admin can publish a new blog post and it appears on the blog page with correct category, date, and author
- **SC-005**: A visitor submitting the contact form receives immediate feedback (success or validation error) and the submission is stored and accessible in admin
- **SC-006**: 100% of content displayed on public pages is managed through Django admin — zero hardcoded content remains in templates
- **SC-007**: Teacher filtering by subject returns correct results and the page loads within 1 second
- **SC-008**: Every public page has correct SEO meta tags in the HTML head (title, description, Open Graph)
- **SC-009**: Admin can manage all content types without technical knowledge — no code editing, shell access, or database queries needed
- **SC-010**: The system supports at least 500 teachers, 1000 blog posts, and 200 FAQs without performance degradation

---

## 20. Acceptance Criteria for This Backend Phase

1. All 7 Django apps (including `accounts`) are registered and have working models with migrations applied
2. Django admin is configured with customized list views, filters, search, and inline editing for all models
3. SiteSettings singleton is functional and available across all templates via context processor
4. All 12 frontend pages render with data from the database (no hardcoded content in templates)
5. Teacher listing supports subject filtering; teacher profile displays full details with reviews
6. Blog listing supports category filtering; blog detail displays full article with related posts
7. FAQ page displays questions by category; homepage shows flagged FAQ entries
8. Contact form validates, saves submissions, and shows feedback
9. Pricing page displays admin-managed packages with feature comparison
10. SEO meta tags render on all pages with fallbacks
11. Publication workflow (draft/published/archived) works correctly — only published content appears publicly
12. All image uploads work and media files are served correctly
13. Admin permission groups (Content Editor, Teacher Manager) restrict access appropriately
14. Initial data is seeded from current frontend content (teachers, subjects, FAQ, etc.)
15. URL routing matches the defined pattern table; slugs work for teacher profiles and blog posts
