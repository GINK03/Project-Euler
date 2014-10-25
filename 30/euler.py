import math, itertools

def generator():
    n = 1
    while True:
        n += 1
        yield n

if __name__ == '__main__':
    ans = 0
    for i in generator():
        s = 0
        th = 0
        for e in str(i):
            s += int(math.pow(int(e), 5))
            th += math.pow(9, 5)
        if i == s:
            print i
            ans += i
        if i > th:
            break

    print 'ans', ans


















