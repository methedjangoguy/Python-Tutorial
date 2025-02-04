# Sorting Lists, Tuples, and Objects
# Sorting a List
# Creates a list of numbers in random order
li = [9,1,8,2,7,3,6,4,5]
# Creates a new sorted list from li in ascending order
s_li = sorted(li, reverse=False)
# Prints the sorted list
print('Sorted Variable:\t', s_li)
# Prints the original unsorted list
print('Original Variable:\t', li)

# Sorts the original list in place in ascending order
li.sort(reverse=False)
# Prints the sorted list
print('Sorted Variable in place:\t', li)

# Creates a tuple of numbers in random order
tup = (9,1,8,2,7,3,6,4,5)
# Creates a new sorted list from the tuple
s_tup = sorted(tup)
# Prints the sorted list
print('Sorted Tuple:\t', s_tup)
# Prints the original unsorted tuple
print('Original Tuple:\t', tup)

# Creates a dictionary with various key-value pairs
di = {'name': 'Corey', 'job': 'programming', 'age': None, 'os': 'Mac'}
# Creates a sorted list of dictionary keys in ascending order
s_di = sorted(di)
# Creates a sorted list of dictionary keys in descending order
s_di = sorted(di, reverse=True)

# Prints the sorted list of keys
print("Sorted Dictionary:\t", s_di)
# Prints the original dictionary
print("Original Dictionary:\t", di)

# Creates a list with positive and negative numbers
li = [-6, -5, -4, 1, 2, 3]
# Sorts the list based on absolute values
s_li = sorted(li, key=abs)
# Prints the sorted list
print('Sorted List:\t', s_li)

# Imports attrgetter from operator module
from operator import attrgetter

# Defines Employee class
class Employee():
    # Initializes Employee object with name, age and salary
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    # Defines string representation of Employee object
    def __repr__(self):
        return '({},{},${})'.format(self.name, self.age, self.salary)

# Creates three Employee objects
e1 = Employee('Carl', 37, 70000)
e2 = Employee('Sarah', 29, 80000)
e3 = Employee('John', 43, 90000)
# Creates list of Employee objects
employees = [e1, e2, e3]

# Defines function to return employee salary for sorting
def e_sort(emp):
    return emp.salary
# Sorts employees by salary using e_sort function
s_employees = sorted(employees, key=e_sort)
# Sorts employees by salary using lambda function
s_employees = sorted(employees, key=lambda e: e.salary)
# Sorts employees by salary using attrgetter
s_employees = sorted(employees, key=attrgetter('salary'))
# Prints the sorted list of employees
print(s_employees)
print(s_employees)
print(s_employees)

# Congratulations! You have completed sorting.
