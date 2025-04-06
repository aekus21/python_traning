from pytest_bdd import given, when, then, parsers
from model.group import Group


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