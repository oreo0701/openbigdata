def hello_func(greeting,name = 'you'):
    return f'{greeting}, {name} Hello Function!'

# print(hello_func)
print(hello_func('Hi', name = 'Corey'))

# hello_func()

#keeping code dry


print(len('Test'))
print(hello_func('Hi').upper())
print(hello_func('Hi'))

def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

student_info('Math','Art', name='John',age=22)

courses = ['Math','Art']
info = {'name':'John','age':22}

student_info(*courses,**info)

month_days = [0, 31,28,31,30,31,30,31,31,30,31,30,31]

def is_leap(year):
    """"Return Treu for leap years, False for non-leap years."""

    return year % 4 ==0 and (year % 100!=0 or year %400 ==0)

def days_in_month(year, month):
    # year 2018
    # month 4
    if not 1 <= month <= 12:
        return 'Invalid Month'
    if month == 2 and is_leap(year):
        return 29

    return month_days[month]
print(is_leap(2018))
print(days_in_month(2018, 4))
