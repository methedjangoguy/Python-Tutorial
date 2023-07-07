# working with dictionaries, working with key-value pairs
student = {"name": "John", "age": 25, "courses": ["Math", "CompSci"]}
print(student)  # print the whole dictionary
print(student["name"])  # print the value of the key "name"
print(student.get("name"))  # print the value of the key "name"
print(student.get("phone"))  # print the value of the key "phone"
print(student.get("phone", "Not Found"))  # print the value of the key "phone"
student["phone"] = "555-5555"  # add a new key-value pair to the dictionary
student["name"] = "Jane"  # change the value of the key "name"
student.update({"name": "Jane", "age": 26, "phone": "555-5555"})  # update the dictionary
print(student)  # print the whole dictionary
del student["age"]  # delete the key-value pair with the key "age"
print(student)  # print the whole dictionary
print(student.keys())  # print the keys of the dictionary
print(student.values())  # print the values of the dictionary
print(student.items())  # print the key-value pairs of the dictionary

# looping through dictionaries
for key, value in student.items():
    print(key, value) # print the key and value of each key-value pair

print(len(student))  # print the length of the dictionary