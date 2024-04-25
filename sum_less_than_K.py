def sum_less_than_K(A, K):
    """
    Функция для вычисления суммы элементов списка, меньших заданного значения K.

    Параметры:
        A (list): Список чисел.
        K: Значение, сравниваемое с элементами списка.

    Возвращает:
        float: Сумма элементов списка, меньших K.
    """
    total = 0
    for elem in A:
        if elem < K:
            total += elem
    return total