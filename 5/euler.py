# coding: utf-8
import os,sys,math,__future__,itertools

def canDivide(n):
    filterList = range(1,20)
    canDivideFlag = True
    for i in filterList:
        if n % i != 0:
            return None
    print(n)
    return True

if __name__ == '__main__':
    n = 1
    while True:
        if canDivide(n):
            break
        n += 1
        
