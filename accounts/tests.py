from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
# Create your tests here.

class CustomUserTest(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username="Jean",
            email="jean@test.com",
            password="test1234"
        )
        self.assertEqual(user.username, "Jean")
        self.assertEqual(user.email, "jean@test.com")
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username="Paul",
            email="paul@test.com",
            password="test1234"
        )
        self.assertEqual(admin_user.username, "Paul")
        self.assertEqual(admin_user.email, "paul@test.com")
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)

class SignUpPageTest(TestCase):

    def setUp(self):
        url = reverse('accounts:signup')
        self.response = self.client.get(url)

    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'registration/signup.html')
        self.assertContains(self.response, 'Création de Compte')

class LoginTest(TestCase):

    def setUp(self):
        url = reverse('accounts:login')
        self.response = self.client.get(url)

    def test_login(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'registration/login.html')
        self.assertContains(self.response, 'Connexion')


class LogoutTest(TestCase):
    def setUp(self):
        url = reverse('accounts:logout')
        self.response = self.client.get(url)

    def test_logout(self):
        # status_code is 302 as logout redirects to homepage iaw the settings.
        self.assertEqual(self.response.status_code, 302)