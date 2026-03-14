# Data Model: Sana Academy Frontend Website

**Branch**: `002-Sana-academy-frontend` | **Date**: 2026-03-14

## Context

This is a static frontend website with no backend or database. All data exists as hardcoded HTML content. This data model defines the **content structure** — the entities and their attributes as they appear in the frontend markup. This model serves two purposes:

1. **Implementation guide**: Ensures consistent data representation across all pages and components
2. **Future-readiness**: Defines the content shape so that when a backend is added, the frontend can be connected with minimal restructuring

No state transitions, data persistence, or relational integrity enforcement applies. These are content display structures.

---

## Entities

### Teacher

Represents an instructor displayed on teacher cards and profile pages.

| Attribute | Type | Required | Display Context | Example |
|-----------|------|----------|-----------------|---------|
| id | string | Yes | URL slug, card link | `ahmed-hassan` |
| name | string | Yes | Card, profile header | `Dr. Ahmed Hassan` |
| photo | URL | Yes | Card thumbnail, profile hero | `https://randomuser.me/api/portraits/men/32.jpg` |
| headline | string | Yes | Card subtitle, profile tagline | `Mathematics & Physics Expert` |
| biography | text (multi-paragraph) | Yes | Profile body | Full teacher bio text |
| qualifications | string[] | Yes | Profile section | `["Ph.D. Mathematics, Cairo University", "10+ Years Teaching"]` |
| subjects | Subject[] (references) | Yes | Card pills, profile section | `["Mathematics", "Physics", "SAT Prep"]` |
| teachingStyle | text | Yes | Profile section | Description of teaching approach |
| experienceLevel | enum | Yes | Card badge, filter | `senior` / `experienced` / `new` |
| lessonFormats | string[] | Yes | Profile section | `["1-on-1 Online", "Group Classes", "In-Person"]` |
| rating | number (1-5, 1 decimal) | Yes | Card stars, profile header | `4.9` |
| reviewCount | integer | Yes | Card text, profile header | `127` |
| priceIndicator | string | Yes | Card text, profile | `From $35/hr` |
| availabilityStatus | enum | No | Card badge | `available` / `limited` / `unavailable` |
| specializations | string[] | No | Profile detail | `["Exam Preparation", "Gifted Students"]` |
| languages | string[] | No | Profile detail | `["English", "Arabic"]` |

**Displayed on**: Teacher cards (listing, homepage featured), Teacher profile page

**Validation rules**:
- `rating` must be between 1.0 and 5.0
- `reviewCount` must be non-negative
- `subjects` must contain at least 1 item
- `photo` must have a corresponding `alt` text attribute

---

### Subject / Category

Represents an academic or skill area offered by the academy.

| Attribute | Type | Required | Display Context | Example |
|-----------|------|----------|-----------------|---------|
| id | string | Yes | URL parameter (future) | `mathematics` |
| name | string | Yes | Category card/pill text | `Mathematics` |
| icon | SVG markup | Yes | Category card visual | Heroicon academic-cap SVG |
| description | string | No | Category card subtitle | `From algebra to advanced calculus` |
| teacherCount | integer | Yes | Category card metric | `24` |

**Displayed on**: Homepage subjects section, Teachers listing filter sidebar

**Validation rules**:
- `name` must be unique across all subjects
- `teacherCount` must be non-negative

**Demo data requirement**: At least 8 distinct subjects

---

### Program / Course

Represents a structured learning offering.

| Attribute | Type | Required | Display Context | Example |
|-----------|------|----------|-----------------|---------|
| id | string | Yes | URL slug, card link | `advanced-mathematics` |
| title | string | Yes | Card title, detail page H1 | `Advanced Mathematics Program` |
| description | text | Yes | Card excerpt, detail overview | Program description |
| category | string | Yes | Card badge, listing filter | `Mathematics` |
| level | enum | Yes | Card badge, detail page | `beginner` / `intermediate` / `advanced` |
| duration | string | Yes | Card meta, detail page | `12 weeks` |
| inclusions | string[] | Yes | Detail page section | `["24 Live Sessions", "Study Materials", "Practice Tests"]` |
| targetAudience | text | Yes | Detail page section | Who this program is for |
| learningOutcomes | string[] | Yes | Detail page section | `["Master calculus fundamentals", "..."]` |
| instructor | Teacher (reference) | Yes | Detail page instructor card | Reference to a Teacher entity |
| priceIndicator | string | Yes | Card text, detail CTA | `$499` or `Contact Us` |
| featured | boolean | No | Homepage display | `true` |

**Displayed on**: Program cards (listing, homepage), Program detail page

**Validation rules**:
- `level` must be one of the enum values
- `inclusions` must contain at least 1 item
- `learningOutcomes` must contain at least 3 items

**Demo data requirement**: At least 6 programs across at least 3 categories

---

### Testimonial / Review

Represents social proof content. Used in two contexts: general testimonials (homepage) and teacher-specific reviews (teacher profile).

| Attribute | Type | Required | Display Context | Example |
|-----------|------|----------|-----------------|---------|
| reviewerName | string | Yes | Card attribution | `Sarah M.` |
| reviewerRole | string | Yes | Card attribution subtitle | `Student` or `Parent` |
| reviewerPhoto | URL | No | Card avatar | Profile photo URL |
| rating | number (1-5) | Yes | Card stars | `5` |
| text | text | Yes | Card body | Review content |
| date | string | Yes | Card meta | `March 2026` |
| associatedTeacher | Teacher (reference) | No | Teacher profile only | Reference when on teacher page |
| associatedProgram | Program (reference) | No | Program detail only | Reference when on program page |

**Displayed on**: Homepage testimonials section, Teacher profile reviews section, Program detail page

**Validation rules**:
- `rating` must be between 1 and 5 (integer for reviews)
- `text` should be between 20 and 500 characters for display consistency

**Demo data requirement**: At least 3 general testimonials, at least 4 reviews per demo teacher profile

---

### Blog Article

Represents educational content for the blog.

| Attribute | Type | Required | Display Context | Example |
|-----------|------|----------|-----------------|---------|
| id | string | Yes | URL slug | `effective-study-techniques` |
| title | string | Yes | Card title, article H1 | `10 Effective Study Techniques` |
| excerpt | text | Yes | Card body text | 1-2 sentence summary |
| body | HTML content | Yes | Article page body | Full article HTML |
| featuredImage | URL | Yes | Card image, article hero | Image URL |
| author | string | Yes | Card meta, article byline | `Sana Academy Team` |
| authorPhoto | URL | No | Article byline avatar | Author photo URL |
| publishDate | string | Yes | Card meta, article date | `March 10, 2026` |
| category | string | Yes | Card tag, listing filter | `Study Tips` |
| tags | string[] | No | Article footer, listing sidebar | `["Study Tips", "Productivity"]` |
| readTime | string | Yes | Card meta, article meta | `5 min read` |

**Displayed on**: Blog listing cards, Blog detail page, Homepage (optional featured article)

**Validation rules**:
- `excerpt` should be 100-200 characters
- `readTime` format: `N min read`
- `featuredImage` must have corresponding `alt` text

**Demo data requirement**: At least 6 articles across at least 3 categories

---

### Trust Metric

Represents a quantified credibility indicator displayed on the homepage.

| Attribute | Type | Required | Display Context | Example |
|-----------|------|----------|-----------------|---------|
| label | string | Yes | Metric card text | `Active Students` |
| value | string | Yes | Metric card number | `15,000+` |
| icon | SVG markup | Yes | Metric card visual | Heroicon users SVG |

**Displayed on**: Homepage trust metrics section

**Demo data requirement**: Exactly 4 trust metrics (students, teachers, satisfaction, lessons)

---

### FAQ Item

Represents a frequently asked question.

| Attribute | Type | Required | Display Context | Example |
|-----------|------|----------|-----------------|---------|
| question | string | Yes | Accordion trigger text | `How do I book a trial lesson?` |
| answer | text | Yes | Accordion content | Answer paragraph |
| category | string | Yes | FAQ page category header | `Getting Started` |

**Displayed on**: FAQ page (full), Homepage FAQ preview (subset)

**Validation rules**:
- Each `category` must contain at least 2 FAQ items

**Demo data requirement**: At least 12 FAQ items across at least 3 categories (Getting Started, Lessons & Teachers, Pricing & Payments)

---

### Navigation Item

Represents a link in the global header or footer navigation.

| Attribute | Type | Required | Display Context | Example |
|-----------|------|----------|-----------------|---------|
| label | string | Yes | Nav link text | `Teachers` |
| href | string | Yes | Nav link URL | `teachers.html` |
| isActive | boolean | Yes | Highlight state | Computed from current page URL |
| isCTA | boolean | No | Header CTA button | `true` for "Book a Free Trial" |

**Displayed on**: Global header, Global footer, Mobile menu

---

## Entity Relationships

```
Teacher ──────┐
  │           │
  │ teaches   │ referenced by
  │           │
  ▼           ▼
Subject    Program/Course
              │
              │ has
              ▼
         Testimonial/Review ◄── Teacher (also has reviews)

Blog Article (standalone, no entity references)
Trust Metric (standalone, homepage only)
FAQ Item (standalone, grouped by category)
Navigation Item (standalone, shared component)
```

## Demo Data Volume

| Entity | Minimum Count | Notes |
|--------|---------------|-------|
| Teacher | 8 | Displayed on listing page cards |
| Subject | 8 | Homepage categories section |
| Program | 6 | Listing page, across 3+ categories |
| Testimonial (general) | 3 | Homepage testimonials |
| Review (per teacher) | 4 | Teacher profile page |
| Blog Article | 6 | Listing page, across 3+ categories |
| Trust Metric | 4 | Homepage trust section |
| FAQ Item | 12 | FAQ page, 3+ categories |
| Navigation Item (header) | 7 | Main nav links |
| Navigation Item (footer) | 15-20 | Grouped footer links |
