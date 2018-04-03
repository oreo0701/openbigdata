class Employee:


    raise_amt = 1.04

    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)


class Developer(Employee):
    raise_amt = 1.10


dev_1 = Employee('Corey', 'Scheffer', 50000)
dev_2 = Developer('Dod','family', 1000)


# print(dev_1.email)
# print(dev_2.email)

print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)