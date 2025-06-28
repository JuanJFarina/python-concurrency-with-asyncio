import threading
import requests
import time

def read_example():
    response = requests.get("https://www.google.com")
    print(response.status_code)

point_one = time.time()

read_example()
read_example()

point_two = time.time()

thread_one = threading.Thread(target=read_example)
thread_two = threading.Thread(target=read_example)

thread_one.start()
thread_two.start()

thread_one.join()
thread_two.join()

point_three = time.time()

print(f"Single threaded execution: {point_two - point_one}")
print(f"Multi threaded execution: {point_three - point_two}")

# Python's Global Interpreter Lock (GIL) makes sure only one line of python code runs at 
# a time inside a given process, making parallelism impossible for one given process. 
# The reason for this is to prevent race conditions when python code make changes in the 
# reference counter of the interpreter, meaning every time a reference to an object is 
# created or removed. The need for all of this is because the internal CPython 
# implementation is not thread-safe.

# While GIL prevents gaining benefits from multithreading in most CPU-bound operations, 
# it does allow for multithreading in I/O-bound operations, which are not directly 
# managed by the GIL because they do not access python objects, and thus benefit from 
# multiple threads.
