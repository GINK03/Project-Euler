# coding: utf-8
import os,sys,math,__future__,itertools

class Kaibuns:
    def __init__(self):
        self.data = []
    def getMax(self):
        sortedData = sorted(self.data, key=lambda x:int(x))
        return sortedData[-1]
kaibuns = Kaibuns()
def checkKaibun(e):
    asList = str(e[0] * e[1])
    isCorrespond = True
    i = 0

    while i < len(asList)/1:
        if asList[i] != asList[(-1) * (i + 1) ]:
            isCorrespond = False
        i += 1
    if isCorrespond :
        kaibuns.data.append(asList)
            

if __name__ == '__main__':
    baseList = range(100,999)
    for e in itertools.permutations(baseList, 2):
        checkKaibun(e)
    print(kaibuns.getMax())
