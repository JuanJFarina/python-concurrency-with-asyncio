import asyncio


async def cpu_bound_work() -> int:
    counter = 0
    for i in range(1_000_000):
        counter += i
    return counter


async def main():
    loop = asyncio.get_event_loop()
    loop.slow_callback_duration = 0.020  # by default this is 0.1 seconds
    long_task = asyncio.create_task(cpu_bound_work())
    await long_task


if __name__ == "__main__":
    asyncio.run(main(), debug=True)
