# coding: utf-8
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
        yield n*(3*n - 2)
        n += 1

genWithList = zip([[], [], [], [], [], []], [triangle, squaragenerator, pentagenerator, octagenerator, nonagenerator, hexagenerator ])
def genMapper(t):
    for i, some in enumerate(t[1]()):
        if 10000 > some > 999:
            t[0].append(str(some))
        if some > 10000:
            break
for t in genWithList:
    genMapper(t)

def parseAndFind(hexnum, n_list, lis):
    n1, n2, n3, n4, n5 = map(lambda x:str(x), n_list)
    for n_depth1 in filter(lambda x:x[:2] == str(hexnum)[-2:], lis[int(n1) - 3]):
        for n_depth2 in filter(lambda x:x[:2] == n_depth1[-2:], lis[int(n2) -3]):
            for n_depth3 in filter(lambda x:x[:2] == n_depth2[-2:], lis[int(n3) -3]):
                for n_depth4 in filter(lambda x:x[:2] == n_depth3[-2:], lis[int(n4) -3]):
                    for n_depth5 in filter(lambda x:x[:2] == n_depth4[-2:] , lis[int(n5) -3]):
                        if n_depth5[-2:] == str(hexnum)[:2]:
                            print (8, hexnum), (n1, n_depth1), (n2, n_depth2), (n3, n_depth3), (n4, n_depth4), (n5, n_depth5)
                            print sum(map(lambda x:int(x[1]), [(8, hexnum), (n1, n_depth1), (n2, n_depth2), (n3, n_depth3), (n4, n_depth4), (n5, n_depth5)]))
    

if __name__ == '__main__': 
    hex_list = genWithList[-1][0]
    for rout in itertools.permutations([3, 4, 5, 6, 7]):
        for hexnum in hex_list:
            #print hexnum, rout
            parseAndFind(hexnum, rout, map(lambda x:x[0], genWithList))
