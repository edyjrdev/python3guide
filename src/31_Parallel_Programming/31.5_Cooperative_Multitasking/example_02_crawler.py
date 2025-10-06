#!/usr/bin/env python

import asyncio
import aiohttp


async def crawl(articles):
    async with aiohttp.ClientSession() as session:
        coroutines = [download(session, art) for art in articles]
        return await asyncio.gather(*coroutines)


async def download(session, article_name):
    url = f"https://en.wikipedia.org/wiki/{article_name}"
    async with session.get(url) as response:
        html = await response.text()
        print(f"I have downloaded {article_name}.")
        return html


if __name__ == "__main__":
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
    htmls = asyncio.run(crawl(articles))
    for article_name, html in zip(articles, htmls):
        with open(f"downloads/{article_name}.html", "w") as f_html:
            f_html.write(html)

