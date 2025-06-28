import asyncio

async def delay(delay_seconds: int) -> int:
    print(f"Sleeping for {delay_seconds} seconds...")
    await asyncio.sleep(delay_seconds)
    print(f"Awake after {delay_seconds} seconds")
    return delay_seconds
