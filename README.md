# Defect Check
Определяет по картинке: OK или DEFECT.

## Запуск
pip install pillow
python check.py ok.png
python check.py defect.png

## Что получилось
Считаем долю красных пикселей. Если больше 5%, то DEFECT, иначе OK.
Тестовые картинки (ok.png, defect.png) нарисованы в Paint.
Минус: дефект другого цвета скрипт не найдёт. Дальше можно подключить ML-модель.
