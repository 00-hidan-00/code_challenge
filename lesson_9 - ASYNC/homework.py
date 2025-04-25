import asyncio
import random

from faker import Faker


# 🧠 Домашнее задание: asyncio и асинхронное

# Задание 1: Простая асинхронная функция
# Напиши асинхронную функцию delayed_print(text, delay), которая будет печатать text после ожидания delay секунд.

# Задание 2: Несколько задач одновременно
# Используя asyncio.gather, запусти 3 вызова delayed_print() с разными текстами и задержками.
# Убедись, что они выполняются параллельно.

async def delayed_print(text: str, delay: int) -> None:
    await asyncio.sleep(delay)
    print(f"{text} after {delay} seconds")


# async def main():
#     tasks = [
#         asyncio.create_task(delayed_print('text', second))
#         for second in [random.randint(1, 5) for _ in range(5)]
#     ]
#
#     # await asyncio.wait(tasks)
#     await asyncio.gather(*tasks)


# Задание 3: Асинхронная загрузка
# Представь, что у тебя есть список URL-адресов. Напиши функцию fetch_url(url),
# которая имитирует асинхронную загрузку данных с помощью asyncio.sleep().
# Затем напиши функцию fetch_all(urls), которая будет параллельно загружать данные со всех URL.
# urls = [
#     "https://example.com/page1",
#     "https://example.com/page2",
#     "https://example.com/page3"
# ]

async def fetch_url(url: str) -> None:
    await asyncio.sleep(random.randint(1, 5))
    print(f'Имитирую загрузку данных с сервиса {url}')


async def fetch_all(urls: list[str]) -> None:
    tasks = [asyncio.create_task(fetch_url(url)) for url in urls]
    await asyncio.wait(tasks)


# async def main():
#     t1 = time.time()
#     urls = [
#         "https://example.com/page1",
#         "https://example.com/page2",
#         "https://example.com/page3"
#     ]
#     await fetch_all(urls)
#     t2 = time.time()
#     print(f"Загрузка завершена за {t2 - t1:.2f} секунд")


# Задание 4: Асинхронный генератор
# Создай асинхронный генератор async_counter(n), который каждую секунду выдает числа от 1 до n.

async def async_counter(n: int) -> int:
    for i in range(1, n + 1):
        await asyncio.sleep(1)
        yield i


# async def main():
#     async for number in async_counter(5):
#         print(number)


# 🧪 Домашнее задание #2: Продвинутая практика с asyncio

# Задание 1: Ограничение параллелизма (семафоры)
# У тебя есть 10 "запросов" (например, имитация скачивания с сайтов).
# Но ты хочешь, чтобы одновременно выполнялось не больше 3.
# Используй asyncio.Semaphore, чтобы ограничить количество одновременных задач.
# Для имитации работы используй asyncio.sleep() с рандомной задержкой.

async def download_files(semaphore: asyncio.Semaphore) -> None:
    async with semaphore:  # Ограничиваем параллелизм
        time_sleep = random.randint(1, 5)
        await asyncio.sleep(time_sleep)
        print(f'Файл скачен, время ожидания: {time_sleep} секунд')


# async def main():
#     tasks = [
#         asyncio.create_task(download_files(asyncio.Semaphore(3))) for i in range(10)
#     ]
#     await asyncio.wait(tasks)


# Задание 2: Таймауты
# Напиши функцию async def fetch_with_timeout(url, timeout), которая:
# Пытается "загрузить" данные с URL (опять же, имитация через asyncio.sleep()).
# Если загрузка занимает дольше timeout, выбрасывает исключение asyncio.TimeoutError.

# Задание 3: Обработка ошибок в асинхронных задачах
# У тебя есть список задач, некоторые из них могут завершиться с ошибкой.
# Запусти их через asyncio.gather(..., return_exceptions=True).
# Собери отдельно успешные результаты и ошибки.

async def fetch_with_timeout(url: str, timeout: int):
    if timeout > 5:
        raise asyncio.TimeoutError(f"Timeout on {url} after {timeout} seconds")
    await asyncio.sleep(timeout)
    return f'{url} | {timeout}'


# async def main():
#     data_dict = {i: {'url': 'url_' + str(i), 'timeout': random.randint(1, 10)} for i in range(5)}
#     tasks = [
#         asyncio.create_task(fetch_with_timeout(url=item[1]['url'], timeout=item[1]['timeout']))
#         for item in data_dict.items()
#     ]
#
#     results = await asyncio.gather(*tasks, return_exceptions=True)
#
#     for result in results:
#         if isinstance(result, Exception):
#             print(f'⚠️ Ошибка: {result}')
#         else:
#             print(f'✅ Результат: {result}')


# Задание 4: Асинхронная очередь (asyncio.Queue)
# Имплементируй простую модель "производитель-потребитель":
# Один producer кладёт элементы в очередь (asyncio.Queue) с задержками.
# Несколько consumer-ов (например, 2) читают из очереди и "обрабатывают" элементы (печатают + задержка).


async def producer(queue) -> str:
    fake = Faker()
    while True:  # Например, производим 10 элементов
        await asyncio.sleep(random.randint(1, 3))  # Задержка между добавлениями
        name = fake.name()  # Генерация случайного имени
        await queue.put(name)  # Добавление элемента в очередь
        print(f'Produced: {name}')


async def consumer(queue):
    while True:
        name = await queue.get()  # Получение элемента из очереди
        sleep_for = random.randint(1, 3)
        await asyncio.sleep(sleep_for)  # Задержка для обработки
        print(f'Consumed: {name} | has slept for {sleep_for} seconds')
        queue.task_done()  # Уведомление о завершении обработки


async def main():
    queue = asyncio.Queue(maxsize=5)  # Ограничиваем размер очереди

    # Создаем задачи для производителей и потребителей
    tasks = [
        asyncio.create_task(consumer(queue))
        for _ in range(2)  # 2 потребителя
    ]
    tasks.append(asyncio.create_task(producer(queue)))  # 1 производитель

    await asyncio.gather(*tasks)  # Запуск всех задач


if __name__ == "__main__":
    asyncio.run(main())
