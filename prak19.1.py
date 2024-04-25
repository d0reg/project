from PIL import Image

# Открываем изображение
image = Image.open('risunok1.jpg')

# Получаем размеры изображения
width, height = image.size

# Получаем данные о пикселях
pixels = image.load()

# Инициализируем переменные для хранения суммы значений R, G, B
total_r = 0
total_g = 0
total_b = 0

# Проходимся по каждому пикселю и суммируем значения R, G, B
for y in range(height):
    for x in range(width):
        r, g, b = pixels[x, y]
        total_r += r
        total_g += g
        total_b += b

# Вычисляем средние значения R, G, B
avg_r = total_r // (width * height)
avg_g = total_g // (width * height)
avg_b = total_b // (width * height)

# Выводим средние значения на экран
print(f"Среднее значение R: {avg_r}, G: {avg_g}, B: {avg_b}")

# Создаем новое изображение, где каждый пиксель имеет среднее значение R, G, B
new_image = Image.new('RGB', (width, height), (avg_r, avg_g, avg_b))

# Сохраняем новое изображение
new_image.save('risunok2.jpg')

# Закрываем изображение
image.close()
