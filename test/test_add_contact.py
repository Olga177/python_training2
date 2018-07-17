from model.contact import Contact
from model.group import *

def test_add_contact(app):
    old_contacts = app.contact.create_contact_list()
    contact = Contact(first_name="first_name4", last_name="last_name4")
    app.contact.add_contact(contact)
    assert (len(old_contacts) + 1) == app.contact.count_contacts()
    # new_contacts = app.contact.get_contact_list()
    # old_contacts.append(contact)
    # assert sorted(old_contacts, key= Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

# def test_add_empty_contact(app):
# #     old_contacts = app.contact.get_contact_list()
# #     app.contact.add_contact(Contact(first_name="", last_name=""))
# #     assert (len(old_contacts) + 1) == app.contact.count_contacts()
# #     new_contacts = app.contact.get_contact_list()