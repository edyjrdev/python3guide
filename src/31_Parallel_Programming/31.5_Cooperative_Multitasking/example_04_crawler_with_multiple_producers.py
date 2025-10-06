#!/usr/bin/env python

import asyncio
import aiohttp
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


async def download(session, i, queue, html_dict):
    while True:
        artikel_name = await queue.get()
        url = f"https://de.wikipedia.org/wiki/{artikel_name}"
        async with session.get(url) as response:
            html_dict[artikel_name] = await response.text()
            print(f"Konsument {i} hat {artikel_name} heruntergeladen.")
        queue.task_done()


async def crawl():
    queue = asyncio.Queue(maxsize=3)
    html_dict = {}
    producers = [
        asyncio.create_task(find_articles1(queue)),
        asyncio.create_task(find_articles2(queue))
    ]
    async with aiohttp.ClientSession() as s:
        consumers = [asyncio.create_task(download(s, i, queue, html_dict)) for i in range(3)]
        await asyncio.gather(*producers)
        await queue.join()
    for c in consumers:
        c.cancel()
    return html_dict


if __name__ == "__main__":
    html_dict = asyncio.run(crawl())
    for name, html in html_dict.items():
        with open(f"downloads/{name}.html", "w") as f_html:
            f_html.write(html)

