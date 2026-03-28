# Data Model: Academy Backend — Django Data Layer & CMS

**Branch**: `005-academy-backend-spec` | **Date**: 2026-03-28

---

## Abstract Base Models (`main/abstract_models.py`)

### TimeStampedModel
| Field | Type | Constraints |
| --- | --- | --- |
| created_at | DateTimeField | auto_now_add=True |
| updated_at | DateTimeField | auto_now=True |

### SEOModel
| Field | Type | Constraints |
| --- | --- | --- |
| meta_title | CharField | max_length=120, blank=True |
| meta_description | TextField | max_length=320, blank=True |
| meta_keywords | CharField | max_length=255, blank=True |

### PublishableModel
| Field | Type | Constraints |
| --- | --- | --- |
| status | CharField | max_length=20, choices=[draft, published, archived], default=draft |
| is_featured | BooleanField | default=False |
| order | PositiveIntegerField | default=0, db_index=True |
| published_at | DateTimeField | blank=True, null=True |

**State Transitions**:
- draft → published (auto-sets `published_at` if null)
- published → archived
- published → draft
- archived → draft
- archived → published

**Manager**: Custom `PublishedManager` filtering `status='published'` for frontend queries.

---

## `accounts` App

### User
| Field | Type | Constraints | Notes |
| --- | --- | --- | --- |
| (all AbstractUser fields) | — | — | username, email, first_name, last_name, password, is_staff, is_active, date_joined |

Extends `AbstractUser` with no extra fields. `AUTH_USER_MODEL = 'accounts.User'`.

---

## `main` App

### SiteSettings (Singleton via django-solo)
| Field | Type | Constraints | Notes |
| --- | --- | --- | --- |
| site_name | CharField | max_length=200 | Arabic name |
| site_name_en | CharField | max_length=200, blank=True | English name |
| tagline | CharField | max_length=300 | |
| logo | ImageField | upload_to='site/' | |
| logo_white | ImageField | upload_to='site/', blank=True | White variant |
| phone | CharField | max_length=20 | |
| email | EmailField | | |
| whatsapp | CharField | max_length=20 | |
| address | TextField | blank=True | |
| working_hours | CharField | max_length=200 | |
| working_hours_friday | CharField | max_length=200, blank=True | |
| instagram_url | URLField | max_length=500, blank=True | |
| twitter_url | URLField | max_length=500, blank=True | |
| tiktok_url | URLField | max_length=500, blank=True | |
| linkedin_url | URLField | max_length=500, blank=True | |
| youtube_url | URLField | max_length=500, blank=True | |
| facebook_url | URLField | max_length=500, blank=True | |
| google_play_url | URLField | max_length=500, blank=True | |
| app_store_url | URLField | max_length=500, blank=True | |
| footer_text | TextField | blank=True | |
| copyright_text | CharField | max_length=300, blank=True | |

**Relationships**: None (singleton)
**Admin**: SingletonModelAdmin (django-solo)

### HeroSection
| Field | Type | Constraints | Notes |
| --- | --- | --- | --- |
| title | CharField | max_length=300 | |
| subtitle | TextField | | |
| primary_cta_text | CharField | max_length=100 | |
| primary_cta_url | CharField | max_length=200 | |
| secondary_cta_text | CharField | max_length=100, blank=True | |
| secondary_cta_url | CharField | max_length=200, blank=True | |
| image | ImageField | upload_to='hero/', blank=True | |
| social_proof_text | CharField | max_length=200, blank=True | e.g. "10k+ students" |

**Inherits**: TimeStampedModel, PublishableModel
**Query**: First published, ordered by `order`

### Statistic
| Field | Type | Constraints | Notes |
| --- | --- | --- | --- |
| label | CharField | max_length=100 | e.g. "Active Students" |
| value | CharField | max_length=50 | e.g. "+10,000" |
| icon | CharField | max_length=50, blank=True | Icon class/SVG name |
| description | CharField | max_length=200, blank=True | |
| order | PositiveIntegerField | default=0 | |

**Inherits**: TimeStampedModel
**Query**: All, ordered by `order`

### Service
| Field | Type | Constraints | Notes |
| --- | --- | --- | --- |
| title | CharField | max_length=200 | |
| subtitle | CharField | max_length=300, blank=True | |
| description | TextField | | |
| image | ImageField | upload_to='services/', blank=True | |
| icon | CharField | max_length=50, blank=True | |
| features | TextField | | One feature per line |

**Inherits**: TimeStampedModel, PublishableModel
**Query**: Published, ordered by `order`

### Partner
| Field | Type | Constraints | Notes |
| --- | --- | --- | --- |
| name | CharField | max_length=200 | |
| logo | ImageField | upload_to='partners/' | |
| url | URLField | max_length=500, blank=True | |
| order | PositiveIntegerField | default=0 | |
| is_active | BooleanField | default=True | |

**Inherits**: TimeStampedModel
**Query**: Active, ordered by `order`

### Testimonial
| Field | Type | Constraints | Notes |
| --- | --- | --- | --- |
| student_name | CharField | max_length=200 | |
| subject | CharField | max_length=100, blank=True | e.g. "Mathematics" |
| grade_level | CharField | max_length=100, blank=True | e.g. "Grade 3" |
| title | CharField | max_length=300 | Headline |
| content | TextField | | |
| rating | PositiveSmallIntegerField | default=5, validators=[1-5] | |
| image | ImageField | upload_to='testimonials/', blank=True | |
| testimonial_type | CharField | max_length=20, choices=[student, parent], default=student | |

**Inherits**: TimeStampedModel, PublishableModel
**Query**: Published, ordered by `order`, limit 4 on homepage

### HowItWorksStep
| Field | Type | Constraints | Notes |
| --- | --- | --- | --- |
| step_number | PositiveSmallIntegerField | unique=True | |
| title | CharField | max_length=200 | |
| description | TextField | | |
| icon | CharField | max_length=50, blank=True | |

**Inherits**: TimeStampedModel
**Query**: All, ordered by `step_number`

### Feature
| Field | Type | Constraints | Notes |
| --- | --- | --- | --- |
| title | CharField | max_length=200 | |
| description | TextField | blank=True | |
| icon | CharField | max_length=50, blank=True | |
| order | PositiveIntegerField | default=0 | |
| page | CharField | max_length=30, choices=[how_it_works, parent_features, why_us] | |

**Inherits**: TimeStampedModel
**Query**: Filtered by `page`, ordered by `order`

### PricingPackage
| Field | Type | Constraints | Notes |
| --- | --- | --- | --- |
| name | CharField | max_length=200 | |
| slug | SlugField | max_length=200, unique=True, allow_unicode=True | |
| subtitle | CharField | max_length=300, blank=True | |
| price | DecimalField | max_digits=8, decimal_places=2 | |
| currency | CharField | max_length=10, default='SAR' | |
| unit | CharField | max_length=50, default='per session' | |
| session_duration_minutes | PositiveSmallIntegerField | default=60 | |
| description | TextField | blank=True | |
| badge_text | CharField | max_length=50, blank=True | e.g. "Most Requested" |
| cta_text | CharField | max_length=100, default='Start Now' | |
| cta_url | CharField | max_length=200, blank=True | |

**Inherits**: TimeStampedModel, PublishableModel, SEOModel
**Relationships**: → PackageFeature (1:N)
**Query**: Published, ordered by `order`

### PackageFeature
| Field | Type | Constraints | Notes |
| --- | --- | --- | --- |
| package | ForeignKey | → PricingPackage, on_delete=CASCADE | |
| feature_text | CharField | max_length=300 | |
| is_included | BooleanField | default=True | |
| order | PositiveIntegerField | default=0 | |

**Inherits**: TimeStampedModel
**Admin**: Inline on PricingPackage (SortableTabularInline)

### FAQ
| Field | Type | Constraints | Notes |
| --- | --- | --- | --- |
| category | ForeignKey | → FAQCategory, on_delete=SET_NULL, null=True, blank=True | |
| question | TextField | min_length=10 | |
| answer | TextField | min_length=20 | |
| show_on_homepage | BooleanField | default=False | |

**Inherits**: TimeStampedModel, PublishableModel
**Query (homepage)**: Published + show_on_homepage=True, ordered by `order`, limit 10
**Query (FAQ page)**: Published, grouped by category, ordered by category.order then FAQ.order

### FAQCategory
| Field | Type | Constraints | Notes |
| --- | --- | --- | --- |
| name | CharField | max_length=100, unique=True | |
| slug | SlugField | max_length=200, unique=True, allow_unicode=True | |
| order | PositiveIntegerField | default=0 | |

**Inherits**: TimeStampedModel
**Query**: All, ordered by `order`

### StaticPage
| Field | Type | Constraints | Notes |
| --- | --- | --- | --- |
| slug | SlugField | max_length=200, unique=True, allow_unicode=True | e.g. "privacy", "terms" |
| title | CharField | max_length=300 | |
| content | CKEditor5Field | | Rich text via django-ckeditor-5 |
| is_active | BooleanField | default=True | |

**Inherits**: TimeStampedModel, SEOModel
**Query**: By slug, is_active=True

---

## `teacher` App

### Teacher
| Field | Type | Constraints | Notes |
| --- | --- | --- | --- |
| name | CharField | max_length=200 | |
| title | CharField | max_length=200 | Professional title |
| slug | SlugField | max_length=200, unique=True, allow_unicode=True | Auto from name |
| initials | CharField | max_length=5 | Avatar display |
| bio | TextField | | |
| image | ImageField | upload_to='teachers/', blank=True | |
| years_of_experience | PositiveSmallIntegerField | max=50 | |
| rating | DecimalField | max_digits=2, decimal_places=1, default=5.0 | Admin-managed, independent of reviews |
| student_count | PositiveIntegerField | default=0 | |
| total_sessions | PositiveIntegerField | default=0 | |
| education | TextField | blank=True | |
| teaching_approach | TextField | blank=True | |
| grade_levels | CharField | max_length=200, blank=True | e.g. "Grades 7-12" |
| session_rate_min | DecimalField | max_digits=8, decimal_places=2, null=True, blank=True | |
| availability_notes | TextField | blank=True | |

**Inherits**: TimeStampedModel, PublishableModel, SEOModel
**Relationships**: → Subject (M2M through TeacherSubject), → TeacherAvailability (1:N), → TeacherReview (1:N)
**Query (listing)**: Published, filtered by subject, ordered by `order` then `name`
**Query (profile)**: By slug, status=published

### TeacherSubject
| Field | Type | Constraints | Notes |
| --- | --- | --- | --- |
| teacher | ForeignKey | → Teacher, on_delete=CASCADE | |
| subject | ForeignKey | → Subject, on_delete=CASCADE | |
| is_primary | BooleanField | default=False | |

**Constraints**: unique_together = (teacher, subject)
**Admin**: Inline on Teacher

### TeacherAvailability
| Field | Type | Constraints | Notes |
| --- | --- | --- | --- |
| teacher | ForeignKey | → Teacher, on_delete=CASCADE | |
| day_of_week | CharField | max_length=20, choices=[saturday..thursday] | |
| start_time | TimeField | | |
| end_time | TimeField | | |

**Inherits**: TimeStampedModel
**Constraints**: unique_together = (teacher, day_of_week)
**Admin**: Inline on Teacher

### TeacherReview
| Field | Type | Constraints | Notes |
| --- | --- | --- | --- |
| teacher | ForeignKey | → Teacher, on_delete=CASCADE | |
| reviewer_name | CharField | max_length=200 | |
| rating | PositiveSmallIntegerField | validators=[1-5] | |
| content | TextField | | |
| review_date | DateField | auto_now_add=True | |

**Inherits**: TimeStampedModel, PublishableModel
**Query**: Published, ordered by `review_date` desc
**Admin**: Inline on Teacher

---

## `courses` App

### Subject
| Field | Type | Constraints | Notes |
| --- | --- | --- | --- |
| name | CharField | max_length=200, unique=True | |
| slug | SlugField | max_length=200, unique=True, allow_unicode=True | |
| icon | CharField | max_length=50, blank=True | |
| description | TextField | blank=True | |
| order | PositiveIntegerField | default=0 | |
| is_active | BooleanField | default=True | |

**Inherits**: TimeStampedModel
**Relationships**: → GradeLevel (M2M through SubjectLevel), → Teacher (M2M through TeacherSubject)
**Query**: Active, ordered by `order`

### GradeLevel
| Field | Type | Constraints | Notes |
| --- | --- | --- | --- |
| name | CharField | max_length=100, unique=True | |
| slug | SlugField | max_length=200, unique=True, allow_unicode=True | |
| order | PositiveIntegerField | default=0 | |

**Inherits**: TimeStampedModel

### SubjectLevel
| Field | Type | Constraints | Notes |
| --- | --- | --- | --- |
| subject | ForeignKey | → Subject, on_delete=CASCADE | |
| grade_level | ForeignKey | → GradeLevel, on_delete=CASCADE | |
| description | CharField | max_length=200, blank=True | |

**Constraints**: unique_together = (subject, grade_level)
**Admin**: Inline on Subject

### ProgramTrack
| Field | Type | Constraints | Notes |
| --- | --- | --- | --- |
| name | CharField | max_length=200 | |
| slug | SlugField | max_length=200, unique=True, allow_unicode=True | |
| subtitle | CharField | max_length=300, blank=True | |
| description | TextField | | |
| image | ImageField | upload_to='programs/', blank=True | |
| features | TextField | | One per line |
| cta_text | CharField | max_length=100, blank=True | |
| cta_url | CharField | max_length=200, blank=True | |

**Inherits**: TimeStampedModel, PublishableModel, SEOModel
**Query**: Published, ordered by `order`

---

## `blogs` App

### BlogCategory
| Field | Type | Constraints | Notes |
| --- | --- | --- | --- |
| name | CharField | max_length=100, unique=True | |
| slug | SlugField | max_length=200, unique=True, allow_unicode=True | |
| icon | CharField | max_length=50, blank=True | |
| order | PositiveIntegerField | default=0 | |

**Inherits**: TimeStampedModel

### BlogPost
| Field | Type | Constraints | Notes |
| --- | --- | --- | --- |
| title | CharField | max_length=400 | |
| slug | SlugField | max_length=200, unique=True, allow_unicode=True | Auto from title |
| category | ForeignKey | → BlogCategory, on_delete=SET_NULL, null=True, blank=True | |
| author_name | CharField | max_length=200 | |
| author_title | CharField | max_length=200, blank=True | |
| author_bio | TextField | blank=True | |
| excerpt | TextField | max_length=500 | |
| content | CKEditor5Field | | Rich text via django-ckeditor-5 |
| featured_image | ImageField | upload_to='blog/', blank=True | |
| read_time_minutes | PositiveSmallIntegerField | default=5 | |

**Inherits**: TimeStampedModel, PublishableModel, SEOModel
**Query (listing)**: Published, filtered by category, ordered by `published_at` desc
**Query (featured)**: Published + is_featured=True, first by `order` then `published_at`
**Query (related)**: Published, same category, exclude current, limit 3
**Pagination**: Django Paginator, 6 per page, AJAX load-more

---

## `about` App

### AboutPage (Singleton via django-solo)
| Field | Type | Constraints | Notes |
| --- | --- | --- | --- |
| mission | TextField | | |
| vision | TextField | | |
| story | TextField | | |
| founding_year | PositiveSmallIntegerField | default=2021 | |

**Inherits**: TimeStampedModel, SEOModel
**Admin**: SingletonModelAdmin

### TeamMember
| Field | Type | Constraints | Notes |
| --- | --- | --- | --- |
| name | CharField | max_length=200 | |
| title | CharField | max_length=200 | |
| image | ImageField | upload_to='team/', blank=True | |
| bio | TextField | blank=True | |
| order | PositiveIntegerField | default=0 | |
| is_active | BooleanField | default=True | |

**Inherits**: TimeStampedModel
**Query**: Active, ordered by `order`

---

## `contact` App

### ContactSubmission
| Field | Type | Constraints | Notes |
| --- | --- | --- | --- |
| full_name | CharField | max_length=200 | |
| email | EmailField | | |
| phone | CharField | max_length=20, blank=True | Saudi format validation |
| subject | CharField | max_length=50, choices=[general_inquiry, book_session, complaint, suggestion, other] | |
| message | TextField | min_length=10, max_length=5000 | |
| status | CharField | max_length=20, choices=[new, in_progress, resolved, closed], default=new | |
| admin_notes | TextField | blank=True | |
| resolved_at | DateTimeField | null=True, blank=True | |

**Inherits**: TimeStampedModel
**Spam Protection**: Honeypot field (hidden, silently discard if filled)
**Admin**: Read-only form fields, editable status + admin_notes

---

## Entity Relationship Diagram (Text)

```
accounts.User (AbstractUser, no extras)

main.SiteSettings (singleton)
main.HeroSection
main.Statistic
main.Service
main.Partner
main.Testimonial
main.HowItWorksStep
main.Feature
main.PricingPackage ──1:N──> main.PackageFeature
main.FAQCategory ──1:N──> main.FAQ
main.StaticPage

courses.Subject ──M2M(SubjectLevel)──> courses.GradeLevel
courses.ProgramTrack

teacher.Teacher ──M2M(TeacherSubject)──> courses.Subject
teacher.Teacher ──1:N──> teacher.TeacherAvailability
teacher.Teacher ──1:N──> teacher.TeacherReview

blogs.BlogCategory ──1:N──> blogs.BlogPost

about.AboutPage (singleton)
about.TeamMember

contact.ContactSubmission
```

---

## Seed Data Required

| Entity | Count | Source |
| --- | --- | --- |
| Subject | 8 | Frontend: Math, Physics, Chemistry, English, Arabic, Biology, Aptitude, Achievement |
| GradeLevel | 4 | Frontend: Elementary, Middle, Secondary, Tracks |
| SubjectLevel | ~16 | Frontend subject-level grid |
| Teacher | 8 | Frontend teacher cards |
| ProgramTrack | 3 | Frontend: Private Tutoring, Measurement Exams, Subject Materials |
| PricingPackage | 3 | Frontend: Basic (150 SAR), Premium (200 SAR), Professional (300 SAR) |
| FAQCategory | 5 | Frontend: General, Pricing, Teachers, Scheduling, Platform |
| FAQ | 14 | Frontend FAQ page |
| BlogCategory | 4 | Frontend: Education, Study Tips, Aptitude & Achievement, Platform News |
| BlogPost | 6 | Frontend blog listing |
| Statistic | 6 | Frontend statistics bar |
| Partner | 8 | Frontend partner logos |
| Testimonial | 4 | Frontend testimonial cards |
| HowItWorksStep | 6 | Frontend how-it-works page (6 steps) |
| Service | 3 | Frontend services section |
| TeamMember | 6 | Frontend about page |
