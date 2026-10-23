number = int(input("введите трёхзначное число: "))
if 100 <= number <= 999
    hundreds = number // 100
    tens = (number // 10) % 10
    units = number % 10
    new_number = hundreds * 100 + units * 10 + tens
    print("Новое число:", new_number)
else:
    print("Ошибка: вы введи не трёхзначное")
input("Нажмите Enter для выхода")