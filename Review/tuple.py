#Tuple : Immutable

list_1 = ['History', 'Math', 'Physic','CompSci']
list_2 = list_1

print(list_1)
print(list_2)

list_1[0] = 'Art'

print(list_1)
print(list_2)

tuple_1 = ('History','Math', 'Physics', 'CompSci')
tuple_2 = tuple_1

print(tuple_1)
print(tuple_2)

#tuple_1[0] = 'Art'  #TypeError: 'tuple' object does not support item assignment
#can't mutate tuple

print(tuple_1)
print(tuple_2)

#Sets : Unorderd, no duplicate

cs_courses = {'History','Math', 'Physics', 'CompSci'}
cs_courses_duplicate = {'History','Math', 'Physics', 'CompSci','Math'}
print(cs_courses)  #order can change all the time
print(cs_courses_duplicate)

#membership test
print('Math' in cs_courses)
print('Math' in cs_courses_duplicate)
art_courses = {'History','Art', 'Physics', 'CompSci','Design'}

#Intersection method: common course
print(cs_courses.intersection(art_courses))
print(cs_courses.difference(art_courses))
print(cs_courses.union(art_courses))

#Empty Lists
empty_list = []
empty_list = list()
#Empmty Tuples
empty_tuple = ()
empty_tuple = tuple()

#Empty Sets
empty_set = {}  # This isn't right! it's a empty dictionary
empty_set = set()
