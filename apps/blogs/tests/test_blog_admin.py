from django.contrib.admin.sites import AdminSite
from django.test import TestCase

from apps.blogs.admin import BlogPostAdmin
from apps.blogs.models import Author, BlogPost, Category


class BlogAdminTests(TestCase):
    def test_blog_post_admin_exposes_status_and_featured_controls(self):
        admin_config = BlogPostAdmin(BlogPost, AdminSite())

        self.assertEqual(
            admin_config.list_display,
            ('title', 'category', 'author', 'status', 'is_featured', 'published_date'),
        )
        self.assertEqual(
            admin_config.list_filter,
            ('status', 'is_featured', 'category', 'author'),
        )
        self.assertEqual(admin_config.prepopulated_fields, {'slug': ('title',)})

    def test_blog_post_slug_autogenerates_and_meta_fields_persist(self):
        category = Category.objects.create(
            name='أخبار المنصة',
            description='فئة تجريبية',
            order=10,
            is_active=True,
        )
        author = Author.objects.create(
            name='فريق أكاديمية سنا',
            title='فريق التحرير',
            bio='نبذة عن فريق التحرير.',
            initials='ف.س',
            order=10,
            is_active=True,
        )

        post = BlogPost.objects.create(
            title='إطلاق مسار جديد للطلاب',
            excerpt='مقال عن إطلاق مسار جديد.',
            content='تفاصيل المقال.',
            category=category,
            author=author,
            icon='trophy',
            read_time_minutes=3,
            status=BlogPost.Status.PUBLISHED,
            meta_title='عنوان ميتا للمقال',
            meta_description='وصف ميتا للمقال',
        )

        self.assertEqual(post.slug, 'إطلاق-مسار-جديد-للطلاب')
        self.assertEqual(post.meta_title, 'عنوان ميتا للمقال')
        self.assertEqual(post.meta_description, 'وصف ميتا للمقال')
