To type-annotate generators in Python, you can use the `Generator` type from the `typing` module. Here's how to do it:

1. **Import the `Generator` Type**: 
   Import the `Generator` type from the `typing` module.

2. **Annotate the Generator Function**:
   Annotate the generator function's return type using `Generator[YieldType, SendType, ReturnType]` syntax, where:
   - `YieldType`: Type of values yielded by the generator.
   - `SendType`: Type of values that can be sent into the generator using the `send()` method (optional).
   - `ReturnType`: Type of the value returned by the generator when it exits (optional).

Here's an example to demonstrate how to type-annotate a generator function:

```python
from typing import Generator

# Define a generator function with type annotations
def count_up(start: int, end: int, step: int) -> Generator[int, None, None]:
    current = start
    while current <= end:
        yield current
        current += step

# Use the generator function
counter = count_up(1, 10, 2)
for num in counter:
    print(num)
```

In this example:
- The `count_up` function is a generator function that yields integers from `start` to `end` with a specified `step`.
- It is type-annotated to indicate that it yields `int` values (`Generator[int, None, None]`).
- The `None` values indicate that the generator does not accept values sent into it (`SendType`) and does not return any value when it exits (`ReturnType`).

By type-annotating generators, you can provide clarity about the types of values produced by the generator and improve code readability and maintainability.