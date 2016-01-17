
import math, os, sys, itertools

def is_right_triangle(P, Q):
    if P[1] == 0 and Q[0] == 0:
        return True
    elif P[0] * (Q[0] - P[0]) == P[1] * (P[1] - Q[1]):
        return True
    elif Q[0] * (P[0] - Q[0]) == Q[1] * (Q[1] - P[1]):
        return True
    return False

def is_right_lower(P, Q):
    return P[0] * Q[1] - P[1] * Q[0] > 0

c = 0
for Q in itertools.product(xrange(0,51), repeat=2):
    for P in itertools.product(xrange(0,51), repeat=2):
        if is_right_lower(P, Q) and is_right_triangle(P, Q):
                c += 1 
        #print Q1, Q2, P1, P2
        pass
print c
