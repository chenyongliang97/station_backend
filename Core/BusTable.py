from Core.getDatabase import getDatabase
from pymongo import MongoClient
from Core.Bus import Bus
PORT = 27017

# Bus表，存放所有bus的信息
class BusTable():
    def __init__(self):
        pass

    def insert_bus(self, b):
        # client, cursor = getDatabase('bus_collections')  # or cursor = db.test_collections auto create the collection
        # cursor.ensure_index('', unique=True)
        client, cursor = getDatabase('bus_collections')
        condition = {'BusDate': b['BusDate'], 'BusId': b['BusId'], 'Departure': b['Departure'], 'Destination': b['Destination']}
        if cursor.find_one(condition) == None:
            cursor.insert_one(b)
            client.close()
            return True
        else:
            client.close()
            return False

    def delete_bus(self, Bus):
        client, cursor = getDatabase('bus_collections')
        if cursor.find(Bus) == None:
            client.close()
            return False
        else:
            cursor.delete_one(Bus)
            client.close()
            return True

    # 根据出发地、目的地和日期来找车
    def find_bus(self, departure, destination, date):
        client, cursor = getDatabase('bus_collections')
        _list = cursor.find({'Departure': departure, 'Destination': destination, 'BusDate': date}).sort('Busdate')
        client.close()
        return _list

    def get_one_bus(self, departure, destination, date, BusId):
        client, cursor = getDatabase('bus_collections')
        condition = {'Departure': departure, 'Destination': destination, 'BusDate': date, 'BusId': BusId}
        bus = cursor.find_one(condition)
        client.close()
        return bus

    def buy(self, departure, destination, date, BusId):
        client, cursor = getDatabase('bus_collections')
        condition = {'BusDate': date, 'BusId': BusId, 'Departure': departure,
                     'Destination': destination}
        b = cursor.find_one(condition)
        if b['left_num'] > 0:
            b['left_num'] = b['left_num'] - 1
            cursor.update(condition, b)
            client.close()
            return True
        return False

