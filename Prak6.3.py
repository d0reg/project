# Считываем начальную дистанцию, которую пробежал спортсмен в первый день
distance = float(input("Введите дистанцию, которую спортсмен пробежал в первый день (в км): "))

# Инициализируем переменную для хранения суммарного пути за неделю
total_distance = distance

# Используем цикл с переменной для перебора дней недели (7 дней)
for day in range(2, 8):
    # Увеличиваем дистанцию на 10% от предыдущей дистанции
    distance *= 1.1
    # Добавляем увеличенную дистанцию к суммарному пути
    total_distance += distance

# Выводим суммарный пробег за неделю
print(f"Суммарный пробег спортсмена за неделю: {total_distance:.2f} км")