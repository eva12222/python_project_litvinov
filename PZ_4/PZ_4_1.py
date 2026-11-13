# Вариант 21, задача 1
# Дано вещественное число X (|X|<1) и целое число N (>0). Найти значение выражения
# X - X^2/2 + X^3/3 - ... + (-1)^(N-1) * X^N / N

x = input("Введите число X (|X|<1): ")
n = input("Введите число N (N>0): ")
while True:
    try:
        x = float(x)
        n = int(n)
        break
    except ValueError:
        print("Введите число!")
        x = input("Введите число X (|X|<1): ")
        n = input("Введите число N (N>0): ")

if abs(x) >= 1 or n <= 0:
    print("X должно быть по модулю меньше 1, а N больше 0!")
else:
    a = 0
    b = 1
    c = x
    d = 1
    while d <= n:
        a += b * c / d
        b = -b
        c *= x
        d += 1
    print(f"Значение выражения: {a}")