import math


class Shape:
    def __init__(self, name, color):
        self.__name = name
        self.__color = color

    def get_name(self):
        return self.__name

    def get_color(self):
        return self.__color


class Polygon(Shape):
    def __init__(self, name, color, sides):
        super().__init__(name, color)
        self.__sides = sides

    def is_convex(self):
        n = len(self.__sides)
        if n < 3:
            return False
        det = 0
        for i in range(n):
            x1, y1 = self.__sides[i]
            x2, y2 = self.__sides[(i + 1) % n]
            x3, y3 = self.__sides[(i + 2) % n]
            det += (x2 - x1) * (y3 - y2) - (y2 - y1) * (x3 - x2)
        return det > 0

    def area(self):
        n = len(self.__sides)
        if n < 3:
            return 0.0
        area = 0
        for i in range(n):
            x1, y1 = self.__sides[i]
            x2, y2 = self.__sides[(i + 1) % n]
            area += (x1 * y2 - x2 * y1)
        return 0.5 * abs(area)

    def perimeter(self):
        n = len(self.__sides)
        perimeter = 0
        for i in range(n):
            x1, y1 = self.__sides[i]
            x2, y2 = self.__sides[(i + 1) % n]
            side_length = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
            perimeter += side_length
        return perimeter


class Rectangle(Polygon):
    def __init__(self, name, color, width, height):
        super().__init__(name, color, [(0, 0), (width, 0), (width, height), (0, height)])
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return 2 * (self.__width + self.__height)

    def set_dimensions(self, width, height):
        self.__width = width
        self.__height = height
        self.__sides = [(0, 0), (width, 0), (width, height), (0, height)]

    def get_dimensions(self):
        return self.__width, self.__height


name = input("Введите название фигуры: ")
color = input("Введите цвет фигуры: ")
width = float(input("Введите ширину: "))
height = float(input("Введите высоту: "))

rectangle1 = Rectangle(name, color, width, height)

print("Название:", rectangle1.get_name())
print("Цвет:", rectangle1.get_color())
print("Выпуклый:", rectangle1.is_convex())
print("Площадь:", rectangle1.area())
print("Периметр:", rectangle1.perimeter())

new_width = float(input("Введите новую ширину: "))
new_height = float(input("Введите новую высоту: "))
rectangle1.set_dimensions(new_width, new_height)
print("Измененные размеры:", rectangle1.get_dimensions())
