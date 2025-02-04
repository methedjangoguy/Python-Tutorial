# List Comprehensions
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# I want 'n' for each 'n' in nums
my_list = []
for n in nums:
    my_list.append(n)
print(my_list)

my_list = [n for n in nums] # List comprehension
print(my_list) # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# I want 'n*n' for each 'n' in nums
my_list = []
for n in nums:
    my_list.append(n*n)
print(my_list)

my_list = [n*n for n in nums] # List comprehension
print(my_list) # Output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Using a map + lambda
my_list = map(lambda n: n*n, nums)
print(list(my_list)) # Output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# I want 'n' for each 'n' in nums if 'n' is even
my_list = []
for n in nums:
    if n % 2 == 0:
        my_list.append(n)
print(my_list) # Output: [2, 4, 6, 8, 10]

my_list = [n for n in nums if n % 2 == 0] # List comprehension
print(my_list) # Output: [2, 4, 6, 8, 10]

# Using a filter + lambda
my_list = filter(lambda n: n % 2 == 0, nums)
print(list(my_list)) # Output: [2, 4, 6, 8, 10]

# I want a (letter, num) pair for each letter in 'abcd' and each number in '0123'
my_list = []
for letter in 'abcd':
    for num in range(4):
        my_list.append((letter, num))

print(my_list) # Output: [('a', 0), ('a', 1), ('a', 2), ('a', 3), ('b', 0), ('b', 1), ('b', 2), ('b', 3), ('c', 0), ('c', 1), ('c', 2), ('c', 3), ('d', 0), ('d', 1), ('d', 2), ('d', 3)]

my_list = [(letter, num) for letter in 'abcd' for num in range(4)] # List comprehension
print(my_list) # Output: [('a', 0), ('a', 1), ('a', 2), ('a', 3), ('b', 0), ('b', 1), ('b', 2), ('b', 3), ('c', 0), ('c', 1), ('c', 2), ('c', 3), ('d', 0), ('d', 1), ('d', 2), ('d', 3)]

names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heros = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']
print(list(zip(names, heros))) # Output: [('Bruce', 'Batman'), ('Clark', 'Superman'), ('Peter', 'Spiderman'), ('Logan', 'Wolverine'), ('Wade', 'Deadpool')]

# Dictionary comprehension
# I want a dict{'name': 'hero'} for each name, hero in zip(names, heros)
my_dict = {}
for name, hero in zip(names, heros):
    my_dict[name] = hero
print(my_dict) # Output: {'Bruce': 'Batman', 'Clark': 'Superman', 'Peter': 'Spiderman', 'Logan': 'Wolverine', 'Wade': 'Deadpool'}

my_dict = {name: hero for name, hero in zip(names, heros)} # Dictionary comprehension
print(my_dict) # Output: {'Bruce': 'Batman', 'Clark': 'Superman', 'Peter': 'Spiderman', 'Logan': 'Wolverine', 'Wade': 'Deadpool'}

# If name not equal to Peter
my_dict = {name: hero for name, hero in zip(names, heros) if name != 'Peter'} # Dictionary comprehension
print(my_dict) # Output: {'Bruce': 'Batman', 'Clark': 'Superman', 'Logan': 'Wolverine', 'Wade': 'Deadpool'}

# Set comprehension
nums = [1, 1, 2, 1, 3, 4, 3, 4, 5, 5, 6, 7, 8, 7, 9, 9]
my_set = set()
for n in nums:
    my_set.add(n)
print(my_set) # Output: {1, 2, 3, 4, 5, 6, 7, 8, 9}

my_set = {n for n in nums} # Set comprehension
print(my_set) # Output: {1, 2, 3, 4, 5, 6, 7, 8, 9}

# Generator expression
# I want to yield 'n*n' for each 'n' in nums
def gen_func(nums):
    for n in nums:
        yield n*n
        # return n*n # This will return only the first value

my_gen = gen_func(nums)
for i in my_gen:
    print(i)

my_gen = (n*n for n in nums) # Generator expression
for i in my_gen:
    print(i) # Output: 1, 4, 9, 16, 25, 36, 49, 64, 81, 100

# Generator expression is more memory efficient than list comprehension
# List comprehension will store the entire list in memory
# Generator expression will yield one value at a time
# Generator expression is not stored in memory
# Generator expression is not evaluated until you iterate through it
# Generator expression is more efficient when you are working with large datasets

# Congratulations! You have learned about comprehensions in Python
