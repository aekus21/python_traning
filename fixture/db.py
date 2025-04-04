import pymysql.cursors
from model.group import Group
from model.contact import Contact

class DbFixture:

    def __init__(self, host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host = host, database = database, user = user, password= password,
                                          autocommit = True)

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute('select group_id, group_name, group_header, group_footer '
                           'from group_list')
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id = str(id), name = name, header = header, footer = footer))
        finally:
            cursor.close()
        return list

    def get_contact_in_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute('select group_id from address_in_groups')
            for row in cursor:
                (id) = row
                list.append(Group(id=str(id)))
        finally:
            cursor.close()
        return list

    def get_contact_list(self):
        contact_list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute('select id, firstname, lastname '
                               'from addressbook')
            for row in cursor:
                (id, firstname, lastname) = row
                contact_list.append(Contact(id = str(id), fname = firstname, lname = lastname))
        finally:
            cursor.close()
        return contact_list

    def destroy(self):
        self.connection.close()