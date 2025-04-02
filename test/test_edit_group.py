# -*- coding: utf-8 -*-
from model.group import Group
from random import randrange

def test_edit_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group('header', 'footer', 'toto'))
    old_groups = db.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name='new_edit_Svyatoslav', footer='nono__toto')
    group.id = old_groups[index].id
    app.group.edit_group_by_index(index, group)
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[index] = group
    if check_ui:
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)