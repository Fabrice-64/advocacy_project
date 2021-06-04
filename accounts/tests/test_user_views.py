from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from django.urls import reverse_lazy
from accounts.models import CustomUser, Volunteer


class VolunteerListViewTest(TestCase):

    def setUp(self):
        self.url = reverse_lazy('volunteer_list')
        self.user1 = CustomUser.objects.create(username="test_user", password="pwd", is_active=True)
        self.response = self.client.get(self.url)

    def test_volunteer_list_view_not_authorized(self):
        # Only members can get access to volunteer list
        self.assertEqual(self.response.status_code, 302)
        self.assertRedirects(
            self.response,
            '/accounts/login/?next=/accounts/volunteer/list/')

    def test_volunteer_list_view_authorized(self):
        perm = Permission.objects.get(codename="view_volunteer")
        self.user1.user_permissions.add(perm)
        self.client.force_login(self.user1)
        self.response = self.client.get(self.url)
        self.assertEqual(self.response.status_code, 200)
        self.assertContains(self.response, "Bénévoles")


class VolunteerDetailViewTest(TestCase):

    def setUp(self):
        self.user1 = CustomUser.objects.create(
            username="test_user", password="pwd",
            is_active=True, status_type="MANAGER")
        self.volunteer = Volunteer.objects.create(
            username="test_user2", password="pwd",
            is_active=True, status_type="VOLUNTEER")

    def test_volunteer_detail_view_not_authorized(self):
        # Only members can get access to volunteer detail
        perm = Permission.objects.get(codename="view_volunteer")
        self.user1.user_permissions.remove(perm)
        self.response = self.client.get(self.volunteer.get_absolute_url())
        self.assertEqual(self.response.status_code, 302)

    def test_volunteer_detail_view_authorized(self):
        perm = Permission.objects.get(codename="view_volunteer")
        self.user1.user_permissions.add(perm)
        self.client.force_login(self.user1)
        self.response = self.client.get(self.volunteer.get_absolute_url())
        self.assertEqual(self.response.status_code, 200)
        self.assertContains(self.response, "volunteer-details")


class StaffListViewTest(TestCase):

    def setUp(self):
        self.url = reverse_lazy('staff_list')
        self.user1 = CustomUser.objects.create(
            username="test_user",
            password="pwd", is_active=True)
        self.response = self.client.get(self.url)

    def test_staff_list_view_not_authorized(self):
        # Only members can get access to volunteer list
        self.assertEqual(self.response.status_code, 302)
        self.assertRedirects(
            self.response,
            '/accounts/login/?next=/accounts/staff/list/')

    def test_staff_list_view_authorized(self):
        perm = Permission.objects.get(codename="view_employee")
        self.user1.user_permissions.add(perm)
        self.client.force_login(self.user1)
        self.response = self.client.get(self.url)
        self.assertEqual(self.response.status_code, 200)
        self.assertContains(self.response, "Membres du Personnel")


class StaffDetailViewTest(TestCase):

    def setUp(self):
        self.user1 = CustomUser.objects.create(
            username="test_user",
            password="pwd", is_active=True,
            status_type="MANAGER")
        self.employee = CustomUser.objects.create(
            username="test_user2",
            password="pwd", is_active=True,
            status_type="EMPLOYEE")

    def test_staff_detail_view_not_authorized(self):
        # Only members can get access to volunteer detail
        perm = Permission.objects.get(codename="view_employee")
        self.user1.user_permissions.remove(perm)
        self.response = self.client.get(
            self.employee.get_absolute_url())
        self.assertEqual(self.response.status_code, 302)

    def test_staff_detail_view_authorized(self):
        perm = Permission.objects.get(codename="view_employee")
        self.user1.user_permissions.add(perm)
        self.client.force_login(self.user1)
        self.response = self.client.get(
            self.employee.get_absolute_url())
        self.assertEqual(self.response.status_code, 200)
        self.assertContains(self.response, "employee-details")
