import networkx as nx

TEST = '''131,673,234,103,18
201,96,342,965,150
630,803,746,422,111
537,699,497,121,956
805,732,524,37,331'''

TGT = [ map(int, x.split(',')) for x in TEST.split('\n') ]
import sys
TGT = []
for line in sys.stdin:
    TGT.append(map(int, line.strip().split(',')))
G = nx.DiGraph()
for v, vect in enumerate(TGT):
    for h, entiti in enumerate(vect):
        #print v,h,entiti, vect
        neighbors = [(v+x, h+y) for x,y in (-1,0), (0,-1), (1,0), (0,1) if 0<=v+x<len(TGT) and 0<=h+y<len(vect)]
        for vx,hy in neighbors:
            G.add_edge( (v,h), (vx,hy), weight= TGT[vx][hy] )

path_length = nx.dijkstra_path_length(G, source=(0,0), target=(v,h))
print "Minimum path sum matrix =", path_length + TGT[0][0]

