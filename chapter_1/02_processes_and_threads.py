import os
import threading

# processes have dedicated memory space for each one
print("Python application is running on process:", os.getpid())

# threads share their parent process's memory space
print(f"Python is using a total of {threading.active_count()} threads")

# every process has at least one main thread, and may have multiple 'worker' or 
# 'background' threads
print("Current thread name is:", threading.current_thread().name)
