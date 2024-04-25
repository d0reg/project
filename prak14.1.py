# Ввод количества номеров телефонов
num_phone_numbers = int(input("Введите количество номеров телефонов: "))

# Создание словаря для хранения номеров телефонов
phone_book = {}

# Ввод номеров телефонов и их владельцев
for _ in range(num_phone_numbers):
    phone, name = input("Введите номер телефона и имя через пробел: ").split()
    phone_book[name] = phone

# Запрос имени для поиска номера телефона
query_name = input("Введите имя, чей телефон нужно найти: ")

# Поиск номера телефона по имени
if query_name in phone_book:
    print("Номер телефона:", phone_book[query_name])
else:
    print("Нет в телефонной книге")
