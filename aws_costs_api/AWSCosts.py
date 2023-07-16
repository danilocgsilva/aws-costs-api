import boto3
import datetime
import os
from aws_costs_api.DateUtil import DateUtil
from aws_costs_api.Storage.SQLiteRepository import SQLiteRepository
from aws_costs_api.Storage.MySQLRepository import MySQLRepository
from aws_costs_api.Storage.Serializer import Serializer
import tempfile
import json

class AWSCosts:
    """Main class"""

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

    def getCosts(self, databaseConnectionString = None):
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
        
        if databaseConnectionString == None:
            return self.client.get_cost_and_usage(**params)
        else:
            return self.__getCostsUsingStorage(databaseConnectionString)

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
        return self

    def setUniqueService(self, service: str):
        self.services = [ service ]
        return self

    def setProfile(self, profile = None):
        if profile:
            os.environ['AWS_PROFILE'] = profile
        return self

    def __prepareStartTime(self) -> str:
<<<<<<< HEAD

        return self.startTime if self.startTime != None else self.dateUtil.get_date_string_format_from_datetime(
            self.dateUtil.get_month_before(self.now)
        )
=======
        if self.startTime == None:
            month_before = self.dateUtil.get_month_before(self.now)
            return self.dateUtil.get_date_string_format_from_datetime(month_before)
        else:
            return self.startTime

    def __getCostsUsingStorage(self, databaseConnectionString):
            
            databaseConnectionStringParts = databaseConnectionString.split(":")

            repository = SQLiteRepository()
            repository.setConnectionString(databaseConnectionString)
            serializer = Serializer()
            serializer.setDictParams(params)
            data_key_serialized = serializer.getClientQueryDataSerialized()
            if repository.dataExists(data_key_serialized):
                rawJsonData = repository.get(data_key_serialized)
                return json.loads(rawJsonData)
            else:
                dataFromAws = client.get_cost_and_usage(**params)
                dataFromAwsJson = json.dumps(dataFromAws)
                repository.store(data_key_serialized, dataFromAwsJson)
                return dataFromAws
>>>>>>> 5539ec88d4fbfd0d857121b3a9e39ca683b3daed
