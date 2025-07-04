from asyncio import Future

new_future = Future()

print(new_future)

print(f"Is my future done ? {new_future.done()}")

new_future.set_result(42)

print(f"Is my future done ? {new_future.done()}")

print(new_future.result())
