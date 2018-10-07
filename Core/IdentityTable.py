from Core.Account import Account
from pymongo import MongoClient
PORT = 27017

# 用来存储一个用户对应的多个身份证的关系：[用户账号(username)，身份证号(card)] 1:m

class IdentityTable():
    def __init__(self):
        pass

    # 返回一个用户所绑定的所有身份证
    def find(self, a):
        client = MongoClient('localhost', PORT)  # ip and port
        db = client.station_database  # or db = client['test_database'] auto create the database
        cursor = db['identity_collections']  # or cursor = db.test_collections auto create the collection
        _list = cursor.find({'username': a['username']})
        client.close()
        return _list

    # 为一个用户添加一个身份证
    def insert(self, a, card):
        client = MongoClient('localhost', PORT)  # ip and port
        db = client.station_database  # or db = client['test_database'] auto create the database
        cursor = db['identity_collections']  # or cursor = db.test_collections auto create the collection

        if cursor.find_one({'username': a['username'], 'card': card}) == None:
            cursor.insert_one({'username': a['username'], 'card': card})
        client.close()

    # 为一个用户删除一个身份证
    def delete(self, a, card):
        username = a['username']
        client = MongoClient('localhost', PORT)
        db = client.station_database
        cursor = db['identity_collections']
        b = cursor.find_one({'username': username, 'card' : card})
        if b == None:
            return False  # 该用户没绑定该身份证
        else:
            cursor.delete_one(b)
            return True  # 删除成功
