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
        self.contact_cache = None


    def edit_contact_by_index(self,index, new_contact):
        wd = self.app.wd
        # Open home page
        self.back_home()
        # Select first contact
        self.select_contact_by_index(index)
        # Find edit element and click it to open edit form
        self.select_edit_button_by_index(index)
        # Populate edit contact form
        self.fill_contact_form(new_contact)
        # Submitting updated contact form
        wd.find_element_by_xpath("//div[@id='content']/form[1]/input[1]").click()
        self.back_home()
        self.contact_cache = None

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        # Open home page
        self.back_home()
        # Select first contact
        self.select_contact_by_index(index)
        # Delete first contact
        # Click edit icon then click delete button
        self.select_edit_button_by_index(index)
        wd.find_element_by_xpath("//div[@id='content']/form[2]/input[2]").click()
        # wd.switch_to_alert().accept()
        self.back_home()
        self.contact_cache = None


    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def select_contact_by_index(self, index):
        wd = self.app.wd
        element = wd.find_elements_by_name("entry")[index]
        element.click()

    def select_edit_button_by_index(self, index):
        wd = self.app.wd
        element1 = wd.find_elements_by_name("entry")[index]
        # Find elements inside element with the name "entry"
        elementList = element1.find_elements_by_tag_name("td")
        element2 = elementList[7]
        element2.find_element_by_tag_name('img').click()

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

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.back_home()
            self.contact_cache = []
            # Find all elements with the name "entry"
            for element in wd.find_elements_by_name("entry"):
                # Find elements inside element with the name "entry"
                element1 = element.find_element_by_name("selected[]")
                elementList = element.find_elements_by_tag_name("td")
                element2 = elementList[1]
                element3 = elementList[2]
                ln = element2.text
                fn = element3.text
                id = element1.get_attribute('value')
                self.contact_cache.append(Contact(first_name=fn, last_name=ln, id=id))
        return list(self.contact_cache)
