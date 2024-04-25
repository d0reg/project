# Программа, использующая созданный модуль

import my_module

# Вывод описания модуля
print("Описание модуля:")
my_module.module_description()

# Приветствие пользователя
name = input("Введите ваше имя: ")
print(my_module.greet_user(name))

# Сложение двух чисел
num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))
print("Сумма чисел:", my_module.add(num1, num2))
