def numb(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Ошибка: пожалуйста, введите корректное число.")
n1 = numb("Введите первое число: ")
o = input("Введите операцию: ").strip()
n2 = numb("Введите второе число: ")
if (o in ["/", "//", "%"]) and n2 == 0:
    print("Ошибка: делить на ноль нельзя")
elif o == "*":
    print("Результат:", n1 * n2)
elif o == "+":
    print("Результат:", n1 + n2)
elif o == "-":
    print("Результат:", n1 - n2)
elif o == "/":
    print("Результат:", n1 / n2)
elif o == "//":
    print("Результат:", n1 // n2)
elif o == "%":
    print("Результат:", n1 % n2)
elif o == "^":
    print("Результат:", n1 ** n2)
else:
    print("Неизвестная операция")