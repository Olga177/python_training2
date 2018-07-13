from model.contact import Contact
from fixture.contact import *


def test_delete_first_contact(app):
    if (app.contact.count_contacts() == 0):
        app.contact.add_contact(Contact(first_name="first_name1", last_name="last_name1"))
    old_contacts = app.contact.get_contact_list()
    app.contact.delete_first_contact()
    assert (len(old_contacts) - 1) == app.contact.count_contacts()
    new_contacts = app.contact.get_contact_list()
    old_contacts[0:1]=[]
    assert sorted(old_contacts, key= Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)




