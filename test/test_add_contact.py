from model.contact import Contact
import pytest
import random
import string
import data.contacts as json_contacts



def test_add_contact(app, json_contacts):
    contact = json_contacts
    old_contacts = app.contact.create_contact_list()
    app.contact.add_contact(contact)
    assert (len(old_contacts) + 1) == app.contact.count_contacts()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key= Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
