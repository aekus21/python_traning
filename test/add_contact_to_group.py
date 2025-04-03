import random
import re
import select
from tkinter.tix import Select

from fixture.orm import ORMFixture
from model.group import Group
from model.contact import Contact

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
        group_id = group.id
        contact_in_group = db_connect.get_contacts_in_group(group)
        contact = random.choice(contact_in_group)
        cont_id = contact.id
        app.open_homepage()
        app.wd.find_element_by_name('group').click()
        app.wd.find_element_by_xpath("//option[@value='%s']" % group_id).click()
        app.contact.select_contact_by_id(cont_id)
        app.wd.find_element_by_name('remove').click()
        app.open_homepage()

    finally:
        pass


def clear_space(s):
    return re.sub('  ', ' ', s.strip())