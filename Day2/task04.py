import random
import asyncio
import time


async def get_wait_random(num) -> int:
    sleep_time = random.randint(1,5)
    await asyncio.sleep(sleep_time)
    result = random.randint(1,10)
    print(f'Корутин {num} спал - {sleep_time} c., вернул {result}')
    return result


async def main(n: int) -> int:
    return sum(await asyncio.gather(*[get_wait_random(_) for _ in range(n)]))

if __name__ == "__main__":
    start = time.perf_counter()
    result = asyncio.run(main(5))
    end = time.perf_counter()
    print(f'Результат: {result}')
    print(f'Время выполнения заняло: {end-start:.2f} c.')