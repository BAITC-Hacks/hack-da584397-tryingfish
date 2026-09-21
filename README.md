# Defect Check
Определяет по картинке: OK или DEFECT.

## Запуск
import sys
import cv2
import numpy as np


def detect_defect(image_path: str) -> None:
    img = cv2.imread(image_path)
    if img is None:
        print(f"Ошибка: не удалось прочитать файл '{image_path}'")
        sys.exit(1)

    # Перевод в HSV для надежного обнаружения красного цвета
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Диапазоны красного цвета в HSV (0-10 и 170-180)
    lower_red1 = np.array([0, 100, 100])
    upper_red1 = np.array([10, 255, 255])

    lower_red2 = np.array([170, 100, 100])
    upper_red2 = np.array([180, 255, 255])

    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
    red_mask = cv2.bitwise_or(mask1, mask2)

    # Подсчет общего количества красных пикселей
    red_pixel_count = np.sum(red_mask > 0)

    # Логика: если найден хотя бы один красный пиксель, это DEFECT
    if red_pixel_count > 0:
        print("DEFECT")
    else:
        print("OK")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Использование: py detect.py <путь_к_изображению>")
        sys.exit(1)

    detect_defect(sys.argv[1])

После этого мы вмещает все файлы в одну папку и делаем detect.py -- в скрипт. После этого мы копируем адрес папки и идем в cmd и пишем команду : cd (ctrl + v) и заходим в директорию нашей папки ( ну в нашу папку) и после этого мы пишем py detect.py whatis.png    или другое название ***.png
 ## Что получилось
Считаем долю красных пикселей. Если есть <1%, то DEFECT, иначе OK.
Тестовые картинки (ok.png, defect.png, 6040.png , whatis.png ) нарисованы в Paint.
Минус: дефект другого цвета скрипт не найдёт. Дальше можно подключить ML-модель.
