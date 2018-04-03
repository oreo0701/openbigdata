message = 'Hello World'

print(message)
print(message.lower())
print(message.upper())
print(message.count('Hello'))
print(message.find('World'))
print(message.find('Univese'))
print(message.replace('World','Universe'))
print(message.lower())

greeting = 'Hello'
name = 'Michale'
hello_message = greeting + ',' + name + '. Welcome!'
hello_message_format = '{}, {}. Welcome!'.format(greeting, name)
hello_message_fstring= f'{greeting}, {name.upper()}. Welcome!'
print(hello_message)
print(hello_message_format)
print(hello_message_fstring)

print(dir(name))
print(help(str))
print(help(str.find))