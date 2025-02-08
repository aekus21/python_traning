# -*- coding: utf-8 -*-
from model.group import Group

def test_edit_group(app):
    app.session.login_form("admin", "secret")
    app.edit_group.edit_first_group()
    app.edit_group.change_group_data((Group('new_edit_Svyatoslav',
                                             'new_data',
                                             'test_group2')))
    app.edit_group.save_new_group_data()
    app.session.logout()