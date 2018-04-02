# numbers = [1,2,3,4,5]
class Calculator:
    def __init__(self):
        self.result = 0

    def sum(self):
        total = 0
        for i in numbers:
            total = total + i
        return total
    def avg(self):
        total = sum(numbers)
        avg = total/len(numbers)
        return avg


cal1 = Calculator([1,2,3,4,5])
cal1.sum()
print(cal1.sum())
cal1.avg()
print(cal1.avg())

cal2 = Calculator([6,7,8,9,10])
cal2.sum()
cal2.avg()