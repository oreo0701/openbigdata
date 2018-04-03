import os
from datetime import datetime
print(os.getcwd())

os.chdir('C:\workspace\openbigdata\Review')
print(os.getcwd())

# os.mkdir('Review2')
# os.makedirs('Reivew3/sub')

print(os.listdir())

mod_time=os.stat('import_random.py').st_mtime
print(datetime.fromtimestamp(mod_time))

for dirpath, dirnames, filenames in os.walk('C:\workspace\openbigdata'):
    print('Current Path:', dirpath)
    print('Directories:', dirnames)
    print('Files:', filenames)
    print()