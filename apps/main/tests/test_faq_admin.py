from django.contrib.admin.sites import AdminSite
from django.test import TestCase

from apps.main.admin import FAQAdmin
from apps.main.models import FAQ, FAQCategory


class FAQAdminTests(TestCase):
    def test_faq_admin_exposes_filters_and_homepage_toggle(self):
        admin_config = FAQAdmin(FAQ, AdminSite())

        self.assertEqual(
            admin_config.list_display,
            ('question_preview', 'category', 'is_active', 'show_on_homepage', 'order'),
        )
        self.assertEqual(admin_config.list_filter, ('category', 'is_active', 'show_on_homepage'))
        self.assertEqual(admin_config.list_editable, ('is_active', 'show_on_homepage', 'order'))

    def test_question_preview_truncates_question(self):
        admin_config = FAQAdmin(FAQ, AdminSite())
        faq = FAQ(
            question='هذا سؤال طويل جدًا لغرض اختبار معاينة السؤال في شاشة الإدارة حتى نتأكد من أن النص لا يتجاوز الحد المتوقع',
            answer='إجابة اختبارية',
            category=FAQCategory.GENERAL,
        )

        self.assertEqual(
            admin_config.question_preview(faq),
            'هذا سؤال طويل جدًا لغرض اختبار معاينة السؤال في شاشة الإدارة',
        )

    def test_show_on_homepage_defaults_to_false(self):
        faq = FAQ.objects.create(
            question='سؤال جديد لا يظهر في الصفحة الرئيسية؟',
            answer='نعم، القيمة الافتراضية معطلة حتى يفعّلها المشرف.',
            category=FAQCategory.GENERAL,
            order=1,
            is_active=True,
        )

        self.assertFalse(faq.show_on_homepage)
