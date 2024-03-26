import time
from typing import Callable

def measure_time(fn: Callable):

    def wrapper(*args, **kwargs):
        start_time = time.time()
        procers = fn(*args, **kwargs)
        end_time = time.time()
        duration = end_time - start_time
        print(f"Function {fn.__name__} took {duration:.6f} seconds to execute.")
        return procers

    return wrapper


@measure_time
def example_function(nr: int):
    for i in range(nr):
        i = i ** 2

@measure_time
def next_function(a: int, b: int, c: int):
    return a+b+c

example_function(nr=1000)

print(example_function(nr=100000))

result = next_function(10, 15, c=20)
print(result)