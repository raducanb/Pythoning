x = [[x, y] for x in range(1, 10) for y in range(0, 10) if((x+y)%7==0)]
print(x)

x = [x for x in range(2, 100) if len([y for y in range(2,x//2+1) if(x%y==0)]) == 0]
print(x)

x = [1,2,3]
x.insert(len(x) + 1, 4)
print(x)

del x[0]
print(x)

y = list(map(lambda e:e**2, x))
print(y)

x = list(filter(lambda x:x%7==0, range(1, 100)))
print(x)

y = list(filter(lambda x:x%3==0, x))
print(y)