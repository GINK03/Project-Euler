import itertools
# sieve algorithme for prime search
def primeTable(n):
    sieve = [True for _ in xrange(n + 1)]
    i = 2
    while i * i <= n:
        if sieve[i]:
            j = i + i
            while j <= n:
                sieve[j] = False
                j += i
        i += 1
    table = [str(i) for i in xrange(n + 1) if sieve[i] and i >= 2]
    return table

def isTrimable(x, primeL):
    result_flag = True
    temp = x
    while True:
        tail = temp[1:]
        # tail is exist in primeL?
        #print x, 'tal',tail
        if tail == '':
            break
        if not tail in primeL:
            return False
        temp = tail
    temp = x
    while True:
        head = temp[:-1]
        #print 'head', x, head
        # head is exist in primeL?
        if head == '':
            break
        if not head in primeL:
            return False
        temp = head

    # if str length is 1 return False
    if len(x) == 1:
        return False
    print 'passed', x
    return True

if __name__ == '__main__':
    c = 0
    primeL = primeTable(1000000)
    for x in primeL:
        if isTrimable(x, primeL):
            c += int(x)
    print 'result', c
