student = {1:'Tom','name':'John', 'age':25,'courses':['Math','CompSci']}

print(student)
print(student['name'])
print(student['courses'])
print(student[1])
#access key that doens't exist
print(student.get('name'))
print(student.get('phone'))
print(student.get('phone', 'Not Found'))

#add values
student['phone'] = '555-5555'
print(student.get('phone', 'Not Found'))

#Update values
student['name'] = 'Jane'
print(student)

#Update multiple values
student.update({'name':'Jimmy','age':26, 'phone': '666-6666'})
print(student)

# del student['age']
print(student)

age = student.pop('age')
print(student)
print(age)
print(len(student))
print(student.keys())
print(student.values())
print(student.items())

for key in student:
    print(key)

for key, value in student.items():
    print(key,value)

for value in student.values():
    print(value)