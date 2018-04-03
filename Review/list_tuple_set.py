#list : sequential data

courses = ['History', 'Math', 'Physic','CompSci']
print(len(courses))   #4 values in list



print(courses[0])
print(courses[3])
print(courses[-1])
print(courses[-4])
print(courses[0:2])
print(courses[:2])
print(courses[2:])

#add values
courses.append('Art')
print(courses)
#choose location to add
courses.insert(0,'Eng')
print(courses)

courses_2 = ['Hello', 'Education']
courses.insert(0, courses_2)  # add entire list
print(courses)
print(courses[0])

#combine two lists
courses.extend(courses_2)
print(courses)

#remove
courses.remove('Hello')
print(courses)

courses.pop() # remove last values of list
print(courses)

popped = courses.pop()
print(popped)
print(courses)

courses.reverse()
print(courses)

nums = [1,5,2,4,3]

nums.sort(reverse=True)

print(courses)
print(nums)

print(min(nums))
print(max(nums))
print(sum(nums))

#sorted_courses = sorted(courses) #sorted version of list
#print(sorted_courses)

print(courses.index('CompSci'))
print('Math' in courses)

for item in courses:
    print(item)

for index, course in enumerate(courses):    #enumerate function
    print(index, course)
for index, course in enumerate(courses, start =1):    #enumerate function
    print(index, course)

courses = ['History', 'Math', 'Physic','CompSci']
#join method
course_str = ', '.join(courses)
print(course_str)
course_str = ' - '.join(courses)
print(course_str)
new_list = course_str.split(' -')

print(course_str)
print(new_list)


