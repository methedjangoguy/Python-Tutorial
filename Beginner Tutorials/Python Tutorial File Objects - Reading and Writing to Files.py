# File Objects: A way to interact with files on your computer

# Open a file
myFile = open('test.txt', 'r') # 'w' is write mode, 'r' is read mode, 'a' is append mode, 'r+' is read and write mode
print(myFile.name) # Print the name of the file
print(myFile.mode) # Print the mode of the file
myFile.close() # Close the file

# Open a file using a context manager
with open('test.txt', 'r') as myFile: # Open the file and close it automatically
    contents = myFile.read() # Read the contents of the file
    print(contents)

with open('test.txt', 'r') as myFile:
    contents = myFile.readlines() # Read the contents of the file line by line
    print(contents)

with open('test.txt', 'r') as myFile:
    contents = myFile.readline() # Read the first line of the file
    print(contents)

with open('test.txt', 'r') as myFile:
    for line in myFile:
        print(line, end='') # Print each line of the file without newlines

with open("test.txt", "r") as myFile:  # Open the file and close it automatically
    contents = myFile.read(2)  # Read the first 2 characters of the file
    print(contents)
    contents = myFile.read(2)  # Read the next 2 characters of the file
    print(contents)
    contents = myFile.read(2)  # Read the next 2 characters of the file
    print(contents)

with open("test.txt", "r") as myFile:  # Open the file and close it automatically
    size_to_read = 3
    contents = myFile.read(size_to_read)  # Read the first 10 characters of the file
    while len(contents) > 0:  # Loop until the end of the file
        print(contents, end='')  # Print the contents of the file without newlines
        contents = myFile.read(size_to_read)  # Read the next 10 characters of the file

# Get the current position in the file
with open("test.txt", "r") as myFile:  # Open the file and close it automatically
    size_to_read = 2
    contents = myFile.read(size_to_read)  # Read the first 10 characters of the file
    print(myFile.tell())  # Print the current position in the file

# Seek to a specific position in the file
with open("test.txt", "r") as myFile:  # Open the file and close it automatically
    contents = myFile.read(2)  # Read the first 2 characters of the file
    print(contents)
    myFile.seek(0)  # Seek to the beginning of the file
    contents = myFile.read(2)  # Read the next 2 characters of the file
    print(contents)

# Write to a file
with open("test2.txt", "w") as myFile:  # Open the file and close it automatically
    myFile.write("Test")  # Write to the file
    myFile.seek(0)  # Seek to the beginning of the file
    myFile.write("R")  # Write to the file

# Copy a file
with open("test.txt", "r") as rf:  # Open the file and close it automatically
    with open("test_copy.txt", "w") as wf:  # Open the file and close it automatically
        for line in rf:
            wf.write(line)  # Write each line of the file to the new file

# Copy a file using binary mode
with open("test.jpg", "rb") as rf:  # Open the file and close it automatically
    with open("test_copy.jpg", "wb") as wf:  # Open the file and close it automatically
        for line in rf:
            wf.write(line)  # Write each line of the file to the new file

# Copy a file uusing chunk size
with open("test.jpg", "rb") as rf:  # Open the file and close it automatically
    with open("test_copy.jpg", "wb") as wf:  # Open the file and close it automatically
        chunk_size = 4096  # Set the chunk size to 4096 bytes
        rf_chunk = rf.read(chunk_size)  # Read the first chunk of the file
        while len(rf_chunk) > 0:  # Loop until the end of the file
            wf.write(rf_chunk)  # Write the chunk to the new file
            rf_chunk = rf.read(chunk_size)  # Read the next chunk of the file

# Congratulations! You have completed the tutorial on file handling basicss
