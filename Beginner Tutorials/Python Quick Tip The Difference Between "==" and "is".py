# Differnce between "==" and "is"
# == - value equality - Two objects have the same value
# is - reference equality - Two references refer to the same object

a = [1, 2, 3]
b = [1, 2, 3]
print(a == b) # True
print(a is b) # False

c = a
print(c == a) # True
print(c is a) # True

# "is" checks if two variables refer to the same object in memory
# "==" checks if two variables have the same value
