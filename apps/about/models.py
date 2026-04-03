from django.db import models

from apps.main.models import ActiveOrderedModel, SeoModel, generate_unique_slug


class PageContent(SeoModel):
    slug = models.SlugField('المعرف', max_length=120, unique=True, blank=True)
    title = models.CharField('العنوان', max_length=200)
    subtitle = models.TextField('العنوان الفرعي', blank=True)
    badge_text = models.CharField('نص الشارة', max_length=100, blank=True)
    header_icon = models.ImageField('أيقونة الرأس', upload_to='about/', blank=True)
    primary_cta_text = models.CharField('نص الزر الرئيسي', max_length=50, blank=True)
    primary_cta_url = models.CharField('رابط الزر الرئيسي', max_length=200, blank=True)
    secondary_cta_text = models.CharField('نص الزر الثانوي', max_length=50, blank=True)
    secondary_cta_url = models.CharField('رابط الزر الثانوي', max_length=200, blank=True)

    class Meta:
        ordering = ['slug']
        verbose_name = 'محتوى صفحة'
        verbose_name_plural = 'محتوى الصفحات'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = generate_unique_slug(self, self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class ContentBlock(ActiveOrderedModel):
    slug = models.SlugField('المعرف', max_length=120, unique=True, blank=True)
    title = models.CharField('العنوان', max_length=200)
    content = models.TextField('المحتوى')
    icon = models.ImageField('الأيقونة', upload_to='about/', blank=True)

    class Meta:
        ordering = ['order', 'id']
        verbose_name = 'بلوك محتوى'
        verbose_name_plural = 'بلوكات المحتوى'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = generate_unique_slug(self, self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Statistic(ActiveOrderedModel):
    number = models.CharField('الرقم', max_length=20)
    label = models.CharField('التسمية', max_length=100)
    icon = models.CharField('الأيقونة', max_length=50, blank=True)

    class Meta:
        ordering = ['order', 'id']
        verbose_name = 'إحصائية'
        verbose_name_plural = 'الإحصائيات'

    def __str__(self):
        return self.label


class TeamMember(ActiveOrderedModel):
    name = models.CharField('الاسم', max_length=100)
    title = models.CharField('المنصب', max_length=100)
    description = models.TextField('الوصف')
    photo = models.ImageField('الصورة', upload_to='about/team/', blank=True)

    class Meta:
        ordering = ['order', 'id']
        verbose_name = 'عضو فريق'
        verbose_name_plural = 'أعضاء الفريق'

    def __str__(self):
        return self.name


class Achievement(ActiveOrderedModel):
    number = models.CharField('الرقم', max_length=20)
    label = models.CharField('التسمية', max_length=100)
    icon = models.CharField('الأيقونة', max_length=50, blank=True)

    class Meta:
        ordering = ['order', 'id']
        verbose_name = 'إنجاز'
        verbose_name_plural = 'الإنجازات'

    def __str__(self):
        return self.label


class HowItWorksStep(ActiveOrderedModel):
    step_number = models.PositiveSmallIntegerField('رقم الخطوة')
    title = models.CharField('العنوان', max_length=100)
    description = models.TextField('الوصف')
    icon = models.CharField('الأيقونة', max_length=50, blank=True)

    class Meta:
        ordering = ['order', 'id']
        verbose_name = 'خطوة كيف نعمل'
        verbose_name_plural = 'خطوات كيف نعمل'

    def __str__(self):
        return f'{self.step_number}. {self.title}'


class WhyUsFeature(ActiveOrderedModel):
    title = models.CharField('العنوان', max_length=100)
    description = models.TextField('الوصف')
    icon = models.CharField('الأيقونة', max_length=50, blank=True)

    class Meta:
        ordering = ['order', 'id']
        verbose_name = 'ميزة لماذا نحن'
        verbose_name_plural = 'مميزات لماذا نحن'

    def __str__(self):
        return self.title


class ParentFeature(ActiveOrderedModel):
    class FeatureType(models.TextChoices):
        CORE = 'core', 'أساسية'
        CAPABILITY = 'capability', 'قدرة'

    title = models.CharField('العنوان', max_length=100)
    description = models.TextField('الوصف')
    feature_type = models.CharField('نوع الميزة', max_length=20, choices=FeatureType.choices)
    icon = models.CharField('الأيقونة', max_length=50, blank=True)

    class Meta:
        ordering = ['feature_type', 'order', 'id']
        verbose_name = 'ميزة لأولياء الأمور'
        verbose_name_plural = 'مميزات لأولياء الأمور'

    def __str__(self):
        return self.title
