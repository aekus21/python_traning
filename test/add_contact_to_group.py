import random
import re
import select

from fixture.orm import ORMFixture


db_connect = ORMFixture(host = '127.0.0.1', database = 'addressbook', user = 'root', password='')

def test_add_contact_to_group(app, db):
    contact_list = db.get_contact_list()
    contact = random.choice(contact_list)
    group_list = db.get_group_list()
    group = random.choice(group_list)
    app.contact.add_contact_to_group(contact.id, group.id)
    print(group.test_name)



def test_del_contact_from_group(app, db):
        group_list = db_connect.get_group_list()
        group = random.choice(group_list)
        group_id = group.id
        contact_in_group = db_connect.get_contacts_in_group(group)
        if len(contact_in_group) == 0:
            contact_list = db_connect.get_contact_list()
            cont = random.choice(contact_list)
            app.contact.add_contact_to_group(cont.id, group.id)
        app.contact.open_home()
        contact_in_group = db_connect.get_contacts_in_group(group)
        contact_del = random.choice(contact_in_group)
        cont_id = contact_del.id
        app.wd.find_element_by_name('group').click()
        app.wd.find_element_by_xpath("//option[@value='%s']" % group_id).click()
        app.contact.select_contact_by_id(cont_id)
        app.wd.find_element_by_name('remove').click()
        app.open_homepage()


def clear_space(s):
    return re.sub('  ', ' ', s.strip())