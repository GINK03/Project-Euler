import math, itertools

MasuL = []
class Masu:
    def __init__(self, num):
        self.num = num
        self.vartical = 0
        self.horizontal = 0
    def whereShouldBe(self):
        if self.num == 1:
            res = Masu(self.num + 1)
            res.vartical = 0
            res.horizontal = 1
            MasuL.append(res)
            return res
        ##print self.num
        ##print MasuL
        # if exist left and not exist under -> make new ins to under 
        if filter(lambda x: x.vartical == self.vartical and x.horizontal == (self.horizontal-1), MasuL) != []:
            print 'make 3 or 12'
            res = Masu(self.num + 1)
            res.vartical = self.vartical -1
            res.horizontal = self.horizontal
            MasuL.append(res)
            return res
        # if exist up and not exist left -> make new ins to under
        if filter(lambda x: x.vartical == self.vartical+1 and x.horizontal == self.horizontal, MasuL) != [] and \
            filter(lambda x: x.vartical == self.vartical and x.horizontal == self.horizontal-1,MasuL) == []:
            print 'make 4 or 15'
            res = Masu(self.num + 1)
            res.vartical = self.vartical
            res.horizontal = self.horizontal - 1
            MasuL.append(res)
            return res
        # if exist right and not exist left -> make new ins to under
        if filter(lambda x: x.vartical-1 == self.vartical and x.horizontal == self.horizontal, MasuL) != [] and \
            filter(lambda x: x.vartical == self.vartical and x.horizontal == self.horizontal+1,MasuL) == []:
            print 'make 5 or 18'
            res = Masu(self.num + 1)
            res.vartical = self.vartical
            res.horizontal = self.horizontal - 1
            MasuL.append(res)
            return res
        # if exist right and not exist under not exist up -> make new ins to under
        if filter(lambda x: x.vartical == self.vartical and x.horizontal == self.horizontal+1, MasuL) != [] and \
            filter(lambda x: x.vartical == self.vartical-1 and x.horizontal == self.horizontal,MasuL) == [] and \
            filter(lambda x: x.vartical == self.vartical+1 and x.horizontal == self.horizontal,MasuL) == []:
            print 'make 6 or 18'
            res = Masu(self.num + 1)
            res.vartical = self.vartical + 1
            res.horizontal = self.horizontal
            MasuL.append(res)
            return res
        # if exist under and not exist up -> make new ins to under
        if filter(lambda x: x.vartical == self.vartical-1 and x.horizontal == self.horizontal, MasuL) != [] and \
            filter(lambda x: x.vartical == self.vartical+1 and x.horizontal == self.horizontal,MasuL) == []:
            print 'make 7 or 21'
            res = Masu(self.num + 1)
            res.vartical = self.vartical + 1
            res.horizontal = self.horizontal
            MasuL.append(res)
            return res
        print 'err', self.vartical, self.horizontal
        #if filter(lambda x: x.vartical == self.vartical and x.horizontal == self.horizontal, MasuL) != []:

def generator():
    n = 1
    while True:
        n += 1
        yield n

nextMasu = Masu(1)
MasuL.append(nextMasu)
for n in generator():
    # now ins
    masu = nextMasu
    # next ins
    nextMasu = nextMasu.whereShouldBe()
    print masu.num, masu.vartical, masu.horizontal
    print nextMasu.num, nextMasu.vartical, nextMasu.horizontal
    if n == 7:
        break
