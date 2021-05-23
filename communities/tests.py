from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from django.urls import reverse, reverse_lazy
from . import views as views
from accounts.models import CustomUser
from teams.models import Team
from .ajax_functions import retrieve_departments_by_region, retrieve_intercoms_by_department, retrieve_city_by_department


class CommunityTypesTest(TestCase):
    
    def setUp(self):
        url = reverse_lazy('communities:list')
        self.response = self.client.get(url)
    
    def test_display_community_types(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, "communities/communities.html")


class LoadDepartmentViewTest(TestCase):
    """
        Test AJAX Department view
    """
    fixtures = ['communities.json']

    def setUp(self):
        url = reverse_lazy('communities:ajax_load_departments')
        self.response = self.client.get(url)
    
    def test_load_intercom_view(self):
        self.assertEqual(self.response.status_code, 200),
        self.assertTemplateUsed(self.response, "communities/department_dropdown_list.html")

class LoadIntercomViewTest(TestCase):
    """
        Test AJAX Intercom view
    """
    fixtures = ['communities.json']

    def setUp(self):
        url = reverse_lazy('communities:ajax_load_intercoms')
        self.response = self.client.get(url)
    
    def test_load_intercom_view(self):
        self.assertEqual(self.response.status_code, 200),
        self.assertTemplateUsed(self.response, "communities/intercom_dropdown_list.html")

class LoadCityViewTest(TestCase):
    """
        Test AJAX Intercom view
    """
    fixtures = ['communities.json']

    def setUp(self):
        url = reverse_lazy('communities:ajax_load_cities')
        self.response = self.client.get(url)
    
    def test_load_intercom_view(self):
        self.assertEqual(self.response.status_code, 200),
        self.assertTemplateUsed(self.response, "communities/city_dropdown_list.html")


class RegionListViewTest(TestCase):
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


class RegionCreateViewTest(TestCase):

    def setUp(self):
        self.url = reverse_lazy('communities:region_create')
        self.response = self.client.post(self.url)
        self.user1 = CustomUser.objects.create(username="test_user", password="pwd", is_active=True)
        self.client = Client()

    def test_region_create_not_authorized(self):
        self.assertEqual(self.response.status_code, 302)
        self.assertRedirects(self.response, 
            '/accounts/login/?next=/communities/region/create/')

    def test_region_create_authorized(self):
        perm = Permission.objects.get(codename="add_region")
        self.user1.user_permissions.add(perm)
        self.client.force_login(self.user1)
        self.response = self.client.post(self.url)
        self.assertEqual(self.response.status_code, 200)
        self.assertContains(self.response, "Région")


class DepartmentListViewTest(TestCase):
    fixtures = ['communities.json']

    def setUp(self):
        url = reverse_lazy('communities:department_list')
        self.response = self.client.get(url)
        
    def test_department_list_view(self):
        #In this test the User is not logged-in.
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, "communities/department_list.html")
        # Authorization Requirements lead to display an empty list
        self.assertContains(self.response, "Bas-Rhin")


class DepartmentCreateViewTest(TestCase):

    def setUp(self):
        self.url = reverse_lazy('communities:department_create')
        self.response = self.client.post(self.url)
        self.user1 = CustomUser.objects.create(username="test_user", password="pwd", is_active=True)
        self.client = Client()

    def test_department_create_not_authorized(self):
        self.assertEqual(self.response.status_code, 302)
        self.assertRedirects(self.response, 
            '/accounts/login/?next=/communities/department/create/')

    def test_department_create_authorized(self):
        perm = Permission.objects.get(codename="add_department")
        self.user1.user_permissions.add(perm)
        self.client.force_login(self.user1)
        self.response = self.client.post(self.url)
        self.assertEqual(self.response.status_code, 200)
        self.assertContains(self.response, "Département")

class IntercomListViewTest(TestCase):
    fixtures = ['communities.json']

    def setUp(self):
        url = reverse_lazy('communities:intercom_list')
        self.response = self.client.get(url)
        
    def test_intercom_list_view(self):
        #In this test the User is not logged-in.
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, "communities/intercom_list.html")
        # Authorization Requirements lead to display an empty list
        self.assertContains(self.response, "Eurométropole")

class IntercomCreateViewTest(TestCase):
    fixtures = ['communities.json']

    def setUp(self):
        self.url = reverse_lazy('communities:intercom_create')
        self.user1 = CustomUser.objects.create(username="test_user", password="pwd", is_active=True)
        self.client = Client()

    def test_intercom_create_not_authorized(self):
        self.response = self.client.post(self.url)
        self.assertEqual(self.response.status_code, 302)
        self.assertRedirects(self.response, 
            '/accounts/login/?next=/communities/intercom/create/')

    def test_intercom_create_authorized(self):
        perm = Permission.objects.get(codename="add_intercom")
        self.user1.user_permissions.add(perm)
        self.client.force_login(self.user1)
        self.response = self.client.post(self.url, {'region': "1"})
        self.assertEqual(self.response.status_code, 200)
        #self.assertContains(self.response, "Intercommunalité")

    def test_ajax_load_department(self):
        self.url = reverse_lazy('communities:ajax_load_departments')
        self.response = self.client.post(self.url, {"region": "1"})
        self.assertEquals(self.response.status_code, 200)
        self.assertTemplateUsed("communities/department_dropdown_list.html")


class CityListViewTest(TestCase):
    fixtures = ['communities.json']

    def setUp(self):
        url = reverse_lazy('communities:city_list')
        self.response = self.client.get(url)
        
    def test_city_list_view(self):
        #In this test the User is not logged-in.
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, "communities/city_list.html")
        # Authorization Requirements lead to display an empty list
        self.assertContains(self.response, "Strasbourg")

class CityCreateViewTest(TestCase):
    fixtures = ['communities.json']

    def setUp(self):
        self.url = reverse_lazy('communities:city_create')
        self.response = self.client.post(self.url)
        self.user1 = CustomUser.objects.create(username="test_user", password="pwd", is_active=True)
        self.client = Client()

    def test_city_create_not_authorized(self):
        self.assertEqual(self.response.status_code, 302)
        self.assertRedirects(self.response, 
            '/accounts/login/?next=/communities/city/create/')

    def test_city_create_authorized(self):
        perm = Permission.objects.get(codename="add_city")
        self.user1.user_permissions.add(perm)
        self.client.force_login(self.user1)
        self.response = self.client.post(self.url)
        self.assertEqual(self.response.status_code, 200)
        self.assertContains(self.response, "Commune")

    def test_city_creation_tree(self):
        perm = Permission.objects.get(codename="add_city")
        self.user1.user_permissions.add(perm)
        self.client.force_login(self.user1)
        self.response = self.client.post(self.url, {'region': "1", "department": "3"})
        self.assertContains(self.response, "Eurométropole Strasbourg")
    
    def test_ajax_load_intercom(self):
        self.url = reverse_lazy('communities:ajax_load_intercoms')
        self.response = self.client.post(self.url, {"department": "3"})
        self.assertEquals(self.response.status_code, 200)
        self.assertTemplateUsed("communities/intercom_dropdown_list.html")


class AjaxFunctionTest:

    def test_retrieve_departments_by_region(self):
        data = {'region': "1"}
        result = retrieve_departments_by_region(data)
        self.assertIsNotNone(result)
        self.assertContains(result, "Bas-Rhin")

    def test_retrieve_intercoms_by_department(self):
        data = {'department' : "3"}
        result = retrieve_intercoms_by_department(data)
        self.assertIsNotNone(result)
        self.assertContains(result, "Eurométropole")

    def test_retrieve_city_by_department(self):
        data = {'department' : "3"}
        result = retrieve_city_by_department(data)
        self.assertIsNotNone(result)
        self.assertContains(result, "Bischwiller")

