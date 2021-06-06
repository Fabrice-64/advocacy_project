"""
    The User Stories related to the accounts management are tested here.

    Are tested:
    authentication:
        def test_plaid_10_authenticate_on_the_website
    create user:
        def test_plaid_2_create_new_user
    check permissions implementation:
        def test_plaid_2_check_permissions

    To be noticed:
       For debugging insert print(self.browser.page_source) wherever you want to
       in order to check where your code stops.
"""


from django.test import LiveServerTestCase
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver import Firefox
import os


class CustomUserTest(LiveServerTestCase):
    fixtures = ['communities.json', 'teams.json', 'groups.json', 'users.json']

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.browser = Firefox()
        cls.browser.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()
        super().tearDownClass()

    def test_plaid_10_authenticate_on_the_website(self):
        """
            The user wants to authenticate in order to have access to
            the functionalities of the website
        """

        self.browser.get(os.path.join(self.live_server_url, ''))
        # Leila gets access to the website
        # L. is logged out and is offered to log in
        self.browser.find_element_by_id("login-status")
        self.browser.find_element_by_id("header-connection").click()
        # Then L. clicks on connexion to access the template
        # L. enters her username
        user_input = self.browser.find_element_by_id("id_username")
        user_input.send_keys('leila')
        # L. enters her password
        user_input_pwd = self.browser.find_element_by_id("id_password")
        user_input_pwd.send_keys('@dmin1234')
        self.browser.find_element_by_xpath('//input[@type="submit"]').click()
        # Finally the logged in page is displayed
        self.browser.find_element_by_id("header-deconnection")
        # print(self.browser.page_source)

    def test_plaid_2_create_new_user(self):
        """
            The manager creates a new user, who gets an email for the account
            activation.
        """

        self.browser.get(os.path.join(self.live_server_url, ''))
        # Sébastien logs in to get access to the admin interface
        self.browser.find_element_by_id("login-status")
        self.browser.find_element_by_id("header-connection").click()
        user_input = self.browser.find_element_by_id("id_username")
        user_input.send_keys('leila')
        # S. enters his password
        user_input_pwd = self.browser.find_element_by_id("id_password")
        user_input_pwd.send_keys('@dmin1234')
        self.browser.find_element_by_xpath('//input[@type="submit"]').click()
        self.browser.find_element_by_id('navbarDropdown').click()
        self.browser.find_element_by_id('new-user').click()
        username_input = self.browser.find_element_by_id('id_username')
        username_input.send_keys('Albert')
        email_input = self.browser.find_element_by_id('id_email')
        email_input.send_keys("albert@test.com")
        phone_number = self.browser.find_element_by_id('id_phone_number')
        phone_number.send_keys("01 02 03 04 05")
        team = Select(self.browser.find_element_by_id('id_team'))
        team.select_by_value("1")
        password1_input = self.browser.find_element_by_id('id_password1')
        password1_input.send_keys('test@1234')
        password2_input = self.browser.find_element_by_id('id_password2')
        password2_input.send_keys('test@1234')
        self.browser.find_element_by_xpath('//input[@type="submit"]')

    def test_plaid_2_check_permissions(self):
        self.browser.get(os.path.join(self.live_server_url, ''))
        # Sébastien logs in to get access to the admin interface
        self.browser.find_element_by_id("header-connection").click()
        user_input = self.browser.find_element_by_id("id_username")
        user_input.send_keys('leila')
        # S. enters his password
        user_input_pwd = self.browser.find_element_by_id("id_password")
        user_input_pwd.send_keys('@dmin1234')
        self.browser.find_element_by_xpath('//input[@type="submit"]').click()
        self.browser.find_element_by_id("link-communities").click()
        self.browser.find_element_by_id("region-list").click()
        regions = self.browser.find_elements_by_class_name("region-name")
        self.assertEqual(len(regions), 7)
