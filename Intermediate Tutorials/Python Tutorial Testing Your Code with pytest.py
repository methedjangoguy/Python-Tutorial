"""
Intermediate's Python Tutorial 13: Testing Your Code with pytest

Pytest is a popular testing framework for Python that makes it easy to write simple and scalable test cases.
This tutorial covers the basics of using pytest to test your code effectively.
"""

# Step 1: Install pytest
# To install pytest, run the following command in your terminal or command prompt:
# pip install pytest

# Step 2: Writing Your First Test
# Pytest identifies test files by looking for files that start with 'test_' or end with '_test.py'


def add(a, b):
    """A simple function to add two numbers"""
    return a + b


def test_add():
    """Test function for add()"""
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0


# Step 3: Running Tests
# Save this file as test_example.py and run the following command:
# pytest test_example.py

# Step 4: Using pytest Fixtures
import pytest


@pytest.fixture
def sample_data():
    """Provides sample data for testing"""
    return {"a": 10, "b": 5}


def test_add_with_fixture(sample_data):
    """Test using fixture"""
    assert add(sample_data["a"], sample_data["b"]) == 15


# Step 5: Running Tests with Detailed Output
# Run tests with verbose output using:
# pytest -v test_example.py

# Step 6: Running a Specific Test Function
# Run a specific test function using:
# pytest -k "test_add"


# Step 7: Handling Expected Failures
@pytest.mark.xfail
def test_fail_example():
    """An expected failing test"""
    assert add(2, 2) == 5  # This test is expected to fail


# Step 8: Measuring Code Coverage
# Install coverage tool: pip install pytest-cov
# Run tests with coverage: pytest --cov=test_example.py

"""
Conclusion:
Pytest is a powerful testing framework that makes testing easier and more effective.
By using fixtures, assertions, and markers, you can write better tests and ensure code quality.
Happy testing! 🚀
"""
