import sys, itertools, math

def isTriangle(h):
    # fomula: 0 = n^2 + n - 2h
    # h = (2n+1)^2 -1  //  8 
    # if exist this Truee
    for x in itertools.count(1):
        fomula = ((x+1)*(x+1) - 1)/8
        if h == fomula:
            return True
        if h < fomula:
            return False
            

def isPentagonal(h):
    # fomula: h = 3n^2 - n
    # h = (6n-1)^2 -1  //  24
    # if exist this Truee
    for x in itertools.count(1):
        fomula = ((6*x-1)*(6*x-1) - 1)/24
        if h == fomula:
            return True
        if h < fomula:
            return False

def hexagonalGenerator():
    g = 1
    while True:
        yield g*(2*g-1)
        g += 1

for i, h in enumerate(hexagonalGenerator()):
    if isTriangle(h) and isPentagonal(h):
        print h, isTriangle(h)
        if 40755 < h:
            break
