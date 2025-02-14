import pytest
from fixture.application import Application


@pytest.fixture(scope= 'session')
def app(request):
    fixture = Application()
    fixture.session.login_form("admin", "secret")
    request.addfinalizer(fixture.destroy)
    return fixture