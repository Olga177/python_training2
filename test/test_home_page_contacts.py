from model.contact import Contact
import re


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
            contact_db = list_of_contacts_from_home_page_db[i]
            assert clear(contact_ui.first_name) == clear(contact_db.first_name)
            assert clear(contact_ui.last_name) == clear(contact_db.last_name)
            if not ((contact_ui.address == "") or (contact_db.address == None)):
                assert clear(contact_ui.address) == clear(contact_db.address)
            if not ((contact_ui.all_emails_from_home_page == "") or (
                    merge_emails_like_on_home_page(contact_db) == None)):
                assert clear(contact_ui.all_emails_from_home_page) == clear(merge_emails_like_on_home_page(contact_db))
            if not ((contact_ui.all_phones_from_home_page == "") or (
                    merge_phones_like_on_home_page(contact_db) == None)):
                assert clear(contact_ui.all_phones_from_home_page) == clear(merge_phones_like_on_home_page(contact_db))


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.home_phone, contact.mobile_phone, contact.work_phone,
                                        contact.secondary_phone]))))


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.email1, contact.email2, contact.email3]))))
