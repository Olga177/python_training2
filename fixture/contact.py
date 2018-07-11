class ContactHelper:
    def __init__(self, app):
        self.app = app

    def open_new_entry_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()


    def back_home(self):
        wd = self.app.wd
        if (self.amount_of_elements() < 1):
            wd.find_element_by_link_text("home").click()

    def amount_of_elements(self):
        wd = self.app.wd
        amount = (len(wd.find_elements_by_xpath("//table[@id='maintable']")))
        return amount

    def add_contact(self, contact):
        wd = self.app.wd
        # Open add contact page
        self.open_new_entry_page()
        # Populate contact form
        self.fill_contact_form(contact)
        # Submitting contact form
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()


    def edit_first_contact(self, contact):
        wd = self.app.wd
        # Select first contact
        self.select_first_contact()
        # Find edit element and click it to open edit form
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()
        # Populate edit contact form
        self.fill_contact_form(contact)
        # Submitting contact form
        wd.find_element_by_xpath("//div[@id='content']/form[1]/input[1]").click()
        self.back_home()


    def delete_first_contact(self):
        wd = self.app.wd
        self.back_home()
        # Select first contact
        self.select_first_contact()
        # Delete first contact
        # Click edit icon then click delete button
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()
        wd.find_element_by_xpath("//div[@id='content']/form[2]/input[2]").click()
        # wd.switch_to_alert().accept()
        self.back_home()


    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()


    def count_contacts(self):
        wd = self.app.wd
        self.back_home()
        return len(wd.find_elements_by_name("selected[]"))


    def change_contact_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)


    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_contact_field_value("firstname", contact.first_name)
        self.change_contact_field_value("lastname", contact.last_name)
        self.change_contact_field_value("address", contact.address)
        self.change_contact_field_value("mobile", contact.mobile_phone)
        self.change_contact_field_value("email", contact.email)

