import cv2
import numpy as np

# Загрузка изображения
image = cv2.imread('blum.r88na4v82j.jpg')

# Преобразование изображения в HSV
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Определение диапазона цвета зелённый
lower_green = np.array([40, 40, 40])
upper_green = np.array([80, 255, 255])

# Фильтрация по цвету
mask = cv2.inRange(hsv_image, lower_green, upper_green)

# Удаление шума с помощью морфологической операции
kernel = np.ones((5, 5), np.uint8)
mask = cv2.erode(mask, kernel, iterations=2)
mask = cv2.dilate(mask, kernel, iterations=2)

# Поиск контуров
contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Вывод координат контуров
for contour in contours:
    x, y, w, h = cv2.boundingRect(contour)
    print(f'Координаты: ({x}, {y}), ширина: {w}, высота: {h}')

    # Отрисовка прямоугольника вокруг контура
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Вывод результата
cv2.imshow('Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()