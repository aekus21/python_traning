from fixture.orm import ORMFixture
from model.group import Group

db = ORMFixture(host = '127.0.0.1', database = 'addressbook', user = 'root', password='')

try:
    l = db.get_contact_in_group(Group(ids='282'))
    for item in l:
        print(item)
    print(len(l))
finally:
    pass #db.destroy()
