import sqlite3

class Repository:

    def setConnectionString(self, connectionString: str):
        self.connectionString = connectionString
        self.conn = sqlite3.connect(self.connectionString)

    def store(self, key, value):
        if not self.tableExists():
            print("Table not exists. Creating...")
            self.createTable()
        query = "INSERT INTO key_value (key, value) VALUES (\"{0}\", \"{1}\");"
        valuedQuery = query.format(key, value)
        cur = self.conn.cursor()
        cur.execute(valuedQuery)
        self.conn.commit()
        cur.close()

    def tableExists(self) -> bool:
        queryCheck = "SELECT name FROM sqlite_master WHERE type='table' AND name='key_value'"
        cur = self.conn.cursor()
        tableResults = cur.execute(queryCheck)
        fetchedResults = tableResults.fetchall()
        return not len(fetchedResults) == 0

    def createTable(self):
        queryCreateTable = "CREATE TABLE key_value(key STRING, value STRING)"
        cur = self.conn.cursor()
        cur.execute(queryCreateTable)
        cur.close()


