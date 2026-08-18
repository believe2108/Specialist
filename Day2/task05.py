import asyncio
import time


async def wait_for() -> None:
    print(f"Моя задача ждать 5 секунд")
    await asyncio.sleep(5)


async def main() -> None:
    task = asyncio.create_task(wait_for())
    await asyncio.sleep(2)
    task.cancel()
    print('Отменил через 2 секунды')
    while not task.cancelled():
        print('Задача еще не отменена. Жду секунду')
        await asyncio.sleep(1)
    print(f'Задача отменена')
    # try:
    #     await task
    # except asyncio.CancelledError:
    #     print('Задание было отменено')


if __name__ == "__main__":
    start = time.perf_counter()
    asyncio.run(main())
    end = time.perf_counter()
    print(f'Время выполнение заняло: {end-start:.2f} c.')