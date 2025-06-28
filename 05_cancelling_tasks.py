import asyncio
from utils import delay


async def main():
    long_task = asyncio.create_task(delay(10))
    print(long_task)  # at this point, the task has a pending status
    seconds_elapsed = 0

    while not long_task.done():
        print("Waiting for a second...")
        await asyncio.sleep(1)  # blocking
        seconds_elapsed += 1
        if seconds_elapsed >= 5:
            long_task.cancel()

    print(long_task)  # at this point, the task has a cancelled status
    try:
        await long_task  # CancelledError is only thrown at an await statement
    except asyncio.CancelledError:
        print("Task was cancelled after 5 seconds.")


if __name__ == "__main__":
    asyncio.run(main())
