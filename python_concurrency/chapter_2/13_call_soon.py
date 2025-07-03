import asyncio
from python_concurrency.utils import delay


def call_later() -> None:
    print("This is called on the next iteration, after starting delay")


async def main() -> None:
    loop = asyncio.get_running_loop()  # throws an exception if no loop is
    # running, instead of get_event_loop() which may create one
    loop.call_soon(call_later)  # will be called on the next iteration
    await delay(1)  # will be started inmediately, but not blocking the loop


asyncio.run(main())
