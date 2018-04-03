class Employee:

    num_of_emmps = 0
    raise_amount = 1.04

    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emmps += 1

    def fullname(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

print(Employee.num_of_emmps)
emp_1 = Employee('Corey', 'Scheffer', 50000)
emp_2 = Employee('Dod','family', 1000)



# print(Employee.__dict__)

emp_1.raise_amount = 1.05
print(emp_1.__dict__)
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

print(Employee.num_of_emmps)
# emp_1.raise_amount
# Employee.raise_amount