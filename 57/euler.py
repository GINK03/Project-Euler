import parser, re

def generator():
    base = '1 + 1/2'
    while True:
        yield base
        base = base.replace('/2', '/(2 + 1/2)')
def parsing(expr):
    #count )num
    removedexpr = expr.replace(')', '')
    calc_odered = removedexpr.split('(')
    calc_odered.reverse()
    tex = ['1', '/', '2']
    for i, e in enumerate(calc_odered):
        if i == 0:
            continue 
        bunbo = tex[-1]
        bunshi_tail = int(tex[0])
        # yakubun
        bunshi_head = int(bunbo)*2 
        bunshi = str(bunshi_head + bunshi_tail) 
        tex = [bunshi, '/', bunbo]
        tex.reverse()
        #print tex
    
    bunshi_head = int(tex[-1])
    bunshi_tail = int(tex[0])
    bunbo       = tex[-1]
    res = [str(bunshi_head+bunshi_tail), '/', bunbo]
    #print res
    return res
c = 0
for i, expr in enumerate(generator()):
    #print expr
    if i+1 > 1000:
        break
    tex = parsing(expr)
    if len(tex[0]) > len(tex[-1]):
        c += 1

print 'result', c
