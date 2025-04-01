# Задачи на работу с функциями:
import random


# 1) Написать функцию, которая будет искать и выводить на экран минимальное число, большее 300 и кратное 19.
def task_1() -> int:
    return 300 + (19 - (300 % 19))


# 2) Написать функцию, которая будет обменивать местами первую и последнюю цифру числа N (1234 → 4231).

def task_2(amount: int = 1234) -> int:
    amount_str = str(amount)
    return int(amount_str[-1] + amount_str[1:len(amount_str) - 1] + amount_str[0])


# 3) Написать функцию, которая будет определять, делится ли число N на: 2, 3, 4, 5, ... (без использования оператора % )

def task_3_optional_1(amount: int = 10) -> list[int]:
    return [
        val for val in range(1, amount + 1)
        if str(amount / val)[-1] == '0'
    ]


def task_3_optional_2(amount: int = 100) -> list[int]:
    return [
        val for val in range(1, amount + 1)
        if (amount // val) * val == amount
    ]


# 4) Написать функцию, которая будет вычислять и выводить на экран значение выражения
# N^M без использования оператора возведения в степень (**).

def task_4(n: int = 3, m: int = 40) -> int:
    result = n
    for _ in range(1, m):
        result *= n

    print(result)


# 5) С клавиатуры вводится пять чисел. Для каждого из них вывести,
# является ли оно степенью числа 3. Вынести определение степени в функцию.

def task_5() -> dict[int, bool]:
    amounts_list = [1, 3, 5, 9, 27, 90, 81]
    main_amount = 3
    bool_dict = {}
    for amount in amounts_list:
        if amount == 1:
            bool_dict[amount] = True
            continue
        power = 1
        while power < amount:
            power *= main_amount
            if power == amount:
                bool_dict[amount] = True
                break
        else:
            bool_dict[amount] = False
    return bool_dict


# 6) Реализовать набор функций для работы со списком:


# • Ввод с клавиатуры/инициализация случайными числами (с параметрами).
def task_6_option_1(lst: list = None, len_lst: int = 10, min_amount: int = 1, max_amount: int = 100) -> list[int]:
    if lst is None:
        lst = [random.randint(min_amount, max_amount) for _ in range(len_lst)]
    return lst


# • Вывод списка на экран (в одну строчку).
def task_6_option_2(lst: list = None) -> str | None:
    if lst is None:
        return lst
    return ' '.join(map(str, lst))


# • Подсчет максимума и минимума (с индексами).
def task_6_option_3(lst: list = None) -> dict[int, int] | None:
    if lst is None or len(lst) == 0:
        return None
    max_val = max(lst)
    min_val = min(lst)
    return {max_val: lst.index(max_val), min_val: lst.index(min_val)}


# • Подсчет количества элементов, равных (больших/меньших) N.
def task_6_option_4(lst: list, n: int = 4) -> dict[str:int]:
    d = {'equal': lst.count(n), "less": 0, "more": 0}
    for val in lst:
        if val < n:
            d['less'] += 1
        elif val > n:
            d['more'] += 1
    return d


# • Добавление элемента К [в конец массива/на N-ю позицию].
def task_6_option_5(lst: list, k: int = 999, n: int = 5) -> list[int]:
    return lst[:n] + [k] + lst[n:]


# • Удаление из списка [последнего/Nго элемента].
def task_6_option_6_1(lst: list, n: int = 5) -> list[int]:
    if n in lst:
        new_lst = lst[::-1]
        new_lst.pop(new_lst.index(n))
        return new_lst[::-1]
    else:
        lst.pop()
        return lst


def task_6_option_6_2(lst: list, n: int = 5) -> list[int]:
    if n in lst:
        index_to_remove = len(lst) - 1 - lst[::-1].index(n)
        del lst[index_to_remove]
    else:
        lst.pop()
    return lst


# • Сортировка списка по (возрастанию/убыванию). Повторяющиеся — убирать.
def task_6_option_7_1(lst: list, increase: bool = False) -> list[int]:
    unique_lst = sorted(set(lst))
    if not increase:
        unique_lst.reverse()
    return unique_lst


def task_6_option_7_2(lst: list, increase: bool = True) -> list[int]:
    return sorted(set(lst), reverse=not increase)

# Bubble Sort
def task_6_option_7_3(lst: list, increase: bool = True) -> list[int]:
    for i in range(len(lst) - 1):
        for index in range(len(lst) - i - 1):
            if lst[index] > lst[index + 1]:
                # tmp = lst[index]
                # lst[index] = lst[index + 1]
                # lst[index + 1] = tmp
                lst[index], lst[index + 1] = lst[index + 1], lst[index]

    if not increase:
        lst.reverse()
    return lst


# 7) Найти третий максимум в списке.
def task_7() -> int:
    lst = [3, 5, 21, 20, 8, 1, 754, 3]
    unique_lst = list(set(lst))
    if len(unique_lst) < 3:
        return None
    unique_lst.remove(max(unique_lst))
    unique_lst.remove(max(unique_lst))
    return max(unique_lst)


# 8) Сдвинуть все элементы массива на два вправо. Оставшиеся элементы — поставить слева в том же порядке.

def task_8_options_1(lst: list = None) -> list:
    if lst is None:
        return lst

    new_lst = [0] * len(lst)

    for index in range(len(lst)):

        if index + 2 < len(lst):
            new_lst[index + 2] = lst[index]
        else:
            new_lst[index + 2 - len(lst)] = lst[index]

    return new_lst


def task_8_options_2(lst: list = None) -> list:
    if lst is None:
        return lst

    new_lst = [0] * len(lst)  # Создаём новый список той же длины

    for index in range(len(lst)):
        new_index = (index + 2) % len(lst)  # Сдвигаем индекс на 2 вправо
        new_lst[new_index] = lst[index]

    return new_lst


def task_8_options_3(lst: list = None) -> list:
    return lst[-2:] + lst[:-2]


# 9) Вставить K после максимального элемента.

def task_9(lst: list, k: int = 10) -> list:
    max_index = lst.index(max(lst))
    return lst[:max_index + 1] + [k] + lst[max_index + 1:]


def main():
    lst = task_6_option_1()
    print(lst)

    result = task_6_option_7_3(lst)
    print(result)


if __name__ == "__main__":
    main()
