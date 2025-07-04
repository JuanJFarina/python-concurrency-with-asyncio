import asyncio
import signal
from asyncio import AbstractEventLoop
from python_concurrency.utils.delay import delay


def cancel_tasks():
    print("Got a SIGINT")
    tasks: set[asyncio.Task] = asyncio.all_tasks()
    print(f"Cancelling {len(tasks)} tasks")
    [task.cancel() for task in tasks]


async def main():
    loop: AbstractEventLoop = asyncio.get_running_loop()
    # loop.add_signal_handler(signal.SIGINT, cancel_tasks)  # this only works in Unix-based systems
    await delay(10)


### Ootional work to make a similar behavior in Windows


class GracefulExit(SystemExit):
    code = 1


def raise_graceful_exit(*args):
    loop = asyncio.get_event_loop()
    print("Got a SIGINT or SIGTERM")
    loop.stop()
    raise GracefulExit("Exiting gracefully")


signal.signal(signal.SIGINT, raise_graceful_exit)  # this works in Windows
signal.signal(signal.SIGTERM, raise_graceful_exit)  # this works in Windows

###

asyncio.run(main())
