"""
What is decorators: A decorators are special function which add special behavior to the
existing function.

It wrap one function into another to give extra functionality
"""

# Simple Decorator
# def create_wrapper(func):
#     def wrapper():
#         print("This is in wrapper upper")
#         func()
#         print("This is in wrapper lower")
#     return wrapper
#
# @create_wrapper
# def my_function():
#     print("I'm inside my function")
#
# my_function()


# Decorator with arguments
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("There should be value goes")
        result = func(*args, **kwargs)
        print("Can you try something else")
        return result

    return wrapper


def my_function(name):
    print(f"My name is : {name}")


some_instance = my_decorator(my_function())
