from pymongo import MongoClient
from Core.BusTable import BusTable
from Core.Bus import Bus
PORT = 27017

class PurchaseTable():

    def __init__(self):
        pass

    def buy(self, username, card, Bus):
        client = MongoClient('localhost', PORT)  # ip and port
        db = client.station_database  # or db = client['test_database'] auto create the database
        cursor = db['purchase_collections']

