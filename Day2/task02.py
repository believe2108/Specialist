import asyncio
import time
from typing import List

async def get_str(num: int) -> str:
    await asyncio.sleep(1)
    return f'Я - корутин {num}'


async def main() -> List[str]:
    tasks = [asyncio.create_task(get_str(n)) for n in range(4)]
    return [await task for task in tasks]


if __name__ == "__main__":
    start = time.perf_counter()
    results = asyncio.run(main())
    end = time.perf_counter()
    print('Результат:')
    for result in results:
        print(result)
    print(f'Время выполнение заняло: {end-start:.2f} c.')