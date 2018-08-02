from model.contact import Contact
from fixture.contact import *
import  random


def test_delete_some_contact(app,db,check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.add_contact(Contact(first_name="first_name1", last_name="last_name1"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
    new_contacts = db.get_contact_list()
    assert (len(old_contacts) - 1) == len(new_contacts)
    old_contacts.remove(contact)
    assert sorted(old_contacts, key= Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key= Contact.id_or_max)






