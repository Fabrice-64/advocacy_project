"""
    These tests are exclusively dedicated to the calculations
    of the influence and propinquity of an Official.
"""
from django.test import TestCase
from officials import models as model
from interviews.models import Interview
from .database_sample import setup_sample_database
import officials.calculations as oc


class ElectoralMandatesTest(TestCase):

    def setUp(self):
        """
        This is the setup of a bunch of officials and their mandates,
        in order to provide material for the influence calculations.
        """
        setup_sample_database()
        self.officials = model.Official.objects.all()
        self.official1 = model.Official.objects.get(first_name="official1")
        self.official2 = model.Official.objects.get(first_name="official2")

    def test_city_influence_calculation(self):
        city_influence = oc.city_influence_calculation(self.official1.id)
        self.assertEqual(city_influence, 1)

    def test_intercom_influence_calculation(self):
        intercom_influence = oc.intercom_influence_calculation(self.official1.id)
        self.assertEqual(intercom_influence, 2)

    def test_department_influence_calculation(self):
        dept_influence = oc.department_influence_calculation(self.official1.id)
        self.assertEqual(dept_influence, 0)
        dept_influence2 = oc.department_influence_calculation(self.official2.id)
        self.assertEqual(dept_influence2, 3)

    def test_region_influence_calculation(self):
        region_influence = oc.region_influence_calculation(self.official1.id)
        self.assertEqual(region_influence, 4)

    def test_mp_influence_calculation(self):
        mp_influence = oc.mp_influence_calculation(self.official1.id)
        self.assertEqual(mp_influence, 5)

    def test_senator_influence_calculation(self):
        senator_influence = oc.senator_influence_calculation(self.official1.id)
        self.assertEqual(senator_influence, 0)

    def test_influence_calculation(self):
        influence_calc = oc.influence_calculation(self.official1.id)
        self.assertEqual(influence_calc, 12)

    def test_interview_propinquity(self):
        propinquity1, qty_interviews = oc.interview_propinquity(self.official1.id)
        self.assertEqual(propinquity1, 6)
        self.assertEqual(qty_interviews, 2)

    def test_no_interview_propinquity(self):
        propinquity, qty_interviews = oc.interview_propinquity(self.official2.id)
        self.assertEqual(propinquity, 0)
        self.assertEqual(qty_interviews, 0)

    def test_importance_summary(self):
        result = oc.importance_summary(self.official1.id, self.official1.first_name, self.official1.last_name)
        self.assertIn("official1", result)

    def test_calculate_ranking(self):
        result = oc.calculate_ranking(self.officials)
        self.assertEqual(len(result), 2)
