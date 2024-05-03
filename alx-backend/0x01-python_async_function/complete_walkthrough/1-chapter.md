Alright, let's break down the concepts step by step:

1. **Concurrency and Parallelism**:
   - **Concurrency** means that multiple tasks can run partially overlapping with each other. It doesn't necessarily mean they are executed at the exact same time. 
   - **Parallelism**, on the other hand, involves performing multiple operations at the same time. It's about simultaneous execution of tasks.

2. **Threading**:
   - **Threading** is a way to achieve concurrency in programming. It involves multiple threads taking turns to execute tasks. One process can contain multiple threads.
   - Python's threading has some complexities due to the Global Interpreter Lock (GIL), which limits true parallelism.

3. **Multiprocessing**:
   - **Multiprocessing** is a means to achieve parallelism by spreading tasks across multiple CPUs or cores. It's well-suited for CPU-bound tasks that require a lot of computational power.

4. **IO-Bound vs. CPU-Bound**:
   - Tasks can be categorized as either **IO-bound** or **CPU-bound**.
   - **CPU-bound tasks** involve a lot of computational work, where the CPU is constantly working hard.
   - **IO-bound tasks**, on the other hand, involve a lot of waiting for input/output operations to complete, such as reading from a disk or network.

5. **Async IO**:
   - **Async IO** is a programming paradigm that focuses on handling IO-bound tasks efficiently.
   - It's a single-threaded, single-process design that uses cooperative multitasking, allowing multiple IO-bound tasks to run concurrently.
   - Python's `asyncio` package provides support for writing async IO code using the `async` and `await` keywords.
   - Async IO is not threading or multiprocessing; it's a distinct approach to concurrency.

6. **Asynchronous Programming**:
   - **Asynchronous routines** can "pause" while waiting for IO operations to complete, allowing other routines to run in the meantime.
   - Through this mechanism, asynchronous code facilitates concurrent execution, providing the look and feel of concurrency.

7. **Comparison and Summary**:
   - Async IO is a style of concurrent programming focused on handling IO-bound tasks efficiently.
   - It's not parallelism but rather a form of concurrency.
   - It's more closely aligned with threading than multiprocessing but is distinct from both.
   - Asynchronous programming enables efficient handling of IO-bound tasks by allowing tasks to pause and resume while waiting for IO operations.

Understanding these concepts will give you a solid foundation for working with async IO and concurrent programming in Python. If you have any specific questions or need further clarification on any of these points, feel free to ask!