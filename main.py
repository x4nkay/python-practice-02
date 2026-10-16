def numb(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Ошибка: введите корректное число.")

def yn(prompt):
    while True:
        an = input(prompt).strip().lower()
        if an in ("да", "нет"):
            return an
        print("Ошибка: введите 'да' или 'нет'.")


def calculate():
    n1 = numb("Введите первое число: ")
    o = input("Введите операцию (+, -, *, /, //, %, ^): ").strip()
    n2 = numb("Введите второе число: ")

    if o in ("/", "//", "%") and n2 == 0:
        print("Ошибка: делить на ноль нельзя")
        return

    if o == "+":
        r = n1 + n2
    elif o == "-":
        r = n1 - n2
    elif o == "*":
        r = n1 * n2
    elif o == "/":
        r = n1 / n2
    elif o == "//":
        r = n1 // n2
    elif o == "%":
        r = n1 % n2
    elif o == "^":
        r = n1 ** n2
    else:
        print("Неизвестная операция")
        return

    if isinstance(r, float) and r.is_integer():
        result = int(r)

    print(f"Результат: {r}")


def main():
    print(" Консольный калькулятор ")
    while True:
        calculate()
        an = yn("Хотите выполнить ещё одну операцию? (да/нет): ")
        if an == "нет":
            print("Работа программы завершена.")
            break


if __name__ == "__main__":
    main()