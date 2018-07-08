from model.contact import Contact

def test_delete_first_contact(app):
    if app.contact.count_contacts() == 0:
        app.contact.add_contact(Contact(first_name="first_name", last_name="last_name",
                                        address="address", mobile_phone="mobile_phone", email="email"))
    app.contact.delete_first_contact()

