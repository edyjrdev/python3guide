#!/usr/bin/env python

import asyncio
import random


async def async_range(n):
    for i in range(n):
        await asyncio.sleep(random.random())
        yield i


async def coroutine(name, n):
    async for i in async_range(n):
        print(f"Current element of {name}: {i}")


async def main():
    await asyncio.gather(
        coroutine("Iterator 1", 10),
        coroutine("Iterator 2", 10)
    )


if __name__ == "__main__":
    asyncio.run(main())
