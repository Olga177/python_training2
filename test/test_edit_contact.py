from model.contact import Contact


def test_edit_first_contact(app):

    app.contact.edit_first_contact(Contact(first_name="first_name2", last_name="last_name2",
                                    address="address2", mobile_phone="mobile_phone2", email="email2"))
    app.session.logout()