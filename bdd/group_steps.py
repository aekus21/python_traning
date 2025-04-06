from pytest_bdd import given, when, then, parsers
from model.group import Group
import random

@given('a group list', target_fixture='group_list')
def group_list(db):
    return db.get_group_list()

@given(parsers.parse('a new group with {name}, {header} and {footer}'), target_fixture='new_group')
def new_group(name, header, footer):
    return Group(name=name, header=header, footer=footer)

@when('I add the group to the list', target_fixture='add_new_group')
def add_new_group(app, new_group):
    app.group.create(new_group)

@then('the new group list is equal to the old list with added group', target_fixture='verify_group_added')
def verify_group_added(db, group_list, new_group):
    old_groups = group_list
    new_groups = db.get_group_list()
    old_groups.append(new_group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

@given('a non-empty group list', target_fixture='non_empty_group_list')
def non_empty_group_list(db, app):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name='name', header='header', footer='footer'))
    return db.get_group_list()

@given('a random group from the list', target_fixture='random_group')
def random_group(non_empty_group_list):
    return random.choice(non_empty_group_list)

@when('I delete the group from the list', target_fixture='delete_group')
def delete_group(app, random_group):
    app.group.delete_group_by_id(random_group.id)

@then('the new group list is equal to the old list without deleted group', target_fixture='verify_group_deleted')
def verify_group_deleted(db, non_empty_group_list, random_group, check_ui):
    old_groups = non_empty_group_list
    new_groups = db.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
    old_groups.remove(random_group)
    assert old_groups == new_groups
    db_list = filter(lambda x: x is not None, (db.get_group_list()))
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)
