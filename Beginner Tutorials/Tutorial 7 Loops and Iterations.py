# Loops and Iterations
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# break and continue
for num in nums:
    if num == 5: # if i is equal to 5
        print("found") # found
        break # break the loop
    print(num) # print i
# Output:
# 1 2 3 4 found

for num in nums:
    if num == 5: # if i is equal to 5
        print("found") # found
        continue # continue the loop
    print(num) # print i
# Output:
# 1 2 3 4 found 6 7 8 9 10

# Nested loops
for num in nums:
    for letter in 'abc':
        print(num, letter)
# Output:
# 1 a 1 b 1 c 2 a 2 b 2 c 3 a 3 b 3 c 4 a 4 b 4 c 5 a 5 b 5 c 6 a 6 b 6 c 7 a 7 b 7 c 8 a 8 b 8 c 9 a 9 b 9 c 10 a 10 b 10 c

# Range
for i in range(10): # range(10) is the same as range(0, 10) which is 0 to 9
    print(i) # print i
# Output:
# 0 1 2 3 4 5 6 7 8 9

for i in range(1, 11): # range(1, 11) is 1 to 10
    print(i) # print i
# Output:
# 1 2 3 4 5 6 7 8 9 10

# While loops
x = 0 # x is 0
while x < 10: # while x is less than 10
    print(x) # print x
    x += 1 # x = x + 1
# Output:
# 0 1 2 3 4 5 6 7 8 9

x = 0 # x is 0
while x < 10: # while x is less than 10
    if x == 5: # if x is equal to 5
        break # break the loop
    print(x) # print x
    x += 1 # x = x + 1
# Output:
# 0 1 2 3 4

# Infinite loop
x = 0 # x is 0
while True: # while True
    if x == 5: # if x is equal to 5
        break # break the loop
    print(x) # print x
    x += 1 # x = x + 1
# Output:
# 0 1 2 3 4

# Infinite loop
# ctrl + c to stop the loop
while True:
    print(x)
    x += 1

# Congratulations! You have completed the tutorial on loops and iterations.
