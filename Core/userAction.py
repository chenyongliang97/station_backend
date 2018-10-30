from Core.BusTable import BusTable
from Core.PurchaseTable import PurchaseTable
from Core.AccountTable import AccountTable
from Core.IdentityTable import IdentityTable

# 定义了用户所能进行的所有动作

#根据用户给定的条件查找对应的巴士，返回巴士列表
def userSearchBus(departure, destination, date):
    BT = BusTable()
    return BT.find_bus(departure, destination, date)

# 为username用户使用card购买符合条件的票，返回成功或失败
def userBuyTicket(username, card, departure, destination, date, BusId):
    BT = BusTable()
    PT = PurchaseTable()
    f = BT.buy(departure, destination, date, BusId)
    if f:
        PT.insertRecord(username, card, departure, destination, date, BusId)
        return True
    else:
        return False

# 登陆名为username的用户,验证password是否正确，返回0：不存在账号；1：密码错误；2：登陆成功
def userLogIn(username, password):
    AT = AccountTable()
    return AT.login(username, password)

# 创建名为username，密码为password的用户，返回成功或失败（已存在名为username的用户）
def userCreateAccount(username, password):
    AT = AccountTable()
    if AT.exist(username):
        return False
    else:
        AT.insert_account(username, password)
        return True

# 返回usernmae用户绑定的所有身份证
def userShowCard(username):
    IT = IdentityTable()
    return IT.find(username)

# 为username的用户添加一张卡card
def userAddCard(username, card):
    IT = IdentityTable()
    IT.insert(username, card)

# 为username的用户删除一张卡card
def userDeleteCard(username, card):
    IT = IdentityTable()
    return IT.delete(username, card)

