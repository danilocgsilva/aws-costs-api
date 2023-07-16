def getMysqlCredentialsMemberFromConnectionString(connectionString: str):
    credentialsMembers = connectionString.split(";")

    db_host = None
    db_user = None
    db_password = None
    db_database = None
    db_port = None
    
    for credentialMember in credentialsMembers:

        keyValuePair = credentialMember.split("=")
        key = keyValuePair[0]
        value = keyValuePair[1]

        if key == "HOST":
            db_host = value
        if key == "USER":
            db_user = value
        if key == "PASSWORD":
            db_password = value
        if key == "DATABASE_NAME":
            db_database = value
        if key == "PORT":
            db_port = value
            
    if db_port == None:
        db_port = 3306

    return db_host, db_user, db_password, db_database, db_port
