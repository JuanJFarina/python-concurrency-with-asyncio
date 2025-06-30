import asyncio
from utils import delay


async def main():
    long_task = asyncio.create_task(delay(10))
    try:
        result = await asyncio.wait_for(long_task, timeout=2)
        print(result)
    except asyncio.exceptions.TimeoutError:  # wait_for() raises a TimeoutError
        print("The task timed out !")
        print(f"Has the task been cancelled ? {long_task.cancelled()}")

if __name__ == "__main__":
    asyncio.run(main())

# asyncio.wait_for() automatically cancells a task if it takes longer than the specified 
# timeout.
