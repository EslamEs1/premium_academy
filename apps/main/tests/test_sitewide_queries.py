from django.db import connection
from django.test import TestCase
from django.test.utils import CaptureQueriesContext
from django.urls import reverse


class SitewideQueryTests(TestCase):
    def test_key_pages_include_shared_site_settings_context(self):
        for route_name in ('main:home', 'main:faq', 'main:privacy', 'main:terms'):
            with self.subTest(route_name=route_name):
                response = self.client.get(reverse(route_name))
                self.assertEqual(response.status_code, 200)
                self.assertIn('site_settings', response.context)
                self.assertTrue(response.context['site_settings'].site_name)

    def test_query_budget_for_sitewide_pages_stays_reasonable(self):
        budgets = {
            'main:home': 20,
            'main:faq': 8,
            'main:privacy': 5,
            'main:terms': 5,
        }

        for route_name, max_queries in budgets.items():
            with self.subTest(route_name=route_name):
                with CaptureQueriesContext(connection) as queries:
                    response = self.client.get(reverse(route_name))

                self.assertEqual(response.status_code, 200)
                self.assertLessEqual(len(queries), max_queries)

    def test_legal_pages_render_dynamic_legal_content(self):
        privacy_response = self.client.get(reverse('main:privacy'))
        terms_response = self.client.get(reverse('main:terms'))

        self.assertContains(privacy_response, 'سياسة الخصوصية')
        self.assertContains(privacy_response, 'البيانات التي نجمعها')
        self.assertContains(terms_response, 'الشروط والأحكام')
        self.assertContains(terms_response, 'نطاق الاستخدام')
