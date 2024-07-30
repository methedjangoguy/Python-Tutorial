# Introduction to Numbers in Python

# 1. Understanding Data Types
# Integers
num = 3
print(type(num))  # Output: <class 'int'>

# Floats
num = 3.14
print(type(num))  # Output: <class 'float'>

# 2. Arithmetic Operators

# Addition:       3 + 2
print(3 + 2)  # Output: 5

# Subtraction:    3 - 2
print(3 - 2)  # Output: 1

# Multiplication: 3 * 2
print(3 * 2)  # Output: 6

# Division:       3 / 2
print(3 / 2)  # Output: 1.5

# Floor Division: 3 // 2
print(3 // 2)  # Output: 1

# Exponent:       3 ** 2
print(3 ** 2)  # Output: 9

# Modulus:        3 % 2
print(3 % 2)  # Output: 1
print(3 % 3)  # Output: 0

# 3. Even and Odd Check using Modulus
print(2 % 2)  # Output: 0 (Even)
print(3 % 2)  # Output: 1 (Odd)
print(4 % 2)  # Output: 0 (Even)
print(5 % 2)  # Output: 1 (Odd)

# 4. Order of Operations (PEMDAS - Parentheses, Exponents, Multiplication and Division, Addition and Subtraction)
print(2 + 3 * 5)  # Output: 17
print((2 + 3) * 5)  # Output: 25
print(2 + (3 * 5))  # Output: 17

# 5. Incrementing Values
num = 1
num = num + 1
print(num)  # Output: 2

num = 1
num += 1
print(num)  # Output: 2

num = 1
num += 10
print(num)  # Output: 11

# 6. Methods for Numbers
num = 3
print(num)  # Output: 3

# Absolute value
print(abs(num))  # Output: 3

# Rounding numbers
num = 3.8
print(round(num))  # Output: 4

num = 3.4
print(round(num))  # Output: 3

# 7. Comparisons
num_1 = 3
num_2 = 2

# Equal:            3 == 2
print(num_1 == num_2)  # Output: False

# Not Equal:        3 != 2
print(num_1 != num_2)  # Output: True

# Greater than:     3 > 2
print(num_1 > num_2)  # Output: True

# Less than:        3 < 2
print(num_1 < num_2)  # Output: False

# Greater or Equal: 3 >= 2
print(num_1 >= num_2)  # Output: True

# Less or Equal:    3 <= 2
print(num_1 <= num_2)  # Output: False

# 8. Type Conversion
# Converting strings to integers
num_1 = '100'
num_2 = '200'
print(num_1 + num_2)  # Output: 100200 (concatenation)

# Solution: String casting to integers
num_1 = int(num_1)
num_2 = int(num_2)
print(num_1 + num_2)  # Output: 300

# Congratulations! You've learned the basics of working with numbers in Python.