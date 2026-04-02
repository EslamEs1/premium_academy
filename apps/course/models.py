from django.db import models
from django.utils.text import slugify


def generate_unique_slug(instance, source_value):
    base_slug = slugify(source_value, allow_unicode=True) or instance._meta.model_name
    slug = base_slug
    suffix = 1

    while instance.__class__.objects.exclude(pk=instance.pk).filter(slug=slug).exists():
        suffix += 1
        slug = f'{base_slug}-{suffix}'

    return slug


class Subject(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=120, unique=True, blank=True)
    description = models.CharField(max_length=200, blank=True)
    icon = models.CharField(max_length=50, blank=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order', 'name']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = generate_unique_slug(self, self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
