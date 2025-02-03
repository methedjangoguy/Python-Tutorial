"""
# Intermediate's Python Tutorial 15: Decorators - Enhancing Functions

## Introduction
Decorators in Python are a powerful tool that allows you to modify the behavior of functions or methods without changing their actual code. They are widely used in logging, authentication, caching, and more.
"""


# 1. Basic Function Without a Decorator
def greet():
    return "Hello, World!"


print(greet())  # Output: Hello, World!

"""
## 2. Understanding Function Wrapping
A decorator is a function that takes another function as an argument, modifies it, and returns a new function.
"""


# 2.1 Creating a Simple Decorator
def uppercase_decorator(func):
    def wrapper():
        result = func()
        return result.upper()

    return wrapper


# Applying the decorator
@uppercase_decorator
def say_hello():
    return "hello, decorators!"


print(say_hello())  # Output: HELLO, DECORATORS!

"""
## 3. Using Decorators with Arguments
Decorators can also be used with functions that accept arguments.
"""


def repeat_decorator(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                func(*args, **kwargs)

        return wrapper

    return decorator


@repeat_decorator(3)
def greet_person(name):
    print(f"Hello, {name}!")


greet_person("Alice")  # Prints "Hello, Alice!" three times

"""
## 4. Using `functools.wraps` to Preserve Metadata
When using decorators, function metadata (like `__name__`, `__doc__`) is altered. Using `functools.wraps` helps preserve the original function metadata.
"""

import functools


def logging_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling function {func.__name__}")
        return func(*args, **kwargs)

    return wrapper


@logging_decorator
def add(a, b):
    """Adds two numbers."""
    return a + b


print(add(3, 5))  # Output: Calling function add \n 8
print(add.__name__)  # Output: add
print(add.__doc__)  # Output: Adds two numbers.

"""
## 5. Applying Multiple Decorators
Multiple decorators can be applied to a single function.
"""


@uppercase_decorator
@logging_decorator
def get_message():
    return "Decorators are powerful! enough said."


print(get_message())  # Output: Calling function get_message \n DECORATORS ARE POWERFUL! ENOUGH SAID.

"""
## Summary
- **Decorators** modify functions without changing their definitions.
- Use `@decorator_name` to apply a decorator.
- **Function wrapping** allows behavior modification.
- **Decorators with arguments** make them more flexible.
- Use `functools.wraps` to preserve function metadata.
- **Multiple decorators** can be stacked for layered functionality.

Decorators help in code reusability and improving readability. Start experimenting with them in your projects! 🚀
"""
