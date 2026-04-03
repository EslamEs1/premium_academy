from django.contrib.admin.sites import AdminSite
from django.test import TestCase

from apps.course.admin import SubjectAdmin
from apps.course.models import Subject


class SubjectModelTests(TestCase):
    def test_slug_autogenerates_from_name(self):
        subject = Subject.objects.create(name='الاقتصاد')
        self.assertEqual(subject.slug, 'الاقتصاد')

    def test_subjects_are_ordered_by_order_then_name(self):
        second = Subject.objects.create(name='Biology', order=2)
        first = Subject.objects.create(name='Math', order=1)

        subjects = list(Subject.objects.filter(name__in=['Math', 'Biology']))
        self.assertEqual(subjects, [first, second])


class SubjectAdminTests(TestCase):
    def test_admin_config_exposes_expected_list_display(self):
        admin_config = SubjectAdmin(Subject, AdminSite())
        self.assertEqual(admin_config.list_display, ('name', 'slug', 'order', 'is_active'))
