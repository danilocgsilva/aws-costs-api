from aws_costs_api.Repository import Repository
import unittest
import tempfile
import os

class test_DateUtil(unittest.TestCase):
    
    def test_exists_register(self):
        db_name = tempfile.gettempdir() + "/" + "test_db.db"
        repository = Repository()
        repository.setConnectionString(db_name)
        key = "key"
        value = "value"
        repository.store(key, value)
        self.assertTrue(repository.dataExists(key))
        os.remove(db_name)
