# -*- coding: utf-8 -*-
import pytest
from application import Application
from group import Group

@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_group(app):
    app.login_form("admin", "secret")
    app.create_group(Group("test_group2", "test_header_2", "test_footer_2"))
    app.logout()

def test_add_empty_group(app):
    app.login_form("admin", "secret")
    app.create_group(Group("", "", ""))
    app.logout()