import threading

def hello_from_thread():
    print(f"Hello from thread {threading.current_thread().name}")

hello_thread = threading.Thread(target=hello_from_thread)
hello_thread.start()

print(f"Python is running a total of {threading.active_count()} threads")
print(f"This print is running on thread {threading.current_thread().name}")

hello_thread.join()

print(f"Now there is only {threading.active_count()} thread, because second one joined the first")
