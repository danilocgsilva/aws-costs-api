class GetMysqlCredentialsMemberFromConnectionString:

    def __init__(self, connectionString: str):
        self.connectionString = connectionString

    def getAllMembers(self):
        credentialsMembers = self.connectionString.split(";")

        self.db_host = None
        self.db_user = None
        self.db_password = None
        self.db_database = None
        self.db_port = 3306
        
        for credentialMember in credentialsMembers:

            keyValuePair = credentialMember.split("=")
            key = keyValuePair[0]
            value = keyValuePair[1]

            if key == "HOST":
                self.db_host = value
            if key == "USER":
                self.db_user = value
            if key == "PASSWORD":
                self.db_password = value
            if key == "DATABASE_NAME":
                self.db_database = value
            if key == "PORT":
                self.db_port = value
                
        return self.db_host, self.db_user, self.db_password, self.db_database, self.db_port

