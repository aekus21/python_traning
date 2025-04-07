# -*- coding: utf-8 -*-
from random import randrange
from model.contact import Contact

def test_edit_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.save_contact_wo_group(Contact('Svyatoslav_wo_new', '_test', 'Ivanov',
                                   'aekus_test', 'тест',
                                   'new_title', 'new_comp',
                                   'new_test_addr', 'test_home', '123546',
                                   'new_test_work', '784512', 'new_test_email1',
                                   'email2', '', 'email3',
                                   '21', 'December', '1111',
                                   '2', 'December', '2222'))
    old_contacts_list = db.get_contact_list()
    contact = Contact(fname='Svyat132', lname='dd11d')
    index = randrange(len(old_contacts_list))
    contact.id = old_contacts_list[index].id
    app.contact.edit_contact_by_id(contact.id, contact)
    new_contact_list = db.get_contact_list()
    assert len(old_contacts_list) == len(new_contact_list)
    old_contacts_list[index] = contact
    db_list = filter(lambda x: x is not None, (db.get_contact_list()))
    assert sorted(old_contacts_list, key=Contact.id_or_max) == sorted(db_list, key=Contact.id_or_max)
    if check_ui:
        assert (sorted(old_contacts_list, key=Contact.id_or_max) ==
                sorted(app.contact.get_contact_list(), key=Contact.id_or_max))