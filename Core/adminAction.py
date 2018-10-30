from Core.BusTable import BusTable
from Core.PurchaseTable import PurchaseTable
from Core.AccountTable import AccountTable
from Core.IdentityTable import IdentityTable

# 传入一个Bus对象，如果该Bus不存在表中，就插入，返回成功或失败
def adminInsertBus(Bus):
    BT = BusTable()
    return BT.insert_bus(Bus)
