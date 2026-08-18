import asyncio
import time


async def wait_random(num: int) -> str:
    await asyncio.sleep(num)
    return f"Задача корутина {num} завершилась через {num} секунд"


async def main() -> None:
    tasks = [asyncio.create_task(wait_random(n)) for n in range(4,0,-1)]
    # [4,3,2,1]
    for task in asyncio.as_completed(tasks):
        print(await task)


if __name__ == "__main__":
    start = time.perf_counter()
    asyncio.run(main())
    end = time.perf_counter()
    print(f'Время выполнение заняло: {end-start:.2f} c.')