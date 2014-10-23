# coding: utf-8
import sys, os, math, __future__, itertools

def isPrime(n):
    for prime in primeBuffer:
        if n % prime == 0:
            return None
    return True

primeBuffer = [2]
i = 2
while True:
    if isPrime(i) :
        primeBuffer.append(i)
    #pastNums.append(i)
    i += 1
    if i % 10000 == 0:
        print 'iter', i
    if i > 2000000:
    #if i > 10:
        break

print(sum(primeBuffer))


