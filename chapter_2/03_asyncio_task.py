import asyncio
from utils import delay


async def print_and_sleep():
    asyncio.create_task(delay(1))
    asyncio.create_task(delay(2))
    asyncio.create_task(delay(3))
    asyncio.create_task(delay(4))
    asyncio.create_task(delay(5))
    asyncio.create_task(delay(6))
    asyncio.create_task(delay(7))
    asyncio.create_task(delay(8))
    asyncio.create_task(delay(9))
    asyncio.create_task(delay(10))


async def main():
    sleep_for_three = asyncio.create_task(delay(3))  # this is executed inmediately
    print(type(sleep_for_three))
    print("Up to this point, sleep_for_three hasn't been executed yet")
    asyncio.create_task(print_and_sleep())  # this is executed inmediately
    print("This code executes inmediately")
    result = await sleep_for_three  # prevents the next lines of code from executing but still allows for the event loop to run other asynchronous tasks
    print("This code is blocked until the task is completed")
    print(
        "You can notice that the async loop is running even though we haven't "
        "used an await for it yet"
    )
    print(f"Awaited result of asyncio task: {result}")
    await asyncio.create_task(
        delay(2)
    )  # once this finishes, the event loop will stop since we haven't awaited for the other tasks


# After the last delay task printing Sleeping for 2 seconds, you'll notice the
# other delay tasks will still awake, because the event loop is still running.


if __name__ == "__main__":
    asyncio.run(main())
