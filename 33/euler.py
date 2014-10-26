import itertools
B = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] + [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

EASE = [10]

resS = set()
for et in itertools.permutations(B,4):
    bunshi = int(''.join(map(lambda x:str(x), et[:2])))
    bunbo  = int(''.join(map(lambda x:str(x), et[2:])))
    if bunshi < 10 or bunbo < 10:
        continue
    ansOrigin = bunshi/float(bunbo)
    easeFalse = False
    for ease in EASE:
        if easeFalse :
            continue
        if bunshi%ease == 0 and bunbo%ease == 0:
            #print 'this is zimei', bunshi, bunbo, ease
            easeFalse = True
            continue
    if not easeFalse:
        #重複する要素のあぶりだし
        if len(set(str(bunshi) +  str(bunbo))) <= 4:
            if list(set(str(bunshi)) & set(str(bunbo))) == []:
                    continue

            duplicateEntitie = str( list(set(str(bunshi)) & set(str(bunbo))).pop() )
            b = []
            for bunshiE in list(str(bunshi)):
                if bunshiE != duplicateEntitie:
                    b.append(bunshiE)
            newBunshi = int(''.join(b))

            b = []
            for bunboE in list(str(bunbo)):
                if bunboE != duplicateEntitie:
                    b.append(bunboE)
            newBunbo = int(''.join(b))
            if newBunbo == 0:
                continue
            
            if bunshi/float(bunbo) == newBunshi/float(newBunbo) and  bunshi/float(bunbo) <= 1.0:
                resS.add( (bunshi, bunbo) )
for r in resS:
    if r[0] == r[1]:
        continue
    print r
