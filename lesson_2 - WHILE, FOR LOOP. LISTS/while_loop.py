# Lesson notes:
# https://spurious-factory-624.notion.site/for-while-4d96c8a9e2c041bfb2bf035b847a3122?pvs=4


def exemple_1():
    i = 1
    while i < 6:
        print(i)
        i += 1


def exemple_2():
    answer = int(input("Guess the number: "))
    guess = int(input("Try to guess the number: "))
    attempts = 1

    while guess != answer:
        guess = int(input("Try to guess the number: "))
        attempts += 1

    print(f"You guessed the number with {attempts}")


def exemple_3():
    i = float(input("Enter a number: "))
    while i != 0.3:
        print(i)
        i += 0.1



def exemple_4():
    i = 1
    while i < 6:

        if i == 3:
            break

        print(i)
        i += 1


def exemple_5():
    i = 1
    while i <= 10:
        if i % 2 == 1:
            i += 1
            continue
        print(i)
        i += 1


def exemple_6():
    lst = [12, 5, 76, 123, 8, 98, 3, 65]

    i, s = 0, 0

    while i < len(lst):
        i += 1
        s += lst[i]

    print(f"Sum of the list: {s}")


def main():
    exemple_6()


if __name__ == "__main__":
    main()
