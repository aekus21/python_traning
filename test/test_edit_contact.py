# -*- coding: utf-8 -*-
from model.contact import Contact

def test_edit_contact(app):
    app.session.login_form("admin", "secret")
    app.contact.open_contact_editor()
    app.contact.change_contact_data(Contact('new_edit_Svyatoslav', 'new_data', 'test_group2',
                                   'new_data', 'D:\python_traning\image.jpg',
                                   'new_data', 'new_data',
                                   'new_data', 'edit', 'new_data',
                                   'new_data', 'new_data', 'new_data',
                                   'new_data', 'new_data', 'new_data',
                                   '1', 'December', '1111',
                                   '1', 'December', '1111', ''))
    app.contact.save_new_contact_data()
    app.session.logout()