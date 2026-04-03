from datetime import timedelta

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from apps.blogs.models import Author, BlogPageSettings, BlogPost, Category
from apps.main.models import CTABlock


class BlogPagesTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        BlogPageSettings.objects.update_or_create(
            pk=1,
            defaults={
                'title': 'المدونة',
                'subtitle': 'محتوى تعليمي متجدد للطلاب والأسر.',
                'description': 'اكتشف مقالات تعليمية، نصائح دراسية، وأخبار المنصة.',
                'meta_title': 'المدونة | أكاديمية سنا',
                'meta_description': 'مقالات أكاديمية سنا المنشورة.',
            },
        )

        cls.education = Category.objects.create(
            name='تعليم',
            description='مقالات تعليمية عامة',
            order=1,
            is_active=True,
        )
        cls.study_tips = Category.objects.create(
            name='نصائح دراسية',
            description='نصائح للمذاكرة والاختبارات',
            order=2,
            is_active=True,
        )

        cls.author = Author.objects.create(
            name='م. فاطمة الحربي',
            title='مديرة المحتوى التعليمي',
            bio='متخصصة في تطوير المناهج والمحتوى التعليمي الرقمي.',
            initials='م. ف',
            order=1,
            is_active=True,
        )

        CTABlock.objects.update_or_create(
            slug='blog-cta',
            defaults={
                'heading': 'هل أنت مستعد للتفوق؟',
                'subheading': 'ابدأ الآن',
                'body_text': 'انضم إلى آلاف الطلاب الذين حققوا أهدافهم الدراسية مع أكاديمية سنا.',
                'primary_cta_text': 'سجّل الآن',
                'primary_cta_url': '/pricing/',
                'secondary_cta_text': 'تواصل معنا',
                'secondary_cta_url': '/contact/',
                'social_proof_text': '',
                'is_active': True,
            },
        )
        CTABlock.objects.update_or_create(
            slug='blog-post-cta',
            defaults={
                'heading': 'هل تريد تحقيق التفوق في اختبار القدرات؟',
                'subheading': 'ابدأ الآن',
                'body_text': 'انضم إلى أكاديمية سنا واحصل على أفضل التحضيرات مع معلمين متخصصين.',
                'primary_cta_text': 'سجّل الآن',
                'primary_cta_url': '/pricing/',
                'secondary_cta_text': 'احجز حصة تجريبية مجانية',
                'secondary_cta_url': '/contact/',
                'social_proof_text': '',
                'is_active': True,
            },
        )

        now = timezone.now()
        cls.featured_post = BlogPost.objects.create(
            title='٥ نصائح للتفوق في اختبار القدرات',
            excerpt='خمس نصائح عملية تساعدك على رفع درجتك في اختبار القدرات.',
            content='محتوى تفصيلي عن اختبار القدرات.\n\nنص إضافي للاختبار.',
            category=cls.study_tips,
            author=cls.author,
            icon='lightbulb',
            read_time_minutes=5,
            status=BlogPost.Status.PUBLISHED,
            is_featured=True,
            published_date=now - timedelta(days=1),
            meta_title='مقال القدرات | أكاديمية سنا',
            meta_description='تفاصيل مقال القدرات.',
        )
        cls.list_post = BlogPost.objects.create(
            title='كيف تتفوق في مادة الرياضيات',
            excerpt='استراتيجيات فعالة لتحسين مستواك في الرياضيات.',
            content='محتوى مقال الرياضيات.',
            category=cls.education,
            author=cls.author,
            icon='calculator',
            read_time_minutes=4,
            status=BlogPost.Status.PUBLISHED,
            is_featured=False,
            published_date=now - timedelta(days=2),
            meta_title='الرياضيات | أكاديمية سنا',
            meta_description='تفاصيل مقال الرياضيات.',
        )
        cls.related_post = BlogPost.objects.create(
            title='١٠ عادات للطلاب المتفوقين',
            excerpt='عادات يومية تساعد على التفوق.',
            content='محتوى مقال العادات.',
            category=cls.study_tips,
            author=cls.author,
            icon='pen',
            read_time_minutes=6,
            status=BlogPost.Status.PUBLISHED,
            is_featured=False,
            published_date=now - timedelta(days=3),
        )
        cls.draft_post = BlogPost.objects.create(
            title='مسودة غير منشورة',
            excerpt='يجب ألا تظهر هذه المسودة للعامة.',
            content='محتوى مسودة.',
            category=cls.study_tips,
            author=cls.author,
            icon='draft',
            read_time_minutes=3,
            status=BlogPost.Status.DRAFT,
            is_featured=False,
            published_date=now,
        )

    def test_blog_listing_shows_published_content_only(self):
        response = self.client.get(reverse('blogs:list'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'المدونة')
        self.assertContains(response, '٥ نصائح للتفوق في اختبار القدرات')
        self.assertContains(response, 'كيف تتفوق في مادة الرياضيات')
        self.assertNotContains(response, 'مسودة غير منشورة')

        for key in (
            'page_settings',
            'featured_post',
            'posts',
            'categories',
            'active_category_slug',
            'cta',
        ):
            self.assertIn(key, response.context)

    def test_blog_listing_filters_by_category_slug(self):
        response = self.client.get(
            reverse('blogs:list'),
            {'category': self.education.slug},
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'كيف تتفوق في مادة الرياضيات')
        self.assertNotContains(response, '١٠ عادات للطلاب المتفوقين')
        self.assertEqual(response.context['active_category_slug'], self.education.slug)

    def test_blog_detail_shows_published_post_and_related_posts(self):
        response = self.client.get(reverse('blogs:detail', args=[self.featured_post.slug]))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '٥ نصائح للتفوق في اختبار القدرات')
        self.assertContains(response, 'م. فاطمة الحربي')
        self.assertContains(response, '١٠ عادات للطلاب المتفوقين')

        for key in ('post', 'author', 'related_posts', 'cta'):
            self.assertIn(key, response.context)

    def test_blog_detail_hides_draft_posts_from_public_routes(self):
        response = self.client.get(reverse('blogs:detail', args=[self.draft_post.slug]))

        self.assertEqual(response.status_code, 404)

    def test_blog_detail_route_supports_unicode_slug(self):
        self.assertTrue(self.featured_post.slug.startswith('٥-نصائح-للتفوق-في-اختبار-القدرات'))

        response = self.client.get(reverse('blogs:detail', args=[self.featured_post.slug]))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '٥ نصائح للتفوق في اختبار القدرات')
