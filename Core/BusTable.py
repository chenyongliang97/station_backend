from pymongo import MongoClient
from .Bus import Bus
from .Date import Date
PORT = 27017

# Bus表，存放所有bus的信息
class BusTable():
    def __init__(self):
        pass

    def insert_bus(self, Bus):
        client = MongoClient('localhost', PORT)  # ip and port
        db = client.station_database  # or db = client['test_database'] auto create the database
        cursor = db['bus_collections']  # or cursor = db.test_collections auto create the collection
        # cursor.ensure_index('', unique=True)
        if cursor.find(Bus) == None:
            cursor.insert_one(Bus)
            client.close()
            return True
        else:
            client.close()
            return False

    def delete_bus(self, Bus):
        client = MongoClient('localhost', PORT)
        db = client.station_database
        cursor = db['bus_collections']
        if cursor.find(Bus) == None:
            client.close()
            return False
        else:
            cursor.delete_one(Bus)
            client.close()
            return True

    # 根据出发地、目的地和日期来找车
    def find_bus(self, departure, destination, date):
        client = MongoClient('localhost', PORT)
        db = client.station_database
        cursor = db['bus_collections']
        _list = cursor.find({'Departure': departure, 'Destination': destination, 'BusDate': date}).sort('Busdate')
        return _list