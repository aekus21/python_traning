# -*- coding: utf-8 -*-
from model.contact import Contact

def test_edit_contact(app):
    app.contact.edit_contact(Contact('n222ew_edit!!@_Svyatoslav', 'new_data', 'test_group2',
                                   'new_data', 'D:\python_traning\image.jpg',
                                   'new_data', 'new_data',
                                   'new_data', 'edit', 'new_data',
                                   'new_data', 'new_data', 'new_data',
                                   'new_data', 'new_data', 'new_data',
                                   '1', 'December', '1111',
                                   '1', 'December', '1111'))
