from django.db import models
from django.urls import reverse
from django.utils import timezone

from apps.main.models import ActiveOrderedModel, SeoModel, generate_unique_slug


class BlogPageSettings(SeoModel):
    title = models.CharField(max_length=200, blank=True)
    subtitle = models.TextField(blank=True)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Blog Page Settings'
        verbose_name_plural = 'Blog Page Settings'

    def __str__(self):
        return self.title or 'Blog Page Settings'


class Category(ActiveOrderedModel):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=120, unique=True, blank=True)
    description = models.CharField(max_length=200, blank=True)

    class Meta:
        ordering = ['order', 'name']
        verbose_name_plural = 'Categories'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = generate_unique_slug(self, self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Author(ActiveOrderedModel):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=120, unique=True, blank=True)
    title = models.CharField(max_length=200)
    bio = models.TextField()
    initials = models.CharField(max_length=10, blank=True)
    photo = models.ImageField(upload_to='authors/', blank=True)

    class Meta:
        ordering = ['order', 'name']

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
    DRAFT = 'draft', 'Draft'
    PUBLISHED = 'published', 'Published'


class BlogPost(SeoModel):
    Status = BlogPostStatus

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=120, unique=True, blank=True)
    excerpt = models.TextField()
    content = models.TextField()
    featured_image = models.ImageField(upload_to='blog/', blank=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name='posts',
    )
    author = models.ForeignKey(
        Author,
        on_delete=models.PROTECT,
        related_name='posts',
    )
    icon = models.CharField(max_length=50, blank=True)
    read_time_minutes = models.PositiveSmallIntegerField(default=5)
    status = models.CharField(
        max_length=20,
        choices=BlogPostStatus.choices,
        default=BlogPostStatus.DRAFT,
    )
    is_featured = models.BooleanField(default=False)
    published_date = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-published_date', '-created_at']

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
