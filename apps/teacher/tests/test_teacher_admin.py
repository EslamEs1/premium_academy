from django.contrib.admin.sites import AdminSite
from django.test import TestCase

from apps.course.models import Subject
from apps.teacher.admin import (
    TeacherAdmin,
    TeacherAvailabilityInline,
    TeacherFeatureInline,
    TeacherReviewInline,
    TeacherSpecializationInline,
)
from apps.teacher.models import Teacher


class TeacherAdminTests(TestCase):
    def test_teacher_admin_exposes_expected_inlines(self):
        admin_config = TeacherAdmin(Teacher, AdminSite())

        self.assertEqual(
            admin_config.inlines,
            [
                TeacherFeatureInline,
                TeacherSpecializationInline,
                TeacherReviewInline,
                TeacherAvailabilityInline,
            ],
        )

    def test_teacher_slug_autogenerates_from_name(self):
        subject = Subject.objects.create(
            name='اللغة العربية المتقدمة',
            description='مادة للاختبار',
            order=80,
            is_active=True,
        )

        teacher = Teacher.objects.create(
            name='أ. نورة الهاجري',
            primary_subject=subject,
            title='معلمة لغة عربية',
            short_bio='نبذة مختصرة',
            full_bio='نبذة كاملة',
            qualifications='بكالوريوس لغة عربية',
            experience_years=8,
            experience_description='متوسط وثانوي',
            rating='4.8',
            student_count=120,
            completed_sessions=640,
            platform_years=2,
            session_rate='120.00',
            is_active=True,
            order=10,
        )

        self.assertEqual(teacher.slug, 'أ-نورة-الهاجري')
