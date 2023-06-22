import sys
sys.path.append("..")
from aws_costs_api.Repository import Repository

try:
    connectionString = sys.argv[1]
except IndexError:
    print("Yoy must put the first argument as a connection string for the database.")
    exit()

try:
    keyStored = sys.argv[2]
except IndexError:
    print("Yoy must put a second argument to be the key to be stored.")
    exit()

try:
    valueStored = sys.argv[3]
except IndexError:
    print("Yoy must put a third argument to be value to be stored.")
    exit()

repository = Repository()

print("Your connection string is: " + connectionString)
repository.setConnectionString(connectionString)
repository.store(keyStored, valueStored)
