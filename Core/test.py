import Core.Bus
import userAction
import time
import adminAction
from Core.getDatabase import getDatabase
from Core.PurchaseTable import PurchaseTable
def test():
    # 插入26个用户和一个管理员
    for i in range(0,26):
        userAction.userCreateAccount(chr(97+i), 123, 0)
    userAction.userCreateAccount('admin', 123, 1)

    for i in range(0, 26):
        userAction.userAddCard(chr(97+i), 440782199701018011, 'aaa', 12345678901)
        userAction.userAddCard(chr(97+i), 440782199701018012, 'bbb', 12345678901)
        userAction.userAddCard(chr(97+i), 440782199701018013, 'ccc', 12345678901)

    # 插入100辆车 每辆车有两个乘客 余票设为1
    PT = PurchaseTable()
    for i in range(0, 100):
        B = Core.Bus.Bus('2018-12-1' + chr(48 + i % 20), i , '13:00', '15:00', chr(65 + i % 24) + chr(65 + i %24), chr(66 + i %24) + chr(66 + i %24), 1, 100)
        adminAction.adminInsertBus(B)
        PT.insertRecord(chr(97+i % 20), 440782199701018011, chr(65 + i % 24) + chr(65 + i %24), chr(66 + i %24) + chr(66 + i %24), '2018-12-1' + chr(48 + i % 20), i, 100)
        PT.insertRecord(chr(97+i % 20), 440782199701018012, chr(65 + i % 24) + chr(65 + i %24), chr(66 + i %24) + chr(66 + i %24), '2018-12-1' + chr(48 + i % 20), i, 100)

