from django.db import models

from apps.main.models import ActiveOrderedModel, SeoModel


class ContactPageSettings(SeoModel):
    hero_title = models.CharField('عنوان الهيرو', max_length=200, blank=True)
    hero_subtitle = models.TextField('العنوان الفرعي للهيرو', blank=True)

    class Meta:
        verbose_name = 'إعدادات صفحة التواصل'
        verbose_name_plural = 'إعدادات صفحة التواصل'

    def __str__(self):
        return self.hero_title or 'إعدادات صفحة التواصل'


class ContactSubmission(models.Model):
    class Subject(models.TextChoices):
        INQUIRY = 'inquiry', 'استفسار عام'
        BOOKING = 'booking', 'حجز حصة'
        COMPLAINT = 'complaint', 'شكوى'
        SUGGESTION = 'suggestion', 'اقتراح'
        OTHER = 'other', 'أخرى'

    full_name = models.CharField('الاسم الكامل', max_length=100)
    email = models.EmailField('البريد الإلكتروني')
    phone = models.CharField('رقم الهاتف', max_length=20, blank=True)
    subject = models.CharField('الموضوع', max_length=50, choices=Subject.choices)
    message = models.TextField('الرسالة')
    is_read = models.BooleanField('تمت القراءة', default=False)
    created_at = models.DateTimeField('تاريخ الإرسال', auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'رسالة تواصل'
        verbose_name_plural = 'رسائل التواصل'

    def __str__(self):
        return f'{self.full_name} - {self.get_subject_display()}'


class WhyChoosePoint(ActiveOrderedModel):
    text = models.CharField('النص', max_length=300)

    class Meta:
        ordering = ['order', 'id']
        verbose_name = 'سبب الاختيار'
        verbose_name_plural = 'أسباب الاختيار'

    def __str__(self):
        return self.text


class OperatingHours(ActiveOrderedModel):
    day_label = models.CharField('اليوم', max_length=100)
    time_range = models.CharField('ساعات العمل', max_length=100)
    note = models.CharField('ملاحظة', max_length=300, blank=True)

    class Meta:
        ordering = ['order', 'id']
        verbose_name = 'ساعات عمل'
        verbose_name_plural = 'ساعات العمل'

    def __str__(self):
        return self.day_label


class ContactFAQ(ActiveOrderedModel):
    question = models.CharField('السؤال', max_length=300)
    answer = models.TextField('الإجابة')

    class Meta:
        ordering = ['order', 'id']
        verbose_name = 'سؤال شائع (التواصل)'
        verbose_name_plural = 'أسئلة شائعة (التواصل)'

    def __str__(self):
        return self.question
