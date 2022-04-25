import boto3
import datetime
import os
from aws_costs_api.DateUtil import DateUtil

class AWSCosts:

    def __init__(self, client = None):
        self.services = []
        if client == None:
            self.clientAlias = "ce"
        else:
            self.client = client
        self.startTime = None
        self.dateUtil = DateUtil()
        self.now = datetime.datetime.now()

    def setStartTime(self, startTime: str):
        self.startTime = startTime
        return self

    def getCosts(self) -> dict:
        params = {
            "TimePeriod": {
                "Start": self.__prepareStartTime(),
                "End": self.dateUtil.get_date_string_format_from_datetime(self.now)
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

        if not hasattr(self, 'client'):
            self.client = boto3.client(self.clientAlias)

        dataFromAws = self.client.get_cost_and_usage(**params)

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

    def __prepareStartTime(self) -> str:

        return self.startTime if self.startTime != None else self.dateUtil.get_date_string_format_from_datetime(
            self.dateUtil.get_month_before(self.now)
        )
