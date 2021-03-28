from django.test import TestCase
from django.contrib.auth import get_user_model
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