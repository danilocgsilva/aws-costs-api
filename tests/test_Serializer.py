import unittest
from aws_costs_api.Storage.Serializer import Serializer
from tests.mocks.ClientParametersMock import ClientParametersMock

class test_DateUtil(unittest.TestCase):
    def testSimpleQueryData(self):
        serializer = Serializer()
        clientParametersMock = ClientParametersMock()
        serializer.setDictParams(
            clientParametersMock.getClientParameterValues()
        )
        expectedString = "{'TimePeriod':{'Start':'2023-05-22','End':'2023-06-22'},'Granularity':'DAILY','Metrics':['BlendedCost']}"
        self.assertEqual(expectedString, serializer.getClientQueryDataSerialized())
        
