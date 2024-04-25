# Считываем число с клавиатуры
number = float(input("Введите число: "))

# Проверяем знак числа и выводим соответствующий результат
if number > 0:
    print("+")
elif number < 0:
    print("-")
else:
    print("0")
