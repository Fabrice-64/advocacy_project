from django.test import TestCase, Client
from django.urls import reverse_lazy
from django.contrib.auth.models import Permission
from accounts.models import CustomUser


class TeamListViewTest(TestCase):

    def setUp(self):
        url = reverse_lazy('teams:team_list')
        self.response = self.client.get(url)

    def test_teams_list_view(self):
        # In this test the User is not logged-in.
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, "teams/team_list.html")
        # Authorization Requirements lead to display an empty list
        self.assertContains(
            self.response, "Liste des Equipes")


class TeamCreateViewTest(TestCase):
    fixtures = ['communities.json']

    def setUp(self):
        self.url = reverse_lazy('teams:team_create')
        self.response = self.client.post(self.url)
        self.user1 = CustomUser.objects.create(
            username="test_user", password="pwd", is_active=True)

    def test_team_create_not_authorized(self):
        self.assertEqual(
            self.response.status_code, 302)
        self.assertRedirects(
            self.response,
            '/accounts/login/?next=/teams/team/create/')

    def test_team_create_authorized(self):
        perm = Permission.objects.get(codename="add_team")
        self.user1.user_permissions.add(perm)
        self.client.force_login(self.user1)
        self.response = self.client.get(self.url, {'city': "1"})
        self.assertEqual(self.response.status_code, 200)
        self.assertContains(self.response, "Nouvelle Equipe")
