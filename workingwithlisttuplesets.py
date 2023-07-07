# working with lists
courses = ["History", "Math", "Physics", "CompSci"]
print(courses)  # prints the list
print(len(courses))  # prints the length of the list

# working with list slicing
print(courses[0])  # prints the first element of the list
print(courses[-1])  # prints the last element of the list
print(courses[0:2])  # prints the first two elements of the list
print(courses[2:])  # prints the elements from the third element to the end of the list

# working with list methods
# courses.append("Art")  # adds the element to the end of the list
# print(courses)
# courses.insert(0, "Art")  # adds the element to the specified index
# print(courses)

courses_2 = ["Art", "Education"]
# courses.insert(0, courses_2)  # adds the list to the specified index
print(courses)
# print(courses[0])  # prints the list
# print(courses[0][1])  # prints the element of the list
courses.extend(courses_2)  # adds the list to the end of the list
print(courses)

# courses.remove("Math")  # removes the element from the list
# print(courses)  

# courses.pop()  # removes the last element of the list
# print(courses)

courses.reverse()  # reverses the list
print(courses)
courses.sort()  # sorts the list 
print(courses)  
num = [1, 3,6,4,7,2,8]  # creates a list of numbers
num.sort()  # sorts the list in ascending order
print(num)  # sorts the list in ascending order
num.sort(reverse=True)  # sorts the list in descending order
print(num)  # sorts the list in descending order
print(min(num))  # prints the minimum value of the list
print(max(num))  # prints the maximum value of the list
print(sum(num))  # prints the sum of the list
print(courses.index("History"))  # prints the index of the element
print("Math" in courses)  # prints true if the element is in the list

# looping through the list
for course in courses:
    print(course)  # prints the element of the list

for index, course in enumerate(courses):
    print(index, course)  # prints the index and the element of the list

for index, course in enumerate(courses, start=1):
    print(index, course)  # prints the index and the element of the list

# turn list to strings separated by comma
print(", ".join(courses))  # prints the element of the list separated by comma

# working with tuples
courses_tuple = ("History", "Math", "Physics", "CompSci")
print(courses_tuple)  # prints the tuple
print(len(courses_tuple))  # prints the length of the tuple
print(courses_tuple[0])  # prints the first element of the tuple
print(courses_tuple[-1])  # prints the last element of the tuple
print(courses_tuple[0:2])  # prints the first two elements of the tuple
print(courses_tuple[0:2])  # prints the first two elements of the tuple
print(courses_tuple[2:])  # prints the elements from the third element to the end of the tuple

# working with sets
courses_set = {"History", "Math", "Physics", "CompSci"}
courses_set1 = {"History", "Math", "Art", "Design"}
print(courses_set)  # prints the set
print(len(courses_set))  # prints the length of the set
print('Math' in courses_set)  # prints true if the element is in the set

print(courses_set.intersection(courses_set1))  # prints the intersection of the sets, displays the common element in both the tuples
print(courses_set.difference(courses_set1))  # prints the difference of the sets, displays the elements in the first tuple but not in the second tuple
print(courses_set.union(courses_set1))  # prints the union of the sets, displays the elements in both the tuples

# empty list
empty_list = []
empty_list = list()

# empty tuple
empty_tuple = ()
empty_tuple = tuple()

# empty set
empty_set = {}  # this is wrong! It will create a dictionary
empty_set = set()  # this will create a set