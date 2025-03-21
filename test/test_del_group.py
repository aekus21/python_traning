import random
from model.group import Group


def test_delete_some_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group('new_test_group', 'header', 'footer'))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    app.group.delete_group_by_id(group.id)
    new_groups = db.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
    old_groups.remove(group)
    assert old_groups == new_groups
    db_list = filter(lambda x: x is not None, (db.get_group_list()))
    if check_ui:
        assert sorted(new_groups, key = Group.id_or_max) == sorted(db_list, key= Group.id_or_max)

