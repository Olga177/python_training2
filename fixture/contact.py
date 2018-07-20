from model.contact import Contact
import re

class ContactHelper:
    def __init__(self, app):
        self.app = app

    def open_new_entry_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()


    def open_home_page(self):
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

    def edit_contact_first_group(self):
        self.edit_contact_by_index(0)

    def edit_contact_by_index(self,index, new_contact):
        wd = self.app.wd
        # Open home page
        self.open_home_page()
        # Select first contact
        self.select_contact_by_index(index)
        # Find edit element and click it to open edit form
        self.select_edit_button_by_index(index)
        # Populate edit contact form
        self.fill_contact_form(new_contact)
        # Submitting updated contact form
        wd.find_element_by_xpath("//div[@id='content']/form[1]/input[1]").click()
        self.open_home_page()
        self.contact_cache = None

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        # Open home page
        self.open_home_page()
        # Select first contact
        self.select_contact_by_index(index)
        # Delete first contact
        # Click edit icon then click delete button
        self.select_edit_button_by_index(index)
        wd.find_element_by_xpath("//div[@id='content']/form[2]/input[2]").click()
        # wd.switch_to_alert().accept()
        self.open_home_page()
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
        self.open_home_page()
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
        self.change_contact_field_value("home", contact.home_phone)
        self.change_contact_field_value("mobile", contact.mobile_phone)
        self.change_contact_field_value("work", contact.work_phone)
        self.change_contact_field_value("phone2", contact.secondary_phone)
        self.change_contact_field_value("email", contact.email1)
        self.change_contact_field_value("email2", contact.email2)
        self.change_contact_field_value("email3", contact.email3)

    contact_cache = None

    def create_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_home_page()
            self.contact_cache = []
            # Find all elements with the name "entry"
            for element in wd.find_elements_by_name("entry"):
                # Find elements inside element with the name "entry"
                element1 = element.find_element_by_name("selected[]")
                elementList = element.find_elements_by_tag_name("td")
                last_name = elementList[1].text
                first_name = elementList[2].text
                address = elementList[3].text
                all_phones = elementList[4].text
                all_emails = elementList[5].text
                id = element1.get_attribute('value')
                self.contact_cache.append(Contact(first_name=first_name, last_name=last_name, address=address, id=id,
                                                  all_phones_from_home_page=all_phones,
                                                  all_emails_from_home_page=all_emails))

        return list(self.contact_cache)

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.contact_cache = []
            # Find all elements with the name "entry"
            for row in wd.find_elements_by_name("entry"):
                # Find elements inside element with the name "entry"
                cells = row.find_elements_by_tag_name("td")
                last_name = cells[1].text
                first_name = cells[2].text
                id = cells[0].find_element_by_tag_name('input').get_attribute('value')
                address = cells[3].text
                all_phones = cells[5].text
                all_emails = cells[4].text
                self.contact_cache.append(Contact(first_name=first_name, last_name=last_name,
                                                  address=address, id=id,
                                                  all_phones_from_home_page=all_phones,
                                                  all_emails_from_home_page=all_emails))
        return list(self.contact_cache)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name('entry')[index]
        # Open Edit (in the 7th cell)
        cell = row.find_elements_by_tag_name('td')[7]
        cell.find_element_by_tag_name('a').click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name('entry')[index]
        cell = row.find_elements_by_tag_name('td')[6]
        cell.find_element_by_tag_name('a').click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        first_name = wd.find_element_by_name('firstname').get_attribute('value')
        last_name = wd.find_element_by_name('lastname').get_attribute('value')
        address = wd.find_element_by_name('address').get_attribute('value')
        id = wd.find_element_by_name('id').get_attribute('value')
        home_phone = wd.find_element_by_name('home').get_attribute('value')
        work_phone = wd.find_element_by_name('work').get_attribute('value')
        mobile_phone = wd.find_element_by_name('mobile').get_attribute('value')
        secondary_phone = wd.find_element_by_name('phone2').get_attribute('value')
        email1 = wd.find_element_by_name('email').get_attribute('value')
        email2 = wd.find_element_by_name('email2').get_attribute('value')
        email3 = wd.find_element_by_name('email3').get_attribute('value')
        return Contact(first_name=first_name, last_name=last_name, address=address, id=id,
                       home_phone=home_phone, mobile_phone=mobile_phone,
                       work_phone=work_phone, secondary_phone=secondary_phone,
                       email1=email1, email2=email2, email3=email3)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id('content').text
        home_phone = re.search("H: (.*)", text).group(1)
        work_phone = re.search("W: (.*)", text).group(1)
        mobile_phone = re.search("M: (.*)", text).group(1)
        secondary_phone = re.search("P: (.*)", text).group(1)
        return Contact(home_phone=home_phone, mobile_phone=mobile_phone,
                       work_phone=work_phone, secondary_phone=secondary_phone)
