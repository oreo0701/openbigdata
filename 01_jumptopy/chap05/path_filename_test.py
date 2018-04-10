file_name='\\poll.txt'
# path='.'
path='new_repository'
f= open(f'{path}{file_name}',"r", encoding='UTF8')
print(f.read())

f.close()