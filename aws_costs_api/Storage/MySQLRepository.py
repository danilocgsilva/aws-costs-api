from aws_costs_api.Storage.IRepository import IRepository
import mysql.connector
from aws_costs_api.Storage.GetMysqlCredentialsMemberFromConnectionString import GetMysqlCredentialsMemberFromConnectionString

class MySQLRepository(IRepository):
    
    def __init__(self):
        self.tableName = "aws_costs"

    def getTableName(self) -> str:
        return self.tableName

    def setConnectionString(self, connectionString: str):

        cs = GetMysqlCredentialsMemberFromConnectionString(connectionString)
        db_host, db_user, db_password, db_name, db_port = cs.getAllMembers()

        self.conn = mysql.connector.connect(
            host=db_host,
            user=db_user,
            password=db_password,
            database=db_name,
            port=db_port
        )

        self.schemaName = db_name

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
        cur.execute(queryValued)
        fetchedResults = cur.fetchall()
        return not len(fetchedResults) == 0

    def store(self, key, value):
        if not self.tableExists():
            self.createTable()
        query = "INSERT INTO `{0}` (`key`, `value`) VALUES (%s, %s);"
        baseQueryWithTable = query.format(self.tableName)
        cur = self.conn.cursor(buffered=True)
        cur.execute(baseQueryWithTable, (key, value))
        self.conn.commit()
        cur.close()
        
    def get(self, key):
        queryBase = "SELECT value FROM " + self.tableName + " WHERE `key` = \"{0}\";"
        valuedQuery = queryBase.format(key)
        cur = self.conn.cursor(buffered=True)
        cur.execute(valuedQuery)
        fetchedResults = cur.fetchall()
        data = []
        for entry in fetchedResults:
            data.append(entry[0])
        return data[0]
        
    def all(self):
        query = "SELECT `key`, `value` FROM " + self.tableName + ";"
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
        query = "SELECT `key`, `value` FROM " + self.tableName + ";"
        cur = self.conn.cursor(buffered=True)
        cur.execute(query)
        fetchedResults = cur.fetchall()
        for entry in fetchedResults:
            entryConverted = list(entry)
            yield {
                "key": entryConverted[0],
                "value": entryConverted[1]
            }

    def dropTable(self):
        queryBase = "DROP TABLE {0}"
        query = queryBase.format(self.tableName)
        cur = self.conn.cursor(buffered=True)
        cur.execute(query)
        self.conn.commit()
        cur.close()
