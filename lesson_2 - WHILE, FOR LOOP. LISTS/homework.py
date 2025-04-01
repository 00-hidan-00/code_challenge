# Уровень 1:
# 1) Температура воды в кастрюле 7 градусов. Кастрюлю поставили на огонь. Температура увеличивается каждые 2с на 1 градус.
# Определить через сколько вода закипит (температура будет 100 градусов)

def lvl_1_task_1():
    temp_watter = 7
    time = 0
    while temp_watter < 100:
        time += 2
        temp_watter += 1
    print(f'Вода закипит через {time} секунд')


# 2) Вывести на экран 5 строк из трех нулей (каждая строка должна быть пронумерована)


def lvl_1_task_2():
    for i in range(1, 6):
        print(f"{i}. 000")


# 3) Вывести прямоугольный треугольник из символа "*" (высота указывается с клавиатуры)


def lvl_1_task_3(x):
    for _ in range(1, x + 1):
        print(f"* " * _)


# Уровень 2:

# 1) Имеется коробка со сторонами A x B x C. Определить, войдет ли она в дверь размером M x K

def lvl_2_task_1_options_1(A, B, C, M, K):
    # Sort the box dimensions in descending order
    box_dims = sorted([A, B, C], reverse=True)
    # Sort the door dimensions in descending order
    door_dims = sorted([M, K], reverse=True)

    # Check if the two smallest dimensions of the box fit through the door
    print(box_dims[1] <= door_dims[0] and box_dims[2] <= door_dims[1])


def lvl_2_task_1options_2(A, B, C, M, K):
    # Sort the box dimensions in descending order
    box_dims = sorted([A, B, C], reverse=True)

    # Sort the door dimensions in descending order
    door_dims = sorted([M, K], reverse=True)
    door_dims.sort(reverse=True)

    # Check if the two smallest dimensions of the box fit through the door
    print(box_dims[1] <= door_dims[0] and box_dims[2] <= door_dims[1])


# 2) Вывести равнобедренный треугольник из символа "*" (высота указывается с клавиатуры)


def lvl_2_tasks_2_options_1(x):
    if x % 2 == 1:
        my_list = []

        for index in range(x):
            if index < x // 2 + 1:
                my_list.append(" * ")
            else:
                my_list.pop()

            print(''.join(my_list))


def lvl_2_tasks_2_options_2(x):
    for i in range(1, x + 1):  # От 1 до x
        print(("* " * i).rjust(x + i - 1))


# Дано число N и последовательность квадратов чисел (1, 4, 9, 16, 25, …). Вывести числа, которые меньше N

def lvl_2_tasks_3_options_1(n):
    numbers = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

    print([number for number in numbers if number < n])


def lvl_2_tasks_3_options_2(n):
    new_list = []
    i = 1
    while i ** 2 < n:
        new_list.append(i ** 2)
        i += 1
    print(new_list)


# Уровень 3:
# 1) В кафе продают по 3 шарика мороженного и по 5. Можно ли купить ровно k шариков мороженного

def lvl_3_tasks_1(need_count):
    for x in range(need_count // 3 + 1):  # Перебираем количество троек
        for y in range(need_count // 5 + 1):  # Перебираем количество пятёрок
            if 3 * x + 5 * y == need_count:
                print("Можно")
                return
    print("Нельзя")


# 2) Клиент оформил вклад на m тысяч рублей в банке под k% годовых.
# Через сколько лет сумма вклада превысит s тысяч рублей, если за это время клиент не будет брать деньги со счета.

def lvl_3_tasks_2(bank_deposit, annual_percentage, need_bank_deposit):
    years = 0
    while bank_deposit < need_bank_deposit:
        bank_deposit *= (1 + annual_percentage / 100)
        years += 1
    print(years, bank_deposit)


# 3) Дано число N. Посчитать сумму цифр

def lvl_3_tasks_3(number):
    print(sum(int(number_str) for number_str in str(number)))


# Уровень 4
# Задачи на работу со списком через цикл:

# 1) есть список из 10 элементов. найти сумму элементов этого списка

def lvl_4_task_1(my_list):
    print(sum(element for element in my_list if isinstance(element, (int, float)) and not isinstance(element, bool)))


# 2) есть список из 10 элементов. Посчитать сумму четных цифр в списке

def lvl_4_task_2(my_list):
    print(
        sum(
            element for element in my_list if
            isinstance(element, int) and not isinstance(element, bool) and element % 2 == 0
        )
    )


# 3*) есть список из 10 элементов. найти наибольшее и наименьшее число в списке (самая простая задача с реального собеседования)

def lvl_4_task_3(my_list):
    new_my_list = [element for element in my_list if
                   isinstance(element, (int, float)) and not isinstance(element, bool)]
    print(max(new_my_list), min(new_my_list))


# 4*) задача 3, но нужно найти индекс минимального и максимального элемента в списке

def lvl_4_task_4_options_1(my_list):
    new_my_list = [element for element in my_list if
                   isinstance(element, (int, float)) and not isinstance(element, bool)]
    print(
        new_my_list.index(max(new_my_list)),
        new_my_list.index(min(new_my_list)),
    )


def lvl_4_task_4_options_2(my_list):
    min_num = my_list[0]
    max_num = my_list[0]
    for element in my_list:
        if isinstance(element, (int, float)) and not isinstance(element, bool) and element < min_num:
            min_num = element
        if isinstance(element, (int, float)) and not isinstance(element, bool) and element > max_num:
            max_num = element
    print(f"{my_list.index(min_num)}, {my_list.index(max_num)}")


# Уровень 5
# Задачи на методы списка:
# 1) Задачу начать решать с пустого списка:
# lst = []
# Папа написал Саше список продуктов (молоко, огурцы, пиво, рыбка) и бабушка тоже попросила купить некоторые продукты
# (чай, сахар, сухарики).
# Мама увидела список и сказала вычеркнуть пиво и рыбку
# Помоги Саше сформировать единый список покупок и посчитать сколько пунктов содержит общий список покупок

def lvl_5_task_1():
    lst = []
    father_list = ["молоко", "огурцы", "пиво", "рыбка"]
    grandmother_list = ['чай', 'сахар', 'сухарики']
    mather_delete_list = ['пиво', 'рыбка']
    # lst.extend(father_list)
    # lst.extend(grandmother_list)
    lst += father_list
    lst += grandmother_list

    for product in mather_delete_list:
        if product in lst:
            lst.remove(product)

    print(lst)


# 2) Есть список. пользователь вводит число. Нужно определить, есть ли это число в списке

def lvl_5_task_2(n):
    my_list = [2, 5, 634, 1, 5, 3, 7, 4]
    # result = my_list.count(n)
    result = my_list.index(n)
    # result = n in my_list
    print(result)


# 3) Есть список и число, которое ввел пользователь
# посчитать сколько раз это число встречается в списке

def lvl_5_task_3(lst, number):
    print(lst.count(number))


def main():
    lvl_5_task_1()
    # lvl_5_task_3([2, 4, 'wqe', 1.421, True, 4, 6, 432.532, '52352', 132], 13)
    # [2, 4, 'wqe', 1.421, True, 4, 6, 432.532, '52352', 132]


if __name__ == "__main__":
    main()
