import math, sys, itertools

def palindromicGenerator(i):
    buff = i + int(str(i)[::-1])
    while True:
        yield buff
        buff = buff + int(str(buff)[::-1])
c = 0
for i in xrange(1, 10000):
    for num, palin in enumerate(palindromicGenerator(i)):
        palinList, palinLen = str(palin), len(str(palin))
        fixer = 0
        if palinLen%2 !=0:
            fixer = 1
        #print 'evaling', i, num+1, palinList, palinList[:palinLen/2+fixer], palinList[palinLen/2:][::-1]
        if palinList[:palinLen/2+fixer] == palinList[palinLen/2:][::-1]:
            print i, num+1, palinList
            break
        if num+1 > 50:
            c += 1
            break
print c
    
