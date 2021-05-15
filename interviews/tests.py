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


class AdvocacyTopicCreateViewTest(TestCase):

    def setUp(self):
        self.url = reverse_lazy('interviews:advocacy_topic_create')
        self.response = self.client.post(self.url)
        self.user1 = CustomUser.objects.create(username="test_user", password="pwd", is_active=True)
        self.client = Client()

    def test_advocacy_topic_create_not_authorized(self):
        self.assertEqual(self.response.status_code, 302)
        self.assertRedirects(self.response, 
            '/accounts/login/?next=/interviews/advocacy_topic/create/')

    def test_advocacy_topic_create_authorized(self):
        perm = Permission.objects.get(codename="add_advocacytopic")
        self.user1.user_permissions.add(perm)
        self.client.force_login(self.user1)
        self.response = self.client.get(self.url)
        self.assertEqual(self.response.status_code, 200)
        self.assertContains(self.response, "Plaidoyer")
# Create your tests here.

class AdvocacyTopicUpdateViewTest(TestCase):
    
    def setUp(self):
        self.topic = AdvocacyTopic.objects.create(slug="test-update")
        self.response = self.client.get(reverse('interviews:advocacy_topic_update', args=[self.topic.slug]))
        self.user1 = CustomUser.objects.create(username="test_user", password="pwd", is_active=True)

    def test_advocacy_topic_update_not_authorized(self):
        self.assertEqual(self.response.status_code, 302)
        self.assertRedirects(self.response, 
            '/accounts/login/?next=/interviews/advocacy_topic/update/test-update/')

    def test_advocacy_topic_update_authorized(self):
        perm = Permission.objects.get(codename="change_advocacytopic")
        self.user1.user_permissions.add(perm)
        self.client.force_login(self.user1)
        self.response = self.client.get(reverse('interviews:advocacy_topic_update', args=[self.topic.slug]))
        self.assertEqual(self.response.status_code, 200)
        self.assertContains(self.response, "Actualiser un Thème de Plaidoyer")
