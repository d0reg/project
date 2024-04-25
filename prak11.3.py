# Создание списка значений под четными номерами
sequence = list(range(16))  # Создаем последовательность из 16 элементов
even_indices_values = [sequence[i] for i in range(len(sequence)) if i % 2 == 0]  # Выбираем значения под четными индексами

# Вывод результата
print("Список значений под четными номерами:", even_indices_values)
