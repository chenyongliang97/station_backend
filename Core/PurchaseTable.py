from Core.getDatabase import getDatabase
from Core.BusTable import BusTable
from pymongo import MongoClient

class PurchaseTable():

    def __init__(self):
        pass

    def insertRecord(self, username, card, departure, destination, date, BusId):
        client, cursor = getDatabase('purchase_collections')
        cursor.insert_one({'username': username, 'card': card, 'departure': departure, 'destination': destination, 'date': date, 'BusId': BusId})
        client.close()

