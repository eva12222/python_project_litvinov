# Вариант 21, задача 2
# Дано целое число N (>0). Если оно является степенью числа 3, то вывести TRUE,
# если не является - вывести FALSE.

n = input("Введите число N (n>0): ")
while True:
    try:
        n = int(n)
        break
    except ValueError:
        print("Введите число!")
        n = input("Введите число N (n>0): ")

if n <= 0:
    print("Число должно быть больше 0!")
else:
    while n % 3 == 0:
        n //= 3
    if n == 1:
        print("TRUE")
    else:
        print("FALSE")