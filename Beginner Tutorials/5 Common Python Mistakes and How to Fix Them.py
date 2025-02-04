# This code demonstrates Python best practices and common pitfalls including:
# - Proper indentation using 4 spaces
# - Avoiding naming conflicts when importing
# - Handling mutable default arguments correctly
# - Working with iterators and timestamps
# - Import specific names vs importing everything with * from os import rename, remove

# Indentation and Spaces
nums = [11, 30, 44, 54]  # No indentation - base level
for num in nums:         # No indentation - base level
    square = num ** 2    # Indented 4 spaces - inside for loop
    print(square)        # Indented 4 spaces - inside for loop

# Naming Conflicts
from math import radians, sin
rads = radians(90)
print(sin(rads))

# Mutable Default Args
def add_employee(emp, emp_list=None):
    if emp_list is None:
        emp_list = []
    emp_list.append(emp)
    print(emp_list)

emps = ['John', 'Jane']
add_employee('Subham', emps)  # ['Subham', 'John','Jane']
add_employee('Subhasish')
add_employee('Subhankar')

# Exhausting Iterators
import time
from datetime import datetime

def display_time(time_to_print=None):
    if time_to_print is None:
        time_to_print = datetime.now()
    print(time_to_print.strftime('%B %d, %Y %H:%M:%S'))
display_time()
time.sleep(1)
display_time()
time.sleep(1)
display_time()
time.sleep(1)

# Importing with *
# not a good practice because it imports all names from the module which can lead to namespace pollution and naming conflicts
from os import *
# The below is a good practice because it explicitly shows which functions are being imported and used
from os import rename, remove
rename('test.txt', 'test2.txt')
remove('test2.txt')
