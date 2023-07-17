import unittest
from aws_costs_api.Storage.MySQLRepository import MySQLRepository
import os
from aws_costs_api.Storage.GetMysqlCredentialsMemberFromConnectionString import GetMysqlCredentialsMemberFromConnectionString
import mysql.connector

class test_MySQLRepository(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.connectionString = os.environ.get('MYSQLCONNECTIONSTRING')
        if self.connectionString == None:
            raise Exception("Missing MYSQLCONNECTIONSTRING environment variable to tests.")
        self.mysqlRepository = MySQLRepository()
        self.mysqlRepository.setConnectionString(self.connectionString)

    def test_exists(self):
        self.assertTrue(self.mysqlRepository.tableExists())

    def test_exists_register(self):
        key = "key"
        value = "value"
        self.mysqlRepository.store(key, value)
        self.assertTrue(self.mysqlRepository.dataExists(key))

    def test_exists_not_register(self):
        key = "some"
        self.assertFalse(self.mysqlRepository.dataExists(key))

    def test_get(self):
        key = "someKey"
        value = "myValue"
        self.mysqlRepository.store(key, value)
        fetchedValue = self.mysqlRepository.get(key)
        self.assertEqual(value, fetchedValue)

    def test_all(self):
        key = "alfa"
        value = "beta"
        self.mysqlRepository.store(key, value)
        fetchedValue = self.mysqlRepository.all()
        self.assertEqual(1, len(fetchedValue))
        self.assertIsInstance(fetchedValue, list)

    def tearDown(self):
        self.__clearTable()

    def __clearTable(self):
        cs = GetMysqlCredentialsMemberFromConnectionString(self.connectionString)
        db_host, db_user, db_password, db_name, db_port = cs.getAllMembers()

        localConnection = mysql.connector.connect(
            host=db_host,
            user=db_user,
            password=db_password,
            database=db_name,
            port=db_port
        )

        cur = localConnection.cursor(buffered=True)
        cur.execute("DELETE FROM " + self.mysqlRepository.getTableName())
        localConnection.commit()

    def test_all_3_elements(self):
        self.mysqlRepository.store("alfa", "beta")
        self.mysqlRepository.store("gamma", "delta")
        self.mysqlRepository.store("epsilon", "zeta")
        fetchedValue = self.mysqlRepository.all()
        self.assertEqual(3, len(fetchedValue))
        self.assertIsInstance(fetchedValue, list)

    def test_all_see_key_and_value(self):
        key = "thekey"
        value = "thecostofawsperiod"
        self.mysqlRepository.store(key, value)
        allData = self.mysqlRepository.all()
        entry = allData[0]
        self.assertEqual("thekey", entry["key"])
        self.assertEqual("thecostofawsperiod", entry["value"])

    def test_all_generator(self):
        self.mysqlRepository.store("alfa", "beta")
        self.mysqlRepository.store("gamma", "delta")
        data = []
        for entry in self.mysqlRepository.allGenerator():
            data.append(entry)
        self.assertEqual(2, len(data))
