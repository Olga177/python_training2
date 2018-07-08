from model.contact import Contact


def test_edit_first_contact(app):
    if app.contact.count_contacts() == 0:
        app.contact.add_contact(Contact(first_name="first_name", last_name="last_name",
                                        address="address", mobile_phone="mobile_phone", email="email"))
    app.contact.edit_first_contact(Contact(first_name="new_first_name", last_name="new_last_name",
                                    address="new_address", mobile_phone="new_mobile_phone", email="new_email"))
