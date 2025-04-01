# Lesson notes:
# (https://spurious-factory-624.notion.site/e8494828eee44846926f68e286f80da4)
import json

import requests
from bs4 import BeautifulSoup as BS
from fake_useragent import FakeUserAgent


def exemple_1():
    # пример GET запроса (то же самое, что открыть ссылку через браузер)
    url = 'https://ruprowork.ru/Курск'
    response = requests.get(url)

    # print(response.status_code)  # 200
    # print(response.content)
    # print(response.text)
    # print(type(response.content))  # <class 'bytes'>
    # print(type(response.text))  # <class 'str'>

    # записываем полученный ответ в файл, чтобы открыть в браузере
    with open('test.html', 'w') as f:
        f.write(response.text)


def exemple_2():
    headers = {
        'user-agent': FakeUserAgent().random
    }

    url = 'https://ruprowork.ru/Курск'
    response = requests.get(url, headers=headers)
    print(response.text)


def exemple_3():
    headers = {
        'user-agent': FakeUserAgent().random
    }

    source_url = 'https://ruprowork.ru/'
    url = source_url + 'Курск'
    response = requests.get(url, headers=headers)

    html = BS(response.content, 'html.parser')
    # получаем список карточек
    cards = html.select('.h-list')
    for card in cards:
        # внутри карточки получаем описание
        worker = card.select('.descr h3')[0].text
        print(worker)

        # получаем src изображения
        img_src = card.select('img')[0].get("src")
        print(source_url + img_src)
        response = requests.get(source_url + img_src)
        filename = img_src.split('/')[-1]
        # сохраняем изображение в файл
        with open(filename, 'wb') as f:
            f.write(response.content)


def exemple_4():
    headers = {
        'authority': 'interface.gateway.uniswap.org',
        'accept': '*/*',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'text/plain;charset=UTF-8',
        'origin': 'https://app.uniswap.org',
        'referer': 'https://app.uniswap.org/',
        'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': FakeUserAgent().random,
        'x-request-source': 'uniswap-web',
    }

    data = {
        "tokenInChainId": 42161,
        "tokenIn": "ETH",
        "tokenOutChainId": 42161,
        "tokenOut": "0xFd086bC7CD5C481DCC9C85ebE478A1C0b69FCbb9",
        "amount": "1000000000000000",
        "sendPortionEnabled": True,
        "type": "EXACT_INPUT",
        "intent": "quote",
        "configs": [
            {
                "protocols": ["V2", "V3", "MIXED"],
                "enableUniversalRouter": True,
                "routingType": "CLASSIC",
                "recipient": "0x36F302d18DcedE1AB1174f47726E62212d1CcEAD",
                "enableFeeOnTransferFeeFetching": True
            }
        ]
    }

    response = requests.post('https://interface.gateway.uniswap.org/v2/quote', headers=headers, data=json.dumps(data))
    print(response.status_code)
    print(response.json())
    print(int(response.json()['quote']['quote']) / 10 ** 6)


def main():
    exemple_1()


if __name__ == "__main__":
    main()
