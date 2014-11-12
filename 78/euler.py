import sys,math,os, itertools

def euler_generator():
    n = 1
    while True:
        yield ( (-1)**(n-1), n*(3*n - 1)/2)
        yield ( (-1)**(n-1), n*(3*n + 1)/2)
        n += 1
mem = { 0:1,
        1:1,
        2:1}

def getdata(n):
    res = 0
    for v,delta in euler_generator():
        #print 'in eval', v,delta, n -delta
        if n - delta >= 0:
            res += v*mem.get(n - delta)
            #print 'geting', mem.get(n - delta), n-delta, res
        else:
            break
    mem.update({n:res})
    return  res
         
        
for i in itertools.count(1):
    result = getdata(i)
    if result%1000000 == 0:
        print 'final result = ', i, result
        break
    if i%10000 == 0:
        print 'res', i, result
