from aws_costs_api.Storage.IRepository import IRepository
import mysql.connector

class MySQLRepository(IRepository):
    
    def __init__(self):
        self.tableName = "aws_cost"
        self.schemaName = "aws"

    def setConnectionString(self, connectionString: str):
        self.connectionString = connectionString
        self.conn = mysql.connect(

        )

    def tableExists(self) -> bool:
        queryCheckBase = """SELECT
            TABLE_NAME
        FROM
            information_schema.TABLES
        WHERE
            TABLE_SCHEMA = '{0}'
            AND TABLE_TYPE = 'BASE TABLE'
            AND TABLE_NAME = '{1}'"""
        queryCheck = queryCheckBase.format(self.schemaName, self.tableName)
        cur = self.conn.cursor()
        tableResults = cur.execute(queryCheck)
        fetchedResults = tableResults.fetchall()
        return not len(fetchedResults) == 0

    def createTable(self):
        queryCreateTable = "CREATE TABLE `" + self.tableName + "` (`key` TEXT, `value` TEXT)"
        cur = self.conn.cursor()
        cur.execute(queryCreateTable)
        cur.close()

    def dataExists(self, key) -> bool:
        if not self.tableExists():
            self.createTable()
        query = "SELECT value FROM {0} WHERE key = \"{1}\";"
        queryValued = query.format(self.tableName, key)
        cur = self.conn.cursor()
        tableResults = cur.execute(queryValued)
        fetchedResults = tableResults.fetchall()
        return not len(fetchedResults) == 0
        
