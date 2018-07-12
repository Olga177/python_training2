from model.contact import Contact

class ContactHelper:
    def __init__(self, app):
        self.app = app

    def open_new_entry_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()


    def back_home(self):
        wd = self.app.wd
        if (self.amount_of_all_email_elements() < 1):
            wd.find_element_by_link_text("home").click()

    def amount_of_all_email_elements(self):
        wd = self.app.wd
        return (len(wd.find_elements_by_xpath("//table[@id='maintable']")))

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

    def get_contact_list(self):
        wd = self.app.wd
        # Go to home page
        self.back_home()
        contacts = []
        for element in wd.find_elements_by_name("selected[]"):
            # text = element.text
            text = element.get_attribute('title')
            ln = text[8:19]
            fn = text [19:30]
            id = element.get_attribute('value')
            # print('8888888888888 text = ', text, '8888888   id = ', id)
            print('8888888888888 ln = ', ln, '8888888   fn = ', fn)
            contacts.append(Contact(first_name=fn, last_name=ln, id=id))
            # print ('************  contacts = ', contacts)
            print ('^^^^^^^^^  length of contacts = ', len(contacts))
        return contacts
