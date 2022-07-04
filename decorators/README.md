# Decorators
---
## Index

- Introduction
- Sintax
    - Inner Function
    - Simple decorator
    - Syntactic Sugar
- Source
---
## Introduction

By definition, a decorator is a function that takes another function and extends the behavior of the latter function without explicitly modifying it.

The decorators in Python are extremly used because you can divide the functionality of the core logic of your code.

For example, if you create a function to save the age of some user, you can create a decorator to validate if the age is in a valid format, something like:

```python
@validate_age
def save_age_in_some_database(age: int):
    db_handler = SomeDBHandler()
    db_handler.save_age(age)
```

In this case, we are splitting two different functionalities, the first one is saving the age to the database and the other is validating the age. It's important to say that the validate_age decorator could be used in different scenarios with other functions.

---
## Sintax

### Inner functions

In Python, you can declare a function inside another function. For example:

```python
def print_inner_function():
    def print_inner():
        print("Inner Function")
    print_inner()

# Result -> Inner Function
```

### Simple decorator

This is the sintax for a simple decorator

```python
def my_decorator(func):
    def wrapper(func):
        print("Something is happening before the main function")
        func()
        print("Something is happening after the main function")
    return wrapper
```

### Syntactic Sugar
Python allow us to use decorators in a simpler way with the "@" symbol, sometimes called the "pie" syntax.

So, we can use our decorator function as:

```python
@my_decorator
def some_function():
    print("Hello Decorators")
```

See the examples folder from more information

## Run Unit Tests

Run `pytest` from decorators folder (the current directory)

---
## Source
- https://realpython.com/primer-on-python-decorators/
