- We've learned how to create coroutines with the async keyword. Coroutines can
  suspend their execution on a blocking operation. This allows for other
  coroutines to run. Once the operation where the coroutine suspended completes,
  our coroutine will wake up and resume where it left off.
- We learned to use await in front of a call to a coroutine to run it and wait
  for it to return a value. To do so, the coroutine with the await inside it will
  suspend its execution, while waiting for a result. This allows other coroutines
  to run while the first coroutine is awaiting its result.
- We've learned how to use asyncio.run to execute a single coroutine. We can
  use this function to run the coroutine that is the main entry point into our
  application.
- We've learned how to use tasks to run multiple long-running operations
  concurrently. Tasks are wrappers around coroutines that will then be run on the
  event loop. When we create a task, it is scheduled to run on the event loop as
  soon as possible.
- We've learned how to cancel tasks if we want to stop them and how to add a
  timeout to a task to prevent them from taking forever. Canceling a task will
  make it raise a CancelledError while we await it. If we have time limits on how
  long a task should take, we can set timeouts on it by using asyncio.wait_for.
- We've learned to avoid common issues that newcomers make when using asyncio.
  The first is runnin CPU-bound code in coroutines. CPU-bound code will block the
  event loop from running other coroutines since we're still single-threaded. The
  second is blocking I/O, since we can't use normal libraries with asyncio, and
  you must use asyncio-specific ones that return coroutines. If your coroutine
  does not have an await in it, you should consider it suspicious. There are
  still ways to use CPU-bound and blocking I/O with asyncio, which we will
  address in chapters 6 and 7.
- We've learned how to use debug mode. Debug mode can help us diagnose common
  issues in asyncio code, such as running CPU-intensive code in a coroutine.
