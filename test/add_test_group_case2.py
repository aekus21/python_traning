# -*- coding: utf-8 -*-
import pytest
from fixture.application import Application
from model.group import Group

@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_group(app):
    app.session.login_form("admin", "secret")
    app.group.create(Group("test_group2", "test_header_2", "test_footer_2"))
    app.session.logout()

def test_add_empty_group(app):
    app.session.login_form("admin", "secret")
    app.group.create(Group("", "", ""))
    app.session.logout()