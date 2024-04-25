from PIL import Image, ImageDraw

# Создаем новое изображение
image = Image.new("RGB", (400, 200), "gray")
draw = ImageDraw.Draw(image)

# Рисуем букву 'Е'
draw.rectangle([20, 20, 40, 120], fill="lightblue")  # Левая вертикальная линия
draw.rectangle([40, 20, 80, 40], fill="lightgreen")   # Верхняя горизонтальная линия
draw.rectangle([40, 60, 80, 80], fill="lightyellow")   # Серединная горизонтальная линия
draw.rectangle([40, 100, 80, 120], fill="lightcoral") # Нижняя горизонтальная линия

# Рисуем букву 'г'
draw.rectangle([110, 20, 130, 120], fill="lightseagreen")  # Вертикальная линия
draw.rectangle([130, 20, 170, 40], fill="lightsalmon")   # Горизонтальная линия

# Рисуем букву 'о'
draw.ellipse([190, 20, 230, 120], fill="lightsteelblue")  # Окружность

# Рисуем букву 'р'
draw.rectangle([250, 20, 270, 120], fill="lightcoral")     # Вертикальная линия
draw.rectangle([270, 20, 310, 60], fill="lightgreen")       # Горизонтальная линия сверху
draw.ellipse([290, 60, 310, 80], fill="lightblue")         # Овал (верхняя часть буквы р)

# Сохраняем изображение
image.save("name6.png")
