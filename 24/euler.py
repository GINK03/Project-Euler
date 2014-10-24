import itertools

B = [0,1,2,3,4,5,6,7,8,9]
c = 1
for i,e in enumerate(itertools.permutations(B, 10)):
    if (i+1) % 100000 == 0:
        print i+1, ''.join(map(lambda x:str(x), list(e)))
