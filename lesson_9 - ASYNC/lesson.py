# Lesson notes:
# https://darkened-currency-983.notion.site/d62a1606afdf4f2488225bb035258dfa


import asyncio
import random
import time

from web3 import AsyncWeb3


# Знакомство с сопрограммами

async def my_coroutine() -> None:
    print('Hello world!')


async def coroutine_add_one_example_1(number: int) -> int:
    return number + 1


def add_one_example_1(number: int) -> int:
    return number + 1


# function_result = add_one_example_1(1)
# coroutine_result = coroutine_add_one_example_1(1)
#
# print(f'Результат функции равен {function_result}, а его тип равен {type(function_result)}')
# print(f'Результат сопрограммы равен {coroutine_result}, а его тип равен {type(coroutine_result)}')


# ----------------------------------------------------------------------------------------------------------------------

async def coroutine_add_one_example_2(number: int) -> int:
    return number + 1


# result = asyncio.run(coroutine_add_one_example_2(1))
# print(result)  # 2


# ----------------------------------------------------------------------------------------------------------------------


async def add_one_example_2(number: int) -> int:
    return number + 1


async def main_example_1() -> None:
    one_plus_one = await add_one_example_2(1)  # Приостановиться и ждать результата add_one(1)
    two_plus_one = await add_one_example_2(2)  # Приостановиться и ждать результата add_one(2)
    print(one_plus_one)
    print(two_plus_one)


# asyncio.run(main_example_1())


# ----------------------------------------------------------------------------------------------------------------------


# Конкурентное выполнение с помощью задач

# Основы создания задач

async def delay_example_1(delay_seconds: int) -> int:
    print(f'засыпаю на {delay_seconds} с')
    await asyncio.sleep(delay_seconds)
    print(f'сон в течение {delay_seconds} с закончился')
    return delay_seconds


async def main_example_2():
    sleep_for_three = asyncio.create_task(delay_example_1(3))
    print(type(sleep_for_three))  # практически мгновенно переходим к этой строке
    result = await sleep_for_three
    print(result)


# asyncio.run(main_example_2())


# ----------------------------------------------------------------------------------------------------------------------


# Конкурентное выполнение нескольких задач

async def delay_example_2(delay_seconds: int) -> int:
    print(f'засыпаю на {delay_seconds} с')
    await asyncio.sleep(delay_seconds)
    print(f'сон в течение {delay_seconds} с закончился')
    return delay_seconds


async def main_example_3():
    sleep_for_three = asyncio.create_task(delay_example_2(3))
    sleep_again = asyncio.create_task(delay_example_2(3))
    sleep_once_more = asyncio.create_task(delay_example_2(3))
    await sleep_for_three
    await sleep_again
    await sleep_once_more


# asyncio.run(main_example_3())


# ----------------------------------------------------------------------------------------------------------------------


# Ещё 1 пример


async def delay_example_3(delay_seconds: int) -> int:
    print(f'засыпаю на {delay_seconds} с')
    await asyncio.sleep(delay_seconds)
    print(f'сон в течение {delay_seconds} с закончился')
    return delay_seconds


async def hello_every_second():
    for i in range(2):
        await asyncio.sleep(1)
        print("пока я жду, исполняется другой код!")


async def main_example_4():
    first_delay = asyncio.create_task(delay_example_3(3))
    second_delay = asyncio.create_task(delay_example_3(3))
    await hello_every_second()
    await first_delay
    await second_delay


# asyncio.run(main_example_4())
'''
засыпаю на 3 с
засыпаю на 3 с
пока я жду, исполняется другой код! 
пока я жду, исполняется другой код! 
сон в течение 3 с закончился
сон в течение 3 с закончился
'''


# ----------------------------------------------------------------------------------------------------------------------


# Запуск нескольких задач с помощью wait и gather

# wait


async def delay_example_4(delay_seconds: int) -> int:
    print(f'засыпаю на {delay_seconds} с')
    await asyncio.sleep(delay_seconds)
    print(f'сон в течение {delay_seconds} с закончился')
    return delay_seconds


async def main_example_5():
    t1 = time.time()
    await asyncio.wait([
        asyncio.create_task(delay_example_4(1)),
        asyncio.create_task(delay_example_4(2)),
        asyncio.create_task(delay_example_4(3)),
    ])
    t2 = time.time()
    print(t2 - t1)


# asyncio.run(main_example_5())


# ----------------------------------------------------------------------------------------------------------------------


# gather


async def delay_example_5(delay_seconds: int) -> int:
    print(f'засыпаю на {delay_seconds} с')
    await asyncio.sleep(delay_seconds)
    print(f'сон в течение {delay_seconds} с закончился')
    return delay_seconds


async def main_example_6():
    t1 = time.time()
    await asyncio.gather(
        asyncio.create_task(delay_example_5(1)),
        asyncio.create_task(delay_example_5(2)),
        asyncio.create_task(delay_example_5(3)),
    )
    t2 = time.time()
    print(t2 - t1)


# asyncio.run(main_example_6())


# ----------------------------------------------------------------------------------------------------------------------


# Обработка исключений

# wait


async def delay_example_6(delay_seconds: int) -> int:
    print(f'засыпаю на {delay_seconds} с')
    await asyncio.sleep(delay_seconds)

    if delay_seconds == 2:
        raise ValueError('Моё собственное исключение')

    print(f'сон в течение {delay_seconds} с закончился')
    return delay_seconds


async def main_example_7():
    t1 = time.time()
    await asyncio.wait([
        asyncio.create_task(delay_example_6(1)),
        asyncio.create_task(delay_example_6(2)),
        asyncio.create_task(delay_example_6(3)),
    ])
    t2 = time.time()
    print(t2 - t1)


# asyncio.run(main_example_7())


# ----------------------------------------------------------------------------------------------------------------------

# as_completed


async def delay_example_7(delay_seconds: int) -> int:
    print(f'засыпаю на {delay_seconds} с')
    await asyncio.sleep(delay_seconds)

    if delay_seconds == 2:
        raise ValueError('Моё собственное исключение')

    print(f'сон в течение {delay_seconds} с закончился')
    return delay_seconds


async def main_example_8():
    t1 = time.time()
    tasks = [
        asyncio.create_task(delay_example_7(1)),
        asyncio.create_task(delay_example_7(2)),
        asyncio.create_task(delay_example_7(3)),
    ]
    for completed_task in asyncio.as_completed(tasks):
        try:
            await completed_task
        except ValueError:
            print(f'Caught ValueError in task: {completed_task}')
        t2 = time.time()
        print(t2 - t1)


# asyncio.run(main_example_8())


# ----------------------------------------------------------------------------------------------------------------------


# gather


async def delay_example_8(delay_seconds: int) -> int:
    print(f'засыпаю на {delay_seconds} с')
    await asyncio.sleep(delay_seconds)

    if delay_seconds == 2:
        raise ValueError('Моё собственное исключение')

    print(f'сон в течение {delay_seconds} с закончился')
    return delay_seconds


async def main_example_9():
    t1 = time.time()
    await asyncio.gather(
        asyncio.create_task(delay_example_8(1)),
        asyncio.create_task(delay_example_8(2)),
        asyncio.create_task(delay_example_8(3)),
    )
    t2 = time.time()
    print(t2 - t1)


# asyncio.run(main_example_9())

# ----------------------------------------------------------------------------------------------------------------------


# Обработка результата

# wait


async def delay_example_9(delay_seconds: int) -> int:
    print(f'засыпаю на {delay_seconds} с')
    await asyncio.sleep(delay_seconds)
    print(f'сон в течение {delay_seconds} с закончился')
    return delay_seconds


async def main_example_10():
    t1 = time.time()

    tasks = [
        asyncio.create_task(delay_example_9(1)),
        asyncio.create_task(delay_example_9(2)),
        asyncio.create_task(delay_example_9(3)),
    ]

    done, pending = await asyncio.wait(tasks)

    # print('-------------------------------------------')
    # print('Done:')
    # for d in done:
    #     print(d, '|', d.result())
    # print('Pending:')
    # for p in pending:
    #     print(p)
    # print('-------------------------------------------')

    print('*******************************************')
    for task in tasks:
        print(task.result())
    print('*******************************************')

    t2 = time.time()
    print(t2 - t1)


# asyncio.run(main_example_10())


# ----------------------------------------------------------------------------------------------------------------------


# gather


async def delay_example_10(delay_seconds: int) -> int:
    print(f'засыпаю на {delay_seconds} с')
    await asyncio.sleep(delay_seconds)
    print(f'сон в течение {delay_seconds} с закончился')
    return delay_seconds


async def main_example_11():
    t1 = time.time()
    results = await asyncio.gather(
        asyncio.create_task(delay_example_10(1)),
        asyncio.create_task(delay_example_10(2)),
        asyncio.create_task(delay_example_10(3)),
    )

    print('-------------------------------------------')
    print(results)
    for result in results:
        print(result)
    print('-------------------------------------------')

    t2 = time.time()
    print(t2 - t1)


# asyncio.run(main_example_11())


# ----------------------------------------------------------------------------------------------------------------------

# Динамическое создание тасков

# wait

async def delay_example_11(delay_seconds: int) -> int:
    print(f'засыпаю на {delay_seconds} с')
    await asyncio.sleep(delay_seconds)
    print(f'сон в течение {delay_seconds} с закончился')
    return delay_seconds


async def main_example_12():
    t1 = time.time()

    tasks = []
    for i in range(1, 6):
        tasks.append(asyncio.create_task(delay_example_11(i)))

    await asyncio.wait(tasks)

    print('-------------------------------------------')
    for task in tasks:
        print(task.result())
    print('-------------------------------------------')

    t2 = time.time()
    print(t2 - t1)


# asyncio.run(main_example_12())


# ----------------------------------------------------------------------------------------------------------------------


# gather


async def delay_example_12(delay_seconds: int) -> int:
    print(f'засыпаю на {delay_seconds} с')
    await asyncio.sleep(delay_seconds)
    print(f'сон в течение {delay_seconds} с закончился')
    return delay_seconds


async def main_example_13():
    t1 = time.time()
    tasks = []
    for i in range(1, 6):
        tasks.append(asyncio.create_task(delay_example_12(i)))

    results = await asyncio.gather(*tasks)

    print('-------------------------------------------')
    for result in results:
        print(result)
    print('-------------------------------------------')

    t2 = time.time()
    print(t2 - t1)


# asyncio.run(main_example_13())


# ----------------------------------------------------------------------------------------------------------------------

# Асинхронность в web3

# Мы будем работать с версией web3.py 6.14.0


class Client:
    def __init__(self, rpc: str, private_key: str | None = None):
        self.rpc = rpc

        self.w3 = AsyncWeb3(AsyncWeb3.AsyncHTTPProvider(rpc))
        if private_key:
            self.account = self.w3.eth.account.from_key(private_key=private_key)
        else:
            self.account = self.w3.eth.account.create(extra_entropy=str(random.randint(1, 999_999_999)))

    async def get_balance(self, address: str | None = None):
        if not address:
            address = self.account.address
        return await self.w3.eth.get_balance(account=address)


async def main_example_14():
    while True:
        client = Client(rpc='https://rpc.ankr.com/arbitrum')
        # client = Client(rpc='https://arbitrum.llamarpc.com')
        balance = await client.get_balance()
        print(client.account.key.hex(), client.account.address, balance, '\n')
        if balance:
            break


# ----------------------------------------------------------------------------------------------------------------------


if __name__ == "__main__":
    asyncio.run(main_example_14())
