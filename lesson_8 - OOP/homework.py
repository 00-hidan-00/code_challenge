import random


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
    def __init__(self, balance: int | float = None, owner: str = ''):
        if not balance or balance < 0:
            self.balance = random.randint(100, 15000)
        else:
            self.balance = balance
        self.owner = owner

    def deposit(self, deposit_amount: int | float) -> str:
        if deposit_amount > 0:
            self.balance += deposit_amount
            return f'Owner {self.owner}\'s balance has been deposited by {deposit_amount}. Final balance: {self.balance}'
        else:
            return 'The deposit amount must be greater than 0'

    def withdraw(self, withdraw_amount: int | float) -> str:
        if withdraw_amount <= 0:
            return 'The withdrawal amount must be greater than 0'
        elif withdraw_amount > self.balance:
            return 'Insufficient balance for withdrawal'
        else:
            self.balance -= withdraw_amount
            return f'Owner {self.owner}\'s balance has been withdrawn by {withdraw_amount}. Final balance: {self.balance}'


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
            self.books.remove(name_book)
            return f'Book {name_book} given by: {name_member}'

    def return_book(self, name_member: str, name_book: str) -> str:
        if name_member not in self.members:
            return f'No member: {name_member}'
        elif name_book not in self.library_data_dict[name_member]:
            return f'{name_member} doesn\'t have a book: {name_book}'
        else:
            self.library_data_dict[name_member].remove(name_book)
            self.books.append(name_book)
            return f'Book {name_book} returned by: {name_member}'


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
    books = ['1', '2', '3']
    members = ['Davyd', 'Masha', 'Sasha']
    library = Library(books=books, members=members)
    # print(library.books)
    # print(library.add_book('444'))
    # print(library.books)
    # print(library.remove_book('2'))
    # print(library.books)
    # print()
    print(f'{library.members=}')
    print(library.add_member('Misha'))
    print(f'{library.members}')
    print()
    print(f"{library.books=}")
    print(f"{library.library_data_dict=}")
    print(library.checkout_book(name_member='Misha', name_book='3'))
    print(f"{library.books=}")
    print(f"{library.library_data_dict=}")
    print()
    print(library.return_book(name_member='Misha', name_book='3'))
    print(f"{library.books=}")
    print(f"{library.library_data_dict=}")


if __name__ == "__main__":
    main()
