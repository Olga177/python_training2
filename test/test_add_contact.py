from model.contact import Contact
import pytest
import random
import string
from data.add_contact import constant as test_data


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


test_data = [Contact(first_name="", last_name="", address="",
                     home_phone="", mobile_phone="",
                     work_phone="", secondary_phone="",
                     email1="", email2="", email3="", )] + [
                Contact(first_name=random_string("first_name1", 5), last_name=random_string("last_name1", 5),
                        address=random_string("address1", 5),
                        home_phone=random_string("home_phone1", 5), mobile_phone=random_string("mobile_phone1", 5),
                        work_phone=random_string("work_phone1", 5),
                        secondary_phone=random_string("secondary_phone1", 5),
                        email1=random_string("email1", 5), email2=random_string("email2", 5),
                        email3=random_string("email3", 5))
                for i in range(5)
            ]

@pytest.mark.parametrize("contact", test_data, ids=[repr(x) for x in test_data])

def test_add_contact(app, contact):
    old_contacts = app.contact.create_contact_list()
    app.contact.add_contact(contact)
    assert (len(old_contacts) + 1) == app.contact.count_contacts()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key= Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
