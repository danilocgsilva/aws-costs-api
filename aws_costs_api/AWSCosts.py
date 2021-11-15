import boto3
import datetime
import os
from datetime import timedelta
from dateutil.relativedelta import relativedelta
from aws_costs_api.DateUtil import DateUtil
class AWSCosts:

    def __init__(self):
        self.services = []

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

        if len(self.services) > 0:
            params["Filter"] = {
                'Dimensions': {
                    'Key': 'SERVICE',
                    'Values': self.services
                }
            }

        print(params)
        #exit()

        dataFromAws = client.get_cost_and_usage(**params)

        return dataFromAws

    def buildFilterParams(self) -> dict:
    
        paramsFilter = {
            'Dimensions': {
                'Key': 'SERVICE',
                'Values': self.services
            }
        }

        return paramsFilter

    def setService(self, service: str):
        self.services.append(service)

    def setProfile(self, profile = None):
        if profile:
            os.environ['AWS_PROFILE'] = profile
        return self

