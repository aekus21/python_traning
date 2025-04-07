from model.group import Group
from model.contact import Contact
import re



def test_compare_contacts_on_homepage(app, db):
    contacts_from_homepage = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    contacts_from_db = sorted(db.get_contact_list(), key=Contact.id_or_max)
    index = 0
    for element in contacts_from_homepage:
        assert element.first_name == contacts_from_db[index].first_name
        assert element.last_name == contacts_from_db[index].last_name
        assert element.address == contacts_from_db[index].address
        assert element.all_phones_from_homepage == merge_phones_like_on_homepage(contacts_from_db[index])
        assert element.all_email == merge_emails_like_on_homepage(contacts_from_db[index]).strip()
        index += 1


def test_group_list(app, db):
    ui_list = app.group.get_group_list()
    def clean(group):
        s = re.sub('  ', ' ', group.test_name)
        return Group(id=group.id, name=s.strip())
    db_list = map(clean, filter(lambda x: x is not None, (db.get_group_list())))
    assert sorted(ui_list, key= Group.id_or_max) == sorted(db_list, key= Group.id_or_max)


def test_contact_list(app, db):
    ui_list = app.contact.get_contact_list()
    def clean(contact):
        s = re.sub('  ', ' ', contact.last_name)
        return Contact(id=contact.id, lname=s.strip())
    db_list = map(clean, (filter(lambda x: x is not None, (db.get_contact_list()))))
    assert sorted(ui_list, key= Contact.id_or_max) == sorted(db_list, key= Contact.id_or_max)


def clear(s):
    return re.sub('[() -]', '', s)

def clear_space(s):
    return re.sub('  ', ' ', s.strip())

def merge_phones_like_on_homepage(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None, [contact.homephone, contact.mobilephone, contact.workphone]))))

def merge_emails_like_on_homepage(email):
    return "\n".join(map(lambda x: clear_space(x),
                         filter(lambda x: x is not None,[email.email1, email.email2, email.email3])))