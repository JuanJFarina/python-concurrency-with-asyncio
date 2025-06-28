import asyncio

async def add_one(number: int) -> int:
    return number + 1

async def hello_world() -> str:
    await asyncio.sleep(1)
    return "Hello, World!"

async def main() -> None:
    message = await hello_world()
    one_plus_one = await add_one(1)
    print(one_plus_one)
    print(message)

if __name__ == "__main__":
    asyncio.run(main())

# For running coroutines, you can use the await keyword. Await behaves in a 
# blocking manner, meaning it will wait for the coroutine to finish.
# In this example, code is still executing sequentially.