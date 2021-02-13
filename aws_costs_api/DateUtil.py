class DateUtil:

    def get_date_string_format_from_datetime(self, datetime):
        year = datetime.year
        month = datetime.month
        day = datetime.day

        return str(year) + "-" + '{0:02}'.format(month) + "-" + '{0:02}'.format(day)
