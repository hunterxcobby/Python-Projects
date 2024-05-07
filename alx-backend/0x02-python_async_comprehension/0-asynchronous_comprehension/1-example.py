import asyncio

# Define an asynchronous iterator function
async def aiter():
    for i in range(10):
        yield i

# # Define an asynchronous function
async def main():
    result = []
    async for i in aiter(): # even numbers
        if i % 2 == 0:
            result.append(i)
    print(result)

# Run the main async function
asyncio.run(main())


# using the async comprehension

async def main():
    result = [i async for i in aiter() if i % 2] # odd numbers
    print(result)

asyncio.run(main())