# -*- coding: utf-8 -*-
from model.group import Group

def test_edit_group(app):
    app.group.edit_first_group()
    app.group.change_group_data((Group('new_edit_Svyatoslav',
                                             'new_data',
                                             'test_group2')))
    app.group.save_new_group_data()
    app.session.logout()