# my_list.py
# Create a list of integers from 0 to 9
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# Print the entire list
print(my_list)

# Create a list of integers from 0 to 9 using the range() function
my_list = list(range(10))

# Print the entire list
print(my_list)

# Print the first element (index 0) of the list
print(my_list[0])

# Print the last element (index -1) of the list
print(my_list[-1])
# Print the second-to-last element (index -2) of the list
print(my_list[-2])

# slicing a list using the colon operator
print(my_list[2:5])

# slicing a list from the beginning to a specific index
print(my_list[:5])

# slicing a list from a specific index to the end
print(my_list[5:])

# slicing a list from the beginning to the end
print(my_list[:])

# slicing a list with a step
print(my_list[2:8:2])

# slicing a list with a step
print(my_list[2:-1:2])

# slicing a list with a negative step
print(my_list[8:2:-2])

# reversing a list using slicing
print(my_list[::-1])

# reversing a list using the reverse() method
my_list.reverse()
print(my_list)

# slicing a list from a specific index to the end with negetive index
print(my_list[-3:])

# slicing a list from the beginning to a specific index with negetive index
print(my_list[:-3])

# slicing a list from a specific index to a specific index with negetive index
print(my_list[3:-3])

# slicing a list from a specific index to a specific index with negetive index and a step
print(my_list[3:-3:-1])  # This will return an empty list

# slicing a string
sample_url = "http://google.com"
print(sample_url)

# reverse the string
print(sample_url[::-1])

# get the top level domain
print(sample_url[-4:])

# get the http or https
print(sample_url[:4])

# get the url without the http or https
print(sample_url[7:])

# get the url without the http or https and the top level domain
print(sample_url[7:-4])

# Congratulations! You have learned how to slice lists and strings in Python.
