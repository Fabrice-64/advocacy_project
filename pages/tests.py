from django.test import SimpleTestCase
from django.urls import reverse, resolve
from .views import HomePageView

# Create your tests here.
class HomePageTest(SimpleTestCase):

    def setUp(self):
        url = reverse('home')
        self.response = self.client.get(url)

    def test_homepage_status(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'home.html')
        self.assertContains(self.response, "Bienvenue sur la page d'accueil")
        self.assertNotContains(self.response, "<h1>Connexion<h1>")

    def test_homepage_url(self):
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_resolves_homepage_view(self):
        view = resolve('/')
        self.assertEqual(view.func.__name__,
            HomePageView.as_view().__name__)
