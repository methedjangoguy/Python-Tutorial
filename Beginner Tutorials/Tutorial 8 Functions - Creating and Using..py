# Functions are a way to encapsulate code that can be called multiple times
# Functions are defined using the def keyword
# Functions can take arguments
# Functions can return values
# Functions can be called multiple times
# Functions can be called from other functions

# Dry Principle - Don't Repeat Yourself
def hello_func():
    """This function prints 'Hello Function!'"""
    print("Hello Function!")

hello_func()
hello_func()
hello_func()
# Output: Hello Function! Hello Function! Hello Function!

def hello_func():
    return "Hello Function!"

print(hello_func()) # Output: Hello Function!

print(len("test")) # Output: 4

print(hello_func().upper()) # Output: HELLO FUNCTION!

def hello_func(greeting):
    """This function greets the user."""
    return f"{greeting} Function."

print(hello_func("Hi")) # Output: Hi Function.

# Default argument
def hello_func(greeting, name = "You"):
    """This function greets the user."""
    return f"{greeting} {name}."
print(hello_func("Hi")) # Output: Hi You.
print(hello_func("Hi", "Subhasish")) # Output: Hi Subhasish.

# *args and **kwargs : positional and keyword arguments
def student_info(*args, **kwargs):
    """This function takes any number of positional and keyword arguments."""
    print(args)
    print(kwargs)

student_info('C++', 'Python', name = 'Subahsish', age = 22)
# Output: ('Math', 'Art') {'name': 'John', 'age': 22}

# *args and **kwargs are used to pass a variable number of arguments to a function
# *args is used to pass a non-keyworded, variable-length argument list
# **kwargs is used to pass a keyworded, variable-length argument list

def student_info(*args, **kwargs):
    """This function takes any number of positional and keyword arguments."""
    print(args)
    print(kwargs)

courses = ['C++', 'Python']
info = {'name': 'Subham', 'age': 22}
student_info(*courses, **info)
# Output: ('C++', 'Python') {'name': 'Subham', 'age': 22}

# Number of days per month. First value placeholder for indexing purposes.
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap(year):
    """Return True for leap years, False for non-leap years."""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(year, month):
    """Return number of days in that month in that year."""

    if not 1 <= month <= 12:
        return "Invalid Month"
    if month == 2 and is_leap(year):
        return 29
    return month_days[month]

print(is_leap(2017)) # Output: False
print(is_leap(2020)) # Output: True
print(days_in_month(2017, 2)) # Output: 28
print(days_in_month(2020, 2)) # Output: 29
print(days_in_month(2020, 13)) # Output: Invalid Month
print(days_in_month(2020, 12)) # Output: 31

# Summary:
# Functions are a way to encapsulate code that can be called multiple times
# Functions are defined using the def keyword
# Functions can take arguments
# Functions can return values
# Functions can be called multiple times

# Congratulations! You have learned how to create and use functions in Python.
