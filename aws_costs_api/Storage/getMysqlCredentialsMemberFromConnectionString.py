def getMysqlCredentialsMemberFromConnectionString(connectionString: str):
    credentialsMembers = connectionString.split(";")

    db_host = None
    db_user = None
    db_password = None
    db_database = None
    db_port = None
    
    for credentialMember in credentialsMembers:

        keyValuePair = credentialMember.split("=")
        key = credentialMember[0]
        value = credentialMember[1]

        if key == "HOST":
            db_host = value
        if key == "USER":
            db_user = value
        if key == "PASSWORD":
            db_passworc = value
        if key == "DATABASE":
            db_database = value
        if key == "PORT":
            db_port = value

    return db_host, db_user, db_password, db_database, db_port
