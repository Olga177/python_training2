
from model.contact import Contact
import random
import fixture.db


def test_edit_some_contact(app,db,json_contacts):
    if len(db.get_contact_list()) == 0:
        app.contact.add_contact(Contact(first_name="first_name1", last_name="last_name1"))
    # Save contacts list before editing
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.edit_contact_by_id(contact.id, contact)
    new_contacts = db.get_contacts_list()
    assert len(old_contacts) == len(new_contacts)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
