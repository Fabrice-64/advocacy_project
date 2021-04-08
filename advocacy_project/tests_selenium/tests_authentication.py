"""
    This is where the User Stories are tested.
    Are tested:

    To be noticed:
        By removing the carret at last line, the current html code
            will be displayed: very convenient for debugging.
"""


from django.test import LiveServerTestCase
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import Firefox
import os
class CustomUserTest(LiveServerTestCase):
    fixtures = ['users.json']

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
        user_input.send_keys('fabricejaouen')
        # L. enters her password
        user_input_pwd = self.browser.find_element_by_id("id_password")
        user_input_pwd.send_keys('admin')
        self.browser.find_element_by_xpath('//input[@type="submit"]').click()
        # Finally the logged in page is displayed
        self.browser.find_element_by_id("header-deconnection")
        #print(self.browser.page_source)

