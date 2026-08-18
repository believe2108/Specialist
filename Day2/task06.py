import time
import aiohttp
import asyncio


async def get_response(session:aiohttp.ClientSession, url:str) -> str:
    response = await session.get(url)
    return f'{url} - Status:{response.status}'


async def main(urls) -> None:
    async with aiohttp.ClientSession() as session:
        tasks = [asyncio.create_task(get_response(session, url)) for url in urls]
        for task in asyncio.as_completed(tasks):
            print(await task)
            for other_task in tasks:
                if not other_task.done():
                    other_task.cancel()
            break


if __name__ == '__main__':
    urls = ["https://www.yandex.com", "https://www.google.com", "https://www.python.org"]
    start = time.perf_counter()
    asyncio.run(main(urls))
    end = time.perf_counter()
    print(f'Время выполнения заняло: {end-start:.2f} c.')

