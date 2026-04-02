from django.contrib.admin.sites import AdminSite
from django.test import TestCase

from apps.about.admin import AchievementAdmin, HowItWorksStepAdmin, TeamMemberAdmin
from apps.about.models import Achievement, HowItWorksStep, TeamMember


class AboutAdminTests(TestCase):
    def test_team_member_admin_exposes_ordering_fields(self):
        admin_config = TeamMemberAdmin(TeamMember, AdminSite())

        self.assertEqual(admin_config.list_display, ('name', 'title', 'is_active', 'order'))
        self.assertEqual(admin_config.list_filter, ('is_active',))
        self.assertEqual(admin_config.list_editable, ('is_active', 'order'))
        self.assertEqual(admin_config.search_fields, ('name', 'title', 'description'))

    def test_achievement_admin_exposes_ordering_fields(self):
        admin_config = AchievementAdmin(Achievement, AdminSite())

        self.assertEqual(admin_config.list_display, ('label', 'number', 'is_active', 'order'))
        self.assertEqual(admin_config.list_filter, ('is_active',))
        self.assertEqual(admin_config.list_editable, ('is_active', 'order'))

    def test_how_it_works_step_admin_supports_ordered_process_content(self):
        admin_config = HowItWorksStepAdmin(HowItWorksStep, AdminSite())

        self.assertEqual(admin_config.list_display, ('step_number', 'title', 'is_active', 'order'))
        self.assertEqual(admin_config.list_editable, ('is_active', 'order'))
