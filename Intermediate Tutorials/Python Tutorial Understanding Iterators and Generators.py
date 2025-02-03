"""
Tutorial 16: Understanding Iterators and Generators

In this tutorial, we will explore iterators and generators in Python.
These concepts are essential for efficient looping, memory optimization, and handling large datasets.
"""


# 1. Understanding Iterators
class MyIterator:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self  # The iterator object itself

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration  # Stops iteration when end is reached
        value = self.current
        self.current += 1
        return value


# Using the custom iterator
print("Iterating using a custom iterator:")
my_iter = MyIterator(1, 5)
for num in my_iter:
    print(num)

# 2. Understanding Generators


def my_generator(start, end):
    """A generator function that yields values from start to end."""
    current = start
    while current < end:
        yield current
        current += 1


# Using the generator function
print("\nIterating using a generator:")
for num in my_generator(1, 5):
    print(num)

# 3. Generator Expressions
print("\nUsing a generator expression:")
gen_exp = (x * x for x in range(1, 6))  # Creates a generator
for value in gen_exp:
    print(value)

"""
Key Takeaways:
1. Iterators are objects that implement the __iter__() and __next__() methods.
2. Generators use the `yield` statement to produce values lazily, making them memory efficient.
3. Generator expressions provide a concise way to create generators.

Use cases:
- Generators are useful when dealing with large datasets (e.g., reading large files line by line).
- Iterators allow for custom looping behavior in classes.
"""
