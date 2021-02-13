import unittest
import sys
import datetime
sys.path.insert(1, "..")
from aws_costs_api.DateUtil import DateUtil

class test_DateUtil(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.dateUtil = DateUtil()

    def test_format_1(self):
        datetimeForged = datetime.datetime(2017, 11, 12)
        expected_results = "2017-11-12"
        self.assertEqual(
            expected_results, 
            self.dateUtil.get_date_string_format_from_datetime(datetimeForged)
        )

    def test_format_2(self):
        datetimeForged = datetime.datetime(2017, 2, 3)
        expected_results = "2017-02-03"
        self.assertEqual(
            expected_results, 
            self.dateUtil.get_date_string_format_from_datetime(datetimeForged)
        )

