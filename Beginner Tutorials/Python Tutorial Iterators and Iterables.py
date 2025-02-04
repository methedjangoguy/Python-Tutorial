# MyRange class implements an iterator that generates numbers from start to end (exclusive)
class MyRange:

    # Initialize with start and end values
    def __init__(self, start, end):
        self.value = start
        self.end = end

    # Make this class iterable by returning self
    def __iter__(self):
        return self

    # Return next value in range or raise StopIteration when done
    def __next__(self):
        if self.value >= self.end:
            raise StopIteration
        current = self.value
        self.value += 1
        return current


# Generator function that yields an infinite sequence starting from given number
def my_range(start):
    current = start
    while True:
        yield current
        current += 1


# Create an infinite sequence starting from 1
nums = my_range(1)

# Print each number in the sequence (this will run forever)
for num in nums:
    print(num)
