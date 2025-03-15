from selenium import webdriver
from fixture.contact import ContactHelper
from fixture.session import SessionHelper
from fixture.group import GroupHelper


class Application:
    def __init__(self, browser='firefox'):
        if browser == 'firefox':
            self.wd = webdriver.Firefox
        elif browser == 'chrome':
            self.wd = webdriver.Chrome
        elif browser == 'ie':
            self.wd = webdriver.Ie
        else:
            raise ValueError('Unrecognized browser %s' % browser)
        # self.wd = webdriver.Firefox()
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_homepage(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()