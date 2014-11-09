import sys,math,os,itertools,fractions
sys.path.append('../pythonlib')
import basic
MAX = 10**6
pSet = set(basic.primeTable(MAX))
fix = -2
table = [0]
for i in xrange(1, MAX+1):
    fi = basic.totientFunction(i,pSet)
    table.append( fi )
c = 0
fibuff = 0
scala  = 0
'''
for i in xrange(1, MAX+1):
    fibuff += table[i] + 1 + fix
    scala  += fibuff
    #c = sum(table[:i+1])
    #print i, fibuff, scala, c
    if i%10000 == 0:
        print 'iter', i
'''
print 'result = ', sum(table) + 1 + fix
