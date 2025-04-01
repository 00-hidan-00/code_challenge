import requests


# 1 уровень:
# 1) Есть 2 словаря. Объединить их без помощи функции update

def task_1_options_1():
    d_1 = {
        1: 1,
        '1': '1',
        1.1: 1.1,
    }
    d_2 = {
        1: 1,
        2: 2,
        '2': '2',
        2.2: 2.2,
    }

    for key, val in d_2.items():
        d_1[key] = val

    print(d_1)


def task_1_options_2():
    d_1 = {
        1: 1,
        '1': '1',
        1.1: 1.1,
    }
    d_2 = {
        1: 1,
        2: 2,
        '2': '2',
        2.2: 2.2,
    }
    d_3 = {**d_1, **d_2}
    print(d_3)


def task_1_options_3():
    d_1 = {
        1: 1,
        '1': '1',
        1.1: 1.1,
    }
    d_2 = {
        1: 1,
        2: 2,
        '2': '2',
        2.2: 2.2,
    }
    print({key: val for d in (d_1, d_2) for key, val in d.items()})


# 2) Есть словарь с числовыми значениями. Посчитать среднюю по значениям

def task_2():
    d = {
        1: 124,
        2: 75437,
        3: 5,
        4: 43.2523,
    }

    print(sum(d.values()) / len(d))


# 3) Даны два списка одинаковой длины. Необходимо создать из них словарь таким образом, чтобы элементы первого списка были ключами, а элементы второго — соответственно значениями нашего словаря.

def task_3_options_1():
    lst_1 = [1, 2, 3, 4, ]
    lst_2 = [124, 75437, 5, 543.2523, ]
    d = {lst_1[index]: lst_2[index] for index in range(len(lst_1))}

    print(d)


def task_3_options_2():
    lst_1 = [1, 2, 3, 4, ]
    lst_2 = [124, 75437, 5, 543.2523, ]
    d = {key: val for key, val in zip(lst_1, lst_2)}

    print(d)

    # 4) Когда Антон прочитал «Войну и мир», ему стало интересно,


# сколько слов и в каком количестве используется в этой книге.
# Помогите Антону написать упрощённую версию такой программы,
# которая сможет подсчитать слова, разделённые пробелом и вывести получившуюся статистику.
# Программа должна считывать одну строку со стандартного ввода и выводить для каждого уникального слова в этой строке число его повторений (без учёта регистра)
# в формате "слово количество" (см. пример вывода).
# Порядок вывода слов может быть произвольным, каждое уникальное слово  должно выводиться только один раз

def task_4_options_1():
    text = 'написать написать Помогите упрощённую Антону написать упрощённую версию такой написать программы'
    lst_words = text.lower().split()
    words_count_d = {word: lst_words.count(word) for word in lst_words}
    for word, count in words_count_d.items():
        print(f"{word} {count}")


def task_4_options_2():
    text = 'написать написать Помогите упрощённую Антону написать упрощённую версию такой написать программы'
    print(set(text.lower().split()))
    words_count_d = {word: text.lower().split().count(word) for word in set(text.lower().split())}
    for word, count in words_count_d.items():
        print(f"{word} {count}")


# 5) Получить json словарь с сайта https://chainid.network/chains.json (с помощью requests) и вывести информацию о всех сетях в формате:
# "name | первое rpc | есть ли поддержка EIP1559 | название нативной монеты | decimals нативной монеты | chain id | ссылка на експлорер"

def task_5():
    url = 'https://chainid.network/chains.json'
    response = requests.get(url)
    data = response.json()

    for chain in data[:11]:
        name = chain.get("name", "Unknown")
        rpc_link = next(iter(chain.get("rpc", [])), "None")
        EIP1559 = any(feature.get("name") == "EIP1559" for feature in chain.get("features", []))

        native_currency = chain.get("nativeCurrency", {})
        token_name = native_currency.get("symbol", "Unknown")
        decimals = native_currency.get("decimals", "Unknown")

        chainId = chain.get("chainId", "Unknown")

        # explorer_lst = chain.get('explorers', [])
        # explorer_link = explorer_lst[0].get('url', "None") if explorer_lst else "None"
        explorer_link = next(
            (exp.get("url", "None") for exp in chain.get("explorers", []) if isinstance(exp, dict)), "None"
        )

        print(
            f'{name=} | {rpc_link=} | {EIP1559=} | {token_name=} | {decimals=} | {chainId=} | {explorer_link=}'
        )


# 6) Пользователь вводит chain_id и нужно вывести coin symbol (название нативной монеты в этой сети).
# Для получения информации использовать json словарь с сайта https://chainid.network/chains.json (с помощью requests)

def task_6():
    url = 'https://chainid.network/chains.json'
    response = requests.get(url)
    data = response.json()
    try:

        chain_id = int(input("Введите chain_id: "))
        result = next(
            (chain.get('nativeCurrency', {}).get('symbol', "Symbol not found")
             for chain in data if chain.get('chainId') == chain_id)
            , "Chain not found"
        )
        print(result)
    except ValueError:
        print("Пожалуйста, введите корректный числовой chain_id.")


def main():
    task_3_options_2()


if __name__ == "__main__":
    main()
