from model.group import Group
from model.contact import Contact
import re

def test_group_list(app, db):
    ui_list = app.group.get_group_list()
    def clean(group):
        s = re.sub('  ', ' ', group.test_name)
        return Group(ids=group.id, name=s.strip())
    db_list = map(clean, filter(lambda x: x is not None, (db.get_group_list())))
    assert sorted(ui_list, key= Group.id_or_max) == sorted(db_list, key= Group.id_or_max)


def test_contact_list(app, db):
    ui_list = app.contact.get_contact_list()
    def clean(contact):
        s = re.sub('  ', ' ', contact.last_name)
        return Contact(ids=contact.id, lname=s.strip())
    db_list = map(clean, (filter(lambda x: x is not None, (db.get_contact_list()))))
    assert sorted(ui_list, key= Contact.id_or_max) == sorted(db_list, key= Contact.id_or_max)