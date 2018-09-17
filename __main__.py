from pymongo import MongoClient
from Core.Bus import Bus
from datetime import date, time, datetime
from Core.BusTime import BusTime
from Core.BusTable import BusTable
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

    a = Account('chen', '123')
    at = AccountTable()
    # if at.exist(a):
    #     print("no")
    # else:
    #     at.insert_account(a)
    #     print("yes")

    it = IdentityTable()
    #it.insert(a, '123456789321')
    list = it.find(a)
    for i in list:
        print(i)
    # print(at.login(a))