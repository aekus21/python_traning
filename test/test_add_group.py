# -*- coding: utf-8 -*-
from model.group import Group

def test_add_group(app):
    app.session.login_form("admin", "secret")
    app.group.create(Group("test_group2", "test_header_2", "test_footer_2"))
    app.session.logout()

def test_add_empty_group(app):
    app.session.login_form("admin", "secret")
    app.group.create(Group("", "", ""))
    app.session.logout()