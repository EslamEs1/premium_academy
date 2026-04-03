from django.test import TestCase
from django.urls import reverse

from apps.main.models import FAQ, FAQCategory, PageMeta, RelatedLink


class FAQPageTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        PageMeta.objects.update_or_create(
            slug='faq',
            defaults={
                'meta_title': 'الأسئلة الشائعة | أكاديمية سنا',
                'meta_description': 'إجابات شاملة على الأسئلة الأكثر شيوعًا حول خدمات أكاديمية سنا.',
                'is_active': True,
            },
        )
        RelatedLink.objects.update_or_create(
            title='كيف نعمل',
            defaults={
                'description': 'تعرف على خطوات البدء وكيف نضمن تجربة تعليمية متميزة من أول حصة.',
                'url': '/how-it-works/',
                'order': 1,
                'is_active': True,
            },
        )
        RelatedLink.objects.update_or_create(
            title='الأسعار والباقات',
            defaults={
                'description': 'اطلع على خططنا المرنة واختر الباقة المناسبة لميزانيتك واحتياجاتك.',
                'url': '/pricing/',
                'order': 2,
                'is_active': True,
            },
        )
        RelatedLink.objects.update_or_create(
            title='تواصل معنا',
            defaults={
                'description': 'فريقنا متاح للرد على استفساراتك ومساعدتك في بدء رحلتك التعليمية.',
                'url': '/contact/',
                'order': 3,
                'is_active': True,
            },
        )
        FAQ.objects.update_or_create(
            question='كيف أبدأ التسجيل في أكاديمية سنا؟',
            defaults={
                'answer': 'ابدأ باختيار المسار المناسب أو تواصل معنا مباشرة عبر واتساب.',
                'category': FAQCategory.GENERAL,
                'order': 1,
                'is_active': True,
                'show_on_homepage': True,
            },
        )
        FAQ.objects.update_or_create(
            question='ما هي أسعار الحصص الخصوصية؟',
            defaults={
                'answer': 'تتراوح الأسعار حسب الباقة وخبرة المعلم.',
                'category': FAQCategory.PRICING,
                'order': 2,
                'is_active': True,
                'show_on_homepage': False,
            },
        )
        FAQ.objects.update_or_create(
            question='كيف أختار المعلم المناسب؟',
            defaults={
                'answer': 'راجع ملفات المعلمين والخبرات والتقييمات المتاحة في المنصة.',
                'category': FAQCategory.TEACHERS,
                'order': 3,
                'is_active': True,
                'show_on_homepage': False,
            },
        )

    def test_faq_page_renders_dynamic_content_and_context(self):
        response = self.client.get(reverse('main:faq'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'كل ما تحتاج معرفته قبل البدء')
        self.assertContains(response, 'كيف أبدأ التسجيل في أكاديمية سنا؟')
        self.assertContains(response, 'الأسعار والباقات')

        for key in ('page_meta', 'faqs', 'faq_categories', 'related_links'):
            self.assertIn(key, response.context)

    def test_faq_page_exposes_category_grouping_from_choices(self):
        response = self.client.get(reverse('main:faq'))

        category_values = [category['value'] for category in response.context['faq_categories']]
        category_labels = [category['label'] for category in response.context['faq_categories']]

        self.assertEqual(
            category_values,
            ['general', 'pricing', 'teachers', 'scheduling', 'platform'],
        )
        self.assertIn('عام', category_labels)
        self.assertIn('الأسعار', category_labels)
        self.assertIn('المعلمون', category_labels)

    def test_homepage_only_shows_faqs_marked_for_homepage(self):
        response = self.client.get(reverse('main:home'))

        self.assertContains(response, 'كيف أبدأ التسجيل في أكاديمية سنا؟')
        self.assertNotContains(response, 'ما هي أسعار الحصص الخصوصية؟')

