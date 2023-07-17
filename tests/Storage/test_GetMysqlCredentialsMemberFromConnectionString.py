from aws_costs_api.Storage.GetMysqlCredentialsMemberFromConnectionString import GetMysqlCredentialsMemberFromConnectionString

import unittest

class test_getMysqlCredentialsMemberFromConnectionStrint(unittest.TestCase):

    def test_getMysqlConnectionsMembers(self):
        connectionString = "USER=my_user;HOST=my_host;PASSWORD=my_password;DATABASE_NAME=my_database_name;PORT=my_database_port"
        cs = GetMysqlCredentialsMemberFromConnectionString(connectionString)
        db_host, db_user, db_password, db_database, db_port = cs.getAllMembers()
        self.assertEqual(db_host, "my_host")
        self.assertEqual(db_user, "my_user")
        self.assertEqual(db_password, "my_password")
        self.assertEqual(db_database, "my_database_name")
        self.assertEqual(db_port, "my_database_port")
        

