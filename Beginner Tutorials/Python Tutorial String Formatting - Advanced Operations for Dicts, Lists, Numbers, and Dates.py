
# Dictionary containing person information
person = {'name': 'Subhasish', 'age': 28}

# Basic string concatenation with type conversion
sentence = 'My name is ' + person['name'] + ' and I am ' + str(person['age']) + ' years old.'
print(sentence)

# String formatting using .format() with unnamed placeholders
sentence2 = 'My name is {} and I am {} years old.'.format(person['name'], person['age'])
print(sentence2)

# String formatting using .format() with numbered placeholders
sentence3 = 'My name is {0} and I am {1} years old.'.format(person['name'], person['age'])
print(sentence3)

# String formatting using .format() with dictionary key access
sentence4 = 'My name is {0[name]} and I am {0[age]} years old.'.format(person)
print(sentence4)

# Class definition for Person object
class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Creating Person instance and formatting with object attribute access
p1 = Person('Subhasish', 28)
sentence5 = 'My name is {0.name} and I am {0.age} years old.'.format(p1)
print(sentence5)

# Keyword argument access in string formatting
sentence6 = 'My name is {name} and I am {age} years old.'.format(name='Subhasish', age='28')
print(sentence6)

# Keyword argument access in string formatting with dictionary
sentence7 = 'My name is {name} and I am {age} years old.'.format(**person)
print(sentence7)

# Formatting leading zeros
for i in range(1, 11):
    sentence8 = 'The value is {:02}'.format(i)
    print(sentence8)

# Formatting float with 2 decimal places
pi = 3.14159265
sentence9 = 'Pi is equal to {:.2f}'.format(pi)
print(sentence9)

# Formatting large numbers with commas
sentence10 = '1 MB is equal to {:,.2f} bytes'.format(1000**2)
print(sentence10)

# Formatting Dates
import datetime

my_date = datetime.datetime(2025, 2, 4, 12, 30, 45)
print(my_date)

sentence11 = '{:%B %d, %Y}'.format(my_date)
print(sentence11)

# Formatting message with date formatting
sentence12 = '{0:%B %d, %Y} fell on a {0:%A} and was the {0:%j} day of the year'.format(my_date)
print(sentence12)

# Congratulations! You have completed the Advanced Formatting.
