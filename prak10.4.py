seq = input("Введите последовательность символов: ")

letters_set = set()
for char in seq:
    if ('A' <= char <= 'F') or ('X' <= char <= 'Z'):
        letters_set.add(char)

print("letters_set:", letters_set)
