# Working with Numeric Data
num_i = 3
print(type(num_i)) # prints type of variable

num_f = 3.12
print(type(num_f)) # prints type of variable

# Arithmatic Operators:
# Addition: 2 + 2
print(3+2) # prints 5

# Subtraction: 2 - 2
print(3-2) # prints 1

# Multiplication: 2 * 2
print(3*2) # prints 6

# Division: 2 / 2
print(3/2) # prints 1.5

# Modulus: 2 % 2
print(3%2) # prints 1

# Exponent: 2 ** 2
print(3**2) # prints 9

# Floor Division: 2 // 2
print(3//2) # prints 1

# order of operations
print(3*2+1) # prints 7
print(3*(2+1)) # prints 9

# incrementing and decrementing
num = 1
num = num + 1
print(num) # prints 2

num = 1
num += 1
print(num) # prints 2
num -= 1
print(num) # prints 1

# some important functions

absnum = -3
print(abs(absnum)) # prints 3

roundnum = 3.75
print(round(roundnum,1)) # prints 3.8

# Comparision Operators:
# Equal: 3 == 2
print(3 == 2) # prints False

# Not Equal: 3 != 2
print(3 != 2) # prints True

# Greater Than: 3 > 2
print(3 > 2) # prints True

# Less Than: 3 < 2
print(3 < 2) # prints False

# Greater Than or Equal: 3 >= 2
print(3 >= 2) # prints True

# Less Than or Equal: 3 <= 2
print(3 <= 2) # prints False

# typecasting in python 
num_i = '100'
num_f = '200'
num_i = int(num_i)
num_f = int(num_f)
print(num_i + num_f) # prints 300