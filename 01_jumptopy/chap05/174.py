class Calculator:   #Calculator : class
    def __init__(self):
        self.result = 0

    def adder(self, num):
        self.result += num
        return self.result

cal1 = Calculator()  #cal1, cal2 : object.  cal1은 Calculator의 instance 이다. instance는 관계를 이야기할때
cal2 = Calculator()  #object는 class를 통해 찍어낸 결과물

print(cal1.adder(3))
print(cal1.adder(4))
print(cal2.adder(3))
print(cal2.adder(7))
