# Intermediate's Python Tutorial 14: Debugging Techniques

## Introduction

Debugging is an essential skill for any Python developer. It helps in identifying and fixing issues in the code efficiently. This tutorial will cover various debugging techniques, from simple `print()` statements to advanced debugging tools like `pdb` and logging.

---

## 1. Using `print()` for Debugging

One of the simplest debugging methods is using `print()` statements to check variable values and program flow.

### Example

```python
def add_numbers(a, b):
    print(f"Adding {a} and {b}")  # Debugging statement
    return a + b

result = add_numbers(5, 10)
print(f"Result: {result}")
```

**Pros:**

- Easy to implement
- Works in all environments

**Cons:**

- Can clutter the code
- Needs manual removal after debugging

---

## 2. Using Python's Built-in `pdb` Module

Python Debugger (`pdb`) allows you to step through the code and inspect variables interactively.

### Example

```python
import pdb

def divide(a, b):
    pdb.set_trace()  # Breakpoint
    return a / b

result = divide(10, 2)
print(result)
```

### Key Commands in `pdb`

- `n` (next): Execute the next line.
- `s` (step): Step into a function.
- `c` (continue): Continue execution until the next breakpoint.
- `q` (quit): Exit the debugger.

---

## 3. Using Logging for Better Debugging

Unlike `print()`, logging provides more control over message levels (INFO, DEBUG, ERROR, etc.).

### Example

```python
import logging

logging.basicConfig(level=logging.DEBUG, format='%(levelname)s: %(message)s')

def multiply(a, b):
    logging.debug(f"Multiplying {a} and {b}")
    return a * b

result = multiply(3, 4)
logging.info(f"Result: {result}")
```

**Advantages:**

- Different log levels (DEBUG, INFO, WARNING, ERROR, CRITICAL)
- Can be written to files for later analysis

---

## 4. Debugging with IDEs (PyCharm, VS Code)

Most modern IDEs come with built-in debugging tools that support:

- Breakpoints
- Step-by-step execution
- Variable inspection

To debug in **VS Code**:

1. Open your Python file.
2. Click on **Run > Start Debugging** (or press `F5`).
3. Set breakpoints by clicking beside line numbers.

---

## 5. Handling Exceptions with `try-except`

Using `try-except` blocks helps in handling runtime errors gracefully.

### Example

```python
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        print(f"Error: {e}")
        return None

print(safe_divide(10, 0))
```

---

## Summary

| Technique  | Pros | Cons |
|------------|------|------|
| `print()`  | Simple, quick | Not scalable |
| `pdb`      | Interactive debugging | Slower for large programs |
| `logging`  | Organized, scalable | Slightly complex setup |
| IDE Debugger | Visual & user-friendly | Requires IDE setup |
| `try-except` | Prevents crashes | Doesn’t fix the bug |

Mastering these debugging techniques will significantly improve your problem-solving skills in Python. Happy coding! 🚀
