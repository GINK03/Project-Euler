import sys, itertools, copy
def triangle():
    n = 1
    while True:
        yield n*(n+1)/2
        n += 1

def squaragenerator():
    n = 1
    while True:
        yield n*n
        n += 1

def pentagenerator():
    n = 1
    while True:
        yield n*(3*n - 1)/2
        n += 1

def octagenerator():
    n = 1
    while True:
        yield n*(2*n - 1)
        n += 1

def nonagenerator():
    n = 1
    while True:
        yield n*(5*n - 3)/2
        n += 1

def hexagenerator():
    n = 1
    while True:
        print n*(3*n - 2)
        yield n*(3*n - 2)
        n += 1
triList = []
squarList = []
pentaList = []
octaList = []
nonaList = []
hexaList = []
genWithList = zip([triList, squarList, pentaList, octaList, nonaList, hexaList], [triangle, squaragenerator, pentagenerator, octagenerator, nonagenerator, hexagenerator ])
def genMapper(t):
    for i, some in enumerate(t[1]()):
        if 10000 > some > 999:
            t[0].append(str(some))
        if some > 10000:
            break
for t in genWithList:
    genMapper(t)
    #print len(t[0])#, t[0]
class Hexa:
    def __init__(self, hex_num):
        self.hex_num = hex_num
        self.headList = []
        self.tailList = []

hexaInstList = []
for ihexa, hexa in enumerate(genWithList[-1][0]):
    hexa_ins = Hexa(hexa)
    print ihexa, hexa
    hexa_head, hexa_tail = hexa[:2], hexa[-2:]
    #print hexa_head, hexa_tail
    for i, t in enumerate(genWithList[:-1]):
        i = i + 3
        entity_head = filter(lambda x:x[-2:] == hexa_head , t[0]) 
        if entity_head != []:
            #print '\thead,', (i, entity_head)
            hexa_ins.headList.append( (i, entity_head) )
        entity_tail = filter(lambda x:x[:2] == hexa_tail and x[-2:] != '00', t[0]) 
        if entity_tail != []:
            #print '\ttail,', (i, entity_tail)
            hexa_ins.tailList.append( (i, entity_tail) )
        entity_tail = filter(lambda x:x[:2] == hexa_tail, t[0]) 
    hexaInstList.append(hexa_ins)
hexaInstList = filter(lambda x:x.headList != [] and x.tailList != [], hexaInstList)

#print hexaInstList

for hexa in hexaInstList:
    print hexa.hex_num
    print '\thead', hexa.headList
    print '\ttail', hexa.tailList
    pass

def make3Pair(hexa):
    for head in hexa.headList:
        usedList = []
        evalList = [3, 4, 5, 6, 7]
        headNum = head[0]
        evalList.remove(headNum)
        for tail in hexa.tailList:
            tailNum = tail[0]
            if headNum == tailNum:
                continue
            remnantList = copy.copy(evalList)
            remnantList.remove(tailNum)
            #print head, tail, remnantList
            for h in head[1]:
                for t in tail[1]:
                    return ','.join(map(lambda x:str(x), [h, hexa.hex_num, t])), remnantList, [head[0], tail[0]]

class TripleIndex:
    def __init__(self):
        self.triple_index = ''
        self.remnant_list = []
        self.head_hook = []
        self.tail_hook = []
        self.already_used = set()
tripleIndexList =[]
for hexa in hexaInstList:
    head_and_tail, remnantList, used_list = make3Pair(hexa)
    print 'head_and_tail,', head_and_tail, remnantList, used_list
    triple_index = TripleIndex()
    triple_index.triple_index = head_and_tail
    triple_index.remnant_list = remnantList
    triple_index.already_used = set(used_list)
    for rem in remnantList:
        rem = rem - 3
        match_head = filter(lambda x:x[:2] == head_and_tail[-2:], genWithList[rem][0])
        if match_head != []:
            triple_index.head_hook.append(map( lambda x:(rem+3, x), match_head))
            #print 'head', map( lambda x:(rem, x), match_head)
        
        match_tail = filter(lambda x:x[-2:] == head_and_tail[:2], genWithList[rem][0])
        if match_tail != []:
            triple_index.tail_hook.append(map( lambda x:(rem+3, x), match_tail))
            #print 'tail', map( lambda x:(rem, x), match_tail)
    if triple_index.head_hook == [] or triple_index.tail_hook == []:
        continue
    tripleIndexList.append(triple_index)

for triple_index in tripleIndexList:
    #print 'len, ' , len(triple_index.already_used)
    for head in itertools.chain.from_iterable(triple_index.head_hook):
        for tail in itertools.chain.from_iterable(triple_index.tail_hook):
            already_used = copy.copy(triple_index.already_used)
            if head[0] == tail[0]:
                continue
            #print 'head and tail', head, tail
            #print '? index', already_used
            already_used.add(head[0])
            already_used.add(tail[0])
            #print 'five index', already_used
            rest_index = (set([3,4,5,6,7]) - already_used).pop()
            five_joined = ','.join([tail[1], triple_index.triple_index, head[1]])
            # find rest index 
            temp = filter(lambda x:x[-2:] == five_joined[:2], genWithList[rest_index-3][0])
            if temp != []:
                print five_joined, temp

