from Core.Account import Account
from pymongo import MongoClient
PORT = 27017

class IdentityTable():
    def __init__(self):
        pass

    def find(self, a):
        client = MongoClient('localhost', PORT)  # ip and port
        db = client.station_database  # or db = client['test_database'] auto create the database
        cursor = db['indentity_collections']  # or cursor = db.test_collections auto create the collection
        #cursor.find_all({'username': a.username})
        list = cursor.find({'username': a['username']})
        client.close()
        return list

    def insert(self, a, card):
        client = MongoClient('localhost', PORT)  # ip and port
        db = client.station_database  # or db = client['test_database'] auto create the database
        cursor = db['indentity_collections']  # or cursor = db.test_collections auto create the collection
        cursor.insert_one({'username': a['username'], 'card': card})
        client.close()
