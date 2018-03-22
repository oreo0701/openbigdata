usernames = ['janny', 'hannah', 'margot', 'kevin', 'min']

def greet_users(a):
    return "Hello, %s" %a[0].upper()+a[1:].lower() + "!"

for names in usernames:
    print(greet_users(names))
