from Core.BusTable import BusTable
from Core.PurchaseTable import PurchaseTable
from Core.AccountTable import AccountTable
from Core.IdentityTable import IdentityTable
import userAction

# 传入一个Bus对象，如果该Bus不存在表中，就插入，返回成功或失败
def adminInsertBus(Bus):
    BT = BusTable()
    return BT.insert_bus(Bus)

# 删除一条Bus记录：
# 根据Bus的出发地，目的地，日期和Id来查找
def adminDeleteBus(departure, destination, date, BusId):
    BT = BusTable()
    b = BT.get_one_bus(departure, destination, date, BusId)
    flag = BT.delete_bus(b)
    PT = PurchaseTable()
    _list = PT.findRecordForOneBus(departure, destination, date, BusId)
    for i in _list:
        userAction.userDeleteTicket(i['username'], i['card'], departure, destination, date, BusId)
    return flag

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


# 传入的参数为起始日期，终止日期，出发站和终点站
# 如果上述输入有缺省，用undefined替代。起始日期和终止日期要么同时存在，要么一起缺省，出发站和终点站则无所谓
# 得到的结果为根据所查信息搜得的乘客总数和营收总金额，以及一个装着符合条件的巴士信息（出发地，目的地，日期，车id，车的总乘客，该车的总营收）的列表和一个每一天的乘客总数及营收金额的列表
def adminSearchRecord(startDate, endDate, departure, destination):
    PT = PurchaseTable()
    totalCustomer, totalRevenue, _list1, _list2 = PT.findRangeRecord(startDate, endDate, departure, destination)
    return totalCustomer, totalRevenue, _list1, _list2
    #      时间段内总乘客  时间段内总营收 巴士统计信息 每天统计信息