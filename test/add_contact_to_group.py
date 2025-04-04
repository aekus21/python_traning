import random
import re
from model.group import Group
from model.contact import Contact
from fixture.orm import ORMFixture


db_connect = ORMFixture(host = '127.0.0.1', database = 'addressbook', user = 'root', password='')

def test_add_contact_to_group(app, db):
    contact_list = db.get_contact_list()
    if len(contact_list) == 0:
        app.contact.save_contact_wo_group(Contact('Svyatoslav_wo_new', '_test', 'Ivanov',
                                                  'aekus_test', 'тест',
                                                  'new_title', 'new_comp',
                                                  'new_test_addr', 'test_home', '123546',
                                                  'new_test_work', '784512', 'new_test_email1',
                                                  'email2', '', 'email3',
                                                  'bla bla', '12', 'December',
                                                  '1032', '2', 'May', '1344'))
    contact_list = db.get_contact_list()
    contact = random.choice(contact_list)
    group_list = db.get_group_list()
    if len(group_list) == 0:
        app.group.create(Group(name='test',header='header', footer='footer'))
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