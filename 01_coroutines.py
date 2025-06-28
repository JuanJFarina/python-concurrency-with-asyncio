def add_one(number: int) -> int:
    return number + 1

# using the async keyword allows us to define a coroutine, in a similar fashion 
# to a function
async def coroutine_add_one(number: int) -> int:
    return number + 1

result_one = add_one(1)
result_two = coroutine_add_one(1)

print(f"Function result is {result_one} and its type is {type(result_one)}")
print(f"Coroutine result is {result_two} and its type is {type(result_two)}")

# difference lies in that the coroutine does not execute inmediately and 
# instead returns a coroutine object, which can be executed later using an 
# event loop
