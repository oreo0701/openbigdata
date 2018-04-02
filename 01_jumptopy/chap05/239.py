from copy import copy

a=3

print(id(3))
print(id(a))

b=a
print(id(b))

c=copy(a)
print(c)
print(id(c))

d= copy(3)
print(d)
print(id(d))

l1=[1,2,3]
l2=l1
l3=copy[l1]
print(id[l1])
print(id[l2])
print(id[l3])