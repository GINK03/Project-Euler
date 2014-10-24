

subList = [1,1]
def Fib(n):
    if n == 0 or n == 1:
        return subList[0]
    else:
        res = subList[-2] + subList[-1]
        subList.append(res)
        return subList[-1]

def gen():
    n = 0
    while True:
        res = Fib(n)
        yield res
        n += 1

for i, e in enumerate(gen()):
    if len(str(e)) == 1000 :
        print i+1, e
        break
