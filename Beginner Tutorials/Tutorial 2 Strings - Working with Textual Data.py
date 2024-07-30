# Introduction to Strings in Python

# 1. Print "Hello World"
print("Hello World")  # prints Hello World

# 2. Storing data in a variable
message = "Hello World"
print(message)  # prints Hello World

# 3. String Length
# Using len() function to get the length of the string
print(len(message))  # prints 11

# 4. String Indexing
# Accessing individual characters using their index
print(message[0])  # prints H

# 5. String Slicing
# Accessing a substring using slicing
print(message[0:5])  # prints Hello
print(message[:5])  # prints Hello
print(message[6:])  # prints World

# 6. String Methods
# Convert to lowercase
print(message.lower())  # prints hello world
# Convert to uppercase
print(message.upper())  # prints HELLO WORLD

# 7. String Count
# Count occurrences of a substring
print(message.count('Hello'))  # prints 1
print(message.count('l'))  # prints 3

# 8. String Find
# Find the position of a substring
print(message.find('Hello'))  # prints 0
print(message.find('world'))  # prints -1 (not found)

# 9. String Replace
# Replace a substring with another substring
new_message = message.replace('World', 'Universe')
print(new_message)  # prints Hello Universe

# 10. String Concatenation
# Combine strings using the + operator
greeting = 'Hello'
name = 'methedjangoguy'
greeting_message = greeting + ', ' + name + '. Welcome!'
print(greeting_message)  # prints Hello, methedjangoguy. Welcome!

# 11. String Formatting
# Using the format() method
name = 'methedjangoguy'
age = 28
message = 'Hello, {}. You are {} years old.'.format(name, age)
print(message)  # prints Hello, methedjangoguy. You are 28 years old.

# 12. String Formatting with f-strings (Python 3.6+)
# Using f-strings for formatting
message = f'Hello, {name}. You are {age} years old.'
print(message)  # prints Hello, methedjangoguy. You are 28 years old.
# Using f-strings with string methods
message = f'Hello, {name.capitalize()}. You are {age} years old.'
print(message)  # prints Hello, Methedjangoguy. You are 28 years old.

# 13. Methods and Attributes of the String Object
# Using dir() to list all methods and attributes of the string object
print(dir(name))  # prints a list of methods and attributes of the string object

# 14. String Formatting with % Operator
# Using the % operator for string formatting
message = 'Hello, %s. You are %d years old.' % (name, age)
print(message)  # prints Hello, methedjangoguy. You are 28 years old.

# 15. Help with String Formatting
# Using help() to get information about string methods
print(help(str))  # prints the help for the string object
print(help(str.format))  # prints the help for the format method of the string object
print(help(str.capitalize))  # prints the help for the capitalize method of the string object

# Congratulations! You've learned the basics of Python strings.