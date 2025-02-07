# -*- coding: utf-8 -*-
from model.contact import Contact

def test_add_contact(app):
    app.session.login_form("admin", "secret")
    app.contact.new_contact_form()
    app.contact.fill_form(Contact('Svyatoslav', '__test', 'Ivanov',
                                   'aekus_test', 'D:\python_traning\image.jpg',
                                   'new_title', 'new_comp',
                                   'new_test_addr', 'test_home', '123546',
                                   'new_test_work', '784512', 'new_test_email1',
                                   'email2', '', 'new_test_homepage',
                                   '16', 'December', '1880',
                                   '10', 'May', '1650', 'test_group2'))
    app.session.logout()