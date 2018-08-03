from model.contact import Contact
import random


def test_edit_some_contact(app, db, check_ui):
    contact_replacement = Contact(first_name = 'first_name99', last_name = 'last_name99')
    if len(db.get_contact_list()) == 0:
        app.contact.add_contact(Contact(first_name='test', last_name = 'test'))
    # Save contacts list before editing
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.edit_contact_by_id(contact.id, contact_replacement)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key= Contact.id_or_max)


    # assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

