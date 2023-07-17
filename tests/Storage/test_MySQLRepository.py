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
        self.__clearTable(self)

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

    def test_key_search(self):
        key = '{\'TimePeriod\':{\'Start\':\'2023-06-17\',\'End\':\'2023-07-17\'},\'Granularity\':\'DAILY\',\'Metrics\':[\'BlendedCost\']}'
        value = '{\'ResultsByTime\': [{\'TimePeriod\': {\'Start\': \'2023-06-17\', \'End\': \'2023-06-18\'}, \'Total\': {\'BlendedCost\': {\'Amount\': \'0.8838501934\', \'Unit\': \'USD\'}}, \'Groups\': [], \'Estimated\': false}, {\'TimePeriod\': {\'Start\': \'2023-06-18\', \'End\': \'2023-06-19\'}, \'Total\': {\'BlendedCost\': {\'Amount\': \'0.8841937134\', \'Unit\': \'USD\'}}, \'Groups\': [], \'Estimated\': false}, {\'TimePeriod\': {\'Start\': \'2023-06-19\', \'End\': \'2023-06-20\'}, \'Total\': {\'BlendedCost\': {\'Amount\': \'0.8840539172\', \'Unit\': \'USD\'}}, \'Groups\': [], \'Estimated\': false}, {\'TimePeriod\': {\'Start\': \'2023-06-20\', \'End\': \'2023-06-21\'}, \'Total\': {\'BlendedCost\': {\'Amount\': \'0.8840346372\', \'Unit\': \'USD\'}}, \'Groups\': [], \'Estimated\': false}, {\'TimePeriod\': {\'Start\': \'2023-06-21\', \'End\': \'2023-06-22\'}, \'Total\': {\'BlendedCost\': {\'Amount\': \'0.889184637\', \'Unit\': \'USD\'}}, \'Groups\': [], \'Estimated\': false}, {\'TimePeriod\': {\'Start\': \'2023-06-22\', \'End\': \'2023-06-23\'}, \'Total\': {\'BlendedCost\': {\'Amount\': \'0.9281567467\', \'Unit\': \'USD\'}}, \'Groups\': [], \'Estimated\': false}, {\'TimePeriod\': {\'Start\': \'2023-06-23\', \'End\': \'2023-06-24\'}, \'Total\': {\'BlendedCost\': {\'Amount\': \'0.8852772607\', \'Unit\': \'USD\'}}, \'Groups\': [], \'Estimated\': false}, {\'TimePeriod\': {\'Start\': \'2023-06-24\', \'End\': \'2023-06-25\'}, \'Total\': {\'BlendedCost\': {\'Amount\': \'0.8840461407\', \'Unit\': \'USD\'}}, \'Groups\': [], \'Estimated\': false}, {\'TimePeriod\': {\'Start\': \'2023-06-25\', \'End\': \'2023-06-26\'}, \'Total\': {\'BlendedCost\': {\'Amount\': \'0.8943557849\', \'Unit\': \'USD\'}}, \'Groups\': [], \'Estimated\': false}, {\'TimePeriod\': {\'Start\': \'2023-06-26\', \'End\': \'2023-06-27\'}, \'Total\': {\'BlendedCost\': {\'Amount\': \'0.8848448185\', \'Unit\': \'USD\'}}, \'Groups\': [], \'Estimated\': false}, {\'TimePeriod\': {\'Start\': \'2023-06-27\', \'End\': \'2023-06-28\'}, \'Total\': {\'BlendedCost\': {\'Amount\': \'1.1149361022\', \'Unit\': \'USD\'}}, \'Groups\': [], \'Estimated\': false}, {\'TimePeriod\': {\'Start\': \'2023-06-28\', \'End\': \'2023-06-29\'}, \'Total\': {\'BlendedCost\': {\'Amount\': \'1.5049051022\', \'Unit\': \'USD\'}}, \'Groups\': [], \'Estimated\': false}, {\'TimePeriod\': {\'Start\': \'2023-06-29\', \'End\': \'2023-06-30\'}, \'Total\': {\'BlendedCost\': {\'Amount\': \'0.8849377422\', \'Unit\': \'USD\'}}, \'Groups\': [], \'Estimated\': false}, {\'TimePeriod\': {\'Start\': \'2023-06-30\', \'End\': \'2023-07-01\'}, \'Total\': {\'BlendedCost\': {\'Amount\': \'1.0548963822\', \'Unit\': \'USD\'}}, \'Groups\': [], \'Estimated\': false}, {\'TimePeriod\': {\'Start\': \'2023-07-01\', \'End\': \'2023-07-02\'}, \'Total\': {\'BlendedCost\': {\'Amount\': \'3.336846317\', \'Unit\': \'USD\'}}, \'Groups\': [], \'Estimated\': true}, {\'TimePeriod\': {\'Start\': \'2023-07-02\', \'End\': \'2023-07-03\'}, \'Total\': {\'BlendedCost\': {\'Amount\': \'0.8567270891\', \'Unit\': \'USD\'}}, \'Groups\': [], \'Estimated\': true}, {\'TimePeriod\': {\'Start\': \'2023-07-03\', \'End\': \'2023-07-04\'}, \'Total\': {\'BlendedCost\': {\'Amount\': \'0.8567650891\', \'Unit\': \'USD\'}}, \'Groups\': [], \'Estimated\': true}, {\'TimePeriod\': {\'Start\': \'2023-07-04\', \'End\': \'2023-07-05\'}, \'Total\': {\'BlendedCost\': {\'Amount\': \'0.8570167291\', \'Unit\': \'USD\'}}, \'Groups\': [], \'Estimated\': true}, {\'TimePeriod\': {\'Start\': \'2023-07-05\', \'End\': \'2023-07-06\'}, \'Total\': {\'BlendedCost\': {\'Amount\': \'0.8569544165\', \'Unit\': \'USD\'}}, \'Groups\': [], \'Estimated\': true}, {\'TimePeriod\': {\'Start\': \'2023-07-06\', \'End\': \'2023-07-07\'}, \'Total\': {\'BlendedCost\': {\'Amount\': \'0.8571375365\', \'Unit\': \'USD\'}}, \'Groups\': [], \'Estimated\': true}, {\'TimePeriod\': {\'Start\': \'2023-07-07\', \'End\': \'2023-07-08\'}, \'Total\': {\'BlendedCost\': {\'Amount\': \'0.8569969765\', \'Unit\': \'USD\'}}, \'Groups\': [], \'Estimated\': true}, {\'TimePeriod\': {\'Start\': \'2023-07-08\', \'End\': \'2023-07-09\'}, \'Total\': {\'BlendedCost\': {\'Amount\': \'0.8569562565\', \'Unit\': \'USD\'}}, \'Groups\': [], \'Estimated\': true}, {\'TimePeriod\': {\'Start\': \'2023-07-09\', \'End\': \'2023-07-10\'}, \'Total\': {\'BlendedCost\': {\'Amount\': \'0.8570650565\', \'Unit\': \'USD\'}}, \'Groups\': [], \'Estimated\': true}, {\'TimePeriod\': {\'Start\': \'2023-07-10\', \'End\': \'2023-07-11\'}, \'Total\': {\'BlendedCost\': {\'Amount\': \'0.8577501615\', \'Unit\': \'USD\'}}, \'Groups\': [], \'Estimated\': true}, {\'TimePeriod\': {\'Start\': \'2023-07-11\', \'End\': \'2023-07-12\'}, \'Total\': {\'BlendedCost\': {\'Amount\': \'0.8569739615\', \'Unit\': \'USD\'}}, \'Groups\': [], \'Estimated\': true}, {\'TimePeriod\': {\'Start\': \'2023-07-12\', \'End\': \'2023-07-13\'}, \'Total\': {\'BlendedCost\': {\'Amount\': \'0.8569534815\', \'Unit\': \'USD\'}}, \'Groups\': [], \'Estimated\': true}, {\'TimePeriod\': {\'Start\': \'2023-07-13\', \'End\': \'2023-07-14\'}, \'Total\': {\'BlendedCost\': {\'Amount\': \'0.8569950815\', \'Unit\': \'USD\'}}, \'Groups\': [], \'Estimated\': true}, {\'TimePeriod\': {\'Start\': \'2023-07-14\', \'End\': \'2023-07-15\'}, \'Total\': {\'BlendedCost\': {\'Amount\': \'0.8577274015\', \'Unit\': \'USD\'}}, \'Groups\': [], \'Estimated\': true}, {\'TimePeriod\': {\'Start\': \'2023-07-15\', \'End\': \'2023-07-16\'}, \'Total\': {\'BlendedCost\': {\'Amount\': \'0.8669947615\', \'Unit\': \'USD\'}}, \'Groups\': [], \'Estimated\': true}, {\'TimePeriod\': {\'Start\': \'2023-07-16\', \'End\': \'2023-07-17\'}, \'Total\': {\'BlendedCost\': {\'Amount\': \'0.9313987321\', \'Unit\': \'USD\'}}, \'Groups\': [], \'Estimated\': true}], \'DimensionValueAttributes\': [], \'ResponseMetadata\': {\'RequestId\': \'105b224b-88ea-4884-882d-8f217a0b6669\', \'HTTPStatusCode\': 200, \'HTTPHeaders\': {\'date\': \'Mon, 17 Jul 2023 19:25:32 GMT\', \'content-type\': \'application/x-amz-json-1.1\', \'content-length\': \'4531\', \'connection\': \'keep-alive\', \'x-amzn-requestid\': \'105b224b-88ea-4884-882d-8f217a0b6669\', \'cache-control\': \'no-cache\'}, \'RetryAttempts\': 0}}'
        self.mysqlRepository.store(key, value)
        fetchedValue = self.mysqlRepository.get(key)
        self.assertEqual(value, fetchedValue)
