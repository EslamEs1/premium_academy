# Public Route Contract

This contract defines the public URL surface that the backend implementation must preserve while converting the static frontend into Django-managed pages.

| Route | Name | Owner App | Template | Primary Lookup / Data Contract |
| --- | --- | --- | --- | --- |
| `/` | `home` | `main` | `apps/main/templates/index.html` | singleton homepage sections plus shared footer/header settings |
| `/about/` | `about` | `about` | `apps/about/templates/about.html` | about page settings, content blocks, stats, team, achievements |
| `/how-it-works/` | `how_it_works` | `about` | `apps/about/templates/how-it-works.html` | how-it-works settings, steps, why-us, parent features |
| `/teachers/` | `teacher_list` | `teacher` | `apps/teacher/templates/teachers.html` | teacher list, subject filters, teacher stats, targeted testimonials |
| `/teachers/<slug:slug>/` | `teacher_detail` | `teacher` | `apps/teacher/templates/teacher-profile.html` | one active teacher by slug, owned child content, similar teachers |
| `/pricing/` | `pricing` | `price` | `apps/price/templates/pricing.html` | pricing settings, plans, comparison rows, pricing FAQ, targeted testimonials |
| `/blog/` | `blog_list` | `blogs` | `apps/blogs/templates/blog.html` | published posts, featured post, active categories, optional category filter |
| `/blog/<slug:slug>/` | `blog_detail` | `blogs` | `apps/blogs/templates/blog-post.html` | one published blog post by slug, author, related posts |
| `/faq/` | `faq` | `main` | `apps/main/templates/faq.html` or equivalent shared FAQ template | active FAQs grouped by category, related links, FAQ page meta |
| `/contact/` | `contact` | `contact` | `apps/contact/templates/contact.html` | contact page settings, contact form, why-choose points, hours, contact FAQ |
| `/privacy/` | `privacy` | `main` | `apps/main/templates/privacy.html` | legal page content for privacy policy |
| `/terms/` | `terms` | `main` | `apps/main/templates/terms.html` | legal page content for terms of service |

## Route Rules

- Teacher and blog detail routes must return only active/published records.
- Shared header/footer data comes from the global site-settings context processor, not per-view duplication.
- Blog category and teacher subject filters may use query parameters without changing the route pattern.
- The FAQ page remains server-rendered, with client-side interaction layered on top of server-provided category data.
