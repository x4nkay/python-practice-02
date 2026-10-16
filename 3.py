def numb(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Ошибка: пожалуйста, введите целое число.")


def main():
    print("Анализ числа")
    n = numb("Введите число: ")

    print(f"\nВаше число: {n}")
    if n > 0:
        print("Положительное: да")
        print("Отрицательное: нет")
        print("Ноль: нет")
    elif n < 0:
        print("Положительное: нет")
        print("Отрицательное: да")
        print("Ноль: нет")
    else:
        print("Положительное: нет")
        print("Отрицательное: нет")
        print("Ноль: да")
    if n % 2 == 0:
        print("Четное: да")
    else:
        print("Четное: нет")
    if n % 3 == 0:
        print("Делится на 3: да")
    else:
        print("Делится на 3: нет")
    if n % 5 == 0:
        print("Делится на 5: да")
    else:
        print("Делится на 5: нет")
    if n > 1:
        f = True
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                f = False
                break
        if f:
            print("Простое: да")
        else:
            print("Простое: нет")
    else:
        print("Простое: нет")  # 0, 1 и отрицательные не являются простыми

    kol = len(str(abs(n)))
    print(f"Количество цифр: {kol}")


if __name__ == "__main__":
    main()