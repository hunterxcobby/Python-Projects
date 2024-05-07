To use async comprehensions in Python, follow these steps:

1. **Define an Async Comprehension Expression**:
   - Use the `[expression async for target in iterable if condition]` syntax to define an async comprehension.
   - Replace `expression` with the expression to be evaluated for each item.
   - Replace `target` with the variable to store each item in the iterable.
   - Replace `iterable` with the iterable (e.g., list, set, or generator) you want to iterate over.
   - Optionally, include a `if condition` clause to filter items.

2. **Place the Async Comprehension in an Async Function**:
   - Async comprehensions must be used within an async function or coroutine.
   - Define an async function using the `async def` syntax.

3. **Await the Results of the Async Comprehension**:
   - If you want to await the results of the async comprehension, use the `await` keyword.

Here's an example to illustrate how to use async comprehensions:

```python
import asyncio

# Define an async function to demonstrate async comprehension
async def async_comprehension_example():
    # Define an async generator function
    async def async_counter(limit):
        for i in range(limit):
            # Simulate an asynchronous operation using asyncio.sleep
            await asyncio.sleep(1)
            # Yield the current value asynchronously
            yield i

    # Use async comprehension to create a list of squared values
    squared_values = [i * i async for i in async_counter(5)]
    print(squared_values)  # Output: [0, 1, 4, 9, 16]

# Run the async function
async def main():
    await async_comprehension_example()

# Run the event loop
if __name__ == "__main__":
    asyncio.run(main())
```

In this example:
- `async_comprehension_example` is an async function that demonstrates the usage of async comprehensions.
- Inside this function, an async generator function `async_counter` is defined to generate values asynchronously.
- An async comprehension `[i * i async for i in async_counter(5)]` is used to create a list of squared values asynchronously.
- The `await` keyword is used to wait for the completion of the async comprehension.
- The event loop is run using `asyncio.run(main())`.

By following these steps, you can effectively use async comprehensions in your Python code to perform asynchronous operations and construct collections asynchronously.