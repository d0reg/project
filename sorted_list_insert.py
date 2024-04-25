def insert_into_sorted_list(sorted_list, value):
    """
    Функция для вставки значения в упорядоченный список.

    Параметры:
        sorted_list (list): Упорядоченный список.
        value: Значение, которое нужно вставить в список.

    Возвращает:
        list: Упорядоченный список с добавленным значением.
    """
    index = 0
    while index < len(sorted_list) and sorted_list[index] < value:
        index += 1
    sorted_list.insert(index, value)
    return sorted_list
