# Define first name and last name variables as strings
firstname = "Subhasish"
lastname = "Swain"

# Different ways to concatenate strings in Python
# Method 1: Using + operator for string concatenation - Basic but less efficient way
sentence = "My name is " + firstname + " " + lastname

# Method 2: Using str.format() method - More flexible than + operator
sentence1 = "My name is {} {}".format(firstname, lastname)

# Method 3: Using f-strings (formatted string literals, Python 3.6+) - Most readable and recommended way
sentence2 = f"My name is {firstname} {lastname}"

# Print all three concatenated strings to compare output
print(sentence)
print(sentence1)
print(sentence2)

# Convert names to uppercase using string method upper()
sentence3 = f"My name is {firstname.upper()} {lastname.upper()}"
print(sentence3)

# Create dictionary with person details and access values in f-string
person = {"name": "Subhasish Swain", "age": 28}
sentence4 = f"My name is {person['name']} and I am {person['age']} years old."
print(sentence4)

# Demonstrate expression evaluation inside f-string
calulation = f"4 times 11 is equal to {4 * 11}"
print(calulation)

# Can be used in loop as well to format numbers with leading zeros
for n in range(1, 11):
    sentence5 = f"The value is {n:02}"
    print(sentence5)

# Define pi value and format it to 4 decimal places
pi = 3.14159265
sentence6 = f"Pi is equal to {pi:.5f}"
print(sentence6)

# datetime module to demonstrate datetime formatting
import datetime

birthday = datetime.datetime(1992, 6, 21)
sentence7 = f"Subhasish has a birthday on {birthday:%B %d, %Y}"
print(sentence7)

# Congratulations! You have learned how to use f-strings in Python for string formatting.
