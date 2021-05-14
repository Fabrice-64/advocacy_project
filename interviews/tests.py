from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from django.urls import reverse, reverse_lazy
from . import views as views
from .models import AdvocacyTopic
from accounts.models import CustomUser



class AdvocacyTopicListViewTest(TestCase):
    
    def setUp(self):
        self.url = reverse_lazy('interviews:advocacy_topic_list')
        self.user1 = CustomUser.objects.create(username="test_user", password="pwd", is_active=True)

    def test_advocacy_topics_list_view(self):
        # Only a user with the rights can see the list.
        perm = Permission.objects.get(codename="view_advocacytopic")
        self.user1.user_permissions.add(perm)
        self.client.force_login(self.user1)
        self.response = self.client.get(self.url)
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, "advocacy_topics/advocacy_topic_list.html")
        self.assertContains(self.response, "Plaidoyer")

"""
class RegionCreateViewTest(TestCase):
    fixtures = ['communities.json', 'permission.json']

    def setUp(self):
        self.url = reverse_lazy('communities:region_create')
        self.response = self.client.post(self.url)
        self.user1 = CustomUser.objects.create(username="test_user", password="pwd", is_active=True)
        self.client = Client()

    def test_region_create_not_authorized(self):
        self.assertEqual(self.response.status_code, 302)
        self.assertRedirects(self.response, 
            '/accounts/login/?next=/communities/region/create/')

    def test_region_create_authorized(self):
        perm = Permission.objects.get(codename="add_region")
        self.user1.user_permissions.add(perm)
        self.client.force_login(self.user1)
        self.response = self.client.post(self.url)
        self.assertEqual(self.response.status_code, 200)
        self.assertContains(self.response, "Région")
# Create your tests here.
"""