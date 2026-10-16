def cen(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Ошибка: пожалуйста, введите корректное число.")

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Ошибка: пожалуйста, введите целое число.")

print("Расчет стоимости покупки")

name = input("Введите название товара: ")
c = cen("Введите цену товара: ")
k = cen("Введите количество: ")
s = c*k
pr = 0
if 5000 <= s <= 9999:
    pr = 0.05
elif 10000 <= s <= 14999:
    pr = 0.1
elif s >= 15000:
    pr = 0.15

sk = s * pr
i = s - pr

# 4. Вывод результатов
print(f"Товар: {name}")
print(f"Цена: {c}")
print(f"Количество: {k}")
print(f"Итого: {s}")
print(f"Скидка в процентах: {pr} %")
print(f"Скидка в рублях: {sk}")
print(f"Итоговая цена: {i}")
