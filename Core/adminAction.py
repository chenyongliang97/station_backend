from Core.BusTable import BusTable
from Core.PurchaseTable import PurchaseTable
from Core.AccountTable import AccountTable
from Core.IdentityTable import IdentityTable

# 传入一个Bus对象，如果该Bus不存在表中，就插入，返回成功或失败
def adminInsertBus(Bus):
    BT = BusTable()
    return BT.insert_bus(Bus)

# 删除一条Bus记录：
# 根据Bus的出发地，目的地，日期和Id来查找
def adminDeleteBus(departure, destination, date, BusId):
    BT = BusTable()
    b = BT.get_one_bus(departure, destination, date, BusId)
    BT.delete_bus(b)


# 如果修改了车的Id，要对Purchase表中对应用户的项进行更新（改了Id，用户则将票换成新Id的车）
# 若是修改其他信息，则不需要对Purchase表中的信息进行修改
def adminUpdateBus(OBus, NBus):
    BT = BusTable()
    PT = PurchaseTable()
    _list = PT.findRecordForOneBus(OBus['Departure'], OBus['Destination'], OBus['BusDate'], OBus['BusId'])
    if NBus['BusId'] != OBus['BusId']:
        for i in _list:
            PT.updateRecord(i, 'undefined', 'undefined', 'undefined', NBus['BusId'])

    BT.update_bus(OBus, NBus)