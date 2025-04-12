import random
from model.group import Group
from model.contact import Contact

def test_del_contact_from_group(app, db):
    group_list = db.get_group_list()
    if len(group_list) == 0:
        app.group.create(Group(name='test', header='header', footer='footer'))
    group_list = db.get_group_list()
    group = random.choice(group_list)
    group_id = group.id
    contact_in_group = db.get_contacts_in_group(group)
    if len(contact_in_group) == 0:
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
        contact_list = db.get_contact_list()
        cont = random.choice(contact_list)
        app.contact.add_contact_to_group(cont.id, group.id)
    app.contact.open_home()
    contact_in_group = db.get_contacts_in_group(group)
    contact_del = random.choice(contact_in_group)
    cont_id = contact_del.id
    app.wd.find_element_by_name('group').click()
    app.wd.find_element_by_xpath("//option[@value='%s']" % group_id).click()
    app.contact.select_contact_by_id(cont_id)
    app.wd.find_element_by_name('remove').click()
    assert app.contact.count() == len(db.get_contacts_in_group(group))
    app.open_homepage()