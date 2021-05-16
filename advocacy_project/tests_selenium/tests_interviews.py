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


class AdvocacyTopicTest(LiveServerTestCase):
    fixtures = ['communities.json', 'teams.json', 'groups.json', 'users.json' ]

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
        self.browser.maximize_window()
        # From the beginning the advocacy coordinator is logged-in
        self.browser.find_element_by_id("header-connection").click()
        user_input = self.browser.find_element_by_id("id_username")
        user_input.send_keys('leila')
        user_input_pwd = self.browser.find_element_by_id("id_password")
        user_input_pwd.send_keys('@dmin1234')
        self.browser.find_element_by_xpath('//input[@type="submit"]').click()
        # The homepage dedicated to connected people is different
        # S. opens the "support documentation" page
        self.browser.find_element_by_id('link-support-docs').click()
        # Then a label "add a Topic" is displayed
        # S. clicks on this item
        self.browser.find_element_by_xpath("//button[@type='submit']").click()
        # Then a window with several fields is displayed
        # S. fills, or selects the following fields:
        # A topic
        self.browser.find_element_by_xpath("//option[@value='Emploi']").click()
        # A key statement
        user_input = self.browser.find_element_by_id('id_key_statement')
        user_input.send_keys("Le travail c'est la santé")
        # The name of the source
        user_input = self.browser.find_element_by_id('id_source_title')
        user_input.send_keys("Henri Salvador")
        # A link to the source
        user_input = self.browser.find_element_by_id('id_source')
        user_input.send_keys("https://www.youtube.com/watch?v=B5VyRmrN0-Q")
        # Quote to be used as a support
        user_input = self.browser.find_element_by_id('id_quote')
        user_input.send_keys("Ne rien faire c'est la conserver")
        # L. decides that the topic is activated
        self.browser.find_element_by_xpath("//select[@id='id_is_active']/option[@value='true']")
        # Then he validates
        self.browser.find_element_by_xpath("//input[@id='create-topic']").click()
        # Then L. is back on the topic list, with the new topic listed
        self.browser.find_element_by_id("topic-list")

class InterviewTest(LiveServerTestCase):
    fixtures = ['communities.json', 'teams.json', 'groups.json', 'users.json' ]

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.browser = Firefox()
        cls.browser.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()
        super().tearDownClass()

    def test_plaid_11_access_the_interviews(self):
        """
            The manager wants to access the interviews
            and check their status.
            He will be able to access the details of each interview.
            The persona is named Leila
           
        """
        self.browser.get(os.path.join(self.live_server_url, ''))
        self.browser.find_element_by_id("header-connection").click()
        user_input = self.browser.find_element_by_id("id_username")
        user_input.send_keys('leila')
        user_input_pwd = self.browser.find_element_by_id("id_password")
        user_input_pwd.send_keys('@dmin1234')
        self.browser.find_element_by_xpath('//input[@type="submit"]').click()
        # The homepage dedicated to connected people is different
        # Once connected, Leila has access to a menu bar.
        self.browser.find_element_by_id('link-interviews').click()
        # L. clicks on interviews.
        # Then L. sees the list of Interviews.
        # The interviews are ordered by status (pending, etc) and by date
        # For every interview she can see several fields:
        # The name of the targeted official
        # The name of the assigned volunteer
        # The date of the interview
        # Then L. clicks on an item
        # And she gets to a page displaying the details

