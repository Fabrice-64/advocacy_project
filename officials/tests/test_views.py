from django.test import TestCase
from django.urls import reverse_lazy, reverse
from django.contrib.auth.models import Permission
from accounts.models import CustomUser
from officials.models import Official


class MandatesChangeTest(TestCase):

    def setUp(self):
        self.url = reverse_lazy('officials:mandate_add')
        self.response = self.client.get(self.url)
        self.user1 = CustomUser.objects.create(username="test_user", password="pwd", is_active=True)

    def test_display_mandate_add_not_authorized(self):
        self.assertEqual(self.response.status_code, 302)
        self.assertRedirects(
            self.response,
            '/accounts/login/?next=/officials/mandate/add/'
        )

    def test_display_mandate_add_authorized(self):
        perm = Permission.objects.get(codename="view_official")
        self.user1.user_permissions.add(perm)
        self.client.force_login(self.user1)
        self.response = self.client.get(self.url)
        self.assertEqual(self.response.status_code, 200)
        self.assertContains(self.response, "Mandats")


class OfficialDispatchTest(TestCase):

    def setUp(self):
        self.url = reverse_lazy('officials:official_dispatch')
        self.response = self.client.get(self.url)
        self.user1 = CustomUser.objects.create(
            username="test_user", password="pwd", is_active=True)

    def test_display_official_list_not_authorized(self):
        self.assertEqual(self.response.status_code, 302)
        self.assertRedirects(
            self.response,
            '/accounts/login/?next=/officials/dispatch/')

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
        self.assertRedirects(
            self.response,
            '/accounts/login/?next=/officials/mandates/add/senator/')

    def test_add_senator_mandate_authorized(self):
        perm = Permission.objects.get(codename="add_senatormandate")
        self.user1.user_permissions.add(perm)
        self.client.force_login(self.user1)
        self.response = self.client.get(self.url)
        self.assertEqual(self.response.status_code, 200)
        self.assertContains(self.response, "S??natorial")


class MPMandateTest(TestCase):

    def setUp(self):
        self.url = reverse_lazy('officials:add_mp_mandate')
        self.response = self.client.get(self.url)
        self.user1 = CustomUser.objects.create(
            username="test_user",
            password="pwd", is_active=True)

    def test_add_senator_mandate_not_authorized(self):
        self.assertEqual(self.response.status_code, 302)
        self.assertRedirects(
            self.response,
            '/accounts/login/?next=/officials/mandates/add/mp/')

    def test_add_senator_mandate_authorized(self):
        perm = Permission.objects.get(codename="add_mpmandate")
        self.user1.user_permissions.add(perm)
        self.client.force_login(self.user1)
        self.response = self.client.get(self.url)
        self.assertEqual(self.response.status_code, 200)
        self.assertContains(self.response, "D??put??")


class RegionMandateTest(TestCase):

    def setUp(self):
        self.url = reverse_lazy('officials:add_region_mandate')
        self.response = self.client.get(self.url)
        self.user1 = CustomUser.objects.create(
            username="test_user", password="pwd", is_active=True)

    def test_add_region_mandate_not_authorized(self):
        self.assertEqual(self.response.status_code, 302)
        self.assertRedirects(
            self.response,
            '/accounts/login/?next=/officials/mandates/add/region/')

    def test_add_region_mandate_authorized(self):
        perm = Permission.objects.get(codename="add_mandateregion")
        self.user1.user_permissions.add(perm)
        self.client.force_login(self.user1)
        self.response = self.client.get(self.url)
        self.assertEqual(self.response.status_code, 200)
        self.assertContains(self.response, "R??gional")


class DepartmentMandateTest(TestCase):

    def setUp(self):
        self.url = reverse_lazy('officials:add_department_mandate')
        self.response = self.client.get(self.url)
        self.user1 = CustomUser.objects.create(
            username="test_user", password="pwd", is_active=True)

    def test_add_department_mandate_not_authorized(self):
        self.assertEqual(self.response.status_code, 302)
        self.assertRedirects(
            self.response,
            '/accounts/login/?next=/officials/mandates/add/department/')

    def test_add_department_mandate_authorized(self):
        perm = Permission.objects.get(codename="add_mandatedepartment")
        self.user1.user_permissions.add(perm)
        self.client.force_login(self.user1)
        self.response = self.client.get(self.url)
        self.assertEqual(self.response.status_code, 200)
        self.assertContains(self.response, "D??partemental")


class IntercomMandateTest(TestCase):

    def setUp(self):
        self.url = reverse_lazy('officials:add_intercom_mandate')
        self.response = self.client.get(self.url)
        self.user1 = CustomUser.objects.create(
            username="test_user", password="pwd", is_active=True)

    def test_add_intercom_mandate_not_authorized(self):
        self.assertEqual(self.response.status_code, 302)
        self.assertRedirects(
            self.response,
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
        self.user1 = CustomUser.objects.create(
            username="test_user", password="pwd", is_active=True)

    def test_add_intercom_mandate_not_authorized(self):
        self.assertEqual(self.response.status_code, 302)
        self.assertRedirects(
            self.response,
            '/accounts/login/?next=/officials/mandates/add/city/')

    def test_add_department_mandate_authorized(self):
        perm = Permission.objects.get(codename="add_mandatecity")
        self.user1.user_permissions.add(perm)
        self.client.force_login(self.user1)
        self.response = self.client.get(self.url)
        self.assertEqual(self.response.status_code, 200)
        self.assertContains(self.response, "Communal")


class OfficialListTest(TestCase):

    def setUp(self):
        self.url = reverse_lazy('officials:official_list')
        self.response = self.client.get(self.url)
        self.user1 = CustomUser.objects.create(
            username="test_user", password="pwd", is_active=True)

    def test_add_intercom_mandate_not_authorized(self):
        self.assertEqual(self.response.status_code, 302)
        self.assertRedirects(
            self.response,
            '/accounts/login/?next=/officials/list/')

    def test_add_department_mandate_authorized(self):
        perm = Permission.objects.get(codename="view_official")
        self.user1.user_permissions.add(perm)
        self.client.force_login(self.user1)
        self.response = self.client.get(self.url)
        self.assertEqual(self.response.status_code, 200)
        self.assertContains(self.response, "Liste des Elus")


class OfficialDetailTest(TestCase):

    def setUp(self):
        self.official = Official.objects.create(
            first_name="Pr??nomElu", last_name="NomElu")
        self.response = self.client.get(reverse(
            'officials:official_details', args=[self.official.id]))
        self.user1 = CustomUser.objects.create(
            username="test_user", password="pwd", is_active=True)

    def test_view_official_details_not_authorized(self):
        self.assertEqual(self.response.status_code, 302)
        self.assertRedirects(
            self.response,
            f'/accounts/login/?next=/officials/official/details/{self.official.id}/')

    def test_view_official_details_authorized(self):
        perm = Permission.objects.get(codename="view_official")
        self.user1.user_permissions.add(perm)
        self.client.force_login(self.user1)
        self.response = self.client.get(
            reverse('officials:official_details', args=[self.official.id]))
        self.assertEqual(self.response.status_code, 200)
        self.assertContains(self.response, "Fiche")


class OfficialCreateTest(TestCase):

    def setUp(self):
        self.url = reverse_lazy('officials:official_create')
        self.response = self.client.post(self.url)
        self.user1 = CustomUser.objects.create(
            username="test_user", password="pwd", is_active=True)

    def test_official_create_not_authorized(self):
        self.assertEqual(self.response.status_code, 302)
        self.assertRedirects(
            self.response,
            '/accounts/login/?next=/officials/official/create/')

    def test_official_create_authorized(self):
        perm = Permission.objects.get(codename="add_official")
        self.user1.user_permissions.add(perm)
        self.client.force_login(self.user1)
        self.response = self.client.get(self.url)
        self.assertEqual(self.response.status_code, 200)
        self.assertContains(self.response, "Nouvel Elu")


class OfficialUpdateTest(TestCase):

    def setUp(self):
        self.url = reverse_lazy('officials:official_update')
        self.official = Official.objects.create(
            first_name="test_official",
            last_name="test_official_name")
        self.response = self.client.get(
            reverse('officials:official_update',
                    args=[self.official.id]))
        self.user1 = CustomUser.objects.create(
            username="test_user", password="pwd", is_active=True)

    def test_official_create_not_authorized(self):
        self.assertEqual(self.response.status_code, 302)
        self.assertRedirects(
            self.response,
            f'/accounts/login/?next=/officials/official/update/{self.official.id}/')

    def test_official_create_authorized(self):
        perm = Permission.objects.get(codename="change_official")
        self.user1.user_permissions.add(perm)
        self.client.force_login(self.user1)
        self.response = self.client.get(reverse(
            'officials:official_update', args=[self.official.id]))
        self.assertEqual(self.response.status_code, 200)
        self.assertContains(self.response, "Actualisation d'un Elu")


class OfficialRankingTest(TestCase):
    fixtures = [
        'communities.json', 'users.json', 'teams.json',
        'permission.json', 'groups.json', 'officials.json',
        'interviews.json']

    def setUp(self):
        self.url = reverse_lazy('officials:officials_ranking')
        self.response = self.client.post(self.url)
        self.user1 = CustomUser.objects.create(
            username="test_user", password="pwd", is_active=True)

    def test_official_ranking_not_authorized(self):
        self.assertEqual(self.response.status_code, 302)
        self.assertRedirects(
            self.response,
            '/accounts/login/?next=/officials/officials_ranking/')

    def test_official_ranking_authorized(self):
        perm = Permission.objects.get(codename="view_official")
        self.user1.user_permissions.add(perm)
        self.client.force_login(self.user1)
        self.response = self.client.get(self.url)
        self.assertEqual(self.response.status_code, 200)
        self.assertContains(self.response, "Cat??gories d'Elus")
        self.assertEqual(
            len(self.response.context["little_proximity_high_influence"]), 0)
        self.assertEqual(
            len(self.response.context["high_proximity_high_influence"]), 1)
        self.assertEqual(
            len(self.response.context["high_proximity_little_influence"]), 1)
        self.assertEqual(
            len(self.response.context["little_proximity_little_influence"]), 0)


class OfficialEngagementTest(TestCase):
    fixtures = [
        'communities.json', 'users.json', 'teams.json',
        'permission.json', 'groups.json',
        'officials.json', 'interviews.json']

    def setUp(self):
        self.url = reverse_lazy('officials:officials_to_engage')
        self.response = self.client.post(self.url)
        self.user1 = CustomUser.objects.create(
            username="test_user", password="pwd", is_active=True)

    def test_official_target_not_authorized(self):
        self.assertEqual(self.response.status_code, 302)
        self.assertRedirects(
            self.response,
            '/accounts/login/?next=/officials/officials/engagement/')

    def test_official_target_authorized(self):
        perm = Permission.objects.get(codename="view_official")
        self.user1.user_permissions.add(perm)
        self.client.force_login(self.user1)
        self.response = self.client.get(self.url)
        self.assertEqual(self.response.status_code, 200)
        self.assertContains(self.response, "Elus ?? Engager")
        self.assertEqual(len(self.response.context["officials_to_engage"]), 0)
