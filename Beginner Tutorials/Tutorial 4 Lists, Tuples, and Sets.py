# Python Lists Tutorial

# 1. Introduction to Lists
# Lists are used to store multiple items in a single variable.
# Lists are created using square brackets [].

# Creating a list of courses
courses = ["History", "Math", "Physics", "CompSci"]
nums = [1, 5, 2, 4, 3]
print("Original list of courses:", courses)
print("Original list of numbers:", nums)
# Output: ['History', 'Math', 'Physics', 'CompSci']

# 2. Accessing List Items
# You can access the items in a list using their index. Indexing starts at 0.

print("First course:", courses[0])  # Output: History
print("Second course:", courses[1])  # Output: Math
print("Third course:", courses[2])  # Output: Physics
print("Fourth course:", courses[3])  # Output: CompSci

# 3. Negative Indexing
# Negative indexing starts from the end of the list.

print("Last course:", courses[-1])  # Output: CompSci

# 4. Slicing a List
# You can slice a list to access a range of items.

print("First two courses:", courses[0:2])  # Output: ['History', 'Math']
print("First two courses (alternative syntax):", courses[:2])  # Output: ['History', 'Math']
print("Courses from third to end:", courses[2:])  # Output: ['Physics', 'CompSci']

# 5. Length of a List
# You can find the number of items in a list using the len() function.

print("Number of courses:", len(courses))  # Output: 4

# 6. Adding Items to a List
# You can add an item to the end of the list using append().

courses.append("Art")
print("After appending 'Art':", courses)  # Output: ['History', 'Math', 'Physics', 'CompSci', 'Art']

# You can add an item at a specific index using insert().

courses.insert(0, "Art")
print("After inserting 'Art' at the beginning:", courses)  # Output: ['Art', 'History', 'Math', 'Physics', 'CompSci', 'Art']

# You can add multiple items to the end of the list using extend().

additional_courses = ["Art", "Education"]
courses.extend(additional_courses)
print("After extending with additional courses:", courses)  # Output: ['Art', 'History', 'Math', 'Physics', 'CompSci', 'Art', 'Art', 'Education']

# 7. Removing Items from a List
# You can remove a specific item using remove().

courses.remove("Math")
print("After removing 'Math':", courses)  # Output: ['Art', 'History', 'Physics', 'CompSci', 'Art', 'Art', 'Education']

# You can remove the last item using pop(). It returns the removed item.

popped_course = courses.pop()
print("Popped course:", popped_course)  # Output: Education
print("After popping the last course:", courses)  # Output: ['Art', 'History', 'Physics', 'CompSci', 'Art', 'Art']

# 8. Reversing a List
# You can reverse the order of items in a list using reverse().

courses.reverse()
print("After reversing the list:", courses)  # Output: ['Art', 'Art', 'CompSci', 'Physics', 'History', 'Art']

# 9. Sorting a List
# You can sort the items in a list in alphabetical order using sort().

courses.sort()
print("After sorting the list:", courses)  # Output: ['Art', 'Art', 'Art', 'CompSci', 'History', 'Physics']

# Sorting a list of numbers in ascending order

nums.sort()
print("Sorted list of numbers:", nums)  # Output: [1, 2, 3, 4, 5]

# 10. Using the sorted() function
# The sorted() function returns a new sorted list without modifying the original list.
courses = ["History", "Math", "Physics", "CompSci"]
sorted_courses = sorted(courses)
print("New sorted list of courses:", sorted_courses)  # Output: ['CompSci', 'History', 'Math', 'Physics']
print("Original list of courses remains unchanged:", courses)  # Output: ['History', 'Math', 'Physics', 'CompSci']

# 11. min and max functions
print("Minimum value in the list of numbers:", min(nums))  # Output: 1
print("Maximum value in the list of numbers:", max(nums))  # Output: 5

# 12. sum function
print("Sum of all numbers in the list:", sum(nums))  # Output: 15

# 13. Find the index of an item in a list
print("Index of 'CompSci' in the list:", courses.index("CompSci"))  # Output: 3
# print("Index of 'Art' in the list:", courses.index("Art"))  # Output: ValueError: 'Art' is not in list

# 14. Check if an item is in a list
print("'Math' is in the list:", "Math" in courses)  # Output: True

# 15. List Comprehension
courses_with_space = [course + " " for course in courses]
print("List of courses with spaces:", courses_with_space)

# 16. Looping through a list
for course in courses:
    print("Course:", course) 

# 17. Enumerate through a list
for index, course in enumerate(courses):
    print(index, course)

for index, course in enumerate(courses, start=1):
    print(index, course)

# 18. Join method
course_str = ", ".join(courses)
print("Joined string:", course_str)
new_course_list = course_str.split(", ")
print("New course list:", new_course_list)

# Python Tuples Tutorial

# 1. Introduction to Tuples
# Tuples are used to store multiple items in a single variable.
# Tuples are created using parentheses ().
# Tuples are immutable, meaning you cannot change their values after creation.

# Creating and comparing lists and tuples
list_1 = ["History", "Math", "Physics", "CompSci"]
list_2 = list_1
print("List 1:", list_1)
print("List 2:", list_2)

list_1[0] = "Art"
print("Modified List 1:", list_1)

tuple_1 = ("History", "Math", "Physics", "CompSci")
tuple_2 = tuple_1
print("Tuple 1:", tuple_1)
print("Tuple 2:", tuple_2)

# Trying to modify a tuple (will raise an error)
# tuple_1[0] = "Art"
# print(tuple_1) # TypeError: 'tuple' object does not support item assignment

# 2. Accessing Tuple Items
# You can access the items in a tuple using their index. Indexing starts at 0.
print("First item in tuple:", tuple_1[0])  # Output: History

# Python Sets Tutorial

# 1. Introduction to Sets
# Sets are used to store unique items.
# Sets are created using curly braces {}.
# Sets do not allow duplicate values.

cs_courses = {"History", "Math", "Physics", "CompSci"}
print("CS Courses Set:", cs_courses)  # Output: {'CompSci', 'History', 'Math', 'Physics'}

# Removing duplicates from a list by converting it to a set
nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
unique_nums = set(nums)
print("Unique numbers:", unique_nums)  # Output: {1, 2, 3, 4, 5}

# Set operations: intersection, difference, and union
art_courses = {"History", "Math", "Art", "Design"}
print("Intersection of CS and Art courses:", cs_courses.intersection(art_courses))  # Output: {'Math', 'History'}
print("Difference between CS and Art courses:", cs_courses.difference(art_courses))  # Output: {'Physics', 'CompSci'}
print("Union of CS and Art courses:", cs_courses.union(art_courses))  # Output: {'Design', 'Math', 'Art', 'Physics', 'History', 'CompSci'}

# Creating empty collections

# Empty Lists
empty_list = []
empty_list = list()
print("Empty List:", empty_list)

# Empty Tuples
empty_tuple = ()
empty_tuple = tuple()
print("Empty Tuple:", empty_tuple)

# Empty Sets
# Note: empty_set = {} creates an empty dictionary, not a set
empty_set = set()
print("Empty Set:", empty_set)

# Congratulations! You've learned the basics of Python lists, tuples, and sets.