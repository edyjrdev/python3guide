#!/usr/bin/env python

import asyncio
import aiohttp


def find_articles(queue):
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
        queue.put_nowait(article_name)


async def download(session, i, queue, html_dict):
    while True:
        article_name = await queue.get()
        url = f"https://en.wikipedia.org/wiki/{article_name}"
        async with session.get(url) as response:
            html_dict[article_name] = await response.text()
            print(f"Consumer {i} has downloaded {article_name}.")
        queue.task_done()


async def crawl():
    queue = asyncio.Queue()
    find_articles(queue)
    html_dict = {}
    async with aiohttp.ClientSession() as s:
        consumers = [asyncio.create_task(download(s, i, queue, html_dict)) for i in range(3)]
        await queue.join()
    for c in consumers:
        c.cancel()
    return html_dict


if __name__ == "__main__":
    html_dict = asyncio.run(crawl())
    for name, html in html_dict.items():
        with open(f"downloads/{name}.html", "w") as f_html:
            f_html.write(html)

