from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from django.urls import reverse_lazy
from accounts.models import CustomUser, Volunteer


class VolunteerListViewTest(TestCase):
    fixtures = ['communities.json', 'users.json', 'permission.json']

    def setUp(self):
        self.url = reverse_lazy('volunteer_list')
        self.user1 = CustomUser.objects.create(username="test_user", password="pwd", is_active=True)
        self.response = self.client.get(self.url)
        
    def test_volunteer_list_view_not_authorized(self):
        # Only members can get access to volunteer list
        self.assertEqual(self.response.status_code, 302)
        self.assertRedirects(self.response, 
            '/accounts/login/?next=/accounts/volunteer/list/')
    
    def test_volunteer_list_view_authorized(self):
        perm = Permission.objects.get(codename="view_volunteer")
        self.user1.user_permissions.add(perm)
        self.client.force_login(self.user1)
        self.response = self.client.get(self.url)
        self.assertEqual(self.response.status_code, 200)
        self.assertContains(self.response, "Bénévoles")

class VolunteerDetailViewTest(TestCase):
    fixtures = ['communities.json', 'users.json', 'permission.json']
    def setUp(self):
        self.url = reverse_lazy('volunteer_detail')
        self.user1 = CustomUser.objects.create(username="test_user", password="pwd", is_active=True)
        self.volunteer = Volunteer.objects.get(username="test_user")
        self.response = self.client.post(self.url)

    def test_volunteer_detail_view_not_authorized(self):
        # Only members can get access to volunteer detail
        self.assertEqual(self.response.status_code, 302)
        self.assertRedirects(self.response, 
            '/accounts/login/?next=/accounts/volunteer/detail/')
    
    def test_volunteer_detail_view_authorized(self):
        perm = Permission.objects.get(codename="view_volunteer")
        self.user1.user_permissions.add(perm)
        self.response = self.client.get(self.volunteer.get_absolute_url())
        self.client.force_login(self.user1)
        self.response = self.client.get(self.url)
        self.assertEqual(self.response.status_code, 200)
        self.assertContains(self.response, "Fiche de Bénévole")