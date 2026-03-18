# Data Model: Premium Arabic Academy Website Frontend

**Branch**: `004-premium-academy-frontend`
**Date**: 2026-03-18

## Overview

This project is a static frontend with no database or API layer.
All data is represented as hardcoded HTML content. This data model
defines the **content entities** and their attributes to ensure
consistency across all pages where the same entity type appears.

The model serves as a contract for content authors: every instance
of a Teacher, Testimonial, FAQ Item, etc. MUST include ALL required
fields with realistic Arabic content.

---

## Entities

### Teacher

Represents a tutor available on the platform. Appears on: homepage
teacher showcase, teachers listing page, teacher profile page,
related teachers sections.

| Attribute        | Type     | Required | Example                            |
| ---------------- | -------- | -------- | ---------------------------------- |
| nameAr           | string   | YES      | "أ. عبدالرحمن الشمري"              |
| photo            | image    | YES      | Gradient placeholder with initials |
| biography        | text     | YES      | 2–3 Arabic paragraphs              |
| subjectsPrimary  | string   | YES      | "الرياضيات"                        |
| subjectsList     | string[] | YES      | ["الرياضيات", "الفيزياء"]          |
| gradeLevels      | string[] | YES      | ["متوسط", "ثانوي"]                 |
| experienceYears  | number   | YES      | 10                                 |
| studentCount     | number   | YES      | 230                                |
| rating           | number   | YES      | 4.9                                |
| priceStarting    | string   | YES      | "١٥٠ ر.س/الحصة"                    |
| availabilityNote | string   | NO       | "متاح أيام السبت–الأربعاء"         |
| cardGradient     | string   | YES      | "#F51140" (warm accent color)      |

**Consistency rule**: Every teacher card across the site MUST
display: nameAr, photo, subjectsPrimary, experienceYears, rating,
studentCount, and a CTA. The teacher profile page additionally
displays: biography, subjectsList, gradeLevels, priceStarting,
availabilityNote.

**Minimum instances**: 8 unique teachers with distinct subjects
and realistic Arabic biographies.

---

### Subject

Represents an academic subject offered by the academy. Appears on:
homepage subject browser, teachers page filter.

| Attribute    | Type     | Required | Example                       |
| ------------ | -------- | -------- | ----------------------------- |
| nameAr       | string   | YES      | "الرياضيات"                   |
| icon         | SVG      | YES      | Calculator icon inline SVG    |
| description  | string   | NO       | "من الابتدائي إلى الثانوي"    |
| gradeLevels  | string[] | YES      | ["ابتدائي", "متوسط", "ثانوي"] |
| teacherCount | number   | NO       | 45                            |
| isActive     | boolean  | YES      | true (false = "قريبًا")       |

**Minimum instances**: 8 subjects (الرياضيات, الفيزياء, الكيمياء,
اللغة الإنجليزية, اللغة العربية, الأحياء, القدرات, التحصيلي).

---

### Testimonial

Represents a student/parent review. Appears on: homepage
testimonials, teacher profile reviews, how-it-works success
stories.

| Attribute     | Type   | Required | Example                         |
| ------------- | ------ | -------- | ------------------------------- |
| studentNameAr | string | YES      | "سارة المطيري"                  |
| gradeLevel    | string | YES      | "ثاني ثانوي"                    |
| subject       | string | YES      | "الرياضيات"                     |
| rating        | number | YES      | 5                               |
| reviewTextAr  | string | YES      | 2–3 sentences in natural Arabic |
| photo         | image  | NO       | Gradient avatar placeholder     |

**Consistency rule**: Every testimonial MUST include studentNameAr,
gradeLevel, subject, rating, and reviewTextAr. No generic "Student
A says great things" placeholders.

**Minimum instances**: 6 unique testimonials with distinct names
and subjects.

---

### FAQ Item

Represents a frequently asked question. Appears on: homepage FAQ
preview, full FAQ page, contact page mini FAQ.

| Attribute  | Type   | Required | Example                        |
| ---------- | ------ | -------- | ------------------------------ |
| questionAr | string | YES      | "كيف أسجل في المنصة؟"          |
| answerAr   | string | YES      | 3–5 sentences in Arabic        |
| category   | string | YES      | "عام" / "الأسعار" / "المعلمون" |

**Categories**: عام (General), الأسعار (Pricing), المعلمون
(Teachers), الجدولة (Scheduling), المنصة (Platform).

**Minimum instances**: 15 questions (3+ per category) with
substantive Arabic answers.

---

### Article (Blog)

Represents a blog post. Appears on: blog listing page, blog
article page, related articles sections.

| Attribute   | Type   | Required | Example                            |
| ----------- | ------ | -------- | ---------------------------------- |
| titleAr     | string | YES      | "٥ نصائح للتفوق في اختبار القدرات" |
| excerptAr   | string | YES      | 2 sentences summarizing article    |
| bodyAr      | text   | YES      | 4–5 paragraphs (article page)      |
| author      | string | YES      | "م. فاطمة الحربي"                  |
| publishDate | string | YES      | "١٥ مارس ٢٠٢٦"                     |
| category    | string | YES      | "نصائح دراسية"                     |
| readingTime | string | YES      | "٥ دقائق"                          |
| thumbnail   | image  | YES      | Gradient placeholder               |

**Categories**: تعليم, نصائح دراسية, القدرات والتحصيلي,
أخبار المنصة.

**Minimum instances**: 6 articles for the blog listing grid +
1 full article for the blog-post page.

---

### Service

Represents a main service category. Appears on: homepage services
overview, homepage service deep-dives.

| Attribute     | Type     | Required | Example                          |
| ------------- | -------- | -------- | -------------------------------- |
| nameAr        | string   | YES      | "الدروس الخصوصية"                |
| descriptionAr | string   | YES      | 1–2 Arabic sentences             |
| features      | string[] | YES      | 6 bullet points in Arabic        |
| tags          | string[] | NO       | ["المنهاج الوطني", "IB/IGCSE"]   |
| ctaTextAr     | string   | YES      | "اعرف أكثر"                      |
| ctaLink       | string   | YES      | "#" or page link                 |
| illustration  | image    | YES      | Educational illustration/graphic |

**Minimum instances**: 3 services (Private Tutoring, Exam Prep,
Curriculum Content).

---

### Team Member

Represents an academy team member. Appears on: about page team
section.

| Attribute | Type   | Required | Example                     |
| --------- | ------ | -------- | --------------------------- |
| nameAr    | string | YES      | "د. أحمد الفهد"             |
| titleAr   | string | YES      | "المدير التنفيذي"           |
| photo     | image  | YES      | Gradient avatar placeholder |
| bioAr     | string | YES      | 1 sentence biography        |

**Minimum instances**: 4–6 team members with distinct roles.

---

### Partner

Represents an institutional partner. Appears on: homepage logo
carousel, about page partners section, footer accreditation.

| Attribute | Type    | Required | Example               |
| --------- | ------- | -------- | --------------------- |
| nameAr    | string  | YES      | "جامعة الملك سعود"    |
| logo      | SVG/img | YES      | Clean SVG placeholder |
| url       | string  | NO       | "#"                   |

**Minimum instances**: 8 partner logos for the carousel.

---

### Pricing Plan

Represents a pricing tier. Appears on: pricing page.

| Attribute | Type     | Required | Example                     |
| --------- | -------- | -------- | --------------------------- |
| nameAr    | string   | YES      | "الباقة الأساسية"           |
| priceAr   | string   | YES      | "١٥٠ ر.س / الحصة"           |
| features  | string[] | YES      | 6–8 feature items in Arabic |
| isPopular | boolean  | YES      | true (highlighted plan)     |
| ctaTextAr | string   | YES      | "اشترك الآن"                |

**Minimum instances**: 3 pricing tiers (Basic, Popular, Premium).

---

### Platform Statistic

Represents a trust metric displayed site-wide.

| Attribute | Type   | Required | Example         |
| --------- | ------ | -------- | --------------- |
| labelAr   | string | YES      | "معلم"          |
| value     | string | YES      | "+٥٠٠"          |
| icon      | SVG    | YES      | Inline SVG icon |

**Fixed instances**: 4 stats (teachers, students, lessons,
satisfaction rate).
