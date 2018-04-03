
# Object Identity : is

language = 'Java'

if language == 'Python':
    print('Language is Python')
elif language == 'Java':
    print('Language is Java')
elif language == 'JavaScript':
    print('Language is JavaScript')
else:
    print('No match')

#and, or , not

user = 'Admin'
logged_in = False

if not logged_in:
    print('Please Log in')
else:
    print('Bad Creds')

a = [1,2,3]
b = [1,2,3]
c = a
print(a == b)
print(a is b) # two different object in memory.   ib is differnet
print(id(a))
print(id(b))
print(a is c) #same object in memeory
print(id(a) == id(c))

condition = 0   #False: 0, None, False, empty sequence('', (), [],), empty mapping( { } )

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')
