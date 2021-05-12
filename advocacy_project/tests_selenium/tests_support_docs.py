"""
    This is where the Speaking Points are tested.

    To be noticed:
        By removing the carret at last line, the current html code
            will be printed on the screen: very convenient for debugging.
"""


from django.test import LiveServerTestCase
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver import Firefox
import os
class CustomUserTest(LiveServerTestCase):
    fixtures = ['users.json', 'communities.json', 'teams.json']

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.browser = Firefox()
        cls.browser.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()
        super().tearDownClass()

    def test_plaid_7_record_some_support_docs(self):
        """
           The coordinator prepare support documentation 
           for the volunteer to be more consistent during the interview.
           The persona is named Sebastien
           
        """
        self.browser.get(os.path.join(self.live_server_url, ''))
        # From the beginning the advocacy coordinator is logged-in
        self.browser.find_element_by_id("header-connection").click()
        user_input = self.browser.find_element_by_id("id_username")
        user_input.send_keys('sebastien')
        user_input_pwd = self.browser.find_element_by_id("id_password")
        user_input_pwd.send_keys('admin')
        self.browser.find_element_by_xpath('//input[@type="submit"]').click()
        # The homepage dedicated to connected people is displayed.
        # S. opens the "support documentation" page
        self.browser.find_element_by_id('link-support-docs').click()
        # Then a label "add a reference" is displayed
        # S. clicks on this item
        # Then a window with several fields is displayed
        # The fields are the following ones:
        # Publication date
        # Link to the source
        # A menu offers some topics
        # Quote to be used as a support
        # Drafter ID
        # S. fills all the fields
        # Then he validates
        # A message informs him of the new record.

