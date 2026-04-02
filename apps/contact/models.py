from django.db import models

from apps.main.models import ActiveOrderedModel, SeoModel


class ContactPageSettings(SeoModel):
    hero_title = models.CharField(max_length=200, blank=True)
    hero_subtitle = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Contact Page Settings'
        verbose_name_plural = 'Contact Page Settings'

    def __str__(self):
        return self.hero_title or 'Contact Page Settings'


class ContactSubmission(models.Model):
    class Subject(models.TextChoices):
        INQUIRY = 'inquiry', 'استفسار عام'
        BOOKING = 'booking', 'حجز حصة'
        COMPLAINT = 'complaint', 'شكوى'
        SUGGESTION = 'suggestion', 'اقتراح'
        OTHER = 'other', 'أخرى'

    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    subject = models.CharField(max_length=50, choices=Subject.choices)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.full_name} - {self.get_subject_display()}'


class WhyChoosePoint(ActiveOrderedModel):
    text = models.CharField(max_length=300)

    class Meta:
        ordering = ['order', 'id']

    def __str__(self):
        return self.text


class OperatingHours(ActiveOrderedModel):
    day_label = models.CharField(max_length=100)
    time_range = models.CharField(max_length=100)
    note = models.CharField(max_length=300, blank=True)

    class Meta:
        ordering = ['order', 'id']
        verbose_name_plural = 'Operating hours'

    def __str__(self):
        return self.day_label


class ContactFAQ(ActiveOrderedModel):
    question = models.CharField(max_length=300)
    answer = models.TextField()

    class Meta:
        ordering = ['order', 'id']

    def __str__(self):
        return self.question
