# -*- coding: utf-8 -*-
from model.group import Group

def test_edit_group(app):
    if app.group.count() == 0:
        app.group.create(Group('header', 'footer', 'toto'))
    app.group.edit_first_group(Group(name='new_ed333it_Svyatoslav', footer='nono__toto'))
