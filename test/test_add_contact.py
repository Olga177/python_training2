from model.contact import Contact
from fixture.application import Application
import pytest

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.add_contact(Contact(first_name="first_name", last_name="last_name",
                                    address="address", mobile_phone="mobile_phone", email="email"))
    app.session.logout()


def test_add_empty_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.add_contact(Contact(first_name="", last_name="", address="", mobile_phone="", email=""))
    app.session.logout()
