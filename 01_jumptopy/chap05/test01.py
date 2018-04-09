f = open(".\\learning_python.txt", "r")

data = f.read()
edit = data.replace('python','C')

f = open(".\\learning_python_copyed.txt", "w")
f.write(edit)
f.close()


