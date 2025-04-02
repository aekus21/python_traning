import random
from model.contact import Contact

def test_delete_some_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.save_contact_wo_group(Contact('Svyatoslav_wo_new_test', '__test', 'Ivanov',
                                   'aekus_test', 'D:\python_traning\image.jpg',
                                   'new_title', 'new_comp',
                                   'new_test_addr', 'test_home', '123546',
                                   'new_test_work', '784512', 'new_test_email1',
                                   'email2', '', 'new_test_homepage',
                                   '16', 'December', '1880',
                                   '10', 'May', '1650'))
    old_contacts_list = db.get_contact_list()
    contact = random.choice(old_contacts_list)
    app.contact.delete_contact_by_id(contact.id)
    new_contact_list = db.get_contact_list()
    assert len(old_contacts_list) - 1 == len(new_contact_list)
    old_contacts_list.remove(contact)
    assert old_contacts_list == new_contact_list
    db_list = filter(lambda x: x is not None, (db.get_contact_list()))
    if check_ui:
        assert sorted(new_contact_list, key=Contact.id_or_max) == sorted(db_list, key=Contact.id_or_max)