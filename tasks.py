# 1. 
# Write a decorator that should check if all arguments passed to the method are positive.
# If not, it should raise a ValueError. A function should calculate square of numbers.

# from typing import Callable

# def positive(fn: Callable):

#     def wrapper(*args, **kwargs):
#         for x in args:
#             if x < 0:
#                 raise ValueError("Only positives, sorry")
#         my_func = fn(*args, **kwargs)
#         return my_func

#     return wrapper


# @positive
# def square(number: int) -> int:
#     return pow(number, 2)

# print(square(4))


# 2.
# Write a decorator that catches any exceptions thrown by the function and 
# prints an error message instead of letting the program crash.

# from typing import Callable

# def error_hunter(fn: Callable):

#     def wrapper(*args, **kwargs):
#         try:
#             result = fn(*args, **kwargs)
#             return result
#         except Exception as err:
#             print(f"Error: {err}")

#     return wrapper


# @error_hunter
# def divide_by_zero(number: int):
#     return number / 0


# print(divide_by_zero(4))


# 3.
# Write a decorato that retries a function if it raises an exception. 
# The function should be retried 3 times before finally raising the exception.


# Bart
# def retry(tries=3):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             for attempt in range(tries):
#                 try:
#                     return func(*args, **kwargs)
#                 except Exception as e:
#                     print(f"Attempt {attempt+1}/{tries} failed: {e}")
#                     if attempt == tries - 1:
#                         raise  # Re-raise the exception on the last attempt
#             # Should never reach here
#         return wrapper
#     return decorator

# @retry(5)
# def my_function():
#     # Code that might raise an exception
#     raise RuntimeError("Something went wrong!")

# # Example usage
# try:
#     my_function()
# except Exception as e:
#     print(f"Failed after all retries: {e}")

# 3. Write a decorator that retries a function if it raises an exception. The function should be retried 3 times before finally raising the exception.

# Albertas
# from typing import Callable

# def error_hunter(fn: Callable):

#     def wrapper(*args, **kwargs):
#         counter = 0
#         for _ in range(3):
#             try:
#                 result = fn(*args, **kwargs)
#                 return result
#             except Exception:
#                 pass
#             counter += 1
#             print(counter)
#         return fn(*args, **kwargs)

#     return wrapper


# @error_hunter
# def divide_by_zero(number: int):
#     return number / 0

# print(divide_by_zero(4))
