sum = lambda a, b: a+b
sum(3,4)

myList = [lambda a,b:a+b, lambda a,b:a*b]
print(myList[0](3,4))
print(myList[1](3,4))