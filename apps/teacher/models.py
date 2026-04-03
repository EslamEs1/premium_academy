from decimal import Decimal

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.urls import reverse

from apps.course.models import Subject
from apps.main.models import ActiveOrderedModel, SeoModel, generate_unique_slug


class TeacherPageSettings(SeoModel):
    hero_title = models.CharField('عنوان الهيرو', max_length=200, blank=True)
    hero_subtitle = models.TextField('العنوان الفرعي للهيرو', blank=True)
    hero_image = models.ImageField('صورة الهيرو', upload_to='teachers/', blank=True)

    class Meta:
        verbose_name = 'إعدادات صفحة المعلمين'
        verbose_name_plural = 'إعدادات صفحة المعلمين'

    def __str__(self):
        return self.hero_title or 'إعدادات صفحة المعلمين'


class TeacherStat(ActiveOrderedModel):
    number = models.CharField('الرقم', max_length=20)
    label = models.CharField('التسمية', max_length=100)
    description = models.CharField('الوصف', max_length=200, blank=True)
    icon = models.CharField('الأيقونة', max_length=50, blank=True)

    class Meta:
        ordering = ['order', 'id']
        verbose_name = 'إحصائية معلم'
        verbose_name_plural = 'إحصائيات المعلمين'

    def __str__(self):
        return self.label


class Teacher(SeoModel, ActiveOrderedModel):
    name = models.CharField('الاسم', max_length=100)
    slug = models.SlugField('المعرف', max_length=120, unique=True, blank=True)
    initials = models.CharField('الأحرف الأولى', max_length=10, blank=True)
    primary_subject = models.ForeignKey(
        Subject,
        on_delete=models.PROTECT,
        related_name='teachers',
        verbose_name='المادة الرئيسية',
    )
    title = models.CharField('اللقب', max_length=200)
    short_bio = models.CharField('نبذة مختصرة', max_length=255, blank=True)
    full_bio = models.TextField('السيرة الذاتية')
    qualifications = models.TextField('المؤهلات', blank=True)
    experience_years = models.PositiveSmallIntegerField('سنوات الخبرة', default=0)
    experience_description = models.CharField('وصف الخبرة', max_length=200, blank=True)
    rating = models.DecimalField(
        'التقييم',
        max_digits=2,
        decimal_places=1,
        default=Decimal('5.0'),
        validators=[MinValueValidator(Decimal('1.0')), MaxValueValidator(Decimal('5.0'))],
    )
    student_count = models.PositiveIntegerField('عدد الطلاب', default=0)
    completed_sessions = models.PositiveIntegerField('الحصص المكتملة', default=0)
    platform_years = models.PositiveSmallIntegerField('سنوات على المنصة', default=0)
    success_rate = models.PositiveSmallIntegerField('نسبة النجاح %', default=98)
    session_rate = models.DecimalField('سعر الحصة', max_digits=8, decimal_places=2, default=Decimal('0.00'))
    photo = models.ImageField('الصورة', upload_to='teachers/', blank=True)
    booking_cta_text = models.CharField('نص زر الحجز', max_length=50, blank=True, default='احجز حصة')
    booking_cta_url = models.CharField('رابط الحجز', max_length=200, blank=True, default='/contact/')
    whatsapp_number = models.CharField('رقم واتساب', max_length=20, blank=True)
    is_featured = models.BooleanField('مميز', default=False)

    class Meta:
        ordering = ['order', 'id']
        verbose_name = 'معلم'
        verbose_name_plural = 'المعلمون'

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
        verbose_name='المعلم',
    )
    text = models.CharField('النص', max_length=200)

    class Meta:
        ordering = ['order', 'id']
        verbose_name = 'ميزة المعلم'
        verbose_name_plural = 'مميزات المعلم'

    def __str__(self):
        return self.text


class TeacherSpecialization(ActiveOrderedModel):
    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.CASCADE,
        related_name='specializations',
        verbose_name='المعلم',
    )
    subject = models.ForeignKey(
        Subject,
        on_delete=models.PROTECT,
        related_name='teacher_specializations',
        null=True,
        blank=True,
        verbose_name='المادة',
    )
    label = models.CharField('التسمية', max_length=100, blank=True)
    grade_level = models.CharField('المرحلة الدراسية', max_length=200, blank=True)

    class Meta:
        ordering = ['order', 'id']
        verbose_name = 'تخصص المعلم'
        verbose_name_plural = 'تخصصات المعلم'

    def __str__(self):
        return self.label or getattr(self.subject, 'name', 'تخصص')


class TeacherReview(ActiveOrderedModel):
    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='المعلم',
    )
    student_name = models.CharField('اسم الطالب', max_length=100)
    student_initials = models.CharField('الأحرف الأولى', max_length=10, blank=True)
    level = models.CharField('المرحلة', max_length=100, blank=True)
    subject = models.CharField('المادة', max_length=100, blank=True)
    rating = models.PositiveSmallIntegerField(
        'التقييم',
        default=5,
        validators=[MinValueValidator(1), MaxValueValidator(5)],
    )
    quote = models.TextField('نص المراجعة')
    review_date = models.DateField('تاريخ المراجعة')

    class Meta:
        ordering = ['order', 'id']
        verbose_name = 'مراجعة معلم'
        verbose_name_plural = 'مراجعات المعلم'

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
        verbose_name='المعلم',
    )
    day_of_week = models.CharField('اليوم', max_length=100)
    start_time = models.TimeField('وقت البدء')
    end_time = models.TimeField('وقت الانتهاء')
    note = models.CharField('ملاحظة', max_length=300, blank=True)

    class Meta:
        ordering = ['order', 'id']
        verbose_name = 'توفر المعلم'
        verbose_name_plural = 'أوقات توفر المعلم'

    def __str__(self):
        return self.day_of_week


class TeacherApplication(models.Model):
    """طلب انضمام معلم جديد."""

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

    full_name = models.CharField('الاسم الكامل', max_length=150)
    phone = models.CharField('رقم الهاتف', max_length=30)
    email = models.EmailField('البريد الإلكتروني', blank=True)
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
    """مرفقات طلب الانضمام."""

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
    uploaded_at = models.DateTimeField('تاريخ الرفع', auto_now_add=True)

    class Meta:
        verbose_name = 'مرفق'
        verbose_name_plural = 'المرفقات'

    def __str__(self):
        return f'{self.get_attachment_type_display()} — {self.application.full_name}'

    @property
    def filename(self):
        import os
        return os.path.basename(self.file.name)
