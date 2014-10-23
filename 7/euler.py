# coding: utf-8
import sys, os, math, __future__, itertools

pastNums = []
def isPrime(n):
    for pastnum in pastNums:
        if n % pastnum == 0:
            return None
    return True

primeBuffer = []
i = 2
while True:
    if isPrime(i) :
        primeBuffer.append(i)
        if len(primeBuffer) == 10001:
            break
    pastNums.append(i)
    i += 1

print(primeBuffer[-1])


