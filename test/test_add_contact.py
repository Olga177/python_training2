from model.contact import Contact


def test_add_contact(app):
    app.contact.add_contact(Contact(first_name="first_name", last_name="last_name",
                                    address="address", mobile_phone="mobile_phone", email="email"))
    app.session.logout()


def test_add_empty_contact(app):
    app.contact.add_contact(Contact(first_name="", last_name="", address="", mobile_phone="", email=""))
    app.session.logout()
