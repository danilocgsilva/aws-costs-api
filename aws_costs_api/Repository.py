import sqlite3

class Repository:
    
    def __init__(self):
        self.tableName = "key_value"

    def setConnectionString(self, connectionString: str):
        self.connectionString = connectionString
        self.conn = sqlite3.connect(self.connectionString)
        
    def dataExists(self, key) -> bool:
        if not self.tableExists():
            self.createTable()
        query = "SELECT value FROM {0} WHERE key = \"{1}\";"
        queryValued = query.format(self.tableName, key)
        cur = self.conn.cursor()
        tableResults = cur.execute(queryValued)
        fetchedResults = tableResults.fetchall()
        return not len(fetchedResults) == 0

    def store(self, key, value):
        if not self.tableExists():
            self.createTable()
        query = "INSERT INTO {0} (key, value) VALUES (?, ?);"
        baseQueryWithTable = query.format(self.tableName)
        cur = self.conn.cursor()
        cur.execute(baseQueryWithTable, (key, value, ))
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

    def get(self, key):
        queryBase = "SELECT value FROM " + self.tableName + " WHERE key = \"{0}\";"
        valuedQuery = queryBase.format(key)
        cur = self.conn.cursor()
        resultsObj = cur.execute(valuedQuery)
        fetchedResults = resultsObj.fetchall()
        return fetchedResults[0][0]
        