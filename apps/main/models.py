from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.text import slugify


def generate_unique_slug(instance, source_value, slug_field='slug'):
    """Generate a unique slug for the given instance and source value."""

    base_slug = slugify(source_value, allow_unicode=True) or instance._meta.model_name
    slug = base_slug
    model_class = instance.__class__
    suffix = 1

    while model_class.objects.exclude(pk=instance.pk).filter(**{slug_field: slug}).exists():
        suffix += 1
        slug = f'{base_slug}-{suffix}'

    return slug


class ActiveModel(models.Model):
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class OrderedModel(models.Model):
    order = models.PositiveIntegerField(default=0)

    class Meta:
        abstract = True


class ActiveOrderedModel(ActiveModel, OrderedModel):
    class Meta:
        abstract = True


class SeoModel(models.Model):
    meta_title = models.CharField(max_length=200, blank=True)
    meta_description = models.TextField(blank=True)

    class Meta:
        abstract = True


class SiteSettings(models.Model):
    site_name = models.CharField(max_length=100, blank=True, default='Sana Academy')
    site_description = models.TextField(blank=True)
    logo = models.ImageField(upload_to='site/', blank=True)
    logo_white = models.ImageField(upload_to='site/', blank=True)
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    whatsapp = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=200, blank=True)
    google_maps_url = models.URLField(blank=True)
    copyright_text = models.CharField(max_length=200, blank=True)
    accreditation_text = models.TextField(blank=True)
    accreditation_badge = models.ImageField(upload_to='site/', blank=True)

    class Meta:
        verbose_name = 'Site Settings'
        verbose_name_plural = 'Site Settings'

    def __str__(self):
        return self.site_name or 'Site Settings'


class SocialLinkPlatform(models.TextChoices):
    WHATSAPP = 'whatsapp', 'WhatsApp'
    INSTAGRAM = 'instagram', 'Instagram'
    X = 'x', 'X'
    YOUTUBE = 'youtube', 'YouTube'
    TIKTOK = 'tiktok', 'TikTok'
    SNAPCHAT = 'snapchat', 'Snapchat'
    LINKEDIN = 'linkedin', 'LinkedIn'
    FACEBOOK = 'facebook', 'Facebook'
    TELEGRAM = 'telegram', 'Telegram'


class SocialLink(ActiveOrderedModel):
    site_settings = models.ForeignKey(
        SiteSettings,
        on_delete=models.CASCADE,
        related_name='social_links',
    )
    platform = models.CharField(max_length=30, choices=SocialLinkPlatform.choices)
    url = models.URLField()

    class Meta:
        ordering = ['order', 'id']

    def __str__(self):
        return f'{self.get_platform_display()}'


class Partner(ActiveOrderedModel):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='partners/', blank=True)
    url = models.URLField(blank=True)

    class Meta:
        ordering = ['order', 'name']

    def __str__(self):
        return self.name


class TestimonialPage(models.TextChoices):
    HOMEPAGE = 'homepage', 'Homepage'
    TEACHERS = 'teachers', 'Teachers'
    PRICING = 'pricing', 'Pricing'
    HOW_IT_WORKS = 'how-it-works', 'How It Works'


class Testimonial(ActiveOrderedModel):
    student_name = models.CharField(max_length=100)
    student_initials = models.CharField(max_length=10)
    level = models.CharField(max_length=100, blank=True)
    subject = models.CharField(max_length=100, blank=True)
    rating = models.PositiveSmallIntegerField(
        default=5,
        validators=[MinValueValidator(1), MaxValueValidator(5)],
    )
    quote = models.TextField()
    page = models.CharField(max_length=20, choices=TestimonialPage.choices)
    is_featured = models.BooleanField(default=False)

    class Meta:
        ordering = ['order', 'student_name']

    def __str__(self):
        return f'{self.student_name} ({self.get_page_display()})'


class FAQCategory(models.TextChoices):
    GENERAL = 'general', 'General'
    PRICING = 'pricing', 'Pricing'
    TEACHERS = 'teachers', 'Teachers'
    SCHEDULING = 'scheduling', 'Scheduling'
    PLATFORM = 'platform', 'Platform'


class FAQ(ActiveOrderedModel):
    question = models.CharField(max_length=300)
    answer = models.TextField()
    category = models.CharField(max_length=20, choices=FAQCategory.choices)
    show_on_homepage = models.BooleanField(default=False)

    class Meta:
        ordering = ['order', 'question']

    def __str__(self):
        return self.question


class CTABlock(ActiveModel):
    slug = models.SlugField(max_length=120, unique=True, blank=True)
    heading = models.CharField(max_length=200)
    subheading = models.CharField(max_length=200, blank=True)
    body_text = models.TextField(blank=True)
    primary_cta_text = models.CharField(max_length=50, blank=True)
    primary_cta_url = models.CharField(max_length=200, blank=True)
    secondary_cta_text = models.CharField(max_length=50, blank=True)
    secondary_cta_url = models.CharField(max_length=200, blank=True)
    social_proof_text = models.CharField(max_length=200, blank=True)

    class Meta:
        ordering = ['slug']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = generate_unique_slug(self, self.heading)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.heading


class PageMeta(SeoModel, ActiveModel):
    slug = models.SlugField(max_length=120, unique=True, blank=True)

    class Meta:
        ordering = ['slug']
        verbose_name_plural = 'Page metadata'

    def save(self, *args, **kwargs):
        if not self.slug:
            source_value = self.meta_title or 'page-meta'
            self.slug = generate_unique_slug(self, source_value)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.slug


class RelatedLink(ActiveOrderedModel):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    url = models.URLField()

    class Meta:
        ordering = ['order', 'title']

    def __str__(self):
        return self.title


class LegalPage(SeoModel):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=120, unique=True, blank=True)
    content = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['title']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = generate_unique_slug(self, self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class HeroSection(models.Model):
    headline = models.CharField(max_length=200)
    subheading = models.CharField(max_length=300, blank=True)
    description = models.TextField()
    primary_cta_text = models.CharField(max_length=50)
    primary_cta_url = models.CharField(max_length=200)
    secondary_cta_text = models.CharField(max_length=50, blank=True)
    secondary_cta_url = models.CharField(max_length=200, blank=True)
    hero_image = models.ImageField(upload_to='home/', blank=True)

    class Meta:
        verbose_name = 'Hero Section'
        verbose_name_plural = 'Hero Section'

    def __str__(self):
        return self.headline


class TrustStat(ActiveOrderedModel):
    number = models.CharField(max_length=20)
    label = models.CharField(max_length=100)
    description = models.CharField(max_length=200, blank=True)
    icon = models.CharField(max_length=50, blank=True)

    class Meta:
        ordering = ['order', 'id']

    def __str__(self):
        return self.label


class EducationalService(ActiveOrderedModel):
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.CharField(max_length=50, blank=True)
    image = models.ImageField(upload_to='services/', blank=True)
    cta_text = models.CharField(max_length=50, blank=True)
    cta_url = models.CharField(max_length=200, blank=True)

    class Meta:
        ordering = ['order', 'id']

    def __str__(self):
        return self.title


class ServiceFeature(OrderedModel):
    service = models.ForeignKey(
        EducationalService,
        on_delete=models.CASCADE,
        related_name='features',
    )
    text = models.CharField(max_length=200)

    class Meta:
        ordering = ['order', 'id']

    def __str__(self):
        return self.text


class FeatureBlock(ActiveOrderedModel):
    slug = models.SlugField(max_length=120, unique=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='features/', blank=True)

    class Meta:
        ordering = ['order', 'id']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = generate_unique_slug(self, self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class FeaturePoint(OrderedModel):
    feature_block = models.ForeignKey(
        FeatureBlock,
        on_delete=models.CASCADE,
        related_name='points',
    )
    text = models.CharField(max_length=300)

    class Meta:
        ordering = ['order', 'id']

    def __str__(self):
        return self.text


class FeatureTab(OrderedModel):
    feature_block = models.ForeignKey(
        FeatureBlock,
        on_delete=models.CASCADE,
        related_name='tabs',
    )
    title = models.CharField(max_length=100)

    class Meta:
        ordering = ['order', 'id']

    def __str__(self):
        return self.title


class FeatureTabPoint(OrderedModel):
    tab = models.ForeignKey(
        FeatureTab,
        on_delete=models.CASCADE,
        related_name='points',
    )
    text = models.CharField(max_length=300)

    class Meta:
        ordering = ['order', 'id']

    def __str__(self):
        return self.text


class ProcessStep(ActiveOrderedModel):
    step_number = models.PositiveSmallIntegerField()
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.CharField(max_length=50, blank=True)

    class Meta:
        ordering = ['order', 'id']

    def __str__(self):
        return f'{self.step_number}. {self.title}'


class AppPromoSection(ActiveModel):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200, blank=True)
    description = models.TextField()
    preview_image = models.ImageField(upload_to='app-promo/', blank=True)
    google_play_url = models.URLField(blank=True)
    app_store_url = models.URLField(blank=True)

    class Meta:
        verbose_name = 'App Promo Section'
        verbose_name_plural = 'App Promo Section'

    def __str__(self):
        return self.title
