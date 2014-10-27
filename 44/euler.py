# coding: utf-8
import itertools
def generator():
    n = 1
    while True:
        yield n*(3*n -1)/2
        n += 1
resister = []
def combinate(li):
    for e in itertools.combinations(li, 2):
        head = e[0] + e[1]
        tail = abs(e[0] - e[1])
        if head in res and tail in res:
            resister.append(tail)
            # ∵  基数の数字は線形以上の増加なので最初の回答が答え
            print resister[0], e
            break

res = []
for i, g in enumerate(generator()):
    res.append(g)
    if len(res) > 2:
        combinate(res)
    if i % 100 == 0:
        print 'iter', i
