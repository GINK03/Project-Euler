

b = [1, 2]

while b[-1] < 4000000:
  c = b[-2] + b[-1]
  b.append(c)
  
s = sum(filter(lambda x:x%2==0, b))
print(s)

