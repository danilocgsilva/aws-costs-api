import datetime
from dateutil.relativedelta import relativedelta

class DateUtil:

    def get_date_string_format_from_datetime(self, userDateTime: datetime.datetime):
        year = userDateTime.year
        month = userDateTime.month
        day = userDateTime.day
        return str(year) + "-" + '{0:02}'.format(month) + "-" + '{0:02}'.format(day)

    def get_month_before(self, userDatetime: datetime.datetime):
        return userDatetime - relativedelta(months=+1)
