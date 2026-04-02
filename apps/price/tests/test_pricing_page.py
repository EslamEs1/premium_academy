from decimal import Decimal

from django.test import TestCase
from django.urls import reverse

from apps.main.models import CTABlock, Testimonial, TestimonialPage
from apps.price.models import ComparisonFeature, PlanFeature, PricingFAQ, PricingPageSettings, PricingPlan


class PricingPageTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        PricingPageSettings.objects.update_or_create(
            pk=1,
            defaults={
                'title': 'خطط مرنة تناسب احتياجاتك',
                'subtitle': 'الأسعار والباقات',
                'description': 'اختر الخطة المناسبة لتحقيق أهدافك التعليمية.',
                'meta_title': 'الأسعار | أكاديمية سنا',
                'meta_description': 'صفحة الأسعار والباقات في أكاديمية سنا.',
            },
        )

        cls.basic = PricingPlan.objects.create(
            name='الباقة الأساسية',
            description='مثالية للطلاب الذين يحتاجون دعمًا دوريًا',
            price=Decimal('150.00'),
            billing_period='ر.س / الحصة',
            cta_text='ابدأ الآن',
            cta_url='/contact/',
            is_popular=False,
            is_active=True,
            order=1,
        )
        cls.premium = PricingPlan.objects.create(
            name='الباقة المميزة',
            description='الخيار الأمثل لتحقيق نتائج ملموسة',
            price=Decimal('180.00'),
            billing_period='ر.س / الحصة',
            cta_text='ابدأ الآن',
            cta_url='/contact/',
            is_popular=True,
            is_active=True,
            order=2,
        )
        cls.professional = PricingPlan.objects.create(
            name='الباقة الاحترافية',
            description='للطلاب الذين يهدفون للتفوق المطلق',
            price=Decimal('300.00'),
            billing_period='ر.س / الحصة',
            cta_text='ابدأ الآن',
            cta_url='/contact/',
            is_popular=False,
            is_active=True,
            order=3,
        )

        for order, text in enumerate(
            [
                'حصة خاصة مباشرة ٦٠ دقيقة',
                'معلم متخصص معتمد',
                'تسجيل الحصة للمراجعة',
            ],
            start=1,
        ):
            PlanFeature.objects.create(
                plan=cls.basic,
                text=text,
                is_included=True,
                order=order,
            )
        PlanFeature.objects.create(
            plan=cls.basic,
            text='تقارير مفصلة',
            is_included=False,
            order=4,
        )

        ComparisonFeature.objects.create(
            label='مدة الحصة',
            basic_value='٦٠ دقيقة',
            premium_value='٦٠ دقيقة',
            professional_value='٧٥ دقيقة',
            order=1,
            is_active=True,
        )
        ComparisonFeature.objects.create(
            label='تقارير المتابعة',
            basic_value='—',
            premium_value='أسبوعية',
            professional_value='يومية',
            order=2,
            is_active=True,
        )

        PricingFAQ.objects.create(
            question='ما هي طرق الدفع المتاحة؟',
            answer='نقبل بطاقات الدفع والتحويل البنكي وApple Pay.',
            order=1,
            is_active=True,
        )

        Testimonial.objects.update_or_create(
            student_name='سارة المطيري',
            page=TestimonialPage.PRICING,
            defaults={
                'student_initials': 'سم',
                'level': 'ثاني ثانوي',
                'subject': 'رياضيات',
                'rating': 5,
                'quote': 'الاستثمار في الباقة المميزة كان أفضل قرار.',
                'order': 1,
                'is_active': True,
            },
        )

        CTABlock.objects.update_or_create(
            slug='pricing-cta',
            defaults={
                'heading': 'جاهز للبدء؟ احجز حصتك التجريبية المجانية',
                'subheading': 'ابدأ الآن',
                'body_text': 'جرب المنصة والمعلم قبل الالتزام.',
                'primary_cta_text': 'احجز حصة تجريبية',
                'primary_cta_url': '/contact/',
                'secondary_cta_text': 'تواصل عبر الواتساب',
                'secondary_cta_url': 'https://wa.me/966500000000',
                'social_proof_text': 'انضم إلى أكثر من ١٠,٠٠٠ طالب يتعلمون معنا',
                'is_active': True,
            },
        )

    def test_pricing_page_renders_dynamic_sections(self):
        response = self.client.get(reverse('price:pricing'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'خطط مرنة تناسب احتياجاتك')
        self.assertContains(response, 'الباقة المميزة')
        self.assertContains(response, '180')
        self.assertContains(response, 'مدة الحصة')
        self.assertContains(response, 'ما هي طرق الدفع المتاحة؟')
        self.assertContains(response, 'جاهز للبدء؟ احجز حصتك التجريبية المجانية')

        for key in (
            'page_settings',
            'plans',
            'comparison_features',
            'pricing_faqs',
            'testimonials',
            'cta',
        ):
            self.assertIn(key, response.context)

    def test_pricing_page_shows_popular_plan_and_comparison_values(self):
        response = self.client.get(reverse('price:pricing'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'الأكثر طلبًا')
        self.assertContains(response, 'أسبوعية')
        self.assertContains(response, 'يومية')

