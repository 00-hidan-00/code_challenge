# Lesson notes:
# (https://spurious-factory-624.notion.site/9938ad14815b402fbf068cdc594035ed?pvs=4)

# Синтаксис создания функции
# def название_функции(параметры):
#     тело_функии

# Пример
def print_triangle():
    print('    *    ')
    print('  * * *  ')
    print('* * * * *')


# Пример с параметрами
def get_smallest_number(a: int | float, b: int | float):
    if a < b:
        print(a)
    else:
        print(b)


# Параметры по-умолчанию

def say_hi(name: str = 'noname'):
    print(f'Hello, {name}')


# Return - возврат значения из функции
def foo(a: int) -> int:
    a = 42
    return a


# Сокращаем код с помощью return
# Было:
def get_smallest_number_1(a: int | float, b: int | float) -> int | float:
    if a < b:
        print(a)
    else:
        print(b)


# Стало:
def get_smallest_number_2(a: int | float, b: int | float) -> int | float:
    if a < b:
        return a
    return b


def main():
    ...


if __name__ == "__main__":
    main()
