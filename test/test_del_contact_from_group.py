import random

def test_del_contact_from_group(app, db):
    group_list = db.get_group_list()
    group = random.choice(group_list)
    group_id = group.id
    contact_in_group = db.get_contacts_in_group(group)
    if len(contact_in_group) == 0:
        contact_list = db.get_contact_list()
        cont = random.choice(contact_list)
        app.contact.add_contact_to_group(cont.id, group.id)
    app.contact.open_home()
    contact_in_group = db.get_contacts_in_group(group)
    contact_del = random.choice(contact_in_group)
    cont_id = contact_del.id
    app.wd.find_element_by_name('group').click()
    app.wd.find_element_by_xpath("//option[@value='%s']" % group_id).click()
    app.contact.select_contact_by_id(cont_id)
    app.wd.find_element_by_name('remove').click()
    app.open_homepage()