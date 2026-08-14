import asyncio

async def count():
    print("one")
    await asyncio.sleep(1)
    print("two")
    await asyncio.sleep(1)

async def main():
    await asyncio.gather(count(), count(), count())

if __name__ == "__main__":
    import time
    start = time.perf_counter()
    asyncio.run(main())
    print(f'Time taken to complete task: (asyncio) - {(time.perf_counter() - start):.04f} seconds')
