# working with conditionals & booleans - If, Else & Elif
language  = 'Java'

if language == 'Python':
    print("Language is Python")
elif language == 'Java':
    print("Language is Java")
else:
    print("No Match!")

# Comparisions:
# Equal:            ==
# Not Equal:        !=
# Greater Than:     >
# Less Than:        <
# Greater or Equal: >=
# Less or Equal:    <=
# Object Identity:  is
# and 
# or
# not

# and example
user = 'Admin'
logged_in = True
if user == 'Admin' and logged_in:
    print("Admin Page")
else:
    print("Bad Creds")

# and example 2
user = 'Admin'
logged_in = False
if user == 'Admin' and logged_in:
    print("Admin Page")
else:
    print("Bad Creds")

# or example
user = 'Admin'
logged_in = False
if user == 'Admin' or logged_in:
    print("Admin Page")
else:
    print("Bad Creds")

# not example
user = 'Admin'
logged_in = True
if not logged_in:
    print("Please Log In")
else:
    print("Welcome to Admin Page.")

# not example2
user = 'Admin'
logged_in = False
if not logged_in:
    print("Please Log In") 
else:
    print("Welcome to Admin Page.") 

# is example 1
a = [1,2,3]
b = [1,2,3]
print(a == b) # True
print(a is b) # False
print(id(a)) # id of a
print(id(b)) # id of b

# is example 2
a = [1,2,3]
b = a
print(a == b) # True
print(a is b) # True
print(id(a)) # id of a
print(id(b)) # id of b

# False values:
    # False
    # None
    # Zero of any numeric type
    # Any empty sequence. For example, '', (), [].
    # Any empty mapping. For example, {}.

condition = False
if condition:
    print("Evaluated to True")
else:
    print("Evaluated to False")

condition = None
if condition:
    print("Evaluated to True")
else:
    print("Evaluated to False")

condition = 0
if condition:
    print("Evaluated to True")
else:
    print("Evaluated to False")

condition = []
if condition:
    print("Evaluated to True")
else:
    print("Evaluated to False")

condition = {}
if condition:
    print("Evaluated to True")
else:
    print("Evaluated to False")