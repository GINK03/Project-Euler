import sys,os,math,itertools, operator, fractions
sys.path.append('../pythonlib')
import basic
MAX = 10**6
MAX = 1500000
result = 0
tgt = [x for x in xrange(1, MAX+1)]
tgt.reverse()
for x in tgt:
    if x%100 == 0:
        print 'iter', x
    temp_res = 0
    for m in xrange(1, int(math.sqrt(x/2)) + 1):
        for n in xrange(1, m):
            a, b, c = m**2 - n**2, 2*m*n, m**2 + n**2
            sum_entity = sum([a,b,c])
            k = 1
            if x%sum_entity == 0:
                k = x/sum_entity
                a, b, c = map(lambda x:x*k,[a, b, c])
            sum_entity = sum([a,b,c])
            if sum_entity == x:
                #print 'heavy', m,n,k,a,b,c
                temp_res += 1
    '''
    for m in xrange(1, int(math.sqrt(x/2)) + 1):   
        n = x/(2*m) - m
        a, b, c = m**2 - n**2, 2*m*n, m**2 + n**2
        cflag = True
        if sum([a,b,c]) == x:
            print 'light', m, n, a, b, c
            temp_res += 1
    ''' 
    if temp_res == 2 or temp_res == 1:
        result += 1
print 'result', result        

