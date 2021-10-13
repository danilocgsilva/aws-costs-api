import boto3
import datetime
import os
from datetime import timedelta
from dateutil.relativedelta import relativedelta
from aws_costs_api.DateUtil import DateUtil
class AWSCosts:

    def __init__(self):
        self.ec2 = False

    def getCosts(self):
        dateUtil = DateUtil()
        now = datetime.datetime.now()
        month_before = dateUtil.get_month_before(now)
        client = boto3.client("ce")

        params = {
            "TimePeriod": {
                "Start": dateUtil.get_date_string_format_from_datetime(month_before),
                "End": dateUtil.get_date_string_format_from_datetime(now)
            },
            "Granularity": "DAILY",
            "Metrics": ["BlendedCost"]
        }

        if self.ec2:
            params["Filter"] = {
                'Dimensions': {
                    'Key': 'SERVICE',
                    'Values': [
                        'ec2'
                    ]
                }
            }

        dataFromAws = client.get_cost_and_usage(**params)

        return dataFromAws

    def setEc2(self):
        self.ec2 = True

    def setProfile(self, profile = None):
        if profile:
            os.environ['AWS_PROFILE'] = profile
        return self

