import asyncio
import random
import time

async def wait_random(num: int) -> None:
    delay = random.randint(1, 5)
    await asyncio.sleep(delay)
    print(f"Задача корутина {num} завершилась через {delay} секунд")


async def main():
    coro1 = asyncio.create_task(wait_random(1))
    await asyncio.gather(wait_random(2),coro1,wait_random(3))


if __name__ == "__main__":
    start = time.perf_counter()
    asyncio.run(main())
    end = time.perf_counter()
    print(f'Время выполнение заняло: {end-start:.2f} c.')