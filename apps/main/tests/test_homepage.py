from django.contrib.admin.sites import AdminSite
from django.test import TestCase
from django.test.utils import CaptureQueriesContext
from django.urls import reverse
from django.db import connection

from apps.main.admin import EducationalServiceAdmin, FeatureBlockAdmin, ServiceFeatureInline, FeaturePointInline, FeatureTabInline
from apps.main.models import (
    AppPromoSection,
    CTABlock,
    EducationalService,
    FAQ,
    FAQCategory,
    FeatureBlock,
    FeaturePoint,
    FeatureTab,
    FeatureTabPoint,
    HeroSection,
    ProcessStep,
    Testimonial,
    TestimonialPage,
    TrustStat,
)


class HomepageViewTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        HeroSection.objects.update_or_create(
            pk=1,
            defaults={
                'headline': 'اختبار عنوان ديناميكي للصفحة الرئيسية',
                'subheading': 'واجهة ديناميكية',
                'description': 'وصف ديناميكي لتجربة الصفحة الرئيسية.',
                'primary_cta_text': 'تصفح المسارات',
                'primary_cta_url': '/pricing/',
                'secondary_cta_text': 'تواصل معنا',
                'secondary_cta_url': '/contact/',
            },
        )
        TrustStat.objects.update_or_create(
            label='إحصائية اختبارية',
            defaults={
                'number': '+١٠٠',
                'description': 'وصف الإحصائية',
                'order': 10,
                'is_active': True,
            },
        )
        service, _ = EducationalService.objects.update_or_create(
            title='خدمة اختبارية',
            defaults={
                'description': 'وصف خدمة اختبارية',
                'cta_text': 'اعرف أكثر',
                'cta_url': '/pricing/',
                'order': 10,
                'is_active': True,
            },
        )
        service.features.update_or_create(text='ميزة مرتبطة بالخدمة', defaults={'order': 1})

        tutoring, _ = FeatureBlock.objects.update_or_create(
            slug='private-tutoring',
            defaults={
                'title': 'الدروس الخصوصية',
                'description': 'وصف مسار الدروس الخصوصية',
                'order': 1,
                'is_active': True,
            },
        )
        tutoring.points.update_or_create(text='ميزة للدروس الخصوصية', defaults={'order': 1})

        aptitude, _ = FeatureBlock.objects.update_or_create(
            slug='aptitude-tests',
            defaults={
                'title': 'القدرات والتحصيلي',
                'description': 'وصف مسار الاختبارات',
                'order': 2,
                'is_active': True,
            },
        )
        aptitude.points.update_or_create(text='ميزة عامة للاختبارات', defaults={'order': 1})
        verbal, _ = FeatureTab.objects.update_or_create(
            feature_block=aptitude,
            title='اللفظي',
            defaults={'order': 1},
        )
        FeatureTabPoint.objects.update_or_create(
            tab=verbal,
            text='نقطة داخل تبويب',
            defaults={'order': 1},
        )

        ProcessStep.objects.update_or_create(
            title='خطوة اختبارية',
            defaults={
                'step_number': 10,
                'description': 'شرح الخطوة',
                'order': 10,
                'is_active': True,
            },
        )
        AppPromoSection.objects.update_or_create(
            pk=1,
            defaults={
                'title': 'تطبيقنا معك في كل مكان',
                'subtitle': 'تجربة تطبيق ديناميكية',
                'description': 'وصف القسم التطبيقي',
                'google_play_url': 'https://play.google.com/store/apps/details?id=test',
                'app_store_url': 'https://apps.apple.com/app/test',
                'is_active': True,
            },
        )
        FAQ.objects.update_or_create(
            question='سؤال ديناميكي للاختبار؟',
            defaults={
                'answer': 'إجابة ديناميكية للاختبار.',
                'category': FAQCategory.GENERAL,
                'order': 1,
                'show_on_homepage': True,
                'is_active': True,
            },
        )
        Testimonial.objects.update_or_create(
            student_name='طالب اختباري',
            page=TestimonialPage.HOMEPAGE,
            defaults={
                'student_initials': 'ط.ا',
                'level': 'الصف الثالث الثانوي',
                'subject': 'الرياضيات',
                'rating': 5,
                'quote': 'اقتباس اختباري يظهر في الصفحة الرئيسية.',
                'order': 10,
                'is_active': True,
            },
        )
        CTABlock.objects.update_or_create(
            slug='homepage-cta',
            defaults={
                'heading': 'جاهزون لبدء رحلتك التعليمية',
                'subheading': 'CTA اختباري',
                'body_text': 'وصف CTA اختباري',
                'primary_cta_text': 'ابدأ الآن',
                'primary_cta_url': '/pricing/',
                'secondary_cta_text': 'واتساب',
                'secondary_cta_url': 'https://wa.me/966500000000',
                'social_proof_text': 'إثبات اجتماعي اختباري',
                'is_active': True,
            },
        )

    def test_homepage_renders_dynamic_sections(self):
        response = self.client.get(reverse('main:home'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'اختبار عنوان ديناميكي للصفحة الرئيسية')
        self.assertContains(response, 'إحصائية اختبارية')
        self.assertContains(response, 'خدمة اختبارية')
        self.assertContains(response, 'سؤال ديناميكي للاختبار؟')
        self.assertContains(response, 'جاهزون لبدء رحلتك التعليمية')

    def test_homepage_context_contains_expected_keys(self):
        response = self.client.get(reverse('main:home'))

        for key in (
            'hero',
            'stats',
            'services',
            'partners',
            'tutoring_block',
            'aptitude_block',
            'subjects',
            'teachers',
            'testimonials',
            'steps',
            'faqs',
            'app_promo',
            'cta',
        ):
            self.assertIn(key, response.context)

        self.assertIn('site_settings', response.context)

    def test_homepage_query_budget_stays_reasonable(self):
        with CaptureQueriesContext(connection) as queries:
            response = self.client.get(reverse('main:home'))

        self.assertEqual(response.status_code, 200)
        self.assertLessEqual(len(queries), 19)


class HomepageAdminTests(TestCase):
    def test_service_admin_exposes_feature_inline(self):
        admin_config = EducationalServiceAdmin(EducationalService, AdminSite())
        self.assertEqual(admin_config.inlines, [ServiceFeatureInline])

    def test_feature_block_admin_exposes_points_and_tabs_inlines(self):
        admin_config = FeatureBlockAdmin(FeatureBlock, AdminSite())
        self.assertEqual(admin_config.inlines, [FeaturePointInline, FeatureTabInline])
