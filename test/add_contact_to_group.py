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
        groups = db_connect.get_group_list()
        group = random.choice(groups)
        contact_in_group = db_connect.get_contacts_in_group(group)
        if len(contact_in_group) == 0:
            all_users = db_connect.get_contact_list()
            contact = random.choice(all_users)
            app.contact.add_contact_to_group(contact.id, group.id)
        contacts_in_group = db_connect.get_contacts_in_group(group)
        contact_to_del = random.choice(contacts_in_group)
        v = contact_to_del.id


        group_list = db_connect.get_group_list()
        group = random.choice(group_list)
        contact_in_group = db_connect.get_contacts_in_group(group)
        v = random.choice(contact_in_group)
        ide = v.id
        print(contact_in_group)
        # l = db_connect.get_contacts_in_group(Group(ids=group.id))
        app.open_homepage()
        app.wd.find_element_by_name('group').click()
        app.wd.find_element_by_xpath("//option[@value='%s']" % g)
        v = select.find_element_by_tag_name('option').value_of_css_property('g')
        # v = Select(app.wd.find_element_by_name('group').get_attribute('value'))
        print(v)
    finally:
        pass


def clear_space(s):
    return re.sub('  ', ' ', s.strip())