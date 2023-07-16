from aws_costs_api.IRepository import IRepository
from pymongo import MongoClient
import os

class MongoRepository(IRepository):
    
    def __init__(self, client = None):
        if not client:
            client = MongoClient(os.environ.get("MONGOCONNECTIONSTRING"))
        self.client = client
        self.collectionName = "aws_costs"
    
    def setConnectionString(self, connectionString: str):
        self.connectionString = connectionString
        
    def store(self, key, value):
        collection = self.client[self.collectionName][self.collectionName]
        collection.insert_one({key: value})
        
    def dataExists(self, key) -> bool:
        collection = self.client[self.collectionName][self.collectionName]
        query = {key: { "$exists": True}}
        cursor = collection.find(query)
        return len(list(cursor)) > 0
        
    def get(self, key):
        collection = self.client[self.collectionName][self.collectionName]
        cursor = collection.find({key: { "$exists": True}})
        
        data = []
        for entry in cursor:
            data.append(entry[key])

        if len(data) == 0:
            return ""
        
        return data[0]
    
    def all(self):
        collection = self.client[self.collectionName][self.collectionName]
        cursor = collection.find()
        
        data = []
        for entry in cursor:
            keys = list(entry.keys())
            values = list(entry.values())
            
            data.append({
                "key": keys[0],
                "value": values[0],
            })
            
        return data
    
    def allGenerator(self):
        collection = self.client[self.collectionName][self.collectionName]
        cursor = collection.find()
        
        for entry in cursor:
            keys = list(entry.keys())
            values = list(entry.values())
            yield {
                "key": keys[0],
                "value": values[0],
            }
