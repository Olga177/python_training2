from model.contact import Contact
from random import randrange


def test_edit_some_contact(app):
    if (app.contact.count_contacts() == 0):
        app.contact.add_contact(Contact(first_name="first_name1", last_name="last_name1"))
    # Save contacts list before editing
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(first_name="first_name6", last_name="last_name6")
    contact.id = old_contacts[index].id
    # Edit with 'new contact' data
    app.contact.edit_contact_by_index(index,contact)
    # Get new list of contacts after editing
    assert len(old_contacts) == app.contact.count_contacts()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key= Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)



# def test_modify_group_name(app):
#     old_groups = app.group.get_group_list()
#     group = Group(name="new_name")
#     group.id = old_groups[0].id
#     app.group.modify_first_group(group)
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == app.group.count()
#     old_groups[0] = group
#     assert sorted(old_groups, key= Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
