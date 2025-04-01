#  Практика:
#
# Простой уровень:
# 1) Создайте класс Car, который имеет атрибуты make (марка) и model (модель). Реализуйте метод display_info(),
#   который выводит информацию о марке и модели автомобиля.


class Car:
    def __init__(self, make: str = '111', model: str = '222'):
        self.make = make
        self.model = model

    def display_info(self) -> dict[str, str]:
        return {'make': self.make, 'model': self.model}


# 2) Создайте класс Rectangle, который имеет атрибуты width (ширина) и height (высота).
#   Реализуйте метод calculate_area(), который возвращает площадь прямоугольника.


class Rectangle:
    def __init__(self, width: int | float, height: int | float):
        self.width = width
        self.height = height

    def calculate_area(self) -> int | float:
        return self.width * self.height


# Средний уровень:
# 1) Разработайте класс BankAccount, который имеет атрибуты balance (баланс) и owner (владелец).
#   Реализуйте методы deposit(amount) для внесения средств на счет и withdraw(amount) для снятия средств со счета.
#       Учтите возможность проверки наличия достаточного баланса перед снятием.
# 2) Создайте класс Library, представляющий библиотеку.
#   Класс должен иметь атрибуты books (список книг) и members (список членов библиотеки).
#   Реализуйте методы add_book(book) для добавления книги в библиотеку,
#   remove_book(book) для удаления книги из библиотеки, add_member(member) для добавления нового члена библиотеки
#   и remove_member(member) для удаления члена библиотеки.
#   Также реализуйте метод checkout_book(book, member) для выдачи книги члену библиотеки и return_book(book, member)
#   для возврата книги в библиотеку.
#
# Сложный уровень:
# 1) Создайте систему регистрации на конференцию. Реализуйте классы Conference (конференция),
#   Participant (участник) и RegistrationSystem (система регистрации).
#   Класс Conference должен иметь атрибуты name (название) и capacity (вместимость),
#   класс Participant - атрибуты name (имя) и email (электронная почта),
#   а класс RegistrationSystem - атрибуты conference (конференция) и participants (список участников),
#   а также методы register(participant) для регистрации участника и is_registration_available()
#   для проверки доступности регистрации на конференцию.
#   Реализуйте проверку наличия свободных мест на конференции перед регистрацией.
# 2) Создайте игру "Магазин животных".
#   Реализуйте базовый класс Animal (животное) с атрибутами name (имя) и price (цена), а также методом sound(),
#   который возвращает звук, издаваемый животным. От него унаследуйте классы Dog, Cat и Bird,
#   каждый из которых переопределяет метод sound() для возврата соответствующего звука для каждого типа животного.
#   Класс Shop должен иметь атрибуты animals (список доступных животных) и budget (бюджет магазина),
#   а также методы buy_animal(animal) для покупки животного и sell_animal(animal) для продажи животного.
#   Реализуйте проверки наличия достаточного бюджета у магазина для покупки и наличия животного в магазине для продажи.


def main():
    area = Rectangle(width=3.3, height=4).calculate_area()
    print(area)


if __name__ == "__main__":
    main()
