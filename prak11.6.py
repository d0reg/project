# Функция для нахождения наибольшего элемента и его индекса в списке
def find_max_index(lst):
    max_value = lst[0]
    max_index = 0
    for i in range(1, len(lst)):
        if lst[i] > max_value:
            max_value = lst[i]
            max_index = i
    return max_index

# Функция для нахождения наименьшего элемента и его индекса в списке
def find_min_index(lst):
    min_value = lst[0]
    min_index = 0
    for i in range(1, len(lst)):
        if lst[i] < min_value:
            min_value = lst[i]
            min_index = i
    return min_index

# Список из 20 целых чисел
list_1 = [int(input(f"Введите {i+1}-е целое число: ")) for i in range(20)]

# Находим индекс наибольшего элемента в списке list_1
max_index = find_max_index(list_1)

# Меняем местами наибольший элемент и первый элемент
list_1[0], list_1[max_index] = list_1[max_index], list_1[0]

print("Список из 20 целых чисел с наибольшим элементом, поменянным местами с первым элементом:", list_1)

# Список из 10 целых чисел
list_2 = [int(input(f"Введите {i+1}-е целое число: ")) for i in range(10)]

# Находим индекс наименьшего элемента в списке list_2
min_index = find_min_index(list_2)

# Меняем местами наименьший элемент и последний элемент
list_2[-1], list_2[min_index] = list_2[min_index], list_2[-1]

print("Список из 10 целых чисел с наименьшим элементом, поменянным местами с последним элементом:", list_2)

# Список из 15 вещественных чисел
list_3 = [float(input(f"Введите {i+1}-е вещественное число: ")) for i in range(15)]

# Находим индекс наибольшего элемента в списке list_3
max_index = find_max_index(list_3)

# Меняем местами наибольший элемент и последний элемент
list_3[-1], list_3[max_index] = list_3[max_index], list_3[-1]

print("Список из 15 вещественных чисел с наибольшим элементом, поменянным местами с последним элементом:", list_3)
