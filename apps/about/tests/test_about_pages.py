from django.test import TestCase
from django.urls import reverse

from apps.about.models import (
    Achievement,
    ContentBlock,
    HowItWorksStep,
    PageContent,
    ParentFeature,
    Statistic,
    TeamMember,
    WhyUsFeature,
)
from apps.main.models import CTABlock, Partner, SiteSettings, Testimonial, TestimonialPage


class AboutPageTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        SiteSettings.objects.update_or_create(
            pk=1,
            defaults={
                'site_name': 'أكاديمية سنا',
                'accreditation_text': 'منصة معتمدة من الجهات التعليمية المختصة.',
            },
        )
        PageContent.objects.update_or_create(
            slug='about',
            defaults={
                'title': 'من نحن',
                'subtitle': 'نبني تجربة تعليمية موثوقة تجمع بين الجودة والمرونة والثقة.',
                'badge_text': 'منصة تعليمية سعودية',
                'meta_title': 'من نحن | أكاديمية سنا',
                'meta_description': 'تعرف على أكاديمية سنا وفريقها ورسالتها.',
            },
        )
        PageContent.objects.update_or_create(
            slug='how-it-works',
            defaults={
                'title': 'ابدأ رحلتك التعليمية في خطوات بسيطة',
                'subtitle': 'من اختيار المادة إلى تحقيق التفوق، نوفر لك تجربة تعليمية متكاملة وواضحة.',
                'badge_text': 'كيف نعمل',
                'primary_cta_text': 'ابدأ الآن',
                'primary_cta_url': '/pricing/',
                'secondary_cta_text': 'تواصل معنا',
                'secondary_cta_url': '/contact/',
                'meta_title': 'كيف يعمل الموقع | أكاديمية سنا',
                'meta_description': 'تعرف على خطوات الدراسة في أكاديمية سنا.',
            },
        )
        for order, (slug, title, content) in enumerate(
            [
                ('mission', 'رسالتنا', 'تمكين كل طالب من الوصول إلى تعليم عالي الجودة.\n\nنوفر تجربة مرنة تناسب احتياجات كل أسرة.'),
                ('vision', 'رؤيتنا', 'أن نكون المنصة التعليمية الأولى في المنطقة العربية.\n\nنكون شريكًا موثوقًا في رحلة التفوق الدراسي.'),
                ('our-story', 'قصتنا', 'بدأت أكاديمية سنا في عام ٢٠٢١ برؤية بسيطة.\n\nتخدم اليوم آلاف الطلاب في مختلف المدن السعودية.'),
            ],
            start=1,
        ):
            ContentBlock.objects.update_or_create(
                slug=slug,
                defaults={
                    'title': title,
                    'content': content,
                    'order': order,
                    'is_active': True,
                },
            )
        Statistic.objects.update_or_create(
            label='سنة التأسيس',
            defaults={'number': '٢٠٢١', 'icon': 'calendar', 'order': 1, 'is_active': True},
        )
        Statistic.objects.update_or_create(
            label='معلم معتمد',
            defaults={'number': '+٥٠٠', 'icon': 'user', 'order': 2, 'is_active': True},
        )
        TeamMember.objects.update_or_create(
            name='د. أحمد الفهد',
            defaults={
                'title': 'المدير التنفيذي',
                'description': 'خبرة ١٥ عامًا في قطاع التعليم.',
                'order': 1,
                'is_active': True,
            },
        )
        TeamMember.objects.update_or_create(
            name='م. فاطمة الحربي',
            defaults={
                'title': 'مديرة المحتوى التعليمي',
                'description': 'متخصصة في تطوير المناهج الدراسية.',
                'order': 2,
                'is_active': True,
            },
        )
        Achievement.objects.update_or_create(
            label='طالب مسجل',
            defaults={'number': '+١٠,٠٠٠', 'icon': 'graduation-cap', 'order': 1, 'is_active': True},
        )
        Achievement.objects.update_or_create(
            label='نسبة الرضا',
            defaults={'number': '٩٨٪', 'icon': 'star-filled', 'order': 2, 'is_active': True},
        )
        Partner.objects.update_or_create(name='جامعة الملك سعود', defaults={'order': 1, 'is_active': True})
        Partner.objects.update_or_create(name='وزارة التعليم', defaults={'order': 2, 'is_active': True})
        CTABlock.objects.update_or_create(
            slug='about-cta',
            defaults={
                'heading': 'انضم إلى عائلة أكاديمية سنا',
                'body_text': 'سواء كنت طالبًا يسعى للتفوق أو معلمًا يبحث عن منصة موثوقة.',
                'primary_cta_text': 'سجّل الآن',
                'primary_cta_url': '/pricing/',
                'secondary_cta_text': 'تواصل معنا',
                'secondary_cta_url': '/contact/',
                'social_proof_text': 'انضم إلى أكثر من ١٠,٠٠٠ طالب حققوا أهدافهم الدراسية معنا',
                'is_active': True,
            },
        )
        for index, title in enumerate(
            [
                'اختر المادة والمرحلة',
                'تصفح المعلمين واختر الأنسب',
                'حدد الموعد المناسب',
                'احضر الحصة أونلاين',
                'تابع تقدمك مع التقارير',
                'حقق التفوق الدراسي',
            ],
            start=1,
        ):
            HowItWorksStep.objects.update_or_create(
                step_number=index,
                defaults={
                    'title': title,
                    'description': 'وصف الخطوة',
                    'icon': 'checkmark-circle',
                    'order': index,
                    'is_active': True,
                },
            )
        WhyUsFeature.objects.update_or_create(
            title='معلمون معتمدون',
            defaults={
                'description': 'نخبة من المعلمين الحاصلين على أعلى الشهادات.',
                'icon': 'graduation-cap',
                'order': 1,
                'is_active': True,
            },
        )
        ParentFeature.objects.update_or_create(
            title='تقارير أسبوعية مفصلة',
            feature_type=ParentFeature.FeatureType.CORE,
            defaults={
                'description': 'استلم تقريرًا عن كل حصة يشمل ما تم إنجازه ونقاط التحسين.',
                'icon': 'checkmark-circle',
                'order': 1,
                'is_active': True,
            },
        )
        ParentFeature.objects.update_or_create(
            title='إشعارات فورية',
            feature_type=ParentFeature.FeatureType.CAPABILITY,
            defaults={
                'description': 'تنبيهات عند انتهاء الحصة وبدء الواجب.',
                'icon': 'bell',
                'order': 2,
                'is_active': True,
            },
        )
        Testimonial.objects.update_or_create(
            student_name='سارة المطيري',
            page=TestimonialPage.HOW_IT_WORKS,
            defaults={
                'student_initials': 'سم',
                'level': 'ثاني ثانوي',
                'subject': 'رياضيات',
                'rating': 5,
                'quote': 'أصبحت أتعامل مع الأسئلة بثقة أكبر في الاختبارات.',
                'order': 1,
                'is_active': True,
            },
        )
        CTABlock.objects.update_or_create(
            slug='how-it-works-cta',
            defaults={
                'heading': 'جاهز للبدء؟ احجز حصتك الأولى',
                'subheading': 'ابدأ الآن',
                'body_text': 'انضم إلى آلاف الطلاب الذين يحققون نتائج ملموسة معنا.',
                'primary_cta_text': 'سجّل الآن',
                'primary_cta_url': '/pricing/',
                'secondary_cta_text': 'تواصل عبر الواتساب',
                'secondary_cta_url': 'https://wa.me/966500000000',
                'social_proof_text': 'حصة تجريبية مجانية - بدون التزام',
                'is_active': True,
            },
        )

    def test_about_page_renders_dynamic_content_and_context(self):
        response = self.client.get(reverse('about:about'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'من نحن')
        self.assertContains(response, 'د. أحمد الفهد')
        self.assertContains(response, 'جامعة الملك سعود')
        self.assertContains(response, 'انضم إلى عائلة أكاديمية سنا')

        for key in ('page', 'blocks', 'statistics', 'team_members', 'achievements', 'partners', 'cta'):
            self.assertIn(key, response.context)

    def test_how_it_works_page_shows_new_steps_in_order(self):
        HowItWorksStep.objects.create(
            step_number=7,
            title='راجع النتائج وخطة الاستمرار',
            description='اختتم رحلتك بخطة متابعة واضحة.',
            icon='chart-up',
            order=7,
            is_active=True,
        )

        response = self.client.get(reverse('about:how_it_works'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'راجع النتائج وخطة الاستمرار')
        self.assertContains(response, 'إشعارات فورية')

        rendered_steps = [step.title for step in response.context['steps']]
        self.assertEqual(rendered_steps[-1], 'راجع النتائج وخطة الاستمرار')
        self.assertEqual(len(rendered_steps), 7)
