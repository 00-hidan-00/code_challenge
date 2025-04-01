import os
import re

from bs4 import BeautifulSoup


# Практика:

# 1 уровень:
# 1) Паша очень любит кататься на общественном транспорте,
# а получая билет, сразу проверяет, счастливый ли ему попался.
# Билет считается счастливым, если сумма первых трех цифр совпадает с
# суммой последних трех цифр номера билета.
# Программа должна выводить “Счастливый” или “Обычный”.
# (Решить с помощью индексов строк, то есть без математики)

def lvl_1_task_1(my_str: str = '123212f') -> str:
    if len(my_str) > 2 and my_str.isdigit():
        start_str = sum(int(digit) for digit in my_str[:3])
        end_str = sum(int(digit) for digit in my_str[-3:])
        if start_str == end_str:
            return 'Счастливый'
        else:
            return 'Обычный'
    return 'Не подходит'


# 2) Дана последовательность символов. Проверить, является ли она палиндромом
# (слово или текст, одинаково читающееся в обоих направлениях)

def lvl_1_task_2(my_str: str = 'A man a plan a canal Panama') -> str:
    new_str = my_str.lower().replace(' ', '')
    if new_str == new_str[::-1]:
        return "Является"
    else:
        return 'Не является'


# 3) Написать функцию проверки email
# (представьте, что для своего сайта эту функцию пишете. Сделать проверки,
# которые считаете нужными, а я буду пробовать сломать)

def lvl_1_task_3(mail_str: str = 'asdf__dda4_4sd@gmail.com') -> str:
    # Проверяем, что в email только один символ '@'
    if mail_str.count('@') != 1:
        return f'{mail_str} не верный (множество "@" или нет)'

    # Разделяем на локальную часть и домен
    local_part, domain_part = mail_str.split("@")

    # Проверка, что локальная часть не пуста и длина не превышает 64 символа
    if not (1 <= len(local_part) <= 64):
        return f'{mail_str} не верный (локальная часть невалидна)'

    # Проверка домена (должен содержать хотя бы одну точку)
    if '.' not in mail_str.split("@")[1]:
        return f'{mail_str} не верный (неверный домен)'

    # Разделяем на SLD и TLD
    SLD, TLD = domain_part.split('.', 1)

    # Проверка длины первой части домена

    if not (1 <= len(SLD) <= 64):
        return f'{mail_str} не верный (первая часть домена невалидна)'

    # Проверка длины TLD
    if not (3 <= len(TLD) <= 6):
        return f'{mail_str} не верный (неверный TLD)'

    # Дополнительная проверка на допустимые символы
    if not re.match(r'^[a-zA-Z0-9._-]+$', local_part):
        return f'{mail_str} не верный (неверные символы в локальной части)'

    # Если все проверки пройдены, email верный
    return f'{mail_str} верный'


# 4) Определить количество слов в строке.
# Вводится строка, состоящая из слов, разделенных пробелами.
# Требуется посчитать количество слов в ней.


def lvl_1_task_4(my_str: str = 'Hello, how are you today?') -> int:
    return len(my_str.split())


# 2 уровень:
# 1) Определить сложность пароля (сделать функцию как на обычных сайтах.
# То есть проверять большие буквы, символы, цифры И так далее. Подсказка: ascii)

def lvl_2_task_1(password: str = 'rrrrrrrrrr#Rr1r') -> str:
    if len(password) < 8:
        return 'Пароль должен быть больше 8 символов'

    has_digit = any(char.isdigit() for char in password)
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_special = any(char in '!@#$%^&*(),.?":{}|<>' for char in password)

    if all([has_digit, has_upper, has_lower, has_special]) and len(password) > 12:
        return 'Очень сильный пароль'

    if all([has_digit, has_upper, has_lower, has_special]):
        return 'Сильный пароль'

    if has_digit and has_upper and has_lower:
        return 'Средний пароль'

    if has_digit or has_upper or has_lower:
        return 'Слабый пароль'

    return 'Очень слабый пароль'


# 2) Необходимо написать программу, которая сможет посчитать повторяющиеся символы и вывести сокращенную строку,
# пример:
# Вход: s = 'aaaabbcaa'
# Выход: 'a4b2c1a2'

def lvl_2_task_2(my_str: str = 'aaaabbca') -> str:
    if not my_str:
        return ""

    new_str = ''
    val = 1

    for index in range(1, len(my_str)):
        if my_str[index] == my_str[index - 1]:
            val += 1
        else:
            new_str += my_str[index - 1] + str(val)
            val = 1

    new_str += my_str[-1] + str(val)

    return new_str


# 3) На основании предоставленного отрывка текста определить 3 наиболее часто встречаемых символа в нем.
# Пробелы нужно игнорировать (не учитывать при подсчете).
# Для выведения результатов вычислений требуется написать функцию top3(st).
# Итог работы функции представить в виде строки: «символ – количество раз, символ – количество раз…».

def lvl_2_task_3(text: str = None) -> str:
    if not text:
        text = ("In programming,%%% it's important to write clean, efficient code. "
                "Clean code is easier to read, ???maintain, and debug. "
                "Efficient code runs faster and consumes less memory.!!!!!")
    d = {}
    top3 = []

    for ch in text:
        if not ch == ' ':
            d[ch] = d.get(ch, 0) + 1

    for _ in range(3):
        max_val = max(d.values())

        for key, val in d.items():
            if val == max_val:
                top3.append(f"{key} - {val}")
                del d[key]
                break

    return ', '.join(top3)


# 4) Дмитрий считает, что когда текст пишут в скобках (как вот тут, например), его читать не нужно.
# Вот и надумал он существенно укоротить время чтения, написав функцию, которая будет удалять все, что расположено внутри скобок.

def lvl_2_task_4(text: str = None) -> str:
    if not text:
        text = ("In (programming,%)%% it's important (to write) clean, efficient code. "
                "Clean code is easier to read, ???maintain, and debug. "
                "Efficient code runs faster and consumes less memory.!!!!!")
    new_text = ''
    in_breakers = False

    for ch in text:
        if ch == "(":
            in_breakers = True
            continue
        elif ch == ')':
            in_breakers = False
            continue
        if not in_breakers:
            new_text += ch
    return new_text


# УРОВЕНЬ ПСиИииХ : (https://media3.giphy.com/media/1guRIRKAgaEOneVda2Q/giphy.gif?cid=ecf05e4776fhaulj9ulwy8eyhtbnbnh3757ndyj30s0yula9&rid=giphy.gif&ct=g)
# 1) Взять из сообщения ниже (там html код таблицы с CoinGecko (https://www.coingecko.com/ru) ~5.5к строк)

def lvl_3_task_1(path_file: str = os.path.join("data", "coingecko.txt")) -> str:
    with open(path_file, 'r', encoding='latin-1') as file:
        html_content = file.read()
    return html_content


# 2) засунуть этот код в переменную (просто скопировать и засунуть в переменную с помощью тройных кавычек)

def lvl_3_task_2():
    code_in_variable = '''
        with open(path_file, 'r', encoding='latin-1') as file:
        html_content = file.read()
        return html_content
    '''
    return code_in_variable


# 3) Вывести все названия криптовалют, которые есть  в этом коде (по сути первая страница coingecko - топ 100)
# P.S. - не пытайтесь читать код coingecko. Откройте консоль разработчика и найдите закономерности
# Подсказка: возле каждого названия криптовалюты есть классы "py-0 coin-name cg-sticky-col cg-sticky-third-col px-0" ориентируйтесь на них, когда будете парсить

def lvl_3_task_3(path_file: str = os.path.join("data", "coingecko.txt")) -> str:
    with open(path_file, 'r', encoding='latin-1') as file:
        html_content = file.read()

    # Парсим HTML
    soup = BeautifulSoup(html_content, 'html.parser')

    elements = soup.find_all(class_='py-0 coin-name cg-sticky-col cg-sticky-third-col px-0')
    crypto_names = [element.get_text(strip=True) for element in elements]

    return ', '.join(crypto_names)


def main():
    result = lvl_2_task_4()
    print(result)


if __name__ == "__main__":
    main()
