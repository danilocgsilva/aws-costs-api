from aws_costs_api.Storage.IRepository import IRepository
import mysql.connector
from aws_costs_api.Storage.getMysqlCredentialsMemberFromConnectionString import getMysqlCredentialsMemberFromConnectionString

class MySQLRepository(IRepository):
    
    def __init__(self):
        self.tableName = "aws_cost"
        self.schemaName = "aws"

    def setConnectionString(self, connectionString: str):

        db_host, db_user, db_password, db_name, db_port = getMysqlCredentialsMemberFromConnectionString(connectionString)

        self.conn = mysql.connector.connect(
            host=db_host,
            user=db_user,
            password=db_password,
            database=db_name,
            port=db_port
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
        
        cur = self.conn.cursor(buffered=True)
        cur.execute(queryCheck)
        fetchedResults = cur.fetchall()
        return not len(fetchedResults) == 0
        # if tableResults == None:
        #     return False
        # return True

    def createTable(self):
        queryCreateTable = "CREATE TABLE `" + self.tableName + "` (`key` TEXT, `value` TEXT)"
        cur = self.conn.cursor(buffered=True)
        cur.execute(queryCreateTable)
        cur.close()

    def dataExists(self, key) -> bool:
        if not self.tableExists():
            self.createTable()
        query = "SELECT value FROM {0} WHERE `key` = \"{1}\";"
        queryValued = query.format(self.tableName, key)
        cur = self.conn.cursor(buffered=True)
        print("----" + queryValued)
        cur.execute(queryValued)
        fetchedResults = cur.fetchall()
        return not len(fetchedResults) == 0

    def store(self, key, value):
        if not self.tableExists():
            self.createTable()
        query = "INSERT INTO `{0}` (`key`, `value`) VALUES (\"{1}\", \"{2}\");"
        # print("------" + query)
        # print("------" + key)
        # print("------" + value)
        value = value.replace("\"", "'")
        baseQueryWithTable = query.format(self.tableName, key, value)
        print("-----" + baseQueryWithTable)
        cur = self.conn.cursor(buffered=True)
        cur.execute(baseQueryWithTable)
        self.conn.commit()
        cur.close()
        
    def get(self, key):
        valuedQuery = "SELECT value FROM " + self.tableName + " WHERE key = ?;"
        cur = self.conn.cursor(buffered=True)
        cur.execute(valuedQuery, (key,))
        fetchedResults = cur.fetchall()
        data = []
        for entry in fetchedResults:
            data.append(entry[0])
        return data[0]
        
    def all(self):
        query = "SELECT key, value FROM " + self.tableName + ";"
        cur = self.conn.cursor(buffered=True)
        cur.execute(query)
        fetchedResults = cur.fetchall()
        data = []
        for entry in fetchedResults:
            entryConverted = list(entry)
            data.append({
                "key": entryConverted[0],
                "value": entryConverted[1],
            })
        return data
    
    def allGenerator(self):
        query = "SELECT key, value FROM " + self.tableName + ";"
        cur = self.conn.cursor(buffered=True)
        cur.execute(query)
        fetchedResults = cur.fetchall()
        for entry in fetchedResults:
            entryConverted = list(entry)
            yield {
                "key": entryConverted[0],
                "value": entryConverted[1]
            }
