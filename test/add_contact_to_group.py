import random
import re
from tkinter.tix import Select

from fixture.orm import ORMFixture
from model.group import Group

db_connect = ORMFixture(host = '127.0.0.1', database = 'addressbook', user = 'root', password='')

def test_add_contact_to_group(app, db):
    contact_list = db.get_contact_list()
    contact = random.choice(contact_list)
    group_list = db.get_group_list()
    group = random.choice(group_list)
    app.contact.add_contact_to_group(contact.id, clear_space(group.test_name))
    print(group.test_name)



def test_del_contact_from_group(app, db):
    try:
        group_list = db.get_group_list()
        group = random.choice(group_list)
        g =group.id
        l = db_connect.get_contacts_in_group(Group(ids=group.id))
        app.open_homepage()
        app.wd.find_element_by_name('group').click()
        v = Select(app.wd.find_element_by_name('group').get_attribute('value'))
        print(v)
    finally:
        pass


def clear_space(s):
    return re.sub('  ', ' ', s.strip())