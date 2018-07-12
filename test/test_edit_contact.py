from model.contact import Contact
from fixture.contact import *


def test_edit_first_contact(app):
    if (app.contact.count_contacts() == 0):
        app.contact.add_contact(Contact(first_name="first_name1", last_name="last_name1"))
    old_contacts = app.contact.get_contact_list()
    app.contact.edit_first_contact(Contact(first_name="first_name5", last_name="last_name5"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
