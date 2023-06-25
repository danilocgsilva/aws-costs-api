import boto3
import datetime
import os
from aws_costs_api.DateUtil import DateUtil
from aws_costs_api.Repository import Repository

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

    def getCosts(self):
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
        
        if existsParametersInDatabase:
            dataFromAws = repository.getdatafromparams(params)
        else:
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

    def setUniqueService(self, service: str):
        self.services = [ service ]

    def setProfile(self, profile = None):
        if profile:
            os.environ['AWS_PROFILE'] = profile
        return self

    def __prepareStartTime(self) -> str:
        if self.startTime == None:
            month_before = self.dateUtil.get_month_before(self.now)
            return self.dateUtil.get_date_string_format_from_datetime(month_before)
        else:
            return self.startTime