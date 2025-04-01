# Lesson notes:
# (https://spurious-factory-624.notion.site/daf8dba486c54e3999c02ce79ce6d276#43a0654084ac434ab8330986d35f52ad)


import random


# переменная -> поле, свойство, атрибут
# фунция -> метод

# атрибуты объекта (self) - переменные что задаются после def __init__(self, ...):
# атрибуты класса (cls) - переменные что задаются после class MyClass:

# Создание класса и объекта
class MyClass:
    pass


class HumanExemple1:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.height = random.randint(150, 200)

    def show_info(self):
        print(f"name: {self.name}; age: {self.age}; height: {self.height}")


# ----------------------------------------------------------------------------------------------------------------------
# Создание объекта


# john = Human_exemple_1(name='John', age=29)
# bob = Human_exemple_1(name='Bob', age=40)
# alice = Human_exemple_1(name='Alice', age=22)

# alex.show_info()  # name: John; age: 29; height: 173
# alice.show_info()  # name: Alice; age: 22; height: 191


# ----------------------------------------------------------------------------------------------------------------------


# Статические поля и методы

# Статические поля

class HumanExemple2:
    population = 0  # статическое поле

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.height = random.randint(150, 200)
        HumanExemple2.population += 1  # Увеличиваем общее число людей при создании нового экземпляра класса

    def show_info(self):
        print(f"name: {self.name}; age: {self.age}; height: {self.height}")


# Создаем несколько экземпляров класса Human
# person1 = HumanExemple2("Alice", 30)
# person2 = HumanExemple2("Bob", 25)
#
# print("Total population:", HumanExemple2.population)  # Выводим общее число людей


# ----------------------------------------------------------------------------------------------------------------------


# Статические методы

class HumanExemple3:
    @staticmethod
    def adult_age(age: int) -> bool:
        return age >= 18


# Использование статического метода без создания экземпляра класса
# print(HumanExemple3.adult_age(20))  # Выведет True
# print(HumanExemple3.adult_age(15))  # Выведет False

# ----------------------------------------------------------------------------------------------------------------------


# Магические методы

'''
1. `__init__(self, ...)`: Инициализация объекта. Этот метод вызывается при создании нового экземпляра класса.
2. `__str__(self)`: Преобразование объекта в строку. Вызывается при использовании функции `str()` или при использовании объекта в форматированных строках.
3. `__repr__(self)`: Представление объекта. Этот метод вызывается функцией `repr()` для получения представления объекта в виде строки.
4. `__add__(self, other)`: Сложение объектов. Вызывается при использовании оператора `+` для сложения объектов.
5. `__len__(self)`: Получение длины объекта. Вызывается функцией `len()` для получения длины объекта.
6. `__getitem__(self, key)`: Получение элемента по ключу. Вызывается при использовании оператора индексации `[]` для доступа к элементам объекта.
7. `__eq__(self, other)`: Проверка на равенство. Вызывается при использовании оператора сравнения `==`.
8. `__lt__(self, other)`, `__gt__(self, other)`, `__le__(self, other)`, `__ge__(self, other)`: Сравнение объектов. Вызывается при использовании операторов сравнения (`<`, `>`, `<=`, `>=`).
9. `__del__(self)`: Удаление объекта. Вызывается при удалении объекта из памяти.
'''


# ----------------------------------------------------------------------------------------------------------------------


# Деструктор

class HumanExemple4:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.height = random.randint(150, 200)

    def __del__(self):
        print(f"{self.name} is being destroyed")

    def show_info(self):
        print(f"name: {self.name}; age: {self.age}; height: {self.height}")


# Создаем экземпляр класса Human
# person = HumanExemple4("Alice", 30)
# person.show_info()

# Удаляем экземпляр класса Human
# del person  # Это приведет к вызову деструктора


# ----------------------------------------------------------------------------------------------------------------------


# Методы __str__() и __repr__()

class HumanExemple5:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Human: name={self.name}, age={self.age}"


# Создаем объект класса Human
# person = HumanExemple5("Alice", 30)
#
# # Вызываем функцию str() для объекта
# print(str(person))  # Выведет: Human: name=Alice, age=30


# ----------------------------------------------------------------------------------------------------------------------


class HumanExemple6:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Human('{self.name}', {self.age})"


# Создаем объект класса Human
# person = HumanExemple6("Alice", 30)
#
# # Вызываем функцию repr() для объекта
# print(repr(person))  # Выведет: Human('Alice', 30)


# ----------------------------------------------------------------------------------------------------------------------


# Метод __call__()

class HumanExemple7:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __call__(self, action):
        print(f"{self.name} is {action}")


# Создаем экземпляр класса Human
# person = HumanExemple7("Alice", 30)
#
# # Вызываем экземпляр класса как функцию, что вызовет метод __call__()
# person("talking")  # Выведет: Alice is talking

# ----------------------------------------------------------------------------------------------------------------------

# Методы для сравнения

'''
1. `__eq__(self, other)`: Проверка на равенство (==).
2. `__ne__(self, other)`: Проверка на неравенство (!=).
3. `__lt__(self, other)`: Проверка на меньше (<).
4. `__le__(self, other)`: Проверка на меньше или равно (<=).
5. `__gt__(self, other)`: Проверка на больше (>).
6. `__ge__(self, other)`: Проверка на больше или равно (>=).

Методы сравнения - это магические методы, которые используются для определения поведения операторов сравнения.
    Когда объекты сравниваются этими операторами, интерпретатор Python автоматически вызывает нужный метод
    для первого объекта, передавая второй объект в качестве аргумента.
'''


class HumanExemple8:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        if isinstance(other, HumanExemple8):
            return self.name == other.name and self.age == other.age
        return False

    def __lt__(self, other):
        if isinstance(other, HumanExemple8):
            return self.age < other.age
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, HumanExemple8):
            return self.age > other.age
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, HumanExemple8):
            return self.age <= other.age
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, HumanExemple8):
            return self.age >= other.age
        return NotImplemented

    def __ne__(self, other):
        return not self.__eq__(other)


# # Создаем несколько экземпляров класса Human
# person_1 = HumanExemple8("Alice", 30)
# person_2 = HumanExemple8("Bob", 25)
# person_3 = HumanExemple8("Alice", 30)
#
# # Сравниваем объекты
# print(person_1 == person_2)  # Выведет False
# print(person_1 == person_3)  # Выведет True
# print(person_1 < person_2)  # Выведет False
# print(person_1 > person_2)  # Выведет True
# print(person_1 <= person_2)  # Выведет False
# print(person_1 >= person_2)  # Выведет True

# ----------------------------------------------------------------------------------------------------------------------


# Математические методы

'''
1. `__add__(self, other)`: Сложение (`+`).
2. `__sub__(self, other)`: Вычитание (`-`).
3. `__mul__(self, other)`: Умножение (`*`).
4. `__truediv__(self, other)`: Деление (`/`).
5. `__floordiv__(self, other)`: Целочисленное деление (`//`).
6. `__mod__(self, other)`: Остаток от деления (`%`).
7. `__pow__(self, other)`: Возведение в степень (`*`).
8. `__abs__(self)`: Модуль числа (`abs()`).

Математические методы - это магические методы, которые используются для определения поведения метематических операторов.
    Когда мы используем математические операторы с объектами данного класса, интерпретатор Python автоматически вызывает 
    нужный метод для первого объекта, передавая второй объект в качестве аргумента.
'''


class HumanExemple9:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __add__(self, other):
        if isinstance(other, HumanExemple9):
            return self.age + other.age
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, HumanExemple9):
            return self.age - other.age
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, HumanExemple9):
            return self.age * other.age
        return NotImplemented

    def __truediv__(self, other):
        if isinstance(other, HumanExemple9):
            return self.age / other.age
        return NotImplemented

    def __floordiv__(self, other):
        if isinstance(other, HumanExemple9):
            return self.age // other.age
        return NotImplemented

    def __mod__(self, other):
        if isinstance(other, HumanExemple9):
            return self.age % other.age
        return NotImplemented

    def __pow__(self, other):
        if isinstance(other, HumanExemple9):
            return self.age ** other.age
        return NotImplemented

    def __abs__(self):
        return abs(self.age)


# # Создаем два объекта класса Human
# person_1 = HumanExemple9("Alice", 30)
# person_2 = HumanExemple9("Bob", 25)
#
# # Выполняем математические операции
# print(person_1 + person_2)  # Выведет: 55 (сумма возрастов)
# print(person_1 - person_2)  # Выведет: 5 (разница возрастов)
# print(person_1 * person_2)  # Выведет: 750 (произведение возрастов)
# print(person_1 / person_2)  # Выведет: 1.2 (деление возрастов)
# print(person_1 // person_2)  # Выведет: 1 (целочисленное деление возрастов)
# print(person_1 % person_2)  # Выведет: 5 (остаток от деления возрастов)
# print(person_1 ** person_2)  # Выведет: 847288609443 (возведение возраста person1 в степень возраста person2)
# print(abs(person_1 - person_2))  # Выведет: 5 (модуль разности возрастов)

# ----------------------------------------------------------------------------------------------------------------------

# Основные принципы ООП

'''
Основные принципы ООП включают:
1. **Инкапсуляция**: Объединение данных и методов, которые работают с этими данными, в единый объект. 
    Это позволяет скрыть детали реализации и предоставить интерфейс для взаимодействия с объектом.
2. **Наследование**: Возможность создания новых классов на основе существующих (родительских) классов. 
    Новый класс наследует свойства и методы родительского класса и может добавлять к ним новый функционал 
    или изменять существующий.
3. **Полиморфизм**: Возможность использования объектов разных классов через общий интерфейс. 
    Это означает, что методы могут иметь разные реализации в разных классах, но обращаться к ним можно одинаково.
4. **Абстракция**: Отделение сущности от ее реализации. 
    Абстракция позволяет сосредоточиться на ключевых аспектах объекта и игнорировать детали, 
    которые не важны для данного контекста.
'''


# ----------------------------------------------------------------------------------------------------------------------

# Основные принципы ООП в коде

# Инкапсуляция

class HumanExemple10:
    def __init__(self, name, age):
        self.name = name  # публичное поле
        self._age = age  # защищенное поле
        self.__height = 160  # приватное поле

    def get_height(self):
        return self.__height

    def set_height(self, height):
        if height > 0:
            self.__height = height


# # Создаем объект класса Human
# person = HumanExemple10("Alice", 30)
#
# # Публичное поле доступно извне
# print(person.name)  # Выведет: Alice
#
# # Защищенное поле доступно извне, но соглашение говорит, что оно предназначено для внутреннего использования
# print(person._age)  # Выведет: 30
#
# # Приватное поле недоступно извне
# # print(person.__height)  # Ошибка: AttributeError: 'Human' object has no attribute '__height'
#
# # Однако его можно получить и изменить, используя "name mangling"
# print(person._HumanExemple10__height)  # Выведет: 160
# person._HumanExemple10__height = 170
# print(person._HumanExemple10__height)  # Выведет: 170
#
# # Лучше использовать геттеры и сеттеры для доступа к приватным полям
# print(person.get_height())  # Выведет: 170
# person.set_height(175)
# print(person.get_height())  # Выведет: 175
#
# # Список всех полей и методов объекта можно увидеть с помощью функции dir(obj)
# print(
#     dir(person))  # ['_HumanExemple10__height', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_age', 'get_height', 'name', 'set_height']


# ----------------------------------------------------------------------------------------------------------------------

# Наследование


class HumanExemple11:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")


# Класс Student наследует функциональность класса Human
class Student(HumanExemple11):
    def __init__(self, name, age, student_id):
        # Вызываем конструктор родительского класса, чтобы инициализировать общие поля
        super().__init__(name, age)
        self.student_id = student_id

    def study(self, subject):
        print(f"{self.name} is studying {subject}.")


# # Создаем объекты классов Human и Student
# person = HumanExemple11("Alice", 30)
# student = Student("Bob", 20, "S12345")
#
# # Вызываем методы объектов
# person.introduce()  # Выведет: Hello, my name is Alice and I am 30 years old.
# student.introduce() # Выведет: Hello, my name is Bob and I am 20 years old.
# student.study("Math")  # Выведет: Bob is studying Math.


# Полиморфизм

class Weapon:
    def fire(self):
        pass


class Pistol(Weapon):
    def fire(self):
        print("Pistol fires a bullet")


class Bazooka(Weapon):
    def fire(self):
        print("Bazooka fires a rocket")


class Human:
    def shoot(self, weapon):
        weapon.fire()


# # Создаем экземпляры классов
# pistol = Pistol()
# bazooka = Bazooka()
# human = Human()

# # Вызываем метод shoot() объекта human, передавая ему объекты разных классов Weapon
# human.shoot(pistol)   # Выведет: Pistol fires a bullet
# human.shoot(bazooka)  # Выведет: Bazooka fires a rocket

def main():
    ...


if __name__ == "__main__":
    main()
