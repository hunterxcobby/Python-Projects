Let's delve into async IO:

1. **Async/await Syntax**:
   - The `async def` keyword introduces a coroutine, allowing suspension with `await`.
   - `await` relinquishes control to the event loop until the awaited operation completes.

```python
async def g():
    r = await f()  # Suspends execution of g() until f() completes
    return r
```

2. **Coroutines and async Functions**:
   - Functions declared with `async def` are coroutines, capable of using `await`, `return`, or `yield` (in async generators).
   - Coroutines must be awaited to fetch their results.

```python
async def f(x):
    y = await z(x)  # OK - `await` and `return` allowed in coroutines
    return y

async def m(x):
    yield from gen(x)  # No - SyntaxError
```

3. **Usage Rules**:
   - `await` and `return` transform a function into a coroutine, requiring it to be awaited.
   - Using `await` outside a coroutine or `yield from` inside an async def raises SyntaxError.

```python
def m(x):
    y = await z(x)  # SyntaxError (no `async def` here)
    return y
```

4. **Async/await Decorator**:
   - Prior to Python 3.5, `@asyncio.coroutine` decorated coroutines to mark them.
   - Prefer native coroutines (`async def`) over generator-based coroutines for clarity.

```python
@asyncio.coroutine
def py34_coro():
    yield from stuff()

async def py35_coro():
    await stuff()
```

5. **Example Program**:
   - Demonstrates async IO's reduction of wait time by concurrently executing coroutines.

```python
import asyncio
import random

async def makerandom(idx: int, threshold: int = 6) -> int:
    print(f"Initiated makerandom({idx}).")
    i = random.randint(0, 10)
    while i <= threshold:
        print(f"makerandom({idx}) == {i} too low; retrying.")
        await asyncio.sleep(idx + 1)
        i = random.randint(0, 10)
    print(f"--> Finished: makerandom({idx}) == {i}")
    return i

async def main():
    res = await asyncio.gather(*(makerandom(i, 10 - i - 1) for i in range(3)))
    return res

if __name__ == "__main__":
    random.seed(444)
    r1, r2, r3 = asyncio.run(main())
    print(f"r1: {r1}, r2: {r2}, r3: {r3}")
```

Understanding async/await syntax and its application is pivotal for proficient asynchronous programming in Python.