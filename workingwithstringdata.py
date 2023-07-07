# print welcome message
print('Hello World')

# working with string data
message = 'Hello World'
print(message)

message1 = "My name's Anonymous"
print(message1)

message2 = """This is a multi-line string. 
It can span multiple lines."""
print(message2)

# print length of string
print(len(message))

# working with string slicing
print(message[0])
print(message[0:5])
print(message[6:])

# working with string manimupation
print(message.lower()) # all lower case
print(message.upper()) # all upper case
print(message.count('Hello')) # count number of Hellos
print(message.find('Hello')) # find index of Helloc
message.replace('World', 'Universe') # replace World with Universe
print(message) # message is still the same

updated_message = message.replace('World', 'Universe') # replace World with Universe
print(updated_message) 

# working with string concatenation
greetings = 'Hello'
name = "Subham"
message = greetings + ', ' + name + '. Welcome!' # formatting using comma and space
message = '{}, {}. Welcome!'.format(greetings, name) # formatting using .format()
message = f'{greetings}, {name.upper()}. Welcome!' # formatting using f-strings (Python 3.6+)
print(message)

# prints all the attributes and methods which are accessible to the variable
print(dir(name))

# Help on class str in module builtins:
print(help(str)) 