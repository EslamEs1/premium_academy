from decimal import Decimal

from django.core.validators import MinValueValidator
from django.db import models

from apps.main.models import ActiveOrderedModel, SeoModel, generate_unique_slug


class PricingPageSettings(SeoModel):
    title = models.CharField(max_length=200, blank=True)
    subtitle = models.TextField(blank=True)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Pricing Page Settings'
        verbose_name_plural = 'Pricing Page Settings'

    def __str__(self):
        return self.title or 'Pricing Page Settings'


class PricingPlan(ActiveOrderedModel):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=120, unique=True, blank=True)
    price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        validators=[MinValueValidator(Decimal('0.01'))],
    )
    billing_period = models.CharField(max_length=50, blank=True, default='ر.س / الحصة')
    description = models.CharField(max_length=200, blank=True)
    cta_text = models.CharField(max_length=50, blank=True)
    cta_url = models.CharField(max_length=200, blank=True)
    is_popular = models.BooleanField(default=False)

    class Meta:
        ordering = ['order', 'id']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = generate_unique_slug(self, self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class PlanFeature(models.Model):
    plan = models.ForeignKey(
        PricingPlan,
        on_delete=models.CASCADE,
        related_name='features',
    )
    text = models.CharField(max_length=200)
    is_included = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'id']

    def __str__(self):
        return self.text


class ComparisonFeature(ActiveOrderedModel):
    label = models.CharField(max_length=100)
    basic_value = models.CharField(max_length=100)
    premium_value = models.CharField(max_length=100)
    professional_value = models.CharField(max_length=100)

    class Meta:
        ordering = ['order', 'id']

    def __str__(self):
        return self.label


class PricingFAQ(ActiveOrderedModel):
    question = models.CharField(max_length=300)
    answer = models.TextField()

    class Meta:
        ordering = ['order', 'id']

    def __str__(self):
        return self.question
