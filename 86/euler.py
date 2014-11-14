import math,decimal,itertools, collections

print 's'
M = 99
c = 0
brute = set()
for x in xrange(1,M):
    for y in xrange(1,M):
        for z in xrange(1,M):
            floor1 = x
            right1 = y + z

            floor2 = x + z
            right2 = y

            floor3 = x + y
            right3 = z
            length = map(decimal.Decimal, [floor1**2 + right1**2, floor2**2 + right2**2, floor3**2 + right3**2])
            nums = str(sorted(map(lambda x:x.sqrt(), length))[0]).split('.')
            #if tail == '0':
            if len(nums) == 1:# and not sorted([x,y+z]) in brute:
                c += 1
                brute.add(nums[0])
                print x,y,z,nums[0],length

print 'result = ', c, len(brute)
