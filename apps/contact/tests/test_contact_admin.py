from django.contrib.admin.sites import AdminSite
from django.test import TestCase

from apps.contact.admin import ContactSubmissionAdmin
from apps.contact.models import ContactSubmission


class ContactAdminTests(TestCase):
    def test_contact_submission_admin_is_read_only_except_read_status(self):
        admin_config = ContactSubmissionAdmin(ContactSubmission, AdminSite())

        self.assertIn('full_name', admin_config.readonly_fields)
        self.assertIn('email', admin_config.readonly_fields)
        self.assertIn('phone', admin_config.readonly_fields)
        self.assertIn('subject', admin_config.readonly_fields)
        self.assertIn('message', admin_config.readonly_fields)
        self.assertIn('created_at', admin_config.readonly_fields)
        self.assertEqual(admin_config.list_editable, ('is_read',))

    def test_new_submission_defaults_to_unread(self):
        submission = ContactSubmission.objects.create(
            full_name='سارة محمد',
            email='sara@example.com',
            phone='512345678',
            subject=ContactSubmission.Subject.BOOKING,
            message='أرغب في حجز حصة تجريبية مع أحد المعلمين.',
        )

        self.assertFalse(submission.is_read)
