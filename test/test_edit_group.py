# -*- coding: utf-8 -*-
from model.group import Group
from random import randrange

def test_edit_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name='tetst'))
    old_groups = db.get_group_list()
    group = Group(name='new_edit_Svyatoslav', footer='nono__toto')
    index = randrange(len(old_groups))
    group.id = old_groups[index].id
    app.group.edit_group_by_id(group.id, group)
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[index] = group
    db_list = filter(lambda x: x is not None, (db.get_group_list()))
    assert sorted(old_groups, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)
    if check_ui:
        assert sorted(old_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)