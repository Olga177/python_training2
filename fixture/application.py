from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper


class Application:

    def __init__(self, browser, base_url):
        if browser == "firefox":
            self.wd = webdriver.Firefox(
                capabilities={"marionette": False},
                firefox_binary='C:\Program Files\Mozilla Firefox ESR/firefox.exe')
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser %s" % browser)

        # self.wd.implicitly_wait(10)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        if (self.amount_of_elements() < 1):
            wd.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()

    def amount_of_elements(self):
        wd = self.wd
        return (len(wd.find_elements_by_xpath("//table[@id='maintable']")))

