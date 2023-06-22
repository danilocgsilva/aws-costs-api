import sqlite3

class Repository:

    def setConnectionString(self, connectionString: str):
        self.connectionString = connectionString

    def store(self, key, value):
        conn = sqlite3.connect(self.connectionString)

