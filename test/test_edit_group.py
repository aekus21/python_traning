# -*- coding: utf-8 -*-
from model.group import Group

def test_edit_group(app):
    app.group.edit_first_group(Group(name='new_ed333it_Svyatoslav'))
    app.group.save_new_group_data()