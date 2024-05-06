import asyncio

async def cook_pasta():
    await boil_water()
    # await add_pasta()
    # await simmer()

async def boil_water():
    print("Boiling water...")
    await asyncio.sleep(2)
    await add_pasta()
    await asyncio.sleep(2)
    print("Water boiled!")

async def add_pasta():
    print("Adding pasta...")
    await asyncio.sleep(2)
    await simmer()
    await asyncio.sleep(2)
    print("Pasta added!")

async def simmer():
    print("Simmering water...")
    await asyncio.sleep(3)
    print("Water simerred!")

async def main():
    await cook_pasta()

asyncio.run(main())
