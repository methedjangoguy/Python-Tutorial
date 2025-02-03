# Basic if statement that will always execute since condition is True
if True:
    print("Conditional was True")

# Basic if statement that will never execute since condition is False
if False:
    print("Conditional was True")

# If statement checking if language variable equals "Python"
language = "Python"
if language == "Python":
    print("Conditional was True")

# If statement checking if language variable equals "Python" and version variable equals "3"
language = "Java"
version = "2"
if language == "Python" and version == "3":
    print("Language is Python 3")
elif language == "Java" and version == "2":
    print("Language is Java 2")
else:
    print("No match")

# If statement checking if language variable equals "Python" and version variable equals "3"
language = "Python"

# boolean operators
# and
# or
# not

# if user is Admin and is logged in
user = "Admin"
logged_in = True
if user == "Admin" and logged_in:
    print("Admin Page")
else:
    print("Bad Creds")

# if user is Admin or is logged in
user = "Admin"
logged_in = False
if logged_in or user == "Admin":
    print("Admin Page")
else:
    print("Bad Creds")

# if user is not logged in
if not logged_in:
    print("Please Log In")
else:
    print("Welcome")

# is operator
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)  # True
print(a is b)  # False
print(id(a))  # Prints the unique identifier of the object 'a'
print(id(b))  # Prints the unique identifier of the object 'b'
# Since 'a' and 'b' are two different objects, the 'is' operator returns False

# If we set 'b' equal to 'a', then 'b' will reference the same object as 'a'
a = [1, 2, 3]
b = a
print(a == b)  # True
print(a is b)  # True
print(id(a))  # Prints the unique identifier of the object 'a'
print(id(b))  # Prints the unique identifier of the object 'b'

# False Values:
# False
# None
# Zero of any numeric type
# Any empty sequence. For example, '', (), [].
# Any empty mapping. For example, {}.
condition = False
if condition:
    print('Evaluated to True') # This will not print since the condition is False
else:
    print('Evaluated to False') # This will print since the condition is False

condition = None
if condition:
    print('Evaluated to True') # This will not print since the condition is None
else:
    print('Evaluated to False') # This will print since the condition is None

condition = 0
if condition:
    print('Evaluated to True') # This will not print since the condition is a zero of any numeric type
else:
    print('Evaluated to False') # This will print since the condition is a zero of any numeric type

condition = 10
if condition:
    print('Evaluated to True') # This will print since the condition is not a zero of any numeric type
else:
    print('Evaluated to False') # This will print since the condition is not a zero of any numeric type

condition = ''
if condition:
    print('Evaluated to True')  # This will not print since the condition is an empty sequence
else:
    print('Evaluated to False') # This will print since the condition is an empty sequence

#empty mapping
condition = {}
if condition:
    print('Evaluated to True') # This will not print since the condition is an empty mapping
else:
    print('Evaluated to False') # This will print since the condition is an empty mapping

condition = 'Test'
if condition:
    print('Evaluated to True') # This will print since the condition is not an empty sequence
else:
    print('Evaluated to False') # This will not print since the condition is not an empty sequence

# Congrratulations, you have completed the tutorial on conditional statements in Python
