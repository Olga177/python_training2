# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import  unittest


def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False


class test_add_group2(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver(capabilities={"marionette": False},
                            firefox_binary="C:\Program Files\Mozilla Firefox ESR/firefox.exe")
        self.wd.implicitly_wait(60)

    def test_test_add_group2(self):
        success = True
        wd = self.wd
        # Open Home page
        wd.get("http://localhost/addressbook/")
        # Login
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("admin")
        wd.find_element_by_xpath("//form[@id='LoginForm']//label[.='Password:']").click()
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("secret")
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()
        # Open group page
        wd.find_element_by_link_text("groups").click()
        # Add new group
        wd.find_element_by_name("new").click()
        # Populate group form
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys("group_name")
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys("group_header")
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys("group_footer")
        # Submitting group form
        wd.find_element_by_name("submit").click()
        # Open group page
        wd.find_element_by_link_text("groups").click()
        # Add new group
        wd.find_element_by_name("new").click()
        # Populate group form
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys("group_name")
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys("group_header")
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys("group_footer")
        # Submitting group form
        wd.find_element_by_name("submit").click()
        # Open group page
        wd.find_element_by_link_text("groups").click()
        # Logout
        wd.find_element_by_link_text("Logout").click()
        self.assertTrue(success)

    def tearDown(self):
        self.wd.quit()


if __name__ == '__main__':
    unittest.main()
