from pymongo import MongoClient
import pickle
import json

if __name__ == '__main__':
    client = MongoClient('localhost', 27017)  # ip and port
    db = client.test_database  # or db = client['test_database'] auto create the database
    cursor = db['test_collections']  # or cursor = db.test_collections auto create the collection

    data1 = {'test': 3, 'hh': 1}  # the data you want to insert
    cursor.ensure_index([('test', 1), ('hh', 1)], unique=True)
    #cursor.insert_one(data1)


    if cursor.find_one({'test': 1, 'hh': 2}) == None:
        print(1)
    else:
        print(2)
    for i in cursor.find():
        print(i)
        cursor.delete_one({'test': 2})

    client.close()
