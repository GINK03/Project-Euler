import itertools
# January(1, 31), March(3, 31), April(4, 30), May(5, 31), June(6, 30), July(7, 31), 
# August(8, 31),September(9, 30), Octorber(10, 31), November(11, 30), December(12, 31) 
class E:
    def __init__(self, month, MAX):
        self.month = month
        self.MAX = MAX
    def getMAX(self, year):
        return self.MAX
    def getMonth(self):
        return self.month
# February
class Feb:
    def __init__(self):
        self.month = 2
        self.MAX   = None
    def getMAX(self, year):
        if year%4 == 0 and not (year%400 != 0 and year%100 == 0) :
            return 29
        else:
            return 28
    def getMonth(self):
        return self.month 

class Buf:
    dayBuffInMonth = 1
    dayBuffInYear = 1
    @staticmethod
    def getMonth():
        return Buf.dayBuffInMonth
    @staticmethod
    def nextMonth():
        Buf.dayBuffInMonth += 1
    @staticmethod
    def getYear():
        return Buf.dayBuffInYear
    @staticmethod
    def nextYear():
        Buf.dayBuffInYear += 1

monthIter = itertools.cycle([ E(1,31), Feb(), E(3, 31), E(4, 30), E(5, 31), E(6, 30), E(7, 31), \
        E(8, 31), E(9, 30), E(10, 31), E(11, 30), E(12, 31)] )
weeks = ['Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun', 'Mon']
countUpResult = 0

nowYear = 1901
oneYearDate = 365
nowMonth = monthIter.next()

for week in itertools.cycle(weeks):
    if Buf.getMonth() == 1 and week == 'Sun':
        countUpResult += 1
    print week, nowYear, nowMonth.getMonth(), Buf.getMonth(), Buf.getYear(), countUpResult
    if Buf.getMonth() % nowMonth.getMAX(nowYear) == 0:
        nowMonth = monthIter.next()
        Buf.dayBuffInMonth = 0
    if nowMonth.getMAX(nowYear) == 29:
        oneYearDate = 366
    if Buf.getYear() % oneYearDate == 0:
        nowYear += 1
        print 'inc year', Buf.getMonth(), oneYearDate, Buf.getYear()
        oneYearDate = 365
        Buf.dayBuffInYear = 0
    Buf.nextMonth()
    Buf.nextYear()
