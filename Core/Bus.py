from .Date import Date
from datetime import date

class Bus(dict):
    def __init__(self, BusDate = "2018-10-07", BusId = 1, Time = "16:55", Departure = "aaa", Destination = "bbb", left_num = 50, Price = 100):
        self['BusDate'] = BusDate
        self['BusId'] = BusId
        self['Time'] = Time
        self['Departure'] = Departure
        self['Destination'] = Destination
        self['left_num'] = left_num
        self['Price'] = Price

    def set_price(self, p):
        self.Price = p

    def set_time(self, BusDate, t):
        if int(BusDate.year + BusDate.month + BusDate.day + t) < int(self.BusDate.year + self.BusDate.month + self.BusDate.day + self.Time):
            return False
        else:
            self.BusDate = BusDate
            self.Time = t
            return True

    def sell_ticket(self):
        if self.left_num > 0:
            self.left_num -= 1
            return True
        else:
            return False

    def cancel_ticket(self):
        self.left_num += 1