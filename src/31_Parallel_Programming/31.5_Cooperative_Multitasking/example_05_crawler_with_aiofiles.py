#!/usr/bin/env python

import asyncio
import aiohttp
import aiofiles
import random


async def find_articles1(queue):
    articles = [
        "George_Washington",
        "John_Adams",
        "Thomas_Jefferson",
        "James_Madison",
        "James_Monroe",
        "John_Quincy_Adams",
        "Andrew_Jackson",
        "Martin_Van_Buren",
        "William_Henry_Harrison"
    ]
    for article_name in articles:
        await queue.put(article_name)
        await asyncio.sleep(random.random())


async def find_articles2(queue):
    articles = [
        "Hubert_Humphrey",
        "Spiro_Agnew",
        "Gerald_Ford",
        "Nelson_Rockefeller",
        "Walter_Mondale",
        "George_H._W._Bush",
        "Dan_Quayle",
        "Al_Gore",
    ]
    for article_name in articles:
        await queue.put(article_name)
        await asyncio.sleep(random.random())


async def download(session, i, queue):
    while True:
        article = await queue.get()
        url = f"https://en.wikipedia.org/wiki/{article}"
        async with session.get(url) as response:
            async with aiofiles.open(f"downloads/{article}.html", "w") as f:
                await f.write(await response.text())
                print(f"Consumer {i} has downloaded {article}.")
        queue.task_done()


async def crawl():
    queue = asyncio.Queue(maxsize=3)
    producers = [
        asyncio.create_task(find_articles1(queue)),
        asyncio.create_task(find_articles2(queue))
    ]
    async with aiohttp.ClientSession() as session:
        consumers = [asyncio.create_task(download(session, i, queue)) for i in range(3)]
        await asyncio.gather(*producers)
        await queue.join()
    for c in consumers:
        c.cancel()


if __name__ == "__main__":
    asyncio.run(crawl())
