from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse, reverse_lazy
from . import fixture as f

class IntercomViewTest(TestCase):
    

class RegionsListViewTest(TestCase):

    def setUp(self):
        f.set_up_db()
        url = reverse_lazy('communities:region_list')
        self.response = self.client.get(url)
        
    def test_regions_list_view(self):
        pass
        #In this test the User is not logged-in.
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, "communities/region_list.html")
        # Authorization Requirements lead to display an empty list
        self.assertContains(self.response, "Grand-Est")