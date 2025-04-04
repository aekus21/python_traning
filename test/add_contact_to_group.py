import random
from model.group import Group
from model.contact import Contact



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
