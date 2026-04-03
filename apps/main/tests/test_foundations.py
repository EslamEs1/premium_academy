from django.contrib.admin.sites import AdminSite
from django.contrib.auth import get_user_model
from django.test import RequestFactory, TestCase

from apps.main.admin import SiteSettingsAdmin
from apps.main.context_processors import get_active_ordered_queryset, site_settings
from apps.main.models import Partner, SiteSettings, SocialLink, SocialLinkPlatform


class SingletonAdminMixinTests(TestCase):
    def setUp(self):
        self.admin = SiteSettingsAdmin(SiteSettings, AdminSite())
        self.request = RequestFactory().get('/admin/main/sitesettings/')
        self.request.user = get_user_model().objects.create_superuser(
            username='admin',
            email='admin@example.com',
            password='password123',
        )

    def test_has_add_permission_when_no_instance_exists(self):
        SiteSettings.objects.all().delete()
        self.assertTrue(self.admin.has_add_permission(self.request))

    def test_has_add_permission_returns_false_once_instance_exists(self):
        site = SiteSettings.objects.first()
        if site is None:
            SiteSettings.objects.create(site_name='Sana Academy')
        self.assertFalse(self.admin.has_add_permission(self.request))


class SiteSettingsContextProcessorTests(TestCase):
    def test_site_settings_returns_singleton_with_prefetched_social_links(self):
        site = SiteSettings.objects.first()
        self.assertIsNotNone(site)
        site.social_links.all().delete()
        SocialLink.objects.create(
            site_settings=site,
            platform=SocialLinkPlatform.WHATSAPP,
            url='https://wa.me/966500000000',
            order=2,
        )
        SocialLink.objects.create(
            site_settings=site,
            platform=SocialLinkPlatform.INSTAGRAM,
            url='https://instagram.com/sanaacademy',
            order=1,
        )

        context = site_settings(RequestFactory().get('/'))
        self.assertEqual(context['site_settings'].pk, site.pk)
        self.assertEqual(
            list(context['site_settings'].social_links.values_list('platform', flat=True)),
            [SocialLinkPlatform.INSTAGRAM, SocialLinkPlatform.WHATSAPP],
        )


class ActiveOrderedQuerysetTests(TestCase):
    def test_get_active_ordered_queryset_filters_and_orders_records(self):
        Partner.objects.create(name='Inactive', logo='partners/inactive.png', order=0, is_active=False)
        second = Partner.objects.create(name='Second', logo='partners/second.png', order=2, is_active=True)
        first = Partner.objects.create(name='First', logo='partners/first.png', order=1, is_active=True)

        partners = list(
            get_active_ordered_queryset(
                Partner,
                filters={'name__in': ['First', 'Second', 'Inactive']},
            )
        )

        self.assertEqual(partners, [first, second])
