from model.contact import Contact
from fixture.contact import *
from random import randrange


def test_delete_some_contact(app):
    if (app.contact.count_contacts() == 0):
        app.contact.add_contact(Contact(first_name="first_name1", last_name="last_name1"))
    old_contacts = app.contact.create_contact_list()
    index = randrange(len(old_contacts))
    app.contact.delete_contact_by_index(index)
    assert (len(old_contacts) - 1) == app.contact.count_contacts()
    new_contacts = app.contact.create_contact_list()
    old_contacts[index :index +1]=[]
    assert sorted(old_contacts, key= Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)




