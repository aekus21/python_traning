# -*- coding: utf-8 -*-
from operator import index
from random import randrange

from model.contact import Contact

def test_edit_contact(app):
    if app.contact.count() == 0:
        app.contact.save_contact_wo_group(Contact('Svyatoslav_wo_new_test', '_test', 'Ivanov',
                                   'aekus_test', 'D:\python_traning\image.jpg',
                                   'new_title', 'new_comp',
                                   'new_test_addr', 'test_home', '123546',
                                   'new_test_work', '784512', 'new_test_email1',
                                   'email2', '', 'new_test_homepage',
                                   '16', 'December', '1880',
                                   '10', 'May', '1650'))
    old_contacts_list = app.contact.get_contact_list()
    contact = Contact(fname='n222ew_edit!!@_Svyatoslav', lname='dd11d')
    index = randrange(len(old_contacts_list))
    contact.id = old_contacts_list[index].id
    app.contact.edit_contact_by_index(index, contact)
    new_contact_list = app.contact.get_contact_list()
    assert len(old_contacts_list) == len(new_contact_list)
    old_contacts_list[index] = contact
    assert sorted(old_contacts_list, key=Contact.id_or_max) == sorted(new_contact_list, key=Contact.id_or_max)