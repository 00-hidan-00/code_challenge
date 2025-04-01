import csv
import json
import os

# Lesson notes:
# (https://spurious-factory-624.notion.site/JSON-CSV-1699fddf9bf34c43ad0fd229afd1be7b?pvs=4)


# Чтение файла через python


path = os.path.join("data_lesson", "example.txt")
# открытие файла
f = open(path, encoding='utf-8')


# Первый способ чтения файла - "прочитать всё и сразу"
def example_1():
    text = f.read()
    f.close()


# 2 способ чтения файла - "построчное чтение"
def example_2():
    line_1 = f.readline()
    line_2 = f.readline()
    f.close()


# Вторым способом можно читать файл в цикле:
def example_3():
    line = f.readline()
    # while len(line) > 0:
    while line:
        print(line, end='')
        line = f.readline()
    f.close()


# 3 Способ чтения файла - "получение списка всех строк"
def example_4():
    lines = f.readlines()
    f.close()


# 4 Способ чтеня файла - "построчно в цикле for" (САМЫЙ УДОБНЫЙ СПОСОБ)
def example_5():
    for line in f:
        print(line.strip())
    f.close()


# ВАЖНО!!!!!!!!!
# Не забываем закрыть файл
# f.close()


# Запись в файл
# Запись в файл через python
def example_6():
    f = open(path, 'a+', encoding='utf-8')
    f.write('какой-то текст\n')
    f.write('вторая строка')
    f.close()


# Менеджен контекста with

def example_7():
    with open(path, encoding='utf-8') as f:
        text = f.read()


# JSON

def example_8():
    # json.dumps(obj) - превращает obj python в json
    # json.loads(str) - превращает json-строку в obj python

    d = {
        'a': 1,
        'b': 2,
        'c': 3,
    }

    j = json.dumps(d)
    print(j)  # '{"a": 1, "b": 2, "c": 3}'
    print(type(j))  # <class 'str'>
    d2 = json.loads(j)
    print(d2)  # {'a': 1, 'b': 2, 'c': 3}
    print(type(d2))  # <class 'dict'>

    # json.dump(obj, fp) - превращает obj python в json, который записывается в поток fp
    # json.load(fp) - превращает json из файла fp в obj python

    path = os.path.join("data_lesson", "example.csv")

    with open(path, 'w') as file:
        json.dump(d, file)

    with open(path) as file:
        j = json.load(file)
        print(j)  # {'a': 1, 'b': 2, 'c': 3}


# CSV
# Запись в CSV файл
def example_9():
    path = os.path.join("data_lesson", "example.csv")

    '''
    каждая строчка в csv файле представляет собой список (list) в python
    '''

    row1 = ['name', 'age']
    row2 = ['Bob', 17]
    row3 = ['John', 71]

    rows = [row1, row2, row3]
    # rows по сути выглядит так:
    '''
    rows = [
    	['name', 'age'],
    	['Bob', 17],
    	['John', 71],
    ]
    '''

    # запись в csv файл
    with open(path, 'w', newline='') as file:
        writer = csv.writer(file)

        # 1 способ: записывать строки по-очереди:
        writer.writerow(row1)
        writer.writerow(row2)
        writer.writerow(row3)

        # 2 способ: записать сразу все строчки
        writer.writerows(rows)


# Чтение из CSV файла
def example_10():
    path = os.path.join("data_lesson", "example.csv")

    with open(path) as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)  # будет выводить каждую строку как список ['name', 'age']


def example_11():
    path = os.path.join("data_lesson", "example.csv")

    rows = []

    with open(path) as file:
        reader = csv.reader(file)
        for row in reader:
            rows.append(row)

    for i in range(len(rows)):
        for j in range(len(rows[i])):
            if rows[i][j].isdigit():
                rows[i][j] = int(rows[i][j]) + 1

    with open(path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)


def main():
    example_11()


if __name__ == "__main__":
    main()
