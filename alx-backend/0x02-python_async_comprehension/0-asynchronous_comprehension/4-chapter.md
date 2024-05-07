The proposal suggests allowing the use of `await` expressions within both asynchronous and synchronous comprehensions. Let's break down what this means and provide some explanations and examples:

1. **Using `await` in List Comprehensions:**
   - You can use `await` within a list comprehension to await the result of async functions.
   - Example:
     ```python
     result = [await fun() for fun in funcs]
     ```

2. **Using `await` in Set Comprehensions:**
   - Similarly, you can use `await` within a set comprehension.
   - Example:
     ```python
     result = {await fun() for fun in funcs}
     ```

3. **Using `await` in Dictionary Comprehensions:**
   - In dictionary comprehensions, you can use `await` both for the keys and the values.
   - Example:
     ```python
     result = {fun: await fun() for fun in funcs}
     ```

4. **Using `await` with Conditions in Comprehensions:**
   - You can use `await` in comprehensions with conditions.
   - Example:
     ```python
     result = [await fun() for fun in funcs if await smth]
     ```

5. **Using `await` with Asynchronous Iteration in Comprehensions:**
   - You can use `await` with asynchronous iteration (`async for`) in comprehensions.
   - Example:
     ```python
     result = [await fun() async for fun in funcs]
     ```

6. **Using `await` with Asynchronous Iteration and Conditions in Comprehensions:**
   - Similar to the previous point, you can combine `await` with asynchronous iteration and conditions.
   - Example:
     ```python
     result = [await fun() async for fun in funcs if await smth]
     ```

It's important to note that using `await` in comprehensions is only valid within an `async def` function body. This restriction ensures that the comprehension is executed within an asynchronous context, allowing the use of `await` expressions.

In summary, by allowing the use of `await` in comprehensions, developers can write concise and expressive code when dealing with asynchronous operations, making it easier to work with async functions and coroutines.