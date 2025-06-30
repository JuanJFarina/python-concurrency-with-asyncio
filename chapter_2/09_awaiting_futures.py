import asyncio
from asyncio import Future


def make_request():  # this simulates a web request that would return a Future object
    future = Future()
    asyncio.create_task(set_future_value(future))
    return future


async def set_future_value(future: Future):
    await asyncio.sleep(1)
    future.set_result(42)


async def main():
    future = make_request()
    print(f"Is the future done? {future.done()}")
    value = await future  # we can use await on this object
    print(f"Is the future done? {future.done()}")
    print(value)


if __name__ == "__main__":
    asyncio.run(main())
