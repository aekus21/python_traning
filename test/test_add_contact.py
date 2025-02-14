# -*- coding: utf-8 -*-
from model.contact import Contact

def test_add_contact_w_group(app):
    app.session.login_form("admin", "secret")
    app.contact.save_contact_w_group(Contact('Svyatoslav_new_test', '__test', 'Ivanov',
                                   'aekus_test', 'D:\python_traning\image.jpg',
                                   'new_title', 'new_comp',
                                   'new_test_addr', 'test_home', '123546',
                                   'new_test_work', '784512', 'new_test_email1',
                                   'email2', '', 'new_test_homepage',
                                   '16', 'December', '1880',
                                   '10', 'May', '1650'), 'test_group2')
    app.session.logout()

def test_add_contact_wo_group(app):
    app.session.login_form("admin", "secret")
    app.contact.save_contact_wo_group(Contact('Svyatoslav_wo_new_test', '__test', 'Ivanov',
                                   'aekus_test', 'D:\python_traning\image.jpg',
                                   'new_title', 'new_comp',
                                   'new_test_addr', 'test_home', '123546',
                                   'new_test_work', '784512', 'new_test_email1',
                                   'email2', '', 'new_test_homepage',
                                   '16', 'December', '1880',
                                   '10', 'May', '1650'))
    app.session.logout()