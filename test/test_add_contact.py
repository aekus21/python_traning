# -*- coding: utf-8 -*-
from importlib.metadata import pass_none

from model.contact import Contact
import pytest
import string
import random
import re

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


def random_personal_data(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*20
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_digit_data(maxlen):
    symbols = string.digits
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_date_data():
   return str(random.randint(1,31))

def random_month_data():
    return random.choice(["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November"])

def randon_year_data():
    return str(random.randrange(1700, 2250))

test_data_wo_group = [
    Contact(fname = re.sub('  ', ' ', random_personal_data("firstName", maxlen = 10)).strip(),
            mname = random_personal_data("middleName", maxlen = 10),
            lname = re.sub('  ', ' ', random_personal_data("lastnameName", maxlen = 10)).strip(),
            nickname = random_personal_data("nickName", maxlen = 10),
            title = random_personal_data("title", maxlen = 10),
            photo= 'D:\python_traning\image.jpg',
            company = random_personal_data("nickName", maxlen = 10),
            address = random_personal_data("address", maxlen = 10),
            homephone = "+7" + random_digit_data(maxlen = 10),
            mobilephone = "+7" + random_digit_data(maxlen = 10),
            workphone = "+7" +  random_digit_data(maxlen = 10),
            fax = "+7" + random_digit_data(maxlen = 10),
            email1 = random_personal_data("email1", maxlen = 10),
            email2 = random_personal_data("email2", maxlen = 10),
            email3 = random_personal_data("email3", maxlen = 10),
            homepage = random_personal_data("homepage", maxlen = 10),
            bday = random_date_data(),
            bmonth = random_month_data(),
            byear = randon_year_data(),
            anniverday = random_date_data(),
            annivermonth = random_month_data(),
            anniveryear = randon_year_data()
            )
]

@pytest.mark.parametrize("contact", test_data_wo_group, ids=[repr(x) for x in test_data_wo_group])
def test_add_contact_wo_group(app, contact):
    old_contacts_list = app.contact.get_contact_list()
    app.contact.save_contact_wo_group(contact)
    assert len(old_contacts_list) + 1 == app.contact.count()
    new_contact_list = app.contact.get_contact_list()
    old_contacts_list.append(contact)
    assert sorted(old_contacts_list, key=Contact.id_or_max) == sorted(new_contact_list, key=Contact.id_or_max)