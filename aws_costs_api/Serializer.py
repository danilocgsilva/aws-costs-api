import re

class Serializer:

    def setDictParams(self, dictParams: dict):
        self.dictParams = dictParams

    def getClientQueryDataSerialized(self):
        rawSerialized = str(self.dictParams)
        return re.sub(r" ", "", rawSerialized)
