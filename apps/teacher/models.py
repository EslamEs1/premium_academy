from decimal import Decimal

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.urls import reverse

from apps.course.models import Subject
from apps.main.models import ActiveOrderedModel, SeoModel, generate_unique_slug


class TeacherPageSettings(SeoModel):
    hero_title = models.CharField(max_length=200, blank=True)
    hero_subtitle = models.TextField(blank=True)
    hero_image = models.ImageField(upload_to='teachers/', blank=True)

    class Meta:
        verbose_name = 'Teacher Page Settings'
        verbose_name_plural = 'Teacher Page Settings'

    def __str__(self):
        return self.hero_title or 'Teacher Page Settings'


class TeacherStat(ActiveOrderedModel):
    number = models.CharField(max_length=20)
    label = models.CharField(max_length=100)
    description = models.CharField(max_length=200, blank=True)
    icon = models.CharField(max_length=50, blank=True)

    class Meta:
        ordering = ['order', 'id']

    def __str__(self):
        return self.label


class Teacher(SeoModel, ActiveOrderedModel):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=120, unique=True, blank=True)
    initials = models.CharField(max_length=10, blank=True)
    primary_subject = models.ForeignKey(
        Subject,
        on_delete=models.PROTECT,
        related_name='teachers',
    )
    title = models.CharField(max_length=200)
    short_bio = models.CharField(max_length=255, blank=True)
    full_bio = models.TextField()
    qualifications = models.TextField(blank=True)
    experience_years = models.PositiveSmallIntegerField(default=0)
    experience_description = models.CharField(max_length=200, blank=True)
    rating = models.DecimalField(
        max_digits=2,
        decimal_places=1,
        default=Decimal('5.0'),
        validators=[MinValueValidator(Decimal('1.0')), MaxValueValidator(Decimal('5.0'))],
    )
    student_count = models.PositiveIntegerField(default=0)
    completed_sessions = models.PositiveIntegerField(default=0)
    platform_years = models.PositiveSmallIntegerField(default=0)
    success_rate = models.PositiveSmallIntegerField(default=98)
    session_rate = models.DecimalField(max_digits=8, decimal_places=2, default=Decimal('0.00'))
    photo = models.ImageField(upload_to='teachers/', blank=True)
    booking_cta_text = models.CharField(max_length=50, blank=True, default='احجز حصة')
    booking_cta_url = models.CharField(max_length=200, blank=True, default='/contact/')
    whatsapp_number = models.CharField(max_length=20, blank=True)
    is_featured = models.BooleanField(default=False)

    class Meta:
        ordering = ['order', 'id']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = generate_unique_slug(self, self.name)
        if not self.initials:
            tokens = [token for token in self.name.split() if token]
            if len(tokens) >= 2:
                self.initials = ''.join(token[0] for token in tokens[:2])
            else:
                self.initials = self.name[:2]
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('teacher:detail', args=[self.slug])

    @property
    def whatsapp_url(self):
        if not self.whatsapp_number:
            return ''
        return f'https://wa.me/{self.whatsapp_number}'


class TeacherFeature(ActiveOrderedModel):
    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.CASCADE,
        related_name='features',
    )
    text = models.CharField(max_length=200)

    class Meta:
        ordering = ['order', 'id']

    def __str__(self):
        return self.text


class TeacherSpecialization(ActiveOrderedModel):
    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.CASCADE,
        related_name='specializations',
    )
    subject = models.ForeignKey(
        Subject,
        on_delete=models.PROTECT,
        related_name='teacher_specializations',
        null=True,
        blank=True,
    )
    label = models.CharField(max_length=100, blank=True)
    grade_level = models.CharField(max_length=200, blank=True)

    class Meta:
        ordering = ['order', 'id']

    def __str__(self):
        return self.label or getattr(self.subject, 'name', 'Specialization')


class TeacherReview(ActiveOrderedModel):
    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.CASCADE,
        related_name='reviews',
    )
    student_name = models.CharField(max_length=100)
    student_initials = models.CharField(max_length=10, blank=True)
    level = models.CharField(max_length=100, blank=True)
    subject = models.CharField(max_length=100, blank=True)
    rating = models.PositiveSmallIntegerField(
        default=5,
        validators=[MinValueValidator(1), MaxValueValidator(5)],
    )
    quote = models.TextField()
    review_date = models.DateField()

    class Meta:
        ordering = ['order', 'id']

    def save(self, *args, **kwargs):
        if not self.student_initials:
            tokens = [token for token in self.student_name.split() if token]
            if len(tokens) >= 2:
                self.student_initials = ''.join(token[0] for token in tokens[:2])
            else:
                self.student_initials = self.student_name[:2]
        super().save(*args, **kwargs)

    def __str__(self):
        return self.student_name


class TeacherAvailability(ActiveOrderedModel):
    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.CASCADE,
        related_name='availability',
    )
    day_of_week = models.CharField(max_length=100)
    start_time = models.TimeField()
    end_time = models.TimeField()
    note = models.CharField(max_length=300, blank=True)

    class Meta:
        ordering = ['order', 'id']
        verbose_name_plural = 'Teacher availability'

    def __str__(self):
        return self.day_of_week


class TeacherApplication(models.Model):
    """Submitted by teachers who want to join the academy."""

    STATUS_PENDING = 'pending'
    STATUS_REVIEWING = 'reviewing'
    STATUS_APPROVED = 'approved'
    STATUS_REJECTED = 'rejected'
    STATUS_CHOICES = [
        (STATUS_PENDING, 'قيد الانتظار'),
        (STATUS_REVIEWING, 'قيد المراجعة'),
        (STATUS_APPROVED, 'مقبول'),
        (STATUS_REJECTED, 'مرفوض'),
    ]

    EXPERIENCE_CHOICES = [
        ('less_1', 'أقل من سنة'),
        ('1_3', 'من 1 إلى 3 سنوات'),
        ('3_5', 'من 3 إلى 5 سنوات'),
        ('5_10', 'من 5 إلى 10 سنوات'),
        ('more_10', 'أكثر من 10 سنوات'),
    ]

    # Identity
    full_name = models.CharField('الاسم الكامل', max_length=150)
    phone = models.CharField('رقم الهاتف', max_length=30)
    email = models.EmailField('البريد الإلكتروني', blank=True)

    # Professional
    specialization = models.CharField('التخصص', max_length=200)
    experience = models.CharField(
        'سنوات الخبرة',
        max_length=20,
        choices=EXPERIENCE_CHOICES,
        default='1_3',
    )
    courses = models.TextField(
        'الكورسات التي يمكنك تدريسها',
        help_text='اذكر الكورسات أو المواد التي تستطيع تدريسها، سطر لكل كورس.',
    )
    description = models.TextField(
        'نبذة عنك',
        help_text='أخبرنا عن نفسك وخبرتك التعليمية.',
    )

    # Admin
    status = models.CharField(
        'الحالة',
        max_length=20,
        choices=STATUS_CHOICES,
        default=STATUS_PENDING,
        db_index=True,
    )
    admin_notes = models.TextField('ملاحظات الإدارة', blank=True)
    submitted_at = models.DateTimeField('تاريخ التقديم', auto_now_add=True)
    reviewed_at = models.DateTimeField('تاريخ المراجعة', null=True, blank=True)

    class Meta:
        verbose_name = 'طلب انضمام معلم'
        verbose_name_plural = 'طلبات انضمام المعلمين'
        ordering = ['-submitted_at']

    def __str__(self):
        return f'{self.full_name} — {self.get_status_display()}'

    @property
    def is_new(self):
        return self.status == self.STATUS_PENDING


def _application_attachment_path(instance, filename):
    return f'teacher_applications/{instance.application_id}/{filename}'


class TeacherApplicationAttachment(models.Model):
    """Files, videos, screenshots, certificates attached to an application."""

    TYPE_CHOICES = [
        ('certificate', 'شهادة'),
        ('video', 'مقطع فيديو'),
        ('screenshot', 'لقطة شاشة'),
        ('cv', 'السيرة الذاتية'),
        ('other', 'أخرى'),
    ]

    application = models.ForeignKey(
        TeacherApplication,
        on_delete=models.CASCADE,
        related_name='attachments',
        verbose_name='الطلب',
    )
    attachment_type = models.CharField(
        'نوع المرفق',
        max_length=20,
        choices=TYPE_CHOICES,
        default='other',
    )
    file = models.FileField('الملف', upload_to=_application_attachment_path)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'مرفق'
        verbose_name_plural = 'المرفقات'

    def __str__(self):
        return f'{self.get_attachment_type_display()} — {self.application.full_name}'

    @property
    def filename(self):
        import os
        return os.path.basename(self.file.name)
