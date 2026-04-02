from datetime import date, time

from django.test import TestCase
from django.urls import reverse

from apps.course.models import Subject
from apps.main.models import CTABlock, Testimonial, TestimonialPage
from apps.teacher.models import (
    Teacher,
    TeacherAvailability,
    TeacherFeature,
    TeacherPageSettings,
    TeacherReview,
    TeacherSpecialization,
    TeacherStat,
)


class TeacherPagesTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.math = Subject.objects.create(
            name='الرياضيات المتقدمة',
            description='وصف لمادة الرياضيات',
            order=50,
            is_active=True,
        )
        cls.physics = Subject.objects.create(
            name='الفيزياء التطبيقية',
            description='وصف لمادة الفيزياء',
            order=51,
            is_active=True,
        )

        TeacherPageSettings.objects.update_or_create(
            pk=1,
            defaults={
                'hero_title': 'معلمون بخبرة واضحة ونتائج قابلة للقياس',
                'hero_subtitle': 'صفحة المعلمين أصبحت ديناميكية بالكامل.',
                'meta_title': 'المعلمون | أكاديمية سنا',
                'meta_description': 'قائمة المعلمين المحدثة من لوحة التحكم.',
            },
        )

        TeacherStat.objects.update_or_create(
            label='معلمون معتمدون',
            defaults={
                'number': '+٥٠٠',
                'description': 'متخصصون في جميع المواد',
                'order': 1,
                'is_active': True,
            },
        )

        Testimonial.objects.update_or_create(
            student_name='طالب صفحة المعلمين',
            page=TestimonialPage.TEACHERS,
            defaults={
                'student_initials': 'ط.م',
                'level': 'ثالث ثانوي',
                'subject': 'الرياضيات',
                'rating': 5,
                'quote': 'تجربة ممتازة مع أحد المعلمين.',
                'order': 1,
                'is_active': True,
            },
        )

        CTABlock.objects.update_or_create(
            slug='teachers-cta',
            defaults={
                'heading': 'اختر معلمك وابدأ رحلة التفوق',
                'subheading': 'دعوة إجراء لصفحة المعلمين',
                'body_text': 'نص CTA اختباري لصفحة المعلمين.',
                'primary_cta_text': 'سجل الآن',
                'primary_cta_url': '/pricing/',
                'secondary_cta_text': 'واتساب',
                'secondary_cta_url': 'https://wa.me/966500000000',
                'social_proof_text': 'أكثر من ١٠,٠٠٠ طالب يتعلمون معنا',
                'is_active': True,
            },
        )
        CTABlock.objects.update_or_create(
            slug='teacher-profile-cta',
            defaults={
                'heading': 'ابدأ رحلتك التعليمية مع معلم متخصص',
                'subheading': 'دعوة إجراء لملف المعلم',
                'body_text': 'نص CTA اختباري لملف المعلم.',
                'primary_cta_text': 'احجز حصتك الأولى',
                'primary_cta_url': '/contact/',
                'secondary_cta_text': 'تواصل عبر الواتساب',
                'secondary_cta_url': 'https://wa.me/966500000000',
                'social_proof_text': 'حصة تجريبية متاحة',
                'is_active': True,
            },
        )

        cls.teacher = Teacher.objects.create(
            name='أ. ليلى السبيعي',
            primary_subject=cls.math,
            title='معلمة رياضيات متخصصة',
            short_bio='خبرة تعليمية ممتدة مع نتائج واضحة.',
            full_bio='فقرة أولى عن أسلوب التدريس.\n\nفقرة ثانية عن المنهجية والمتابعة.',
            qualifications='بكالوريوس رياضيات\nماجستير مناهج وطرق تدريس',
            experience_years=9,
            experience_description='متوسط وثانوي',
            rating='4.9',
            student_count=230,
            completed_sessions=1500,
            platform_years=3,
            session_rate='150.00',
            whatsapp_number='966500000000',
            is_active=True,
            is_featured=True,
            order=1,
            meta_title='ليلى السبيعي | أكاديمية سنا',
            meta_description='ملف المعلمة ليلى السبيعي',
        )
        TeacherFeature.objects.create(
            teacher=cls.teacher,
            text='حصص مسجلة متاحة',
            order=1,
            is_active=True,
        )
        TeacherFeature.objects.create(
            teacher=cls.teacher,
            text='تقارير أسبوعية',
            order=2,
            is_active=True,
        )
        TeacherSpecialization.objects.create(
            teacher=cls.teacher,
            subject=cls.math,
            label='الرياضيات',
            grade_level='متوسط',
            order=1,
            is_active=True,
        )
        TeacherSpecialization.objects.create(
            teacher=cls.teacher,
            subject=cls.physics,
            label='الفيزياء',
            grade_level='ثانوي',
            order=2,
            is_active=True,
        )
        TeacherReview.objects.create(
            teacher=cls.teacher,
            student_name='سارة المطيري',
            student_initials='سم',
            level='ثاني ثانوي',
            subject='الرياضيات',
            rating=5,
            quote='شرح واضح وخطة متابعة ممتازة.',
            review_date=date(2026, 3, 15),
            order=1,
            is_active=True,
        )
        TeacherAvailability.objects.create(
            teacher=cls.teacher,
            day_of_week='السبت',
            start_time=time(16, 0),
            end_time=time(22, 0),
            note='متاح للحجز المباشر',
            order=1,
            is_active=True,
        )

        cls.similar_teacher = Teacher.objects.create(
            name='أ. مريم القحطاني',
            primary_subject=cls.physics,
            title='معلمة فيزياء للمرحلة الثانوية',
            short_bio='معلمة ثانية لكتلة المعلمين المشابهين.',
            full_bio='نبذة قصيرة عن المعلمة الثانية.',
            qualifications='بكالوريوس رياضيات',
            experience_years=7,
            experience_description='ثانوي',
            rating='4.8',
            student_count=180,
            completed_sessions=940,
            platform_years=2,
            session_rate='135.00',
            is_active=True,
            is_featured=False,
            order=2,
        )

    def test_teacher_listing_renders_dynamic_content(self):
        response = self.client.get(reverse('teacher:list'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'معلمون بخبرة واضحة ونتائج قابلة للقياس')
        self.assertContains(response, 'أ. ليلى السبيعي')
        self.assertContains(response, 'اختر معلمك وابدأ رحلة التفوق')

        for key in (
            'page_settings',
            'subjects',
            'teachers',
            'stats',
            'testimonials',
            'cta',
            'active_subject_slug',
        ):
            self.assertIn(key, response.context)

    def test_teacher_listing_filters_by_subject_slug(self):
        response = self.client.get(
            reverse('teacher:list'),
            {'subject': self.math.slug},
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'أ. ليلى السبيعي')
        self.assertNotContains(response, 'أ. مريم القحطاني')
        self.assertEqual(response.context['active_subject_slug'], self.math.slug)

    def test_teacher_detail_renders_all_dynamic_sections(self):
        response = self.client.get(reverse('teacher:detail', args=[self.teacher.slug]))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'أ. ليلى السبيعي')
        self.assertContains(response, 'حصص مسجلة متاحة')
        self.assertContains(response, 'سارة المطيري')
        self.assertContains(response, 'السبت')
        self.assertContains(response, 'أ. مريم القحطاني')

        for key in (
            'teacher',
            'features',
            'specializations',
            'reviews',
            'availability',
            'similar_teachers',
            'cta',
        ):
            self.assertIn(key, response.context)

    def test_featured_teacher_appears_on_homepage_showcase(self):
        response = self.client.get(reverse('main:home'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'أ. ليلى السبيعي')

    def test_teacher_detail_route_supports_unicode_slug(self):
        self.assertEqual(self.teacher.slug, 'أ-ليلى-السبيعي')

        response = self.client.get(reverse('teacher:detail', args=[self.teacher.slug]))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'أ. ليلى السبيعي')
