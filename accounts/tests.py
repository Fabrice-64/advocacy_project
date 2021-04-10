from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.core import mail
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

class LoginTest(TestCase):

    def setUp(self):
        url = reverse('auth_login')
        self.response = self.client.get(url)

    def test_login(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'registration/login.html')
        self.assertContains(self.response, 'Connexion')


class LogoutTest(TestCase):
    def setUp(self):
        url = reverse('auth_logout')
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
        mail.send_mail(
            'Création de Compte', 'Corps du Message',
            'from@example.com', ['to@example.com'],
            fail_silently=False)
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, "Création de Compte")
