import sys, os, operator, itertools

TEST = '''131,673,234,103,18
201,96,342,965,150
630,803,746,422,111
537,699,497,121,956
805,732,524,37,331'''
source = [ map(int, x.split(',')) for x in TEST.split('\n')]

source = []
for line in sys.stdin:
    line.strip()
    source.append(map(int, line.split(',')))

# make dinamo
def dinamo(source_ref, v, h):
    def get_left(tag_v):
        if h -1 >= 0:
            return source_ref[tag_v][h - 1]
        else:
            return 0
    resultlist = []
    verticallist = [s[h] for s in source_ref]
    for tag_v in xrange(len(source)):
        if tag_v > v:
            #print v, tag_v, v - tag_v, verticallist[v+1:tag_v+1], get_left(tag_v)
            resultlist.append(sum(verticallist[v+1:tag_v+1]) + get_left(tag_v))
        elif v > tag_v:
            #print v, tag_v, tag_v - v, verticallist[tag_v:v], get_left(tag_v)
            resultlist.append(sum(verticallist[tag_v:v]) + get_left(tag_v))
        elif v == tag_v:
            #print 'selfrefarence, ', [verticallist[v]], get_left(tag_v)
            if h != 0:
                resultlist.append(get_left(tag_v))
            else:
                resultlist.append(0)
    return resultlist

# make matrix 
for h in xrange(len(source[-1])):
    updatetup = []
    for v in xrange(len(source)):
            res = dinamo(source, v, h)
            #print source[v][h], sorted(res, reverse=True)
            update = sorted(res, reverse=True).pop()
            updatetup.append( (v,update) )
            #print 'v=',v,'h=',h, source[v][h], update, source
            #print res
    for t in updatetup:
        source[t[0]][h] += t[1]
        #print t[0], t[1]
        #print source
print sorted(map(lambda s:s[-1], source), reverse=True).pop()
