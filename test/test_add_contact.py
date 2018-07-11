from model.contact import Contact


def test_add_contact(app):
    app.contact.add_contact(Contact(first_name="added_name", last_name="added last name", address="added address",
                                    mobile_phone="added_mobile_phone", email="added email"))

# def test_add_empty_contact(app):
#     app.contact.add_contact(Contact(first_name="", last_name="", address="", mobile_phone="", email=""))

