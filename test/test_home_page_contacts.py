from model.contact import Contact
import re

# def test_phones_on_home_page(app):
#     list_of_contacts_from_home_page = app.contact.get_contact_list()
#     index = randrange(len(list_of_contacts_from_home_page))
#     contact_from_home_page = list_of_contacts_from_home_page[index]
#     contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
#     assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)


def test_names_and_address(app, db):
    list_of_contacts_from_home_page_ui = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    list_of_contacts_from_home_page_db = sorted(db.get_contact_list(), key=Contact.id_or_max)
    length_ui = len(list_of_contacts_from_home_page_ui)
    length_db = len(list_of_contacts_from_home_page_db)
    if not (length_ui == length_db):
        return print("Different amount of Contacts on UI and in database, "
                     "'length_ui = ', length_ui, 'length_db = ', length_db ")
    else:
        for i in range(length_ui):
            contact_ui = list_of_contacts_from_home_page_ui[i]
            print('contact_ui = ', contact_ui)
            contact_db = list_of_contacts_from_home_page_db[i]
            print('contact_db = ', contact_db)
            assert clear(contact_ui.first_name) == clear(contact_db.first_name)
            assert clear(contact_ui.last_name) == clear(contact_db.last_name)
            if not ((contact_ui.address =="") or (contact_db.address == None)):
                assert clear(contact_ui.address) == clear(contact_db.address)

# def test_emails_on_home_page(app):
#     list_of_contacts_from_home_page = app.contact.get_contact_list()
#     index = randrange(len(list_of_contacts_from_home_page))
#     contact_from_home_page = list_of_contacts_from_home_page[index]
#     contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
#     assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_homepage(contact_from_edit_page)

def clear(s):
    return re.sub("[() -]","",s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "", map(lambda x: clear(x), filter(lambda x: x is not None,
                                                                              [contact.home_phone, contact.work_phone,
                                                                               contact.mobile_phone,
                                                                               contact.secondary_phone]))))


def merge_emails_like_on_homepage(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.email1, contact.email2, contact.email3]))))