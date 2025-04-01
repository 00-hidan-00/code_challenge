# Lesson notes:
# https://spurious-factory-624.notion.site/for-while-4d96c8a9e2c041bfb2bf035b847a3122?pvs=4


def exemple_1():
    for _ in range(1, 6):
        print(_)


def exemple_2():
    wallets = [
        "0xfer424ffh92g829g4h",
        "0xfg43567890abcdefg",
        "0xghjklmnpqrstuvwx",
    ]

    for wallet in wallets:
        print(f"Wallet: {wallet}")


def exemole_3():
    lst = [88, 'hi', True, 57, 9]
    print(lst[0])  # 88
    print(lst[1])  # 'hi'
    print(lst[3])  # 57
    print(lst[4])  # 9
    print(lst[5])  # IndexError: list index out of range
    print(lst[-1])  # 9
    print(lst[-2])  # 57
    print(lst[-3])  # True


def exemple_4():
    lst = [12, 5, 76, 123, 8, 98, 3, 65]
    print(lst[0:2])  # [12, 5]
    print(lst[:2])  # [12, 5]
    print(lst[4:6])  # [8, 98]
    print(lst[4:-1])  # [8, 98, 3]
    print(lst[4:])  # [8, 98, 3, 65]
    print(lst[1:5:2])  # [5, 123]
    print(lst[1:-1:2])  # [5, 123, 98]
    print(lst[-1:1:-1])  # [65, 3, 98, 8, 123, 76]
    print(lst[::-1])  # [65, 3, 98, 8, 123, 76, 5, 12]


def exemple_5():
    lst = [12, 5, 76, 123, 8, 98, 3, 65]

    # длина списка
    print(len(lst))  # 8

    # добавить элемент в конец списка
    lst.append(11111)
    print(lst)  # [12, 5, 76, 123, 8, 98, 3, 65, 11111]

    # удаление элемента по индексу
    del lst[0]
    print(lst)  # [5, 76, 123, 8, 98, 3, 65, 11111]

    # проверить наличие элемента в списке
    if 98 in lst:
        print('yes')  # выведется 'yes' так как 98 есть в списке
    else:
        print('no')

    # удаление элемента по значению
    lst.remove(98)
    print(lst)  # [5, 76, 123, 8, 3, 65, 11111]

    # получить индекс элемента (возвращает первое вхождение)
    print(lst.index(65))  # 5


def main():
    exemple_4()


if __name__ == "__main__":
    main()
