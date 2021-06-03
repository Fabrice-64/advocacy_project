from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.urls import reverse
from django.core import mail

from accounts.models import CustomUser
from accounts.views import change_password


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


class LoginTest(TestCase):

    def setUp(self):
        url = reverse('login')
        self.response = self.client.get(url)

    def test_login(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'accounts/login.html')
        self.assertContains(self.response, 'Connexion')


class LogoutTest(TestCase):
    def setUp(self):
        url = reverse('logout')
        self.response = self.client.get(url)

    def test_logout(self):
        # status_code is 302 as logout redirects to homepage iaw the settings.
        self.assertEqual(self.response.status_code, 302)
        self.assertRedirects(self.response, '/')


class RegistrationTest(TestCase):
    def setUp(self):
        url = reverse('registration_register')
        self.response = self.client.get(url)

    def test_registration(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed('registration/registration_form.html')
        self.assertContains(self.response, "Saisie d\'un Nouvel Utilisateur")

    def test_sendmail(self):
        """
            On the development configuration, emails are sent to the CLI.
        """
        mail.send_mail(
            'Création de Compte', 'Corps du Message',
            'from@example.com', ['to@example.com'],
            fail_silently=False)
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, "Création de Compte")


class ChangePasswordTest(TestCase):

    def setUp(self):
        self.user = CustomUser.objects.create_user(username="paul", password="pwd", is_active=True)
        Group.objects.create(name="VOLUNTEER")
        self.url = reverse('change_password')
        self.response = self.client.post(
            self.url,
            {"username": "paul", "old_password": "pwd"})
        self.client = Client()

    def test_password_change_not_logged_in(self):
        self.assertEqual(self.response.status_code, 302)
        self.assertRedirects(self.response, '/accounts/login/?next=/accounts/change_password/')

    def test_password_change_logged_in(self):
        logged_in = self.client.login(username="paul", password="pwd")
        self.assertTrue(logged_in)
        self.response = self.client.post(
            self.url, 
            {
            "username": "paul", "old_password": "pwd",
            "new_password1": "pwd1", "new_password2": "pwd1",
            "status_type": "VOLUNTEER"},
            follow=True)
        self.assertEqual(self.response.status_code, 200)
        self.assertIsNotNone(self.response.context['form'])

    def test_password_change_short_password(self):
        logged_in = self.client.login(username="paul", password="pwd")
        self.assertTrue(logged_in)
        self.response = self.client.post(
            self.url,
            {
            "username": "paul", "old_password": "pwd",
            "new_password1": "pwd1", "new_password2": "pwd1",
            "status_type": "VOLUNTEER"},
            follow=True)
        self.assertEqual(self.response.status_code, 200)
        self.assertIsNotNone(self.response.context['messages'])
        self.assertTemplateUsed('accounts/change_password.html')
        self.assertFormError(self.response,
            "form", "new_password2", 
            ['Ce mot de passe est trop court. Il doit contenir au minimum 8 caractères.'])
        
    def test_password_change_compliant_password(self):
        logged_in = self.client.login(username="paul", password="pwd")
        self.assertTrue(logged_in)
        self.response = self.client.post(self.url, 
            {
            "username": "paul", "old_password": "pwd",
            "new_password1": "@password1", "new_password2": "@password1",
            "status_type": "VOLUNTEER"},
            follow=True)
        self.assertEqual(self.response.status_code, 200)
        self.assertIsNotNone(self.response.context['messages'])
        self.assertTemplateUsed('accounts/change_password.html')
        self.assertNotContains(
            self.response,
            "S\'il vous plait, corrigez l\'erreur.")
        self.assertContains(self.response, "Votre mot de passe a été changé")
