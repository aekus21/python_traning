from pytest_bdd import scenario
from .group_steps import *


@scenario('groups.feature', 'Add new group')
def test_add_new_group():
    pass

@scenario('groups.feature', 'Delete group')
def test_delete_group():
    pass