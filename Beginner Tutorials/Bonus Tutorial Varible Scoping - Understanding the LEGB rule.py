
# LEGB
# Local, Enclosing, Global, Built-in

import builtins

# Global & Local Scope
x = 'global x' # x is 'global x'

def test():
    y = 'local y' # y is 'local y'
    print(y) # print y
    print(x) # print x

test() # call test()
# Output:
# local y
# global x

print(x) # print x
# Output:
# global x

def test():
    x = "local xx"  # x is 'local x'
    print(x)  # print y

test()  # call test()
# Output:
# local xx
print(x)  # print x

def test():
    global x  # x is now global
    x = "local x"  # y is 'local y'
    print(x)  # print y

test()  # call test()
# Output:
# local x
print(x)  # print x
# Output:
# local x

def test(z):
    x = "local x"  # x is 'local x'
    print(z)  # print z

test('local z')  # call test()
# Output:
# local z

# built-in scope
m = min([5, 1, 4, 2, 3])  # m is 1
print(m)  # print m

print(dir(builtins))  # print all built-in functions
# prints all built-in functions

# Enclosing Scope
def outer():
    x = 'outer x'  # x is 'outer x'

    def inner():
        x = 'inner x'  # x is 'inner x'
        print(x)  # print x

    inner()  # call inner()
    print(x)  # print x
outer()  # call outer()

# Output:
# inner x
# outer x

def outer():
    x = 'outer x'  # x is 'outer x'

    def inner():
        nonlocal x  # x is now nonlocal
        x = 'inner x'  # x is 'inner x'
        print(x)  # print x

    inner()  # call inner()
    print(x)  # print x
outer()  # call outer()
# Output:
# inner x
# inner x

# Summary
# LEGB Rule:
# Local: Names assigned in any way within a function (def or lambda), and not declared global in that function.
# Enclosing: Names in the local scope of any and all enclosing functions (def or lambda), from inner to outer.
# Global: Names assigned at the top-level of a module file, or declared global in a def within the file.
# Built-in: Names preassigned in the built-in names module: open, range, SyntaxError, etc.

# Conclusion
# In this tutorial, we learned about variable scoping in Python. We learned about the LEGB rule, which stands for Local, Enclosing, Global, and Built-in. We learned about the order in which Python looks for variables in different scopes. We also learned about the global and nonlocal keywords, which allow us to modify variables in different scopes. Finally, we learned about the built-in scope, which contains all the built-in functions in Python. I hope you found this tutorial helpful. Thanks for reading!

# Congratulations! You have completed the tutorial on variable scoping in Python.
