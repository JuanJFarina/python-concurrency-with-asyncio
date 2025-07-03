import functools
import time
from typing import Callable, Any


def async_timed(func: Callable[..., Any]) -> Callable[..., Any]:
    @functools.wraps(func)
    async def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"Starting function {func.__name__} with args {args} {kwargs}")
        start_time = time.time()
        try:
            result = await func(*args, **kwargs)
        finally:
            end_time = time.time()
            elapsed_time = end_time - start_time
            print(f"Finished function {func.__name__} in {elapsed_time:.4f} seconds")
        return result

    return wrapper
