from django.test import TestCase
from django.urls import reverse_lazy
from django.contrib.auth.models import Permission
from accounts.models import CustomUser


class MandatesChangeTest(TestCase):
    
    def setUp(self):
        self.url = reverse_lazy('officials:mandate_add')
        self.response = self.client.get(self.url)
        self.user1 = CustomUser.objects.create(username="test_user", password="pwd", is_active=True)
    
    def test_display_mandate_add_not_authorized(self):
        self.assertEqual(self.response.status_code, 302)
        self.assertRedirects(self.response, 
            '/accounts/login/?next=/officials/mandate/add/')

    def test_display_mandate_add_authorized(self):
        perm = Permission.objects.get(codename="view_official")
        self.user1.user_permissions.add(perm)
        self.client.force_login(self.user1)
        self.response = self.client.get(self.url)
        self.assertEqual(self.response.status_code, 200)
        self.assertContains(self.response, "Mandats")

class OfficialPagesTest(TestCase):
    
    def setUp(self):
        self.url = reverse_lazy('officials:official_list')
        self.response = self.client.get(self.url)
        self.user1 = CustomUser.objects.create(username="test_user", password="pwd", is_active=True)
    
    def test_display_official_list_not_authorized(self):
        self.assertEqual(self.response.status_code, 302)
        self.assertRedirects(self.response, 
            '/accounts/login/?next=/officials/official/list/')

    def test_display_official_list_authorized(self):
        perm = Permission.objects.get(codename="view_official")
        self.user1.user_permissions.add(perm)
        self.client.force_login(self.user1)
        self.response = self.client.get(self.url)
        self.assertEqual(self.response.status_code, 200)
        self.assertContains(self.response, "Elus")
       

class SenatorMandateTest(TestCase):
    
    def setUp(self):
        self.url = reverse_lazy('officials:add_senator_mandate')
        self.response = self.client.get(self.url)
        self.user1 = CustomUser.objects.create(username="test_user", password="pwd", is_active=True)

    def test_add_senator_mandate_not_authorized(self):
        self.assertEqual(self.response.status_code, 302)
        self.assertRedirects(self.response, 
            '/accounts/login/?next=/officials/mandates/add/senator/')

    def test_add_senator_mandate_authorized(self):
        perm = Permission.objects.get(codename="add_senatormandate")
        self.user1.user_permissions.add(perm)
        self.client.force_login(self.user1)
        self.response = self.client.get(self.url)
        self.assertEqual(self.response.status_code, 200)
        self.assertContains(self.response, "Sénatorial")
    
class MPMandateTest(TestCase):
    
    def setUp(self):
        self.url = reverse_lazy('officials:add_mp_mandate')
        self.response = self.client.get(self.url)
        self.user1 = CustomUser.objects.create(username="test_user", password="pwd", is_active=True)

    def test_add_senator_mandate_not_authorized(self):
        self.assertEqual(self.response.status_code, 302)
        self.assertRedirects(self.response, 
            '/accounts/login/?next=/officials/mandates/add/mp/')

    def test_add_senator_mandate_authorized(self):
        perm = Permission.objects.get(codename="add_mpmandate")
        self.user1.user_permissions.add(perm)
        self.client.force_login(self.user1)
        self.response = self.client.get(self.url)
        self.assertEqual(self.response.status_code, 200)
        self.assertContains(self.response, "Député")


class RegionMandateTest(TestCase):
    
    def setUp(self):
        self.url = reverse_lazy('officials:add_region_mandate')
        self.response = self.client.get(self.url)
        self.user1 = CustomUser.objects.create(username="test_user", password="pwd", is_active=True)

    def test_add_region_mandate_not_authorized(self):
        self.assertEqual(self.response.status_code, 302)
        self.assertRedirects(self.response, 
            '/accounts/login/?next=/officials/mandates/add/region/')

    def test_add_region_mandate_authorized(self):
        perm = Permission.objects.get(codename="add_mandateregion")
        self.user1.user_permissions.add(perm)
        self.client.force_login(self.user1)
        self.response = self.client.get(self.url)
        self.assertEqual(self.response.status_code, 200)
        self.assertContains(self.response, "Régional")

class DepartmentMandateTest(TestCase):
    
    def setUp(self):
        self.url = reverse_lazy('officials:add_department_mandate')
        self.response = self.client.get(self.url)
        self.user1 = CustomUser.objects.create(username="test_user", password="pwd", is_active=True)

    def test_add_department_mandate_not_authorized(self):
        self.assertEqual(self.response.status_code, 302)
        self.assertRedirects(self.response, 
            '/accounts/login/?next=/officials/mandates/add/department/')

    def test_add_department_mandate_authorized(self):
        perm = Permission.objects.get(codename="add_mandatedepartment")
        self.user1.user_permissions.add(perm)
        self.client.force_login(self.user1)
        self.response = self.client.get(self.url)
        self.assertEqual(self.response.status_code, 200)
        self.assertContains(self.response, "Départemental")


class IntercomMandateTest(TestCase):
    
    def setUp(self):
        self.url = reverse_lazy('officials:add_intercom_mandate')
        self.response = self.client.get(self.url)
        self.user1 = CustomUser.objects.create(username="test_user", password="pwd", is_active=True)

    def test_add_intercom_mandate_not_authorized(self):
        self.assertEqual(self.response.status_code, 302)
        self.assertRedirects(self.response, 
            '/accounts/login/?next=/officials/mandates/add/intercom/')

    def test_add_department_mandate_authorized(self):
        perm = Permission.objects.get(codename="add_mandateintercom")
        self.user1.user_permissions.add(perm)
        self.client.force_login(self.user1)
        self.response = self.client.get(self.url)
        self.assertEqual(self.response.status_code, 200)
        self.assertContains(self.response, "Intercommunal")

class CityMandateTest(TestCase):
    
    def setUp(self):
        self.url = reverse_lazy('officials:add_city_mandate')
        self.response = self.client.get(self.url)
        self.user1 = CustomUser.objects.create(username="test_user", password="pwd", is_active=True)

    def test_add_intercom_mandate_not_authorized(self):
        self.assertEqual(self.response.status_code, 302)
        self.assertRedirects(self.response, 
            '/accounts/login/?next=/officials/mandates/add/city/')

    def test_add_department_mandate_authorized(self):
        perm = Permission.objects.get(codename="add_mandatecity")
        self.user1.user_permissions.add(perm)
        self.client.force_login(self.user1)
        self.response = self.client.get(self.url)
        self.assertEqual(self.response.status_code, 200)
        self.assertContains(self.response, "Communal")