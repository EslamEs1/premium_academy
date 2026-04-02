from decimal import Decimal

from django.contrib.admin.sites import AdminSite
from django.core.exceptions import ValidationError
from django.test import TestCase

from apps.price.admin import PlanFeatureInline, PricingPlanAdmin
from apps.price.models import PricingPlan


class PricingAdminTests(TestCase):
    def test_pricing_plan_admin_exposes_feature_inline(self):
        admin_config = PricingPlanAdmin(PricingPlan, AdminSite())
        self.assertEqual(admin_config.inlines, [PlanFeatureInline])

    def test_pricing_plan_rejects_negative_price(self):
        plan = PricingPlan(
            name='خطة غير صالحة',
            price=Decimal('-1.00'),
            billing_period='ر.س / الحصة',
            description='وصف',
            cta_text='ابدأ الآن',
            cta_url='/contact/',
            is_active=True,
            order=1,
        )

        with self.assertRaises(ValidationError):
            plan.full_clean()
