import asyncio
import requests

from python_concurrency.utils import async_timed


@async_timed
async def get_status_code() -> int:
    return requests.get("https://www.google.com").status_code


@async_timed
async def main() -> None:
    run_1 = asyncio.create_task(get_status_code())
    run_2 = asyncio.create_task(get_status_code())
    run_3 = asyncio.create_task(get_status_code())
    await run_1
    await run_2
    await run_3


if __name__ == "__main__":
    asyncio.run(main())

# You'll notice that we don't benefit from concurrency here.
# This is because the requests library is blocking the event loop on its calls.
# Many APIs / libraries are blocking by default, so you'll need to use either
# multiples threads or multiple processes to run them concurrently.
# Other option is to use async libraries like httpx or aiohttp.
