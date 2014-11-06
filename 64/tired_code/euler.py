import sys, itertools, math, re

def calcformula(f):
    tag = re.search('(\^\/.*?)\)$',f).group(1)
    b,a = tag.split('+')
    print 'b, a', b, a
    original_base = None
    if '/' in a:
        a,original_base = a.split('/')
    b_raw = b.replace('^/','')
    bunbo = int(b_raw) - int(a)**2
    if original_base:
        bunbo = bunbo/int(original_base)
    #print bunbo, int(a), abs(int(a))
    if abs(int(a)) >= abs(bunbo):
        left_candi = range(0,1000)
        # change definition of left
        try:
            left = filter(lambda x:(abs(int(a)) - x*abs(bunbo))**2 < int(b_raw), left_candi).pop()
        except:
            print 'illigal bunbo=', bunbo, 'a=', a, 'b_raw=', b_raw
        right = abs(int(a)) - left*bunbo
        #print 'a', abs(int(a)), bunbo, left, right
        target = str(left) + '+' +  b + '+' + str(right) + '/' + str(bunbo) 
        f = re.sub('\d{1,}\/\(\^\/.*?\)', target, f)
        return f
    # this is a illigal pattern 
    if abs(int(a)) < bunbo:
        bunshi_left = int(a) + bunbo
        target = '1' + '+' +  b + '+-' + str(bunshi_left) + '/' + str(bunbo)
        f = re.sub('\d{1,}\/\(\^\/.*?\)', target, f)
        return f

def inverse(f):
    tag = re.search('(\^\/.*?)$',f).group(1)
    f = re.sub('(\^\/.*?)$','1/1/(' + tag + ')',f)
    return f

def lexical_parse(f):
    lex = re.findall('\/(\d{1,})', f)[:-2]
    return lex

def maybePattern(lex):
    for i in xrange(1, len(lex)):
        if lex[:i] == lex[i:i*2] == lex[i*2:i*3] == lex[i*3:i*4] == lex[i*4:i*5] == lex[i*5:i*6] == lex[i*6:i*7] == lex[i*8:i*9] == lex[i*9:i*10] == lex[i*10:i*11] == lex[i*11:i*12]:
            return i
def formula(N):
    #describe as N as root
    d = int(math.sqrt(N))
    # build initial fomula
    f = str(d) + '+' + '^/' + str(N) + '+-' + str(d) + '' 
    # original
    for i in xrange(1,150):
        f = inverse(f)
        f = calcformula(f)
        #print N, f
    #print 'calced', N,  f
    lex = lexical_parse(f)
    print lex
    print N, maybePattern(lex)
    if maybePattern(lex)%2 != 0:
        return True
    return False
c = 0
for i in xrange(28,30):
    if int(math.sqrt(i))**2 == i:
        continue
    if formula(i):
        c += 1
print 'result', c 
