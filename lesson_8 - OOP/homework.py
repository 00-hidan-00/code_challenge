import random
from decimal import Decimal


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

class BankAccount:
    def __init__(self, balance: int | float | Decimal | None = None, owner: str = ''):
        if not balance or Decimal(f'{balance}') < 0:
            self.balance = Decimal(f'{random.randint(100, 15000)}')
        else:
            self.balance = Decimal(f'{balance}')
        self.owner = owner

    def deposit(self, deposit_amount: int | float | Decimal) -> str:
        decimal_deposit_amount = Decimal(f'{deposit_amount}')
        if decimal_deposit_amount > 0:
            self.balance += decimal_deposit_amount
            return f'Owner {self.owner}\'s balance has been deposited by {decimal_deposit_amount}. Final balance: {self.balance}'
        else:
            return 'The deposit amount must be greater than 0'

    def withdraw(self, withdraw_amount: int | float | Decimal) -> str:
        decimal_withdraw_amount = Decimal(f'{withdraw_amount}')
        if decimal_withdraw_amount <= 0:
            return 'The withdrawal amount must be greater than 0'
        elif decimal_withdraw_amount > self.balance:
            return 'Insufficient balance for withdrawal'
        else:
            self.balance -= decimal_withdraw_amount
            return f'Owner {self.owner}\'s balance has been withdrawn by {decimal_withdraw_amount}. Final balance: {self.balance}'

    def __str__(self):
        return f'owner: {self.owner} | balance: {self.balance}'


# def main():
#     a = BankAccount(owner='Davyd', balance='1000')
#     b = BankAccount(owner='Masha', balance='750')
#     print(a)
#     print(b)
#     print(a.deposit('300'))
#     print(b.withdraw('600'))
#     print(a)
#     print(b)
#     print(a.deposit('300'))
#     print(b.withdraw('600'))
#     print(a)
#     print(b)


# 2) Создайте класс Library, представляющий библиотеку.
#   Класс должен иметь атрибуты books (список книг) и members (список членов библиотеки).
#   Реализуйте методы add_book(book) для добавления книги в библиотеку,
#   remove_book(book) для удаления книги из библиотеки, add_member(member) для добавления нового члена библиотеки
#   и remove_member(member) для удаления члена библиотеки.
#   Также реализуйте метод checkout_book(book, member) для выдачи книги члену библиотеки и return_book(book, member)
#   для возврата книги в библиотеку.


class Library:

    def __init__(self, books: list[str], members: list[str]):
        self.books = books
        self.members = members
        self.library_data_dict = {member: [] for member in self.members}

    def add_book(self, name_book: str) -> str:
        self.books.append(name_book)
        return f'Add book: {name_book}'

    def remove_book(self, name_book: str) -> str:
        if name_book in self.books:
            self.books.remove(name_book)
            return f'Remove book: {name_book}'
        else:
            return f'No book found: {name_book}'

    def add_member(self, name_member: str) -> str:
        if name_member not in self.members:
            self.members.append(name_member)
            self.library_data_dict[name_member] = []
            return f'Add member: {name_member}'
        else:
            return f'Member {name_member} already exists'

    def remove_member(self, name_member: str) -> str:
        if name_member in self.members:
            self.members.remove(name_member)
            del self.library_data_dict[name_member]
            return f'Remove member: {name_member}'
        else:
            return f'No member: {name_member}'

    def checkout_book(self, name_member: str, name_book: str) -> str:
        if name_member not in self.members:
            return f'No member: {name_member}'
        elif name_book not in self.books:
            return f'No book: {name_book}'
        else:
            if name_book in self.library_data_dict[name_member]:
                return f'{name_member} already has the book: {name_book}'
            self.library_data_dict[name_member].append(name_book)
            self.remove_book(name_book)
            return f'Book {name_book} given by: {name_member}'

    def return_book(self, name_member: str, name_book: str) -> str:
        if name_member not in self.members:
            return f'No member: {name_member}'
        elif name_book not in self.library_data_dict[name_member]:
            return f'{name_member} doesn\'t have a book: {name_book}'
        else:
            self.library_data_dict[name_member].remove(name_book)
            self.add_book(name_book)
            return f'Book {name_book} returned by: {name_member}'

    def __str__(self):
        return f'books: {self.books} | members: {self.members}\n{self.library_data_dict}'


# Сложный уровень:
# 1) Создайте систему регистрации на конференцию.
# Реализуйте классы Conference (конференция), Participant (участник) и RegistrationSystem (система регистрации).

#   Класс Conference должен иметь атрибуты name (название) и capacity (вместимость),
#   класс Participant - атрибуты name (имя) и email (электронная почта),
#   а класс RegistrationSystem - атрибуты conference (конференция) и participants (список участников),

#   а также методы register(participant) для регистрации участника и is_registration_available()
#   для проверки доступности регистрации на конференцию.

#   Реализуйте проверку наличия свободных мест на конференции перед регистрацией.

class Conference:
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity


class Participant:
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email

    def __repr__(self):
        return f'name: {self.name} | email: {self.email}'


class RegistrationSystem:
    def __init__(self, conference: Conference, participants: list[Participant]):
        self.conference = conference
        self.participants = participants

    def __str__(self):
        return f'conference: {self.conference.name} | participants: {self.participants}'

    def register(self, participant: Participant) -> str:
        if not self.is_registration_available():
            return f'All seats for the {self.conference.name} conference are taken'

        if participant.email in self.participants:
            return f'{participant.name} - {participant.email} is already registered'

        self.participants.append({participant.email: participant.name})
        return f'{participant.name} - {participant.email}: registered for the {self.conference.name} conference'

    def is_registration_available(self) -> bool:
        return len(self.participants) < self.conference.capacity


# def main():
#     conference = Conference(name='1', capacity=3)
#     participants = [
#         Participant(name='Davyd', email='asddsadsda@gmail.com'),
#         Participant(name='Davydd', email='asddsadsda@gmail.com'),
#         Participant(name='Davyddd', email='aвsddsadsda@gmail.com'),
#         Participant(name='Davydddd', email='aввsddsadsda@gmail.com'),
#         Participant(name='Davydddddd', email='aввввsddsadsda@gmail.com')
#     ]
#
#     registration_system = RegistrationSystem(conference=conference, participants=participants)
#
#     print(registration_system)


# 2) Создайте игру "Магазин животных".
#   Реализуйте базовый класс Animal (животное) с атрибутами name (имя) и price (цена), а также методом sound(),
#   который возвращает звук, издаваемый животным. От него унаследуйте классы Dog, Cat и Bird,

#   каждый из которых переопределяет метод sound() для возврата соответствующего звука для каждого типа животного.

#   Класс Shop должен иметь атрибуты animals (список доступных животных) и budget (бюджет магазина),
#   а также методы buy_animal(animal) для покупки животного и sell_animal(animal) для продажи животного.
#   Реализуйте проверки наличия достаточного бюджета у магазина для покупки и наличия животного в магазине для продажи.


class Animal:
    def __init__(self, name: str, price: int | float):
        self.name = name
        self.price = price

    def sound(self) -> str:
        pass

    def __str__(self):
        return f'{self.__class__.__name__} "{self.name}" — {self.price}$'


class Dog(Animal):
    def sound(self) -> str:
        return 'Woof!'


class Cat(Animal):
    def sound(self) -> str:
        return 'Meow!'


class Bird(Animal):
    def sound(self) -> str:
        return 'Tweet!'


class Shop:
    def __init__(self, animals: list[Animal], budget: int | float = 1000):
        self.animals = animals
        self.budget = budget

    def __str__(self):
        return f'animals: {[animal.name for animal in self.animals]} | budget: {self.budget}'

    def buy_animal(self, animal: Animal) -> str:
        if self.budget >= animal.price:
            self.animals.append(animal)
            self.budget -= animal.price
            return f'{animal} was bought. Budget left: {self.budget}$'
        return f'Not enough money to buy {animal.name}: need {animal.price - self.budget}$ more'

    def sell_animal(self, animal: Animal) -> str:
        if animal in self.animals:
            self.animals.remove(animal)
            self.budget += animal.price
            return f'{animal} was sold. Budget now: {self.budget}$'
        return f'{animal.name} is not in the shop'


def main():
    dog = Dog(name='Rex', price=300)
    cat = Cat(name='Murka', price=500)
    bird = Bird(name='Kesha', price=500)
    shop = Shop(animals=[dog])

    print(f'Initial budget: {shop.budget}$\n')

    print(shop.buy_animal(dog))
    print(shop.buy_animal(bird))
    print()
    print('Current animals in shop:')
    for animal in shop.animals:
        print(f'- {animal} says: {animal.sound()}')
    print()
    print(shop.sell_animal(cat))
    print(shop.sell_animal(bird))  # не в магазине
    print()
    print('Final animals in shop:')
    for animal in shop.animals:
        print(f'- {animal}')
    print(f'Final budget: {shop.budget}$')

    print(shop)


if __name__ == "__main__":
    main()
