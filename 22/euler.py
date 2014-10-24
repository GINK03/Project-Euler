import math

def gen(entities):
    for i,e in enumerate(sorted(entities)):
        res = (i+1) * reduce(lambda x,y:x+y, map(lambda c:ord(c) - 64, e))
        yield res

for line in open('p022_names.txt'):
    entities = line.replace('"','').split(',')
    print reduce(lambda x,y:x+y, gen(entities))

