from django.contrib.messages import get_messages
from django.test import TestCase
from django.urls import reverse

from apps.contact.models import ContactFAQ, ContactPageSettings, ContactSubmission, OperatingHours, WhyChoosePoint
from apps.main.models import CTABlock, SiteSettings


class ContactPageTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        SiteSettings.objects.update_or_create(
            pk=1,
            defaults={
                'site_name': 'أكاديمية سنا',
                'phone': '+966 11 400 0000',
                'email': 'info@premiumacademy.sa',
                'whatsapp': '966500000000',
                'address': 'الرياض، المملكة العربية السعودية',
                'google_maps_url': 'https://maps.google.com',
            },
        )
        ContactPageSettings.objects.update_or_create(
            pk=1,
            defaults={
                'hero_title': 'تواصل معنا',
                'hero_subtitle': 'نسعد بتواصلك معنا. فريقنا جاهز للإجابة على استفساراتك.',
                'meta_title': 'تواصل معنا | أكاديمية سنا',
                'meta_description': 'نموذج التواصل ومعلومات الاتصال في أكاديمية سنا.',
            },
        )
        WhyChoosePoint.objects.create(
            text='معلمون معتمدون بخبرة تزيد عن ٥ سنوات',
            order=1,
            is_active=True,
        )
        OperatingHours.objects.create(
            day_label='السبت – الخميس',
            time_range='٨ صباحًا – ١٠ مساءً',
            note='يمكن حجز الحصص في أي وقت من خلال المنصة.',
            order=1,
            is_active=True,
        )
        ContactFAQ.objects.create(
            question='كيف أتواصل بسرعة؟',
            answer='أسرع طريقة للتواصل هي عبر واتساب.',
            order=1,
            is_active=True,
        )
        CTABlock.objects.update_or_create(
            slug='contact-cta',
            defaults={
                'heading': 'ابدأ رحلتك التعليمية الآن',
                'subheading': 'تواصل معنا',
                'body_text': 'فريقنا جاهز لمساعدتك في اختيار المسار المناسب.',
                'primary_cta_text': 'احجز حصة تجريبية',
                'primary_cta_url': '/contact/',
                'secondary_cta_text': 'واتساب',
                'secondary_cta_url': 'https://wa.me/966500000000',
                'social_proof_text': 'رد سريع خلال ساعات العمل',
                'is_active': True,
            },
        )

    def test_contact_page_renders_dynamic_sections_and_context(self):
        response = self.client.get(reverse('contact:contact'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'تواصل معنا')
        self.assertContains(response, 'معلمون معتمدون بخبرة تزيد عن ٥ سنوات')
        self.assertContains(response, 'كيف أتواصل بسرعة؟')
        self.assertContains(response, 'الرياض، المملكة العربية السعودية')

        for key in (
            'page_settings',
            'form',
            'why_choose_points',
            'operating_hours',
            'contact_faqs',
            'site_contact',
            'cta',
        ):
            self.assertIn(key, response.context)

    def test_valid_contact_submission_is_saved_and_shows_success_message(self):
        response = self.client.post(
            reverse('contact:contact'),
            data={
                'full_name': 'محمد الأحمد',
                'email': 'mohamed@example.com',
                'phone': '512345678',
                'subject': ContactSubmission.Subject.INQUIRY,
                'message': 'أرغب في معرفة تفاصيل الحصة التجريبية المتاحة.',
            },
            follow=True,
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(ContactSubmission.objects.count(), 1)
        submission = ContactSubmission.objects.get()
        self.assertEqual(submission.full_name, 'محمد الأحمد')
        self.assertFalse(submission.is_read)
        messages = [message.message for message in get_messages(response.wsgi_request)]
        self.assertTrue(any('تم إرسال رسالتك بنجاح' in message for message in messages))

    def test_invalid_email_is_rejected_without_saving(self):
        response = self.client.post(
            reverse('contact:contact'),
            data={
                'full_name': 'محمد الأحمد',
                'email': 'not-an-email',
                'phone': '512345678',
                'subject': ContactSubmission.Subject.INQUIRY,
                'message': 'هذه رسالة كافية الطول لتجاوز شرط الحد الأدنى.',
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(ContactSubmission.objects.count(), 0)
        self.assertFormError(response.context['form'], 'email', 'أدخل بريدًا إلكترونيًا صالحًا.')

