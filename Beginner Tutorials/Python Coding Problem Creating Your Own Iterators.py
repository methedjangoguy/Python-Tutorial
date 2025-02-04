# Sentence class implements an iterator for processing sentences word by word
class Sentence:

    def __init__(self, sentence):
        # Store the original sentence and initialize word list
        self.words = sentence.split()
        self.index = 0

    def __iter__(self):
        # Return self as iterator
        return self

    def __next__(self):
        # Check if we've reached the end of words
        if self.index >= len(self.words):
            raise StopIteration
        # Get current word and increment index
        word = self.words[self.index]
        self.index += 1
        return word


# Generator function that yields words from a sentence
# More memory efficient than class-based iterator for simple use cases
def sentence(text):
    yield from text.split()


# Example usage
my_sentence = sentence("This is a test")

# Two ways to iterate:
# 1. Using for loop:
# for word in my_sentence:
#     print(word)

# 2. Using next() function:
try:
    print(next(my_sentence))  # This
    print(next(my_sentence))  # is
    print(next(my_sentence))  # a
    print(next(my_sentence))  # test
    print(next(my_sentence))  # Will raise StopIteration
except StopIteration:
    pass
