from fixture.application import Application
import pytest


@pytest.fixture
def app(request):
    fixture = Application()
    fixture.session.login(username="admin", password="secret")
    request.addfinalizer(fixture.destroy)
    return fixture
