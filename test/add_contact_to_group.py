import random
from model.group import Group
from model.contact import Contact



def test_add_contact_to_group(app, db):
    contact_list = db.get_contact_list()
    if len(contact_list) == 0:
        app.contact.save_contact_wo_group(Contact('Svyatoslav_wo_new', '_test', 'Ivanov',
                                                  'aekus_test', '',
                                                  'new_title', 'new_comp',
                                                  'new_test_addr', 'test_home', '123546',
                                                  'new_test_work', '784512', 'new_test_email1',
                                                  'email2', '', 'email3',
                                                  '1', 'December', '2222',
                                                  '1', 'December', '3333'))
    group_list = db.get_group_list()
    if len(group_list) == 0:
        app.group.create(Group(name='test', header='header', footer='footer'))
    group_list = db.get_group_list()
    group = random.choice(group_list)
    contact_wo_group = db.get_contacts_not_in_group(group)
    if len(contact_wo_group) == 0:
        app.contact.save_contact_wo_group(Contact('Svyatoslav_wo_new', '_test', 'Ivanov',
                                                  'aekus_test', '',
                                                  'new_title', 'new_comp',
                                                  'new_test_addr', 'test_home', '123546',
                                                  'new_test_work', '784512', 'new_test_email1',
                                                  'email2', '', 'email3',
                                                  '1', 'December', '2222',
                                                  '1', 'December', '3333'))
    contact_wo_group = db.get_contacts_not_in_group(group)
    contact = random.choice(contact_wo_group)
    app.contact.add_contact_to_group(contact.id, group.id)

