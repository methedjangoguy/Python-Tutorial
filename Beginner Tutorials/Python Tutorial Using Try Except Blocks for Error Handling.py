# Error and Exception Handling: Try, Except, Finally
# This script demonstrates basic error handling in Python using try-except blocks

# Try block attempts to open a file named "testfile.txt"
# The try block contains code that might raise an exception
try:
    f = open("testfile.txt")
# Except block handles the specific case where the file is not found
# FileNotFoundError is raised when the specified file does not exist
except FileNotFoundError as f:
    print(f"Sorry, this file does not exist in the path. {f}")
# Generic except block catches any other exceptions that may occur
# This acts as a catch-all for any other unexpected errors
except Exception as e:
    print(f"Sorry, something went wrong. {e}")
else:
    # This block is executed if no exceptions are raised
    # If file is successfully opened, read and display its contents
    print(f.read())
    # Close the file handle to free up system resources
    f.close()
finally:
    # This block is always executed
    # The finally block runs regardless of whether an exception occurred
    print("Executing Finally...")

# output:
# Sorry, this file does not exist in the path. [Errno 2] No such file or directory: 'testfile.txt'
# Executing Finally...

# Congratulations! You have learned the basics of error and exception handling in Python.
