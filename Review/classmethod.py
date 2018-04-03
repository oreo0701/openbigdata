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

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() ==6:
            return False
        return True

emp_1 = Employee('Corey', 'Scheffer', 50000)
emp_2 = Employee('Dod','family', 1000)

emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-3000'
emp_str_3 = 'Jane-Doe-90000'


new_emp_1 = Employee.from_string(emp_str_1)

print(new_emp_1.email)
print(new_emp_1.pay)

Employee.set_raise_amt(1.05)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

import datetime

my_date = datetime.date(2016,7,11)
print(Employee.is_workday(my_date))