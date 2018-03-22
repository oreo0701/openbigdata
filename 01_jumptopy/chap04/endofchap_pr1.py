def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)

fib_sum=0
for i in range(0,9):
    fib_sum = fib(i)
    print(str(fib_sum)+",",end =' ')
print(fib(9))