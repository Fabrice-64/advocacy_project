from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from . import fixture as f

class RegionsListViewTest(TestCase):

    def setUp(self):
        f.set_up_db()
        
    def test_regions_list_view(self):
        # In this test the User is not logged-in.
        response = self.client.get(reverse('communities:region_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "communities/region_list.html")
        # Authorization Requirements lead to display an empty list
        self.assertNotContains(response, "Grand-Est")