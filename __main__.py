from pymongo import MongoClient
from Core.Bus import Bus
# from datetime import date, time, datetime
# from Core.BusTime import BusTime
# from Core.BusTable import BusTable
# from Core.PurchaseTable import PurchaseTable
import userAction
import time
import adminAction

import pickle
import json

from Core.Account import Account
from Core.AccountTable import AccountTable
from Core.IdentityTable import IdentityTable


if __name__ == '__main__':
    # client = MongoClient('localhost', 27017)  # ip and port
    # db = client.test_database  # or db = client['test_database'] auto create the database
    # cursor = db['test_collections']  # or cursor = db.test_collections auto create the collection
    #
    # data1 = {'test': 5, 'hh': 1}  # the data you want to insert
    # # cursor.ensure_index([('test', 1), ('hh', 1)], unique=True)
    # cursor.insert_one(data1)
    # client.close()

    # a = Account('liu', '123')
    # at = AccountTable()
    # if at.exist(a):
    #     print("no")
    # else:
    #     at.insert_account(a)
    #     print("yes")

    # it = IdentityTable()
    # it.insert(a, '123456789321')
    # print(it.delete(a, '123456789321'))

    # bt = BusTable()
    # b = Bus()
    # condition = {'BusDate': b['BusDate'], 'BusId': b['BusId'], 'Departure': b['Departure'],
    #              'Destination': b['Destination']}
    # print(bt.insert_bus(condition, b))
    # b2 = bt.get_one_bus(b['Departure'], b['Destination'], b['BusDate'], b['BusId'])
    # print(b2)
    # # _list = bt.find_bus('aaa', 'bbb', '2018-10-07')
    # # for i in _list:
    # #     print(i)
    # pt = PurchaseTable()
    # pt.buy('liu', 123456789123, b2)
    # b2 = bt.get_one_bus(b['Departure'], b['Destination'], b['BusDate'], b['BusId'])
    # print(b2)
    # print(at.login(a))

    # BusDate = "2018-10-07", BusId = 1, dTime = "16:55", aTime = "17:50", Departure = "aaa", Destination = "bbb", left_num = 50, Price = 100

    # OBus = Bus('2018-10-08',  2, '01:00', '03:00', '出发地1', '目的地1', 50, 2200)
    # adminAction.adminInsertBus(OBus)
    # userAction.userAddCard('chen', 111111111)
    # userAction.userBuyTicket('chen', 111111111, '出发地1', '目的地1', '2018-10-08', 2)
    # list = userAction.userSearchBus('出发地', '目的地', '2018-10-07')
    # for i in list:
    #     print(i)
    #
    # # NBus = Bus('2018-10-07',  2, '01:00', '03:00', '出发地', '目的地', 50, 4396)
    # # NBus['BusId'] = 3
    # # NBus['left_num'] = 49
    # # adminAction.adminUpdateBus(OBus, NBus)
    # _list, tn = userAction.checkBookList('chen', 111111111)
    # print(tn)
    # for i in _list:
    #     print(i)
    # adminAction.adminDeleteBus('aaa', 'bbb', '2018-10-07', 1)
    # adminAction.adminSearchRecord('undefined', 'undefined', 'undefined', 'undefined')
    # userAction.userDeleteTicket('chen', 123456789, '出发地', '目的地', '2018-10-07', 1)
    # print(time.strftime('%Y-%m-%d%H:%M', time.localtime(time.time())))
    userAction.userCreateAccount('liang', 123, 1)
    print(userAction.userGetLevel('liang'))
    userAction.userAddCard('liang', 440782199707088014, '陈泳良', 15902056460)
    _list = userAction.userShowCard('liang')
    for i in _list:
        print(i)