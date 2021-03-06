"""Написать класс треугольник. В конструкторе определить длины сторон. Добавить методы для вычисления площади,
периметра, определения типа треугольника (прямой, равнобедренный, равносторонний, разносторонний)"""


def _triangle_exist(triangle):
    if (triangle.side1 + triangle.side2 > triangle.side3 and triangle.side1 + triangle.side3 > triangle.side2 and
       triangle.side2 + triangle.side3 > triangle.side1):
        return True
    else:
        return False


class Triangle(object):

    def __init__(self, side1, side2, side3):
        self.side1 = float(side1)
        self.side2 = float(side2)
        self.side3 = float(side3)
        self.is_exist = _triangle_exist(self)

    def triangle_perimeter(self):
        if self.is_exist is True:
            perimeter = self.side1 + self.side2 + self.side3
            return round(perimeter, 2)
        else:
            return "Треугольник не существует."

    def triangle_square(self):
        if self.is_exist is True:
            half_perimeter = (self.side1 + self.side2 + self.side3)/2
            square = (half_perimeter * (half_perimeter - self.side1) * (half_perimeter - self.side2) *
                      (half_perimeter - self.side3)) ** 0.5
            return round(square, 2)
        else:
            return "Треугольник не существует."

    def triangle_type(self):
        if self.is_exist is True:
            if self.side1 == self.side2 == self.side3:
                return "Треугольник равностронний"
            elif ((self.side1 == self.side2 and self.side2 != self.side3) or (self.side2 == self.side3 and
                  self.side3 != self.side1) or (self.side3 == self.side1 and self.side1 != self.side2)):
                return "Треугольник равнобедренный"
            elif ((self.side1 ** 2 == self.side2 ** 2 + self.side3 ** 2) or
                  (self.side2 ** 2 == self.side1 ** 2 + self.side3 ** 2) or
                  (self.side3 ** 2 == self.side1 ** 2 + self.side2 ** 2)):
                return "Треугольник прямоугольный"
            else:
                return "Треугольник разносторонний"
        else:
            return "Треугольник не существует."
