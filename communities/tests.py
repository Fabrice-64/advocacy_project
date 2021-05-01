from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse, reverse_lazy
from . import views as views

class CommunityTypesTest(TestCase):
    
    def setUp(self):
        url = reverse_lazy('communities:list')
        self.response = self.client.get(url)
    
    def test_display_community_types(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, "communities/communities.html")


class IntercomViewTest(TestCase):
    """
        Test AJAX Intercom view
    """
    fixtures = ['communities.json']

    def setUp(self):
        url = reverse_lazy('communities:ajax_load_intercom')
        self.response = self.client.get(url)
    
    def test_load_intercom_view(self):
        self.assertEqual(self.response.status_code, 200),
        self.assertTemplateUsed(self.response, "communities/intercom_dropdown_list.html")


class RegionsListViewTest(TestCase):
    fixtures = ['communities.json']

    def setUp(self):
        url = reverse_lazy('communities:region_list')
        self.response = self.client.get(url)
        
    def test_regions_list_view(self):
        #In this test the User is not logged-in.
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, "communities/region_list.html")
        # Authorization Requirements lead to display an empty list
        self.assertContains(self.response, "Grand-Est")