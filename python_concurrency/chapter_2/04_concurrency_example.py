import asyncio
import time
from python_concurrency.utils import delay


async def hello_every_second():
    for _ in range(2):
        await asyncio.sleep(1)
        print("I'm running other code while I'm waiting!")


async def main():
    first_delay = asyncio.create_task(delay(3))  # non-blocking, starts inmediately
    second_delay = asyncio.create_task(delay(3))  # non-blocking, starts inmediately

    await hello_every_second()  # blocking, starts inmediately
    await first_delay  # blocking, after hello_every_second finishes it will wait for first_delay to finish
    await (
        second_delay
    )  # blocking, after first_delay finishes it will wait for second_delay to finish


if __name__ == "__main__":
    start_time = time.time()
    asyncio.run(main())
    end_time = time.time()
    print(f"Total execution time: {end_time - start_time:.2f} seconds")

# this code takes roughly 3 seconds to run because its concurrent, but would it 
# be synchronous/sequential, it would have taken roughly 8 seconds.