import unittest
from aws_costs_api.Storage.MySQLRepository import MySQLRepository
import os

class test_MySQLRepository(unittest.TestCase):

    def test_createTable(self):
        mysqlRepository = MySQLRepository()
        
        connectionStringFull = os.environ.get('MYSQLCONNECTIONSTRING')
        
        