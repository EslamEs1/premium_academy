from decimal import Decimal

from django.core.validators import MinValueValidator
from django.db import models

from apps.main.models import ActiveOrderedModel, SeoModel, generate_unique_slug


class PricingPageSettings(SeoModel):
    title = models.CharField('العنوان', max_length=200, blank=True)
    subtitle = models.TextField('العنوان الفرعي', blank=True)
    description = models.TextField('الوصف', blank=True)

    class Meta:
        verbose_name = 'إعدادات صفحة الأسعار'
        verbose_name_plural = 'إعدادات صفحة الأسعار'

    def __str__(self):
        return self.title or 'إعدادات صفحة الأسعار'


class PricingPlan(ActiveOrderedModel):
    name = models.CharField('اسم الباقة', max_length=100)
    slug = models.SlugField('المعرف', max_length=120, unique=True, blank=True)
    price = models.DecimalField(
        'السعر',
        max_digits=8,
        decimal_places=2,
        validators=[MinValueValidator(Decimal('0.01'))],
    )
    billing_period = models.CharField('فترة الفوترة', max_length=50, blank=True, default='ر.س / الحصة')
    description = models.CharField('الوصف', max_length=200, blank=True)
    cta_text = models.CharField('نص الزر', max_length=50, blank=True)
    cta_url = models.CharField('رابط الزر', max_length=200, blank=True)
    is_popular = models.BooleanField('الأكثر شيوعاً', default=False)

    class Meta:
        ordering = ['order', 'id']
        verbose_name = 'باقة سعرية'
        verbose_name_plural = 'الباقات السعرية'

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
        verbose_name='الباقة',
    )
    text = models.CharField('النص', max_length=200)
    is_included = models.BooleanField('مشمولة', default=True)
    order = models.PositiveIntegerField('الترتيب', default=0)

    class Meta:
        ordering = ['order', 'id']
        verbose_name = 'ميزة باقة'
        verbose_name_plural = 'مميزات الباقة'

    def __str__(self):
        return self.text


class ComparisonFeature(ActiveOrderedModel):
    label = models.CharField('الوصف', max_length=100)
    basic_value = models.CharField('الباقة الأساسية', max_length=100)
    premium_value = models.CharField('الباقة المميزة', max_length=100)
    professional_value = models.CharField('الباقة الاحترافية', max_length=100)

    class Meta:
        ordering = ['order', 'id']
        verbose_name = 'ميزة مقارنة'
        verbose_name_plural = 'مميزات المقارنة'

    def __str__(self):
        return self.label


class PricingFAQ(ActiveOrderedModel):
    question = models.CharField('السؤال', max_length=300)
    answer = models.TextField('الإجابة')

    class Meta:
        ordering = ['order', 'id']
        verbose_name = 'سؤال شائع (الأسعار)'
        verbose_name_plural = 'أسئلة شائعة (الأسعار)'

    def __str__(self):
        return self.question
