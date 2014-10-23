# coding: utf-8
class MakeFib:
    def __init__(self):
        self.a = 1
        self.b = 2
        self.c = 0
    def add(self):
        self.c = self.a + self.b
        return self
    def increment(self):
        self.a = self.b
        self.b = self.c
        return self
    def get(self):
        return self.a + self.b
class IntHolder:
    def __init__(self):
        self.i = 0
    def pushRestrict(self, i):
        if i % 2 == 0:
            self.i += i

if __name__ == '__main__':
    makefib = MakeFib()
    holder  = IntHolder()
    for i in range(1,4000000):
        if i == 1 or i == 2:
            holder.pushRestrict(i) 
        else:
            makefib.add().increment()
            if makefib.get() > 4000000:
                print 'fib', makefib.get()
                break
            holder.pushRestrict(makefib.get())
        print 'ans', holder.i
