from django.db import models
from django.urls import reverse
from django.utils import timezone

from apps.main.models import ActiveOrderedModel, SeoModel, generate_unique_slug


class BlogPageSettings(SeoModel):
    title = models.CharField('العنوان', max_length=200, blank=True)
    subtitle = models.TextField('العنوان الفرعي', blank=True)
    description = models.TextField('الوصف', blank=True)

    class Meta:
        verbose_name = 'إعدادات صفحة المدونة'
        verbose_name_plural = 'إعدادات صفحة المدونة'

    def __str__(self):
        return self.title or 'إعدادات صفحة المدونة'


class Category(ActiveOrderedModel):
    name = models.CharField('الاسم', max_length=100)
    slug = models.SlugField('المعرف', max_length=120, unique=True, blank=True)
    description = models.CharField('الوصف', max_length=200, blank=True)

    class Meta:
        ordering = ['order', 'name']
        verbose_name = 'تصنيف'
        verbose_name_plural = 'التصنيفات'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = generate_unique_slug(self, self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Author(ActiveOrderedModel):
    name = models.CharField('الاسم', max_length=100)
    slug = models.SlugField('المعرف', max_length=120, unique=True, blank=True)
    title = models.CharField('اللقب', max_length=200)
    bio = models.TextField('النبذة')
    initials = models.CharField('الأحرف الأولى', max_length=10, blank=True)
    photo = models.ImageField('الصورة', upload_to='authors/', blank=True)

    class Meta:
        ordering = ['order', 'name']
        verbose_name = 'كاتب'
        verbose_name_plural = 'الكتّاب'

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


class BlogPostStatus(models.TextChoices):
    DRAFT = 'draft', 'مسودة'
    PUBLISHED = 'published', 'منشور'


class BlogPost(SeoModel):
    Status = BlogPostStatus

    title = models.CharField('العنوان', max_length=200)
    slug = models.SlugField('المعرف', max_length=120, unique=True, blank=True)
    excerpt = models.TextField('المقتطف')
    content = models.TextField('المحتوى')
    featured_image = models.ImageField('الصورة المميزة', upload_to='blog/', blank=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name='posts',
        verbose_name='التصنيف',
    )
    author = models.ForeignKey(
        Author,
        on_delete=models.PROTECT,
        related_name='posts',
        verbose_name='الكاتب',
    )
    icon = models.CharField('الأيقونة', max_length=50, blank=True)
    read_time_minutes = models.PositiveSmallIntegerField('وقت القراءة (دقائق)', default=5)
    status = models.CharField(
        'الحالة',
        max_length=20,
        choices=BlogPostStatus.choices,
        default=BlogPostStatus.DRAFT,
    )
    is_featured = models.BooleanField('مميز', default=False)
    published_date = models.DateTimeField('تاريخ النشر', null=True, blank=True)
    created_at = models.DateTimeField('تاريخ الإنشاء', auto_now_add=True)
    updated_at = models.DateTimeField('تاريخ التحديث', auto_now=True)

    class Meta:
        ordering = ['-published_date', '-created_at']
        verbose_name = 'مقالة'
        verbose_name_plural = 'المقالات'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = generate_unique_slug(self, self.title)
        if self.status == BlogPostStatus.PUBLISHED and self.published_date is None:
            self.published_date = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blogs:detail', args=[self.slug])
