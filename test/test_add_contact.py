from model.contact import Contact
from fixture.contact import *


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    print ('888888888888 old contacts', len(old_contacts))
    app.contact.add_contact(Contact(first_name="first_name4", last_name="last_name4"))
    new_contacts = app.contact.get_contact_list()
    print('888888888888 new contacts', len(new_contacts))
    assert (len(old_contacts) + 1) == len (new_contacts)

# def test_add_empty_contact(app):
#     app.contact.add_contact(Contact(first_name="", last_name="", address="", mobile_phone="", email=""))

