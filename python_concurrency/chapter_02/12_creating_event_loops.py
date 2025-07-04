import asyncio


async def main() -> None:
    await asyncio.sleep(1)


event_loop = asyncio.get_event_loop()
try:
    event_loop.run_until_complete(main())  # this does not cancel any tasks and
    # we need to close the loop and clean up resources
finally:
    event_loop.close()
