# coding:utf-8
import math, sys, os, __future__, itertools

if __name__ == '__main__':
    baseList = range(1,101)
    ans1 = sum(map(lambda x:x*x, baseList))
    print(baseList)
    ans2 = sum(baseList) * sum(baseList)
    print(ans2 - ans1)
