import csv
import json
import os
from collections import Counter


# Практика:
# Файл log_100.json:
# 1) чему равен общий вклад топ-3 всех IP по количеству посещений? Указать процентом

def task_1_example_1() -> str:
    path = os.path.join("data_homework", "log_100.json")
    all_ip_and_count_visits = {}
    top_3_ip_and_count_visits = []
    sum_top_3_ip_count_visits_in_percentage: int = 0

    with open(path) as file:
        json_data = json.load(file)

    for ip_info in json_data:
        all_ip_and_count_visits[ip_info['ip']] = all_ip_and_count_visits.get(ip_info['ip'], 0) + 1

    count_all_visits_ip = sum(all_ip_and_count_visits.values())

    for _ in range(3):
        top_1_count_visit = max(all_ip_and_count_visits.values())

        for ip, count_visit in all_ip_and_count_visits.items():
            if count_visit == top_1_count_visit:
                top_3_ip_and_count_visits.append({ip: count_visit})
                del all_ip_and_count_visits[ip]
                break

    for ip_and_count_visits in top_3_ip_and_count_visits:
        for ip, count_visits in ip_and_count_visits.items():
            sum_top_3_ip_count_visits_in_percentage += round((count_visits / count_all_visits_ip) * 100, 2)

    return f'Вклад топ-3 всех IP по количеству посещений равен: {sum_top_3_ip_count_visits_in_percentage}%'


def task_1_example_2() -> str:
    path = os.path.join("data_homework", "log_100.json")
    all_ip_and_count_visits = {}

    with open(path) as file:
        json_data = json.load(file)

    for ip_info in json_data:
        all_ip_and_count_visits[ip_info['ip']] = all_ip_and_count_visits.get(ip_info['ip'], 0) + 1

    count_all_visits_ip = sum(all_ip_and_count_visits.values())

    # Получаем топ-3 IP, сортируя словарь по количеству посещений
    top_3_ip_and_count_visits = sorted(all_ip_and_count_visits.items(), key=lambda x: x[1], reverse=True)[:3]

    # Подсчет вклада топ-3 IP в процентах
    sum_top_3_ip_count_visits_in_percentage = sum(
        round((count / count_all_visits_ip) * 100, 2) for _, count in top_3_ip_and_count_visits
    )

    return f'Вклад топ-3 всех IP по количеству посещений равен: {sum_top_3_ip_count_visits_in_percentage}%'


# 2) сколько в файле уникальных IP, с которых на сайт заходили только 1 раз
def task_2_example_1() -> list:
    path = os.path.join("data_homework", "log_100.json")
    all_ip_and_count_visits = {}

    with open(path) as file:
        json_data = json.load(file)

    for ip_info in json_data:
        all_ip_and_count_visits[ip_info['ip']] = all_ip_and_count_visits.get(ip_info['ip'], 0) + 1

    unique_ip = [ip for ip, count_visits in all_ip_and_count_visits.items() if count_visits == 1]

    return unique_ip


def task_2_example_2() -> list:
    path = os.path.join("data_homework", "log_100.json")

    with open(path) as file:
        json_data = json.load(file)

    # Используем Counter для подсчета посещений
    all_ip_and_count_visits = Counter(ip_info['ip'] for ip_info in json_data)

    # Ищем уникальные IP, с которых заходили только 1 раз
    unique_ip = [ip for ip, count_visits in all_ip_and_count_visits.items() if count_visits == 1]

    return unique_ip


# Файл log_cereals.csv:
# 3) наименьшая стоимость пачки манки

def task_3_example_1() -> float:
    path = os.path.join("data_homework", "log_cereals.csv")

    with open(path, encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)
        return min([float(row[1]) for row in reader])


def task_3_example_2() -> float:
    path = os.path.join("data_homework", "log_cereals.csv")

    with open(path, encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Пропускаем заголовок

        prices = []
        for row in reader:
            if len(row) > 1 and row[1].replace('.', '', 1).isdigit():  # Проверяем, что это число
                prices.append(float(row[1]))

        return min(prices) if prices else 0.0  # Возвращаем 0.0, если список пуст


# 4) средняя цена на крупу за весь период наблюдений

def task_4() -> float:
    path = os.path.join("data_homework", "log_cereals.csv")

    with open(path, encoding='utf-8') as file:
        reader = csv.reader(file)
        header = next(reader)
        csv_data = list(reader)

    count_groats = len(header[1:])
    groats_data = {index: {} for index in range(1, count_groats + 1)}

    for index, name in enumerate(header[1:]):
        groats_data[index + 1]['name of groats'] = name

    for row in csv_data:
        for index in range(1, count_groats + 1):
            groats_data[index]['count_years'] = groats_data[index].get('count_years', 0) + 1
            groats_data[index]['sum_prices'] = groats_data[index].get('sum_prices', 0) + float(row[index])

    for index in range(1, count_groats + 1):
        groats_data[index]['average_price'] = groats_data[index]['sum_prices'] / groats_data[index]['count_years']

    result = round(
        sum([groats_data[index]['average_price'] for index in range(1, count_groats + 1)]) / len(groats_data), 3)

    return result


# Файл log_full.csv:
# 5) найти максимально часто встречающийся IP
# 6) посчитать в процентах вклад этого IP адреса в общее кол-во запросов
# 7) найти последнюю запись в логах с этим IP и выяснить какой user-agent был у этой записи
# получить словарь:
"""

suspicious_agent = {
    "ip": '...',            # самый частовстречаемый ip в логах
    'fraction': 70.205,     # процент запросов с таким ip от общего кол-ва запросов
    'count': 29427,         # число запросов с таким IP
    'last': {               # вложенный словарь с 2-мя полями
        'agent': '...',     # последний user-agent для этого ip
        'timestamp': '...', # последний timestap для этого ip
    }
}

"""


def task_5() -> dict:
    path = os.path.join("data_homework", "log_full.csv")

    with open(path, encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Пропускаем заголовок, если он есть
        csv_data = list(reader)

    # Подсчёт количества запросов с каждого IP
    ip_count = Counter(row[1] for row in csv_data)

    # Определяем самый частый IP и его количество запросов
    top_ip, top_ip_count = max(ip_count.items(), key=lambda x: x[1])

    # Общее число запросов
    total_requests = sum(ip_count.values())

    # Доля этого IP в общем количестве запросов
    fraction = round((top_ip_count / total_requests) * 100, 3)

    last_agent, last_timestamp = "Unknown", "Unknown"

    for row in reversed(csv_data):
        if row[1] == top_ip:
            last_agent = row[2]
            last_timestamp = row[0]
            break

    suspicious_agent = {
        'ip': top_ip,
        'fraction': fraction,
        'count': top_ip_count,
        'last': {
            'agent': last_agent,
            'timestamp': last_timestamp

        }
    }
    return suspicious_agent


def main():
    result = task_5()
    print(result)


if __name__ == "__main__":
    main()
