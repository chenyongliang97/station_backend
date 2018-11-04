from Core.getDatabase import getDatabase
from Core.BusTable import BusTable
from pymongo import MongoClient

class PurchaseTable():

    def __init__(self):
        pass

    def insertRecord(self, username, card, departure, destination, date, BusId, price):
        client, cursor = getDatabase('purchase_collections')
        cursor.insert_one({'username': username, 'card': card, 'departure': departure, 'destination': destination, 'date': date, 'BusId': BusId, 'price': price})
        client.close()

    def updateRecord(self, oldRecord, departure = 'undefined', destination = 'undefined', date = 'undefined',
                    BusId = -1):
        client, cursor = getDatabase('purchase_collections')
        if departure == 'undefined':
            Ndeparture = oldRecord['departure']
        else:
            Ndeparture = departure

        if destination == 'undefined':
            Ndestination = oldRecord['destination']
        else:
            Ndestination = destination

        if date == 'undefined':
            Ndate = oldRecord['date']
        else:
            Ndate = date

        if BusId == -1:
            NBusId = oldRecord['BusId']
        else:
            NBusId = BusId

        cursor.update(oldRecord, {'$set': {'departure': Ndeparture, 'destination': Ndestination, 'date': Ndate, 'BusId': NBusId}})
        client.close()
        return

    # admin使用
    def findRecordForOneBus(self, departure, destination, date, BusId):
        client, cursor = getDatabase('purchase_collections')
        _list = cursor.find({'departure': departure, 'destination': destination, 'date': date, 'BusId': BusId})
        client.close()
        return _list

    # 用户使用
    def searchRecord(self, condition):
        client, cursor = getDatabase('purchase_collections')
        _list = cursor.find(condition)
        client.close();
        return _list
