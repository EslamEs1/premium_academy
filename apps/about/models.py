from django.db import models

from apps.main.models import ActiveOrderedModel, SeoModel, generate_unique_slug


class PageContent(SeoModel):
    slug = models.SlugField(max_length=120, unique=True, blank=True)
    title = models.CharField(max_length=200)
    subtitle = models.TextField(blank=True)
    badge_text = models.CharField(max_length=100, blank=True)
    header_icon = models.ImageField(upload_to='about/', blank=True)
    primary_cta_text = models.CharField(max_length=50, blank=True)
    primary_cta_url = models.CharField(max_length=200, blank=True)
    secondary_cta_text = models.CharField(max_length=50, blank=True)
    secondary_cta_url = models.CharField(max_length=200, blank=True)

    class Meta:
        ordering = ['slug']
        verbose_name = 'Page Content'
        verbose_name_plural = 'Page Content'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = generate_unique_slug(self, self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class ContentBlock(ActiveOrderedModel):
    slug = models.SlugField(max_length=120, unique=True, blank=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    icon = models.ImageField(upload_to='about/', blank=True)

    class Meta:
        ordering = ['order', 'id']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = generate_unique_slug(self, self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Statistic(ActiveOrderedModel):
    number = models.CharField(max_length=20)
    label = models.CharField(max_length=100)
    icon = models.CharField(max_length=50, blank=True)

    class Meta:
        ordering = ['order', 'id']

    def __str__(self):
        return self.label


class TeamMember(ActiveOrderedModel):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.TextField()
    photo = models.ImageField(upload_to='about/team/', blank=True)

    class Meta:
        ordering = ['order', 'id']

    def __str__(self):
        return self.name


class Achievement(ActiveOrderedModel):
    number = models.CharField(max_length=20)
    label = models.CharField(max_length=100)
    icon = models.CharField(max_length=50, blank=True)

    class Meta:
        ordering = ['order', 'id']

    def __str__(self):
        return self.label


class HowItWorksStep(ActiveOrderedModel):
    step_number = models.PositiveSmallIntegerField()
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.CharField(max_length=50, blank=True)

    class Meta:
        ordering = ['order', 'id']
        verbose_name = 'How It Works Step'
        verbose_name_plural = 'How It Works Steps'

    def __str__(self):
        return f'{self.step_number}. {self.title}'


class WhyUsFeature(ActiveOrderedModel):
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.CharField(max_length=50, blank=True)

    class Meta:
        ordering = ['order', 'id']

    def __str__(self):
        return self.title


class ParentFeature(ActiveOrderedModel):
    class FeatureType(models.TextChoices):
        CORE = 'core', 'Core'
        CAPABILITY = 'capability', 'Capability'

    title = models.CharField(max_length=100)
    description = models.TextField()
    feature_type = models.CharField(max_length=20, choices=FeatureType.choices)
    icon = models.CharField(max_length=50, blank=True)

    class Meta:
        ordering = ['feature_type', 'order', 'id']

    def __str__(self):
        return self.title
