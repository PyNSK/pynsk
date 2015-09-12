Title: Извлечение информации: скачиваем список ссылок с помощью asyncio
Date: 2015-09-09 10:00
Tags: asyncio, aiohttp
Category: Извлечение информации

Порой возникают рутинные задачи, которые не хочется делать руками. Примером такой задачи может являться - скачать множество страниц по ссылкам. Если 5 ссылок еще вручную сохранить можно, а если их 1000? или 6250, как было в моем случае. 

На Python эту задачу можно с помощью модуля asyncio и aiohttp. 

Вот такой код можно написать за пару минут:


```python
import asyncio
import aiohttp

@asyncio.coroutine
def download(url):
    try:
        response = yield from aiohttp.request('GET', url)
        data = yield from response.text()
        yield from save_page(url, data) # сохраняем страницу в файл, или еще куда
    except Exception as e:
        return None

@asyncio.coroutine
def download_parallel(urls):
    tasks = [asyncio.Task(download(url)) for url in urls]
    yield from asyncio.gather(*tasks)

urls = [<список ссылок>] # список ссылок

loop = asyncio.get_event_loop()
loop.run_until_complete(download_parallel(urls))

```