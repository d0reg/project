# Ввод количества специальностей
num_specialties = int(input("Введите количество специальностей: "))

# Создание словаря для хранения информации о специальностях
specialties_dict = {}

# Ввод информации о специальностях
for _ in range(num_specialties):
    specialty, group_numbers = input("Введите название специальности и номера групп через тире и запятую: ").split('-')
    specialties_dict[specialty] = group_numbers.split(',')

# Запрос номера группы
query_group_number = input("Введите номер группы для поиска специальности: ")

# Поиск специальности по номеру группы
found_specialty = None
for specialty, groups in specialties_dict.items():
    if query_group_number in groups:
        found_specialty = specialty
        break

# Вывод специальности, к которой относится группа
if found_specialty:
    print("Специальность, к которой относится группа", query_group_number + ":", found_specialty)
else:
    print("Строка ответа пуста")