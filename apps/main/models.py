from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.text import slugify


def generate_unique_slug(instance, source_value, slug_field='slug'):
    """توليد slug فريد للنموذج."""
    base_slug = slugify(source_value, allow_unicode=True) or instance._meta.model_name
    slug = base_slug
    model_class = instance.__class__
    suffix = 1
    while model_class.objects.exclude(pk=instance.pk).filter(**{slug_field: slug}).exists():
        suffix += 1
        slug = f'{base_slug}-{suffix}'
    return slug


class ActiveModel(models.Model):
    is_active = models.BooleanField('نشط', default=True)

    class Meta:
        abstract = True


class OrderedModel(models.Model):
    order = models.PositiveIntegerField('الترتيب', default=0)

    class Meta:
        abstract = True


class ActiveOrderedModel(ActiveModel, OrderedModel):
    class Meta:
        abstract = True


class SeoModel(models.Model):
    meta_title = models.CharField('عنوان الصفحة (SEO)', max_length=200, blank=True)
    meta_description = models.TextField('وصف الصفحة (SEO)', blank=True)

    class Meta:
        abstract = True


class SiteSettings(models.Model):
    site_name = models.CharField('اسم الموقع', max_length=100, blank=True, default='Sana Academy')
    site_description = models.TextField('وصف الموقع', blank=True)
    logo = models.ImageField('الشعار', upload_to='site/', blank=True)
    logo_white = models.ImageField('الشعار الأبيض', upload_to='site/', blank=True)
    phone = models.CharField('رقم الهاتف', max_length=20, blank=True)
    email = models.EmailField('البريد الإلكتروني', blank=True)
    whatsapp = models.CharField('واتساب', max_length=20, blank=True)
    address = models.CharField('العنوان', max_length=200, blank=True)
    google_maps_url = models.URLField('رابط خريطة جوجل', blank=True)
    copyright_text = models.CharField('نص حقوق النشر', max_length=200, blank=True)
    accreditation_text = models.TextField('نص الاعتماد', blank=True)
    accreditation_badge = models.ImageField('شارة الاعتماد', upload_to='site/', blank=True)

    class Meta:
        verbose_name = 'إعدادات الموقع'
        verbose_name_plural = 'إعدادات الموقع'

    def __str__(self):
        return self.site_name or 'إعدادات الموقع'


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
        verbose_name='إعدادات الموقع',
    )
    platform = models.CharField('المنصة', max_length=30, choices=SocialLinkPlatform.choices)
    url = models.URLField('الرابط')

    class Meta:
        ordering = ['order', 'id']
        verbose_name = 'رابط تواصل اجتماعي'
        verbose_name_plural = 'روابط التواصل الاجتماعي'

    def __str__(self):
        return f'{self.get_platform_display()}'


class Partner(ActiveOrderedModel):
    name = models.CharField('اسم الشريك', max_length=100)
    logo = models.ImageField('الشعار', upload_to='partners/', blank=True)
    url = models.URLField('الرابط', blank=True)

    class Meta:
        ordering = ['order', 'name']
        verbose_name = 'شريك'
        verbose_name_plural = 'الشركاء'

    def __str__(self):
        return self.name


class TestimonialPage(models.TextChoices):
    HOMEPAGE = 'homepage', 'الرئيسية'
    TEACHERS = 'teachers', 'المعلمون'
    PRICING = 'pricing', 'الأسعار'
    HOW_IT_WORKS = 'how-it-works', 'كيف نعمل'


class Testimonial(ActiveOrderedModel):
    student_name = models.CharField('اسم الطالب', max_length=100)
    student_initials = models.CharField('الأحرف الأولى', max_length=10)
    level = models.CharField('المرحلة الدراسية', max_length=100, blank=True)
    subject = models.CharField('المادة', max_length=100, blank=True)
    rating = models.PositiveSmallIntegerField(
        'التقييم',
        default=5,
        validators=[MinValueValidator(1), MaxValueValidator(5)],
    )
    quote = models.TextField('المراجعة')
    page = models.CharField('الصفحة', max_length=20, choices=TestimonialPage.choices)
    is_featured = models.BooleanField('مميز', default=False)

    class Meta:
        ordering = ['order', 'student_name']
        verbose_name = 'مراجعة'
        verbose_name_plural = 'المراجعات'

    def __str__(self):
        return f'{self.student_name} ({self.get_page_display()})'


class FAQCategory(models.TextChoices):
    GENERAL = 'general', 'عام'
    PRICING = 'pricing', 'الأسعار'
    TEACHERS = 'teachers', 'المعلمون'
    SCHEDULING = 'scheduling', 'الجدول'
    PLATFORM = 'platform', 'المنصة'


class FAQ(ActiveOrderedModel):
    question = models.CharField('السؤال', max_length=300)
    answer = models.TextField('الإجابة')
    category = models.CharField('الفئة', max_length=20, choices=FAQCategory.choices)
    show_on_homepage = models.BooleanField('يظهر في الرئيسية', default=False)

    class Meta:
        ordering = ['order', 'question']
        verbose_name = 'سؤال شائع'
        verbose_name_plural = 'الأسئلة الشائعة'

    def __str__(self):
        return self.question


class CTABlock(ActiveModel):
    slug = models.SlugField('المعرف', max_length=120, unique=True, blank=True)
    heading = models.CharField('العنوان', max_length=200)
    subheading = models.CharField('العنوان الفرعي', max_length=200, blank=True)
    body_text = models.TextField('النص', blank=True)
    primary_cta_text = models.CharField('نص الزر الرئيسي', max_length=50, blank=True)
    primary_cta_url = models.CharField('رابط الزر الرئيسي', max_length=200, blank=True)
    secondary_cta_text = models.CharField('نص الزر الثانوي', max_length=50, blank=True)
    secondary_cta_url = models.CharField('رابط الزر الثانوي', max_length=200, blank=True)
    social_proof_text = models.CharField('نص الدليل الاجتماعي', max_length=200, blank=True)

    class Meta:
        ordering = ['slug']
        verbose_name = 'بلوك دعوة للعمل (CTA)'
        verbose_name_plural = 'بلوكات الدعوة للعمل (CTA)'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = generate_unique_slug(self, self.heading)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.heading


class PageMeta(SeoModel, ActiveModel):
    slug = models.SlugField('المعرف', max_length=120, unique=True, blank=True)

    class Meta:
        ordering = ['slug']
        verbose_name = 'بيانات صفحة'
        verbose_name_plural = 'بيانات الصفحات'

    def save(self, *args, **kwargs):
        if not self.slug:
            source_value = self.meta_title or 'page-meta'
            self.slug = generate_unique_slug(self, source_value)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.slug


class RelatedLink(ActiveOrderedModel):
    title = models.CharField('العنوان', max_length=200)
    description = models.TextField('الوصف', blank=True)
    url = models.URLField('الرابط')

    class Meta:
        ordering = ['order', 'title']
        verbose_name = 'رابط ذو صلة'
        verbose_name_plural = 'روابط ذات صلة'

    def __str__(self):
        return self.title


class LegalPage(SeoModel):
    title = models.CharField('العنوان', max_length=200)
    slug = models.SlugField('المعرف', max_length=120, unique=True, blank=True)
    content = models.TextField('المحتوى')
    updated_at = models.DateTimeField('تاريخ التحديث', auto_now=True)

    class Meta:
        ordering = ['title']
        verbose_name = 'صفحة قانونية'
        verbose_name_plural = 'الصفحات القانونية'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = generate_unique_slug(self, self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class HeroSection(models.Model):
    headline = models.CharField('العنوان الرئيسي', max_length=200)
    subheading = models.CharField('العنوان الفرعي', max_length=300, blank=True)
    description = models.TextField('الوصف')
    primary_cta_text = models.CharField('نص الزر الرئيسي', max_length=50)
    primary_cta_url = models.CharField('رابط الزر الرئيسي', max_length=200)
    secondary_cta_text = models.CharField('نص الزر الثانوي', max_length=50, blank=True)
    secondary_cta_url = models.CharField('رابط الزر الثانوي', max_length=200, blank=True)
    hero_image = models.ImageField('صورة الـ Hero', upload_to='home/', blank=True)

    class Meta:
        verbose_name = 'قسم الـ Hero'
        verbose_name_plural = 'قسم الـ Hero'

    def __str__(self):
        return self.headline


class TrustStat(ActiveOrderedModel):
    number = models.CharField('الرقم', max_length=20)
    label = models.CharField('التسمية', max_length=100)
    description = models.CharField('الوصف', max_length=200, blank=True)
    icon = models.CharField('الأيقونة', max_length=50, blank=True)

    class Meta:
        ordering = ['order', 'id']
        verbose_name = 'إحصائية ثقة'
        verbose_name_plural = 'إحصائيات الثقة'

    def __str__(self):
        return self.label


class EducationalService(ActiveOrderedModel):
    title = models.CharField('العنوان', max_length=100)
    description = models.TextField('الوصف')
    icon = models.CharField('الأيقونة', max_length=50, blank=True)
    image = models.ImageField('الصورة', upload_to='services/', blank=True)
    cta_text = models.CharField('نص الزر', max_length=50, blank=True)
    cta_url = models.CharField('رابط الزر', max_length=200, blank=True)

    class Meta:
        ordering = ['order', 'id']
        verbose_name = 'خدمة تعليمية'
        verbose_name_plural = 'الخدمات التعليمية'

    def __str__(self):
        return self.title


class ServiceFeature(OrderedModel):
    service = models.ForeignKey(
        EducationalService,
        on_delete=models.CASCADE,
        related_name='features',
        verbose_name='الخدمة',
    )
    text = models.CharField('النص', max_length=200)

    class Meta:
        ordering = ['order', 'id']
        verbose_name = 'ميزة خدمة'
        verbose_name_plural = 'مميزات الخدمة'

    def __str__(self):
        return self.text


class FeatureBlock(ActiveOrderedModel):
    slug = models.SlugField('المعرف', max_length=120, unique=True, blank=True)
    title = models.CharField('العنوان', max_length=200)
    description = models.TextField('الوصف')
    image = models.ImageField('الصورة', upload_to='features/', blank=True)

    class Meta:
        ordering = ['order', 'id']
        verbose_name = 'بلوك مميزات'
        verbose_name_plural = 'بلوكات المميزات'

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
        verbose_name='بلوك المميزات',
    )
    text = models.CharField('النص', max_length=300)

    class Meta:
        ordering = ['order', 'id']
        verbose_name = 'نقطة ميزة'
        verbose_name_plural = 'نقاط الميزة'

    def __str__(self):
        return self.text


class FeatureTab(OrderedModel):
    feature_block = models.ForeignKey(
        FeatureBlock,
        on_delete=models.CASCADE,
        related_name='tabs',
        verbose_name='بلوك المميزات',
    )
    title = models.CharField('العنوان', max_length=100)

    class Meta:
        ordering = ['order', 'id']
        verbose_name = 'تبويب ميزة'
        verbose_name_plural = 'تبويبات المميزات'

    def __str__(self):
        return self.title


class FeatureTabPoint(OrderedModel):
    tab = models.ForeignKey(
        FeatureTab,
        on_delete=models.CASCADE,
        related_name='points',
        verbose_name='التبويب',
    )
    text = models.CharField('النص', max_length=300)

    class Meta:
        ordering = ['order', 'id']
        verbose_name = 'نقطة تبويب'
        verbose_name_plural = 'نقاط التبويب'

    def __str__(self):
        return self.text


class ProcessStep(ActiveOrderedModel):
    step_number = models.PositiveSmallIntegerField('رقم الخطوة')
    title = models.CharField('العنوان', max_length=100)
    description = models.TextField('الوصف')
    icon = models.CharField('الأيقونة', max_length=50, blank=True)

    class Meta:
        ordering = ['order', 'id']
        verbose_name = 'خطوة عملية'
        verbose_name_plural = 'خطوات العملية'

    def __str__(self):
        return f'{self.step_number}. {self.title}'


class AppPromoSection(ActiveModel):
    title = models.CharField('العنوان', max_length=200)
    subtitle = models.CharField('العنوان الفرعي', max_length=200, blank=True)
    description = models.TextField('الوصف')
    preview_image = models.ImageField('صورة المعاينة', upload_to='app-promo/', blank=True)
    google_play_url = models.URLField('رابط Google Play', blank=True)
    app_store_url = models.URLField('رابط App Store', blank=True)

    class Meta:
        verbose_name = 'قسم ترويج التطبيق'
        verbose_name_plural = 'قسم ترويج التطبيق'

    def __str__(self):
        return self.title
