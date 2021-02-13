import boto3
import datetime
from datetime import timedelta

class AWSCosts:

    def getCosts(self):
        now = datetime.datetime.now()
        client = boto3.client("ce")
        return client.get_cost_and_usage()
