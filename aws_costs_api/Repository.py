import sqlite3

class Repository:
    
    def __init__(self):
        self.tableName = "key_value"

    def setConnectionString(self, connectionString: str):
        self.connectionString = connectionString
        self.conn = sqlite3.connect(self.connectionString)
        
    def dataExists(self, key) -> bool:
        query = "SELECT value FROM {0} WHERE key = \"{1}\";"
        queryValued = query.format(self.tableName, key)
        cur = self.conn.cursor()
        tableResults = cur.execute(queryValued)
        fetchedResults = tableResults.fetchall()
        return not len(fetchedResults) == 0

    def store(self, key, value):
        if not self.tableExists():
            self.createTable()
        query = "INSERT INTO {0} (key, value) VALUES (\"{1}\", \"{2}\");"
        valuedQuery = query.format(self.tableName, key, value)
        cur = self.conn.cursor()
        cur.execute(valuedQuery)
        self.conn.commit()
        cur.close()

    def tableExists(self) -> bool:
        queryCheck = "SELECT name FROM sqlite_master WHERE type='table' AND name='" + self.tableName + "'"
        cur = self.conn.cursor()
        tableResults = cur.execute(queryCheck)
        fetchedResults = tableResults.fetchall()
        return not len(fetchedResults) == 0

    def createTable(self):
        queryCreateTable = "CREATE TABLE " + self.tableName + "(key STRING, value STRING)"
        cur = self.conn.cursor()
        cur.execute(queryCreateTable)
        cur.close()


