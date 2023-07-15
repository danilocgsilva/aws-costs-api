import re

class Serializer:
    """
    Converts the input params to a string. So it becomes a key for a given result.
    If the api tries to search data using the same criteria preivously used, the results
    shall be exactly the same. Once saved, no need to fetch again from the AWS api, which
    is expensive.
    """

    def setDictParams(self, dictParams: dict):
        self.dictParams = dictParams

    def getClientQueryDataSerialized(self):
        rawSerialized = str(self.dictParams)
        return re.sub(r" ", "", rawSerialized)
