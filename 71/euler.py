import sys,math,os,sys,itertools,fractions

MAX = 10**6
if __name__ == '__main__':
    for b in xrange(2, MAX+1):
        a = (3*b - 1)/7
        if a != 0 and 7*a < 3*b:
            print a,b

