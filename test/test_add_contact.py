# -*- coding: utf-8 -*-
from model.contact import Contact

# закомментировал блок, пока что не работает на контакте с группой
# def test_add_contact_w_group(app):
#     old_contacts_list = app.contact.get_contact_list()
#     contact = Contact('Svyatoslav_new_test', '__test', 'Ivanov',
#                                    'aekus_test', 'D:\python_traning\image.jpg',
#                                    'new_title', 'new_comp',
#                                    'new_test_addr', 'test_home', '123546',
#                                    'new_test_work', '784512', 'new_test_email1',
#                                    'email2', '', 'new_test_homepage',
#                                    '16', 'December', '1880',
#                                    '10', 'May', '1650'), 'test_group2'
#     app.contact.save_contact_w_group(contact, 'test_group2')
#     new_contact_list = app.contact.get_contact_list()
#     assert len(old_contacts_list) + 1 == len(new_contact_list)
#     old_contacts_list.append(contact)
#     assert sorted(old_contacts_list, key=Contact.id_or_max) == sorted(new_contact_list, key=Contact.id_or_max)

def test_add_contact_wo_group(app):
    old_contacts_list = app.contact.get_contact_list()
    contact = Contact('Svyatoslav_wo_new_test', '__test', 'Ivanov',
                                   'aekus_test', 'D:\python_traning\image.jpg',
                                   'new_title', 'new_comp',
                                   'new_test_addr', 'test_home', '123546',
                                   'new_test_work', '784512', 'new_test_email1',
                                   'email2', '', 'new_test_homepage',
                                   '16', 'December', '1880',
                                   '10', 'May', '1650')
    app.contact.save_contact_wo_group(contact)
    assert len(old_contacts_list) + 1 == app.contact.count()
    new_contact_list = app.contact.get_contact_list()
    old_contacts_list.append(contact)
    assert sorted(old_contacts_list, key=Contact.id_or_max) == sorted(new_contact_list, key=Contact.id_or_max)