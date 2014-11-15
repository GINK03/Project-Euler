import sys,itertools,math



def euler_generator():
    n = 1
    while True:
        yield 1
        yield 1
        yield 2*n
        n += 1

t = [2, 3]
def calcFomula(n, e):
    # t = e*t-1 + t-2
    t.append(e*t[-1] + t[-2])
    return t[-1]

# main
for i, e in enumerate(euler_generator()):
    i += 1
    if i > 2:
        print i, e, sum(map(lambda x:int(x), str(calcFomula(i, e))))
        if i == 100:
            break


