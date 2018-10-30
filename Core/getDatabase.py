from pymongo import MongoClient
PORT = 27017

def getDatabase(dbname):
    client = MongoClient('localhost', PORT)
    db = client.station_database
    cursor = db[dbname]
    return client, cursor
