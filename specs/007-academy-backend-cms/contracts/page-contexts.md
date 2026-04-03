# Template Context Contract

This contract defines the minimum context keys each locked template must receive from the backend.

## Homepage

Route: `/`

Required context:

- `hero`
- `stats`
- `services`
- `partners`
- `tutoring_block`
- `aptitude_block`
- `subjects`
- `teachers`
- `testimonials`
- `steps`
- `faqs`
- `app_promo`
- `cta`

## About

Route: `/about/`

Required context:

- `page`
- `blocks`
- `statistics`
- `team_members`
- `achievements`
- `partners`
- `cta`

## How It Works

Route: `/how-it-works/`

Required context:

- `page`
- `steps`
- `why_us_features`
- `success_testimonials`
- `parent_features`
- `cta`

## Teachers Listing

Route: `/teachers/`

Required context:

- `page_settings`
- `subjects`
- `teachers`
- `stats`
- `testimonials`
- `cta`
- `active_subject_slug`

## Teacher Detail

Route: `/teachers/<slug>/`

Required context:

- `teacher`
- `features`
- `specializations`
- `reviews`
- `availability`
- `similar_teachers`
- `cta`

## Pricing

Route: `/pricing/`

Required context:

- `page_settings`
- `plans`
- `comparison_features`
- `pricing_faqs`
- `testimonials`
- `cta`

## Blog Listing

Route: `/blog/`

Required context:

- `page_settings`
- `featured_post`
- `posts`
- `categories`
- `active_category_slug`
- `cta`

## Blog Detail

Route: `/blog/<slug>/`

Required context:

- `post`
- `author`
- `related_posts`
- `cta`

## FAQ

Route: `/faq/`

Required context:

- `page_meta`
- `faqs`
- `faq_categories`
- `related_links`

## Contact

Route: `/contact/`

Required context:

- `page_settings`
- `form`
- `why_choose_points`
- `operating_hours`
- `contact_faqs`
- `site_contact`
- `cta`

## Legal Pages

Routes: `/privacy/`, `/terms/`

Required context:

- `page`

## Shared Context

Every public page receives:

- `site_settings`

Implementation note:

- `site_settings` should come from a context processor with `social_links` prefetched.
