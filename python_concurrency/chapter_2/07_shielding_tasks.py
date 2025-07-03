import asyncio
from python_concurrency.utils import delay


async def main():
    long_task = asyncio.create_task(delay(3))
    try:
        result = await asyncio.wait_for(asyncio.shield(long_task), timeout=1)
        print(result)
    except asyncio.exceptions.TimeoutError:  # wait_for() raises a TimeoutError
        print("The task is taking too long")
        print(f"Has the task been cancelled ? {long_task.cancelled()}")
        result = await long_task
        print(f"After awaiting enough time, this is the result: {result}")


if __name__ == "__main__":
    asyncio.run(main())

# asyncio.shield() protects the task from cancellation requests
