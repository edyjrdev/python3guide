#!/usr/bin/env python

import asyncio


async def sleep_print(n):
    print(f"I'll wait for {n} seconds ...")
    await asyncio.sleep(n)
    print(f"... I'm back (after {n} seconds)!")
    return n


async def program1():
    await sleep_print(5)
    await sleep_print(2)
    await sleep_print(1)


async def program2():
    task1 = asyncio.create_task(sleep_print(5))
    task2 = asyncio.create_task(sleep_print(2))
    task3 = asyncio.create_task(sleep_print(1))

    await task1
    await task2
    await task3


if __name__ == "__main__":
    print("Programm 1:")
    asyncio.run(program1())

    print("Programm 2:")
    asyncio.run(program2())
