import csv
import json
import os
import random
import time
from datetime import datetime

import requests
from bs4 import BeautifulSoup as BS
from fake_useragent import FakeUserAgent


# Практика:
# 1) Зайти на сайт с Риком и Морти: https://rickandmortyapi.com/
# Выгрузить с сайта все изображения персонажей с главной страницы (задача делается через запросы, а не через BS4)


def task_1_exemple_1():
    headers = {
        'user-agent': FakeUserAgent().random
    }

    main_folder = 'data'
    folder = 'rickandmortyapi_imgs'
    full_path = os.path.join(main_folder, folder)
    os.makedirs(full_path, exist_ok=True)

    source_url = 'https://rickandmortyapi.com/api/character'
    response = requests.get(source_url, headers=headers)

    response_data = response.json()
    for data in response_data['results']:
        url_img = data['image']

        response_img = requests.get(url_img)
        filename = url_img.split('/')[-1]
        file_path = os.path.join(full_path, filename)

        if response_img.status_code == 200:
            with open(file_path, 'wb') as f:
                f.write(response_img.content)
        else:
            print(f"Failed to retrieve {url_img}")
        time.sleep(random.uniform(1, 3))


def task_1_exemple_2():
    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/json',
        'origin': 'https://rickandmortyapi.com',
        'priority': 'u=1, i',
        'referer': 'https://rickandmortyapi.com/',
        'sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': FakeUserAgent().random,
    }

    json_data = {
        'query': '\n    query randomCharacters($ids: [ID!]!) {\n      charactersByIds(ids: $ids) {\n        id\n        name\n        status\n        species\n        image\n        episode {\n          name\n          id\n        }\n        location {\n          name\n          id\n        }\n      }\n    }\n  ',
        'variables': {
            'ids': [
                393,
                97,
                773,
                747,
                434,
                730,
            ],
        },
    }

    response = requests.post('https://rickandmortyapi.com/graphql', headers=headers, json=json_data)

    main_folder = 'data'
    folder = 'rickandmortyapi_imgs'
    full_path = os.path.join(main_folder, folder)
    os.makedirs(full_path, exist_ok=True)

    json_data = response.json().get('data', {}).get('charactersByIds', {})

    for data in json_data:
        img_src = data['image']

        response_img = requests.get(img_src)
        filename = img_src.split('/')[-1]
        file_path = os.path.join(full_path, filename)
        if response_img.status_code == 200:
            with open(file_path, 'wb') as f:
                f.write(response_img.content)
        else:
            print(f"Failed to retrieve {img_src}")
        time.sleep(random.uniform(1, 3))


# 2) Зайти на сайт с Риком и Морти: https://rickandmortyapi.com/
# Определить в каких эпизодах появлялся персонаж с главной страницы. Выгрузить все фотографии персонажей из данного эпизода в папку, которая называется episode_N (N - номер эпизода)
# Для создания папок используйте модуль os


def task_2():
    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/json',
        'origin': 'https://rickandmortyapi.com',
        'priority': 'u=1, i',
        'referer': 'https://rickandmortyapi.com/',
        'sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': FakeUserAgent().random,
    }
    json_data = {
        'query': '\n    query randomCharacters($ids: [ID!]!) {\n      charactersByIds(ids: $ids) {\n        id\n        name\n        status\n        species\n        image\n        episode {\n          name\n          id\n        }\n        location {\n          name\n          id\n        }\n      }\n    }\n  ',
        'variables': {
            'ids': [
                393,
                97,
                773,
                747,
                434,
                730,
            ],
        },
    }
    response = requests.post('https://rickandmortyapi.com/graphql', headers=headers, json=json_data)
    json_data = response.json().get('data', {}).get('charactersByIds', {})

    main_folder = 'data'
    os.makedirs(main_folder, exist_ok=True)

    episodes_by_id_list = [data['episode'][0]['id'] for data in json_data]

    for episode_by_id in episodes_by_id_list:
        full_path = os.path.join(main_folder, f'episode_{episode_by_id}')
        os.makedirs(full_path, exist_ok=True)
        episode_json_data = requests.get(f'https://rickandmortyapi.com/api/episode/{episode_by_id}').json()
        for character_url in episode_json_data['characters']:
            character_json_data = requests.get(character_url).json()
            response_img = requests.get(character_json_data['image'])
            filename = character_json_data['image'].split('/')[-1]
            file_path = os.path.join(full_path, filename)
            with open(file_path, 'wb') as f:
                f.write(response_img.content)


# 3) Зайти на сайт генерации юзернеймов: https://www.spinxo.com/
# Сгенерировать 100 рандомных юзернеймов и сохранить их в файл


def task_3(names_count: int = 100):
    headers = {
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'en,en-US;q=0.9,uk;q=0.8,ru;q=0.7,ru-RU;q=0.6',
        'content-type': 'application/json; charset=UTF-8',
        # 'cookie': 'ASP.NET_SessionId=oedkpbem02qouulbfdk4djev',
        'origin': 'https://www.spinxo.com',
        'priority': 'u=1, i',
        'referer': 'https://www.spinxo.com/',
        'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132", "Opera GX";v="117"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': FakeUserAgent().random,
        'x-requested-with': 'XMLHttpRequest',
    }
    json_data = {
        'snr': {
            'category': 0,
            'UserName': '',
            'Hobbies': '',
            'ThingsILike': '',
            'Numbers': '',
            'WhatAreYouLike': '',
            'Words': '',
            'Stub': 'usernames',
            'LanguageCode': 'en',
            'NamesLanguageID': '45',
            'Rhyming': False,
            'OneWord': False,
            'UseExactWords': False,
            'ScreenNameStyleString': '',
            'PersonalitySlug': '',
            'CharacterTypeSlug': '',
            'ThemeSlug': '',
            'GenderAny': False,
            'GenderMale': False,
            'GenderFemale': False,
        },
    }

    names_list = []
    main_folder = 'data'
    os.makedirs(main_folder, exist_ok=True)
    filename = f'random_names_{names_count}.json'
    file_path = os.path.join(main_folder, filename)
    result_dict = {}

    while len(names_list) < names_count:
        response = requests.post(
            'https://www.spinxo.com/services/NameService.asmx/GetNames',
            headers=headers,
            json=json_data,
        )
        names_list += response.json().get('d', {}).get('Names', {})

        result_dict = {'names': names_list[:names_count]}

    with open(file_path, 'w') as file:
        json.dump(result_dict, file)


# 4) Написать программу, которая будет заходить на сайт с новостями: https://www.Benzinga.com/markets
# С помощью python и bs4 нужно забрать с главной страницы:
# - заголовок новости (если есть)
# - текст новости (если есть)
# - ссылку на новость
# Данные нужно сохранять в csv таблицу с колонками:
# время,ссылка,заголовок новости,текст новости
# время использовать то, в которое спарсили новость.
# Программа должна обновлять csv таблицу раз в N секунд (пареметр должен быть настраиваемым)
# Если новость уже есть в таблице, её добавлять заново не нужно


def task_4(time_sleep: int = 300):
    headers = {'user-agent': FakeUserAgent().random}
    url = 'https://www.Benzinga.com/markets'

    main_folder = 'data'
    os.makedirs(main_folder, exist_ok=True)
    filename = f'benzinga_news.csv'
    file_path = os.path.join(main_folder, filename)
    titles_exist_list = []

    while True:
        print(f'{datetime.now()} - Start scraping news')

        response = requests.get(url, headers=headers)
        html = BS(response.content, 'html.parser')

        file_exists = os.path.exists(file_path)
        with open(file_path, 'a+', newline='', encoding='utf-8') as file:
            file.seek(0)
            reader = csv.reader(file)
            writer = csv.writer(file)
            if not file_exists:
                writer.writerow(['Time', 'Title', 'Text', 'Link'])

            for row in reader:
                if row[1] not in titles_exist_list:
                    titles_exist_list.append(row[1])

            cards = html.select('.sc-cyVgJG.gWOEHs')

            for card in cards[::-1]:
                title = card.select('.sc-bqjyeg.sc-PqBve span')[0].text

                if title not in titles_exist_list:
                    print(f'{datetime.now()} - News added: {title}')
                    text_card = card.select('span.post-teaser')[0].text
                    row = [
                        datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                        card.select('.sc-bqjyeg.sc-PqBve span')[0].text,
                        text_card.strip() if text_card.strip() != '' else 'Nothing',
                        card.select('a.post-card-article-link')[0].get('href')
                    ]

                    writer.writerow(row)

        print(f'{datetime.now()} - End scraping, wait for {time_sleep / 60} minutes')
        time.sleep(time_sleep)


def main():
    task_4()


if __name__ == "__main__":
    main()
