import os
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(BASE_DIR / ".env")

SECRET_KEY = os.getenv(
    "SECRET_KEY",
    "django-insecure-e-kss^0ww-i5$sm6#w48+f_j6&vl76l)!-@4-h7!1g!x818$5f",
)

DEBUG = os.getenv("DEBUG", "False").lower() == "true"

ALLOWED_HOSTS = [
    "snaacademy.com",
    "www.snaacademy.com",
    "127.0.0.1",
    "localhost",
]



INSTALLED_APPS = [
    "jazzmin",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "apps.about.apps.AboutConfig",
    "apps.blogs.apps.BlogsConfig",
    "apps.contact.apps.ContactConfig",
    "apps.course.apps.CourseConfig",
    "apps.main.apps.MainConfig",
    "apps.price.apps.PriceConfig",
    "apps.teacher.apps.TeacherConfig",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "apps" / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "apps.main.context_processors.site_settings",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": os.getenv("DB_ENGINE", "django.db.backends.sqlite3"),
        "NAME": os.getenv("DB_NAME", str(BASE_DIR / "db.sqlite3")),
        "USER": os.getenv("DB_USER", ""),
        "PASSWORD": os.getenv("DB_PASSWORD", ""),
        "HOST": os.getenv("DB_HOST", ""),
        "PORT": os.getenv("DB_PORT", ""),
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

LANGUAGE_CODE = "en"

TIME_ZONE = "Asia/Riyadh"

USE_I18N = True

USE_TZ = True

STATIC_URL = "/staticfiles/"
STATICFILES_DIRS = [BASE_DIR / "staticfiles"]
STATIC_ROOT = BASE_DIR / "static"

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

if not DEBUG:
    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
    SECURE_SSL_REDIRECT = os.getenv("SECURE_SSL_REDIRECT", "False") == "True"
    SESSION_COOKIE_SECURE = os.getenv("SESSION_COOKIE_SECURE", "True") == "True"
    CSRF_COOKIE_SECURE = os.getenv("CSRF_COOKIE_SECURE", "True") == "True"
    SECURE_BROWSER_XSS_FILTER = (
        os.getenv("SECURE_BROWSER_XSS_FILTER", "True") == "True"
    )
    SECURE_CONTENT_TYPE_NOSNIFF = (
        os.getenv("SECURE_CONTENT_TYPE_NOSNIFF", "True") == "True"
    )

CSRF_TRUSTED_ORIGINS = [
    "https://snaacademy.com",
    "https://www.snaacademy.com",
]
# ── Jazzmin Admin ─────────────────────────────────────────────────────────────
JAZZMIN_SETTINGS = {
    "site_title": "أكاديمية سنا | لوحة التحكم",
    "site_header": "أكاديمية سنا",
    "site_brand": "أكاديمية سنا",
    "welcome_sign": "مرحباً بك في لوحة تحكم أكاديمية سنا",
    "copyright": "أكاديمية سنا © 2026",
    "site_logo": "assets/logos/brand-logo.svg",
    "site_logo_classes": "img-circle",
    "site_icon": "assets/logos/brand-logo.svg",
    "topmenu_links": [
        {"name": "الموقع", "url": "/", "new_window": True},
        {"model": "auth.user"},
    ],
    "usermenu_links": [
        {"name": "الموقع", "url": "/", "new_window": True},
    ],
    "show_sidebar": True,
    "navigation_expanded": True,
    "hide_apps": [],
    "hide_models": [],
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
        "main.SiteSettings": "fas fa-cog",
        "main.SocialLink": "fas fa-share-alt",
        "main.Testimonial": "fas fa-star",
        "main.FAQ": "fas fa-question-circle",
        "main.Partner": "fas fa-handshake",
        "main.CTABlock": "fas fa-bullhorn",
        "main.LegalPage": "fas fa-file-alt",
        "main.HeroSection": "fas fa-image",
        "main.TrustStat": "fas fa-chart-bar",
        "main.EducationalService": "fas fa-graduation-cap",
        "main.FeatureBlock": "fas fa-th-large",
        "main.ProcessStep": "fas fa-list-ol",
        "main.AppPromoSection": "fas fa-mobile-alt",
        "blogs.BlogPost": "fas fa-newspaper",
        "blogs.Category": "fas fa-tags",
        "blogs.Author": "fas fa-pen-nib",
        "blogs.BlogPageSettings": "fas fa-blog",
        "teacher.Teacher": "fas fa-chalkboard-teacher",
        "teacher.TeacherApplication": "fas fa-user-plus",
        "teacher.TeacherPageSettings": "fas fa-sliders-h",
        "teacher.TeacherStat": "fas fa-chart-line",
        "contact.ContactSubmission": "fas fa-envelope",
        "contact.ContactPageSettings": "fas fa-address-card",
        "contact.OperatingHours": "fas fa-clock",
        "contact.ContactFAQ": "fas fa-comments",
        "price.PricingPlan": "fas fa-tags",
        "price.PricingPageSettings": "fas fa-money-bill-wave",
        "price.ComparisonFeature": "fas fa-balance-scale",
        "price.PricingFAQ": "fas fa-question",
        "course.Subject": "fas fa-book",
        "about.PageContent": "fas fa-info-circle",
        "about.TeamMember": "fas fa-users",
        "about.Achievement": "fas fa-trophy",
        "about.HowItWorksStep": "fas fa-shoe-prints",
        "about.Statistic": "fas fa-poll",
    },
    "default_icon_parents": "fas fa-folder",
    "default_icon_children": "fas fa-circle",
    "search_model": [
        "auth.user",
        "blogs.BlogPost",
        "teacher.Teacher",
        "contact.ContactSubmission",
        "teacher.TeacherApplication",
    ],
    "related_modal_active": True,
    "show_ui_builder": False,
    "changeform_format": "horizontal_tabs",
}

JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": False,
    "brand_small_text": False,
    "brand_colour": "navbar-primary",
    "accent": "accent-primary",
    "navbar": "navbar-dark",
    "no_navbar_border": False,
    "navbar_fixed": True,
    "layout_boxed": False,
    "footer_fixed": False,
    "sidebar_fixed": True,
    "sidebar": "sidebar-dark-primary",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": True,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": False,
    "theme": "default",
    "dark_mode_theme": None,
    "button_classes": {
        "primary": "btn-primary",
        "secondary": "btn-secondary",
        "info": "btn-info",
        "warning": "btn-warning",
        "danger": "btn-danger",
        "success": "btn-success",
    },
}
