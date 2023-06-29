from aws_costs_api.SQLiteRepository import SQLiteRepository
import unittest
import tempfile
import os

class test_SQLiteRepository(unittest.TestCase):
    
    def setUp(self):
        self.db_name = tempfile.gettempdir() + "/" + "test_db.db"
        self.repository = SQLiteRepository()
        self.repository.setConnectionString(self.db_name)
        
    def tearDown(self):
        os.remove(self.db_name)

    def test_exists_register(self):
        key = "key"
        value = "value"
        self.repository.store(key, value)
        self.assertTrue(self.repository.dataExists(key))

    def test_exists_register(self):
        key = "key"
        self.assertFalse(self.repository.dataExists(key))
        
    def test_get(self):
        key = "key"
        value = "myValue"
        self.repository.store(key, value)
        fetchedValue = self.repository.get(key)
        self.assertEqual(value, fetchedValue)
        
    def test_all(self):
        key = "alfa"
        value = "beta"
        self.repository.store(key, value)
        fetchedValue = self.repository.all()
        self.assertEqual(1, len(fetchedValue))
        self.assertIsInstance(fetchedValue, list)
        
    def test_all_3_elements(self):
        self.repository.store("alfa", "beta")
        self.repository.store("gamma", "delta")
        self.repository.store("epsilon", "zeta")
        fetchedValue = self.repository.all()
        self.assertEqual(3, len(fetchedValue))
        self.assertIsInstance(fetchedValue, list)
        
    def test_all_see_key_and_value(self):
        key = "thekey"
        value = "thecostofawsperiod"
        self.repository.store(key, value)
        allData = self.repository.all()
        entry = allData[0]
        self.assertEqual("thekey", entry["key"])
        self.assertEqual("thecostofawsperiod", entry["value"])
        
    def test_all_generator(self):
        self.repository.store("alfa", "beta")
        self.repository.store("gamma", "delta")
        data = []
        for entry in self.repository.allGenerator():
            data.append(entry)
        self.assertEqual(2, len(data))
        
    
