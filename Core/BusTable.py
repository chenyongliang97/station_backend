from pymongo import MongoClient
from .Bus import Bus
from .Date import Date
PORT = 6666

class BusTable():
    def __init__(self):
        pass

    def insert_bus(self, Bus):
        client = MongoClient('localhost', PORT)  # ip and port
        db = client.station_database  # or db = client['test_database'] auto create the database
        cursor = db['bus_collections']  # or cursor = db.test_collections auto create the collection
        cursor.ensure_index('test', unique=True)
        cursor.insert_one(Bus)

        cursor.close()