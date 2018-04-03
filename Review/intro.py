import sys
sys.path.append('C:\workspace\my_module')
from module import find_index, test


courses = ['History','Math','Physics', 'CompSci']

index = find_index(courses, 'Math')

# print(index)
# print(test)
print(sys.path)


#>nano ~/.bash_profile
#>export PYTHONPATH="C:\workspace\my_module" Contrl x
#>import module
#>sys.path