class ContactHelper:
    def __init__(self, app):
        self.app = app

    def open_new_entry_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def back_home(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()

    def add_contact(self, contact):
        wd = self.app.wd
        # Open add contact page
        self.open_new_entry_page()
        # Populate contact form
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.first_name)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.last_name)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.address)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact.mobile_phone)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.email)
        # Submitting contact form
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def edit_first_contact(self, contact):
        wd = self.app.wd
        # Select first contact
        wd.find_element_by_name("selected[]").click()
        # Find edit element and click it to open edit form
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()
        # Populate edit contact form
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.first_name)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.last_name)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.address)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact.mobile_phone)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.email)
        # Submitting contact form
        wd.find_element_by_xpath("//div[@id='content']/form[1]/input[1]").click()
        self.back_home()

    def delete_first_contact(self):
        wd = self.app.wd
        self.back_home()
        # Select first contact
        wd.find_element_by_name("selected[]").click()
        # Delete first contact
        # Click edit icon then click delete button
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()
        wd.find_element_by_xpath("//div[@id='content']/form[2]/input[2]").click()
        # wd.switch_to_alert().accept()
        self.back_home()
