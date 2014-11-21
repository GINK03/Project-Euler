#coding: utf-8
import os,sys,math
class IntHolder:
    def __init__(self):
        self.i = 0
def sum(holder, i):
    holder.i += i


if __name__ == '__main__':
    holder = IntHolder()
    for i in range(1,1000):
        if i % 3 == 0 or i % 5 == 0:
            sum(holder, i)    

    print holder.i

