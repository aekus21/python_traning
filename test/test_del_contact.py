from operator import index
from random import randrange

from model.contact import Contact

def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.save_contact_wo_group(Contact('Svyatoslav_wo_new_test', '__test', 'Ivanov',
                                   'aekus_test', 'D:\python_traning\image.jpg',
                                   'new_title', 'new_comp',
                                   'new_test_addr', 'test_home', '123546',
                                   'new_test_work', '784512', 'new_test_email1',
                                   'email2', '', 'new_test_homepage',
                                   '16', 'December', '1880',
                                   '10', 'May', '1650'))
    old_contacts_list = app.contact.get_contact_list()
    index = randrange(len(old_contacts_list))
    app.contact.delete_contact_by_index(index)
    new_contact_list = app.contact.get_contact_list()
    assert len(old_contacts_list) - 1 == len(new_contact_list)
    old_contacts_list[index:index+1] = []
    assert old_contacts_list == new_contact_list