# coding: utf-8

class PrimeStack:
    def __init__(self):
        self.l = []
    def calcX(self):
        buff = 1
        for x in self.l:
            buff *= x
        return buff
TGT_NUM = 600851475143
if __name__ == '__main__':
    stack = PrimeStack()
    for i in xrange(2, TGT_NUM):
        if TGT_NUM % i == 0:
            print i, 'is prime'
            stack.l.append(i)
            print 'calcX = ', stack.calcX()
            if stack.calcX() == TGT_NUM:
                break
