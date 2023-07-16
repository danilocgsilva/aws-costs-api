from aws_costs_api.IRepository import IRepository

class MySQLRepository(IRepository):
    
    def __init__(self):
        self.tableName = "aws_cost"
        self.schemaName = "aws"

    def setConnectionString(self, connectionString: str):
        self.connectionString = connectionString
        
