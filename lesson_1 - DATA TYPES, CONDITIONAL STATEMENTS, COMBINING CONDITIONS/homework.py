# Level 1

# 1) Пользователь вводит число a и число b. Возвести а в степень b

def lvl_1_task_1():
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    result = a ** b
    print(f"{a} raised to the power of {b} is {result}")
    return result


# 2) Пользователь вводит число от 1 до 7. Вывести соответствующий день недели

def lvl_1_task_2():
    number = int(input("Enter a number from 1 to 7: "))

    if 1 <= number <= 7:
        if number == 1:
            print("Monday")
        elif number == 2:
            print("Tuesday")
        elif number == 3:
            print("Wednesday")
        elif number == 4:
            print("Thursday")
        elif number == 5:
            print("Friday")
        elif number == 6:
            print("Saturday")
        elif number == 7:
            print("Sunday")
    else:
        print("The number is not equal to 1-7")

    # days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    #
    # if 1 <= number <= 7:
    #     print(days_of_week[number - 1])
    # else:
    #     print("The number is not equal to 1-7")


# 3) Пользователь вводит 2 числа. Вывести наибольшее из них

def lvl_1_task_3():
    first_number = int(input("Enter the first number: "))
    second_number = int(input("Enter the second number: "))
    #
    if first_number > second_number:
        print(f"The largest number: {first_number}")
        return first_number
    elif first_number < second_number:
        print(f"The largest number: {second_number}")
        return second_number
    else:
        print("The numbers are equal.")
        return first_number

    # if a == b:
    #     print("The numbers are equal.")
    #     return a
    # else:
    #     result = max(a, b)
    #     print(f"The largest number: {result}")
    #     return result


# 4) Пользователь вводит свой депозит и хороший курс доллара. Вывести в консоль депо в грн и заплакать

def lvl_1_task_4():
    deposit = int(input("Enter your deposit: "))
    dollar_exchange_rate = int(input("Enter dollar exchange rate: "))

    print(f"{deposit / dollar_exchange_rate:.2f}$ :*(")


################################

# Level 2


# 1) Пользователь вводит число. Если оно четное, вывести "четное". Если оно нечетное, вывести "нечетное"

def lvl_2_task_1():
    number = int(input("Enter the number: "))
    if number % 2 == 0:
        print("Even number")
    else:
        print("Odd number")


# 2) Пользователь вводит 3 числа. Вывести наименьшее из них

def lvl_2_task_2():
    number_1 = int(input("Enter the first number: "))
    number_2 = int(input("Enter the second number: "))
    number_3 = int(input("Enter the third number: "))

    if number_1 <= number_2 and number_1 <= number_3:
        print(f"The smallest number: {number_1}")
    elif number_2 <= number_1 and number_2 <= number_3:
        print(f"The smallest number: {number_2}")
    else:
        print(f"The smallest number: {number_3}")

    # if number_1 == number_2 == number_3:
    #     print("The numbers are equal.")
    # else:
    #     print(f"The smallest number: {min(number_1, number_2, number_3)}")


# 3) Из нарнийского чата Аня узнала, что рекомендуется спать хотя бы A часов в сутки, но пересыпать тоже вредно
# и не стоит спать более B часов. Сейчас Аня спит H часов в сутки.
# Если режим сна Ани удовлетворяет рекомендациям Сергея, выведите “Это нормально”.
# Если Аня спит менее A часов, выведите “Недосып”, если же более B часов, то выведите “Пересып”.
# Получаемое число A всегда меньше либо равно B (то есть это проверять не надо).

def lvl_2_task_3():
    a = int(input("Enter number A: "))
    b = int(input("Enter number B: "))
    h = int(input("Enter number H: "))

    if a <= h <= b:
        print("Это нормально")
    elif a > h:
        print("Недосып")
    elif b < h:
        print("Пересып")


################################

# Level 3

# 1) Написать простой калькулятор, который считывает с пользовательского ввода три строки:
# первое число, второе число и операцию, после чего применяет операцию к введенным числам
# (“первое число” “операция” “второе число”) и выводит результат на экран.
# Поддерживаемые операции: +, -, /, *, mod, pow, div, где:
#
# mod - это взятие остатка от деления,
# pow - возведение в степень,
# div - целочисленное деление.

def lvl_3_task_1():
    number_1 = int(input("Enter the first number: "))
    number_2 = int(input("Enter the second number: "))
    operation = input("Enter operation: ")

    if operation == "+":
        print(f"{number_1} {operation} {number_2} = {number_1 + number_2}")
    elif operation == "-":
        print(f"{number_1} {operation} {number_2} = {number_1 - number_2}")
    elif operation == "/" and number_2 != 0:
        print(f"{number_1} {operation} {number_2} = {number_1 / number_2}")
    elif operation == "*":
        print(f"{number_1} {operation} {number_2} = {number_1 * number_2}")
    elif operation == "mod" and number_2 != 0:
        print(f"{number_1} {operation} {number_2} = {number_1 % number_2}")
    elif operation == "pow":
        print(f"{number_1} {operation} {number_2} = {number_1 ** number_2}")
    elif operation == "div" and number_2 != 0:
        print(f"{number_1} {operation} {number_2} = {number_1 // number_2}")
    else:
        print("Invalid operation or division by zero")


# 2) даны 2 числа a и b. Определить, делится ли a на b нацело. Делится ли b на a?

def lvl_3_task_2():
    number_1 = int(input("Enter the first number: "))
    number_2 = int(input("Enter the second number: "))

    if number_1 % number_2 == 0:
        print(f"{number_1} на {number_2} делится нацело")
    else:
        print(f"{number_1} на {number_2} НЕ делится нацело")

    if number_2 % number_1 == 0:
        print(f"{number_2} на {number_1} делится нацело")
    else:
        print(f"{number_2} на {number_1} НЕ делится нацело")


# 3) дано трёхзначное число. Определить, есть ли среди его цифр одинаковые

def lvl_3_task_3():
    number = int(input("Please enter a three digit number: "))
    if 100 <= number <= 999:

        digit_1 = number // 100
        digit_2 = (number // 10) % 10
        digit_3 = number % 10

        if digit_1 == digit_2 or digit_1 == digit_3 or digit_2 == digit_3:
            print("Есть одинаковые цифры")
        else:
            print("Нет одинаковых цифр")
    else:
        print("Введено не трёхзначное число или не число")

    # if len(number)== 3 and number.isdigit():
    #     if number[0] == number[1] or number[0] ==number[2] or number[1] == number[2]:
    #         print("Есть одинаковые цифры")
    #     else:
    #         print("Нет одинаковых цифр")
    # else:
    #     print("Введено не трёхзначное число или не число")

################################

def main():
    lvl_3_task_3()


if __name__ == "__main__":
    main()
