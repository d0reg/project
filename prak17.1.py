import random
import string

def generate_passwords(N, K):
    """
    Генерирует N различных паролей длиной K символов.

    Параметры:
    - N (int): Количество паролей для генерации.
    - K (int): Длина каждого пароля.

    Возвращает:
    - list: Список сгенерированных паролей.
    """
    passwords = []
    for _ in range(N):
        password = ''.join(random.choices(string.ascii_letters + string.digits, k=K))
        passwords.append(password)
    return passwords

# Запрос пользователю для ввода количества и длины паролей
N = int(input("Введите количество паролей: "))
K = int(input("Введите длину паролей: "))

print("Список паролей:")
# Генерация и вывод паролей
for password in generate_passwords(N, K):
    print(password)
