# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest
from group import Group


class AddTestGroup2(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def open_homepage(self, wd):
        wd.get("http://localhost/addressbook/")

    def login_form(self, wd, username, password):
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_groups_page(self, wd):
        # open group page
        wd.find_element_by_link_text("groups").click()

    def create_group(self, wd, group):
        # create new group
        wd.find_element_by_name("new").click()
        # fill group info
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.test_name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.test_header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.test_footer)
        # submit new group
        wd.find_element_by_name("submit").click()

    def return_group_page(self, wd):
        wd.find_element_by_link_text("groups").click()

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def test_add_group(self):
        wd = self.wd
        self.open_homepage(wd)
        self.login_form(wd, "admin", "secret")
        self.open_groups_page(wd)
        self.create_group(wd, Group("test_group2", "test_header_2", "test_footer_2"))
        self.return_group_page(wd)
        self.logout(wd)

    def test_add_empty_group(self):
        wd = self.wd
        self.open_homepage(wd)
        self.login_form(wd, "admin", "secret")
        self.open_groups_page(wd)
        self.create_group(wd, Group(" ", " ", " "))
        self.return_group_page(wd)
        self.logout(wd)

    def is_element_present(self, how, what):
        try: self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.wd.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()
