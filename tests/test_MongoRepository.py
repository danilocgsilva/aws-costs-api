import unittest
from mongomock import MongoClient as MockMongoClient
from aws_costs_api.MongoRepository import MongoRepository

class test_MongoRepository(unittest.TestCase):
    
    def setUp(self):
        self.repository = MongoRepository(MockMongoClient())
    
    def test_exists_register(self):
        key = "key"
        value = "value"
        self.repository.store(key, value)
        self.assertTrue(self.repository.dataExists(key))
        
    def test_get(self):
        key = "thekey"
        value = "thecostofawsperiod"
        self.repository.store(key, value)
        self.assertEqual(value, self.repository.get(key))
    