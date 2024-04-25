from PIL import Image

# Открываем изображение
image = Image.open('risunok5.jpg')

# Получаем размеры изображения
width, height = image.size

# Получаем данные о пикселях
pixels = image.load()

# Создаем новое изображение для результата
new_image = Image.new('RGB', (width, height))

# Проходимся по каждому пикселю и преобразуем его
for y in range(height):
    for x in range(width):
        r, g, b = pixels[x, y]
        # Находим максимальное и минимальное значение среди компонент пикселя
        max_value = max(r, g, b)
        min_value = min(r, g, b)
        # Записываем минимальное значение в красную компоненту, а максимальное в синюю
        new_color = (min_value, g, max_value)
        # Записываем преобразованный пиксель в новое изображение (переворачиваем по вертикали)
        new_image.putpixel((x, height - y - 1), new_color)

# Сохраняем преобразованное изображение
new_image.save('risunok6.jpg')

# Закрываем изображения
image.close()
new_image.close()
