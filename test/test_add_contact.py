# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact_wo_group(app, db, json_contacts):
    contact = json_contacts
    old_contacts_list = db.get_contact_list()
    app.contact.save_contact_wo_group(contact)
    # assert len(old_contacts_list) + 1 == app.contact.count()
    new_contact_list = db.get_contact_list()
    old_contacts_list.append(contact)
    assert sorted(old_contacts_list, key=Contact.id_or_max) == sorted(new_contact_list, key=Contact.id_or_max)