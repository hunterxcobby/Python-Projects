async for and async generators, along with asynchronous comprehensions, extend Python's capabilities in managing asynchronous code. async for allows iteration over asynchronous iterators, while async generators enable the use of both await and yield within the same coroutine function body.

```python
async def mygen(u: int = 10):
    """Yield powers of 2."""
    i = 0
    while i < u:
        yield 2 ** i
        i += 1
        await asyncio.sleep(0.1)

async def main():
    # This does *not* introduce concurrent execution
    # It is meant to show syntax only
    g = [i async for i in mygen()]
    f = [j async for j in mygen() if not (j // 3 % 5)]
    return g, f

g, f = asyncio.run(main())
print(g)
print(f)
```

It's important to note that async iterators and generators don't introduce concurrency; they allow the enclosing coroutine to yield control to the event loop while waiting for asynchronous operations to complete.

The event loop in asyncio is responsible for managing coroutines, scheduling their execution, and handling their results. asyncio.run() simplifies event loop management by handling the setup, execution, and closing of the event loop automatically. However, for more fine-tuned control, you can use get_event_loop() to manually manage the event loop.

```python
loop = asyncio.get_event_loop()
try:
    loop.run_until_complete(main())
finally:
    loop.close()
```

Understanding the mechanics of the event loop is crucial for effective asyncio programming. Coroutines must be tied to the event loop to execute, and by default, asyncio runs in a single-threaded event loop on a single CPU core. However, asyncio supports pluggable event loops, allowing for custom implementations if needed.