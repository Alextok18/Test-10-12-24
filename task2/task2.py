import sys
import math

def read_circle(file_path):
    """Считывает координаты центра окружности и радиус из файла."""
    with open(file_path, 'r') as file:
        x, y, r = map(float, file.readline().split())
    return x, y, r

def read_points(file_path):
    """Считывает координаты точек из файла."""
    points = []
    with open(file_path, 'r') as file:
        for line in file:
            points.append(tuple(map(float, line.split())))
    return points

def determine_position(circle, points):
    """Определяет положение точек относительно окружности."""
    cx, cy, r = circle
    results = []
    for x, y in points:
        distance = math.sqrt((x - cx) ** 2 + (y - cy) ** 2)
        if math.isclose(distance, r, rel_tol=1e-9):  # Точка лежит на окружности
            results.append(0)
        elif distance < r:  # Точка внутри
            results.append(1)
        else:  # Точка снаружи
            results.append(2)
    return results

def main():
    # Получение путей к файлам из аргументов командной строки
    if len(sys.argv) != 3:
        print("Укажите пути к файлам с окружностью и точками в качестве аргументов!")
        return

    circle_file = sys.argv[1]
    points_file = sys.argv[2]

    # Считывание данных из файлов
    circle = read_circle(circle_file)
    points = read_points(points_file)

    # Определение положения точек
    results = determine_position(circle, points)

    # Вывод результата
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
