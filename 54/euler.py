import sys, math, os

m = {'A':14,
     '2':2,
     '3':3,
     '4':4,
     '5':5,
     '6':6,
     '7':7,
     '8':8,
     '9':9,
     'T':10,
     'J':11,
     'Q':12,
     'K':13}

def isRoyalflash(li):
    eval_set = set([10, 11,12,13,1])
    eval_tgt_num = set(map(lambda x:x[0], li))
    eval_tgt_suit = set(map(lambda x:x[1], li))
    if eval_set == eval_tgt_num and len(eval_tgt_suit) == 1:
        return True
    return False

def isStreatflash(li):
    pass

def isFourcard(li):
    eval_tgt = sorted(map(lambda x:x[0], li), key=lambda x:x)
    if eval_tgt.count(eval_tgt[0]) == 4:
        return True
    if eval_tgt.count(eval_tgt[1]) == 4:
        return True
    return False

def isFullhouse(li):
    eval_li = sorted(map(lambda x:x[0], li))
    if eval_li.count(eval_li[0]) == 3 and eval_li.count(eval_li[-1]) == 2:
        return True
    if eval_li.count(eval_li[0]) == 2 and eval_li.count(eval_li[-1]) == 3:
        return True
    return False

def isFlash(li):
    eval_tgt = set(map(lambda x:x[1], li))
    if len(eval_tgt) == 1:
        return True
    return False

def isStraight(li):
    eval_li = sorted(map(lambda x:x[0], li))
    if len(set(eval_li)) == 5 and eval_li[0] + 4 == eval_li[-1]:
        return True
    return False

def isThreecard(li):
    eval_li = sorted(map(lambda x:x[0], li))
    if len(set(eval_li)) == 3:
        if eval_li.count(eval_li[0]) == 3 or eval_li.count(eval_li[1]) == 3 or eval_li.count(eval_li[2]) == 3:
            return True
    return False

def isTwopair(li):
    eval_li = sorted(map(lambda x:x[0], li))
    if len(set(eval_li)) == 3:
        if eval_li.count(eval_li[0]) == 2 and eval_li.count(eval_li[3]) == 2:
            return True
        if eval_li.count(eval_li[1]) == 2 and eval_li.count(eval_li[4]) == 2:
            return True
    return False

def isOnepair(li):
    eval_li = sorted(map(lambda x:x[0], li))
    if len(set(eval_li)) == 4:
        return True
    return False

def isHighcard(li):
    eval_li = sorted(map(lambda x:x[0], li))
    if len(set(eval_li)) == 5:
        return True
    return False

class Score:
    def __init__(self, li):
        self.li = sorted(li)
        self.score = 0
    def eval(self):
        if isRoyalflash(self.li):
            self.score = 9
            return
        if isStreatflash(self.li):
            self.score = 8
            return
        if isFourcard(self.li):
            self.score = 7
            return
        if isFullhouse(self.li):
            self.score = 6
            return
        if isFlash(self.li):
            self.score = 5
            return
        if isStraight(self.li):
            self.score = 4
            return
        if isThreecard(self.li):
            self.score = 3
            return
        if isTwopair(self.li):
            self.score = 2
            return
        if isOnepair(self.li):
            self.score = 1
            return
        if isHighcard(self.li):
            self.score = 0
            return
        sys.exit(0)

def mappedCheck(mapped):
    for i in xrange(0,5):
        if mapped[i] < 0:
            return False
        if mapped[i] > 0:
            return True
c = 0
for l in sys.stdin:
    l = l.strip()
    li = map(lambda x:(m.get(x[0]), x[1]), l.split(' '))
    p1 = li[:5]
    p2 = li[5:]
    score1 = Score(p1)
    score1.eval()
    score2 = Score(p2)
    score2.eval()
    
    sp1, sp2 = sorted(map(lambda x:x[0], p1), key=lambda x:x*(-1)), sorted(map(lambda x:x[0], p2), key=lambda x:x*(-1))
    zipped  = zip(sp1, sp2)
    mapped  = map(lambda x:x[0] - x[1],zipped)
    print sp1, sp2, mapped, score1.score, score2.score, (lambda x,y:x > y)(score1.score, score2.score), (lambda x:mappedCheck(x))(mapped)
    if score1.score > score2.score:
        c+=1
        continue
    if score1.score < score2.score:
        sp1, sp2 = sorted(map(lambda x:x[0], p1), key=lambda x:x*(-1)), sorted(map(lambda x:x[0], p2), key=lambda x:x*(-1))
        zipped  = zip(sp1, sp2)
        mapped  = map(lambda x:x[0] - x[1],zipped)
        continue
    if score1.score == score2.score:
        pass
print 'result', c
