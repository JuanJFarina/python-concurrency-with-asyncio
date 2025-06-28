- CPU-bound work is work that primarily utilizes our computer's processor 
whereas I/O-bound work primarily utilizes our network or other input/output 
devices. Asyncio primarily helps us make I/O-bound work concurrent, but it 
exposes APIs for making CPU-bound work concurrent as well.
- Processes and threads are the basic most units of concurrency at the 
operating system level. Processes can be used for I/O and CPU-bound workloads 
and threads can (usually) only be used to manage I/O-bound work effectively in 
Python due to the GIL preventing code from executing in parallel.
- We've seen how, with non-blocking sockets, instead of stopping our 
application wihle we wait for data to come in, we can instruct the operating 
system to tell us when data has come in. Exploiting this is part of what allows 
asyncio to achieve concurrency with only a single thread.
- We've introduced the event loop, which is the core of asyncio applications. 
The event loop loops forever, looking for tasks with CPU-bound work to run 
while also pausing tasks that are waiting for I/O.