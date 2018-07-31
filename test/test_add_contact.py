from model.contact import Contact


def test_add_contact(app,db,json_contacts):
    contact = json_contacts
    print('in test_add_contact: contact = ', contact)
    old_contacts = db.get_contact_list()
    print(' in test_add_contact: old contacts = ', old_contacts)
    app.contact.add_contact(contact)
    new_contacts = db.get_contact_list()
    print(' in test_add_contact: new contacts = ', new_contacts)
    old_contacts.append(contact)
    print(' in test_add_contact: SORTED old contacts = ', sorted(old_contacts, key= Contact.id_or_max))
    print(' in test_add_contact: SORTED new contacts = ', sorted(new_contacts, key=Contact.id_or_max))
    # assert sorted(old_contacts, key= Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

