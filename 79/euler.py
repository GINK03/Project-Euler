import itertools, sys, os, math
Keys = '''319
680
180
690
129
620
762
689
762
318
368
710
720
710
629
168
160
689
716
731
736
729
316
729
729
710
769
290
719
680
318
389
162
289
162
718
729
319
790
680
890
362
319
760
316
729
380
319
728
716'''
import collections
maybe = []
for key in Keys.split('\n'):
    maybe.append( [k for k in key] )
before = {}
after  = {}
for may in maybe:
    bef, mid, aft = map(lambda x:x, may)
    if before.get(mid) and not bef in before[mid] :
        before[mid] += ',' + bef
    elif before.get(mid) == None:
        before.update({mid:bef})
    if after.get(mid) and not aft in after[mid]:
        after[mid] += ',' + aft
    elif after.get(mid) == None:
        after.update({mid:aft})
for k,v in before.iteritems():
    print 'before:', k, v
for k,v in after.iteritems():
    print 'after:', k, v
    
