# Quickstart: Academy Backend CMS

## Goal

Implement the backend CMS in the existing Django project without changing the locked frontend layouts.

## 1. Prepare the project

```bash
cd /media/eslam/work/backend/premium_academy
source venv/bin/activate
python manage.py check
```

Update `config/settings.py` first:

- register all seven domain apps in `INSTALLED_APPS`
- add media settings (`MEDIA_URL`, `MEDIA_ROOT`)
- switch `LANGUAGE_CODE` and `TIME_ZONE` to the project's Arabic/Saudi deployment defaults when implementation begins
- add the shared site-settings context processor

## 2. Implement the shared foundation first

Create and migrate these first:

1. `main.SiteSettings` and `main.SocialLink`
2. `course.Subject`
3. `main.CTABlock`
4. `main.Partner`
5. `main.Testimonial`
6. `main.FAQ`
7. `main.PageMeta`

Then wire:

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

## 3. Convert pages in the recommended order

1. Base template shared data via the site-settings context processor
2. Homepage (`main`)
3. Teachers listing and teacher profile (`teacher`)
4. Blog listing and blog detail (`blogs`)
5. Pricing (`price`)
6. Contact and FAQ (`contact` + shared `main.FAQ`)
7. About and how-it-works (`about`)
8. Privacy and terms (`main`)

For each page conversion:

- define the models and admin registration
- add or update the view/queryset contract
- wire the route
- replace hardcoded template content with context variables
- verify that no template structure or section is removed

## 4. Seed current frontend content

After the relevant models exist, create initial records matching the current hardcoded content so that templates remain visually identical when switched to dynamic rendering.

Recommended approach:

```bash
python manage.py shell
```

Inside the shell or a dedicated data migration:

- create singleton settings/page records first
- create shared lookup content next (`Subject`, `Partner`, `CTABlock`, `FAQ`, `Testimonial`)
- create page-specific collections after their parent/settings records exist

## 5. Verify the CMS surface

Run:

```bash
venv/bin/python manage.py test
venv/bin/python manage.py runserver
```

Minimum smoke checks:

1. Admin can edit homepage hero copy and the homepage updates.
2. A featured teacher appears on the homepage and on `/teachers/`.
3. A published blog post appears publicly, while a draft does not.
4. Pricing edits change the rendered pricing page.
5. Contact form validation rejects bad email and stores valid submissions.
6. FAQ and blog filters work without breaking the locked frontend layout.
7. Shared footer/header data renders on every page from `SiteSettings`.

## 6. Validation Status

Validation run date: `2026-04-02`

Successful commands:

```bash
venv/bin/python manage.py check
venv/bin/python manage.py migrate main
venv/bin/python manage.py test apps.main.tests.test_foundations apps.main.tests.test_homepage apps.main.tests.test_faq_page apps.main.tests.test_faq_admin apps.main.tests.test_sitewide_queries apps.about.tests.test_about_pages apps.about.tests.test_about_admin apps.blogs.tests.test_blog_pages apps.blogs.tests.test_blog_admin apps.contact.tests.test_contact_page apps.contact.tests.test_contact_admin apps.course.tests.test_foundations apps.price.tests.test_pricing_page apps.price.tests.test_pricing_admin apps.teacher.tests.test_teacher_pages apps.teacher.tests.test_teacher_admin
```

Observed gaps:

1. `venv/bin/python manage.py test` currently reports `0` discovered tests in this repo.
2. Package-level test labels such as `venv/bin/python manage.py test apps.main.tests` fail discovery with a `TypeError` from Django's test loader.
3. Manual `venv/bin/python manage.py runserver` smoke checks were not executed in this environment, so browser-level verification of navigation, assets, and interactions remains a manual follow-up step.

Current automated validation result:

- `49` targeted module-level tests passed.
- `System check identified no issues (0 silenced).`
