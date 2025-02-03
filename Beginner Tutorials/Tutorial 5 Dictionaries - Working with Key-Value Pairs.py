# Dictionary containing student information including name, age and courses
student = {'name': 'Subham', 'age': 28, 'courses': ['Math', 'CompSci']}

# Print the entire student dictionary
print(student)

# Print just the student's name
print(student['name'])

# Print the list of courses the student is taking
print(student['courses'])

# Try to get phone number - returns None since key doesn't exist
print(student.get('phone'))

# If key doesn't exist, return a default value
print(student.get('phone', 'Not Found'))

# Add a new key-value pair to the dictionary
student['phone'] = '555-5555'
print(student.get('phone', 'Not Found'))

# Update the value of a key
student['phone'] = '555-5556'
print(student.get('phone', 'Not Found')) # Returns the updated value

# Update multiple key-value pairs at once
student.update({'name': 'Subhasish', 'age': 29, 'phone': '555-5557'})
print(student)  # Returns the updated dictionary

# Delete a key-value pair from the dictionary
del student['age']
print(student)  # Returns the updated dictionary without the 'age' key

# Remove a key-value pair from the dictionary and return the value
phone = student.pop('phone')
print(student)  # Returns the updated dictionary without the 'phone' key

# Print the value that was removed from the dictionary
print(phone)

# length of the dictionary
print(len(student))

# print the keys in the dictionary
print(student.keys())

# print the values in the dictionary
print(student.values())

# print the key-value pairs in the dictionary
print(student.items())

# loop through the keys in the dictionary
student = {'name': 'Subham', 'age': 28, 'courses': ['Math', 'CompSci']}
for key in student:
    print(key)

# loop through the key-value pairs in the dictionary
for key, value in student.items():
    print(key, value)

# loop through the values in the dictionary
for value in student.values():
    print(value)

# loop through the keys in the dictionary
for key in student.keys():
    print(key)

# Congratulations! You have learned how to work with dictionaries in Python!
