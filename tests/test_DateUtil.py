import unittest
import sys
import datetime
sys.path.insert(1, "..")
from aws_costs_api.DateUtil import DateUtil

class test_DateUtil(unittest.TestCase):

    def setUp(self):
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

    def test_forget_set_datetime(self):
        with self.assertRaises(Exception):
            self.dateUtil.get_date_string_format_from_datetime()

    def test_get_month_before_object(self):
        datetimeForged = datetime.datetime(2017, 9, 3)
        dateTimeBeforeMonth = self.dateUtil.get_month_before(datetimeForged)
        self.assertTrue(
            isinstance(dateTimeBeforeMonth, datetime.datetime)
        )

    def test_get_month_before_object_no_set(self):
        now = datetime.datetime.now()
        dateTimeBeforeMonth = self.dateUtil.get_month_before(now)
        self.assertTrue(
            isinstance(dateTimeBeforeMonth, datetime.datetime)
        )

    def test_exception_if_forget_set_in_get_month_before(self):
        with self.assertRaises(Exception):
            self.dateUtil.get_month_before()

    def test_get_month_before_1(self):
        datetimeForged = datetime.datetime(2017, 9, 3)
        dateTimeBeforeMonth = self.dateUtil.get_month_before(datetimeForged)
        expected_before_month = 8
        self.assertEqual(expected_before_month, dateTimeBeforeMonth.month)
