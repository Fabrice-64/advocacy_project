from django.test import TestCase
from django.urls import reverse_lazy
from django.contrib.auth.models import Permission
from accounts.models import CustomUser


class MandatesChangeTest(TestCase):
    
    def setUp(self):
        self.url = reverse_lazy('officials:mandate_change')
        self.response = self.client.get(self.url)
        self.user1 = CustomUser.objects.create(username="test_user", password="pwd", is_active=True)
    
    def test_display_mandate_change_not_authorized(self):
        self.assertEqual(self.response.status_code, 302)
        self.assertRedirects(self.response, 
            '/accounts/login/?next=/officials/mandate/change/')

    def test_display_mandate_change_authorized(self):
        perm = Permission.objects.get(codename="view_official")
        self.user1.user_permissions.add(perm)
        self.client.force_login(self.user1)
        self.response = self.client.get(self.url)
        self.assertEqual(self.response.status_code, 200)
        self.assertContains(self.response, "Mandats")

class OfficialPagesTest(TestCase):
    
    def setUp(self):
        self.url = reverse_lazy('officials:official_list')
        self.response = self.client.get(self.url)
        self.user1 = CustomUser.objects.create(username="test_user", password="pwd", is_active=True)
    
    def test_display_official_list_not_authorized(self):
        self.assertEqual(self.response.status_code, 302)
        self.assertRedirects(self.response, 
            '/accounts/login/?next=/officials/official/list/')

    def test_display_official_list_authorized(self):
        perm = Permission.objects.get(codename="view_official")
        self.user1.user_permissions.add(perm)
        self.client.force_login(self.user1)
        self.response = self.client.get(self.url)
        self.assertEqual(self.response.status_code, 200)
        self.assertContains(self.response, "Elus")
       

