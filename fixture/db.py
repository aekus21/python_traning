import pymysql.cursors

class DbFixture:

    def __init__(self, host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host = host, database = database, user = user, password= password)

    def destroy(self):
        self.connection.close()