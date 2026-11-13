# Вариант 21, задача 2
# Даны два числа. Вывести порядковый номер меньшего из них.
a = input("Введите первое число: ")
b = input("Введите второе число: ")
while True:
    try:
        a = int(a)
        b = int(b)
        break
    except ValueError:
        print("Ошибка! Введите числа!")
        a = input("Введите первое число: ")
        b = input("Введите второе число: ")

if a < b:
    print(1)
elif b < a:
    print(2)
else:
    print("Числа равны")