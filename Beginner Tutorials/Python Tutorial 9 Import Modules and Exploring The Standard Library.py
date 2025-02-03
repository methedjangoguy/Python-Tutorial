# This file demonstrates various ways to import and use Python modules

# Different methods of importing modules
import usermodule # Basic import of a custom module
import usermodule as um # Import with an alias for shorter reference
from usermodule import * # Import all contents (not recommended in production code)
from usermodule import find_index, test # Import specific functions/variables

import sys # System-specific parameters and functions

# Sample list to demonstrate module usage
courses = ['History', 'Math', 'Physics', 'CompSci']

# Using imported function to find index of 'Math' in courses list
index = find_index(courses, 'Math')
print(index)
print(test)

# Get filesystem path of imported module
print(usermodule.__file__)

# Display Python's module search paths
print(sys.path)

# Import commonly used built-in Python modules
import random # For random number generation and selection
import math # For mathematical operations
import datetime # For date and time operations
import calendar # For calendar related functions
import os # For operating system dependent functionality

# Demonstrate random selection from a list
random_course = random.choice(courses)
print(random.choice(courses))
print(random.choice(courses))

# Convert degrees to radians and calculate sine
rads = math.radians(90)
print(math.sin(rads))

# Get and display current date
today = datetime.date.today()
print(today)

# Check if 2020 is a leap year
print(calendar.isleap(2020)) # True

# Display filesystem information
print(os.__file__) # Show location of os module
print(os.getcwd()) # Show current working directory

# Congratulations! You have learned how to import and use Python modules and packages.
