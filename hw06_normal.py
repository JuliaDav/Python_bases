'''
Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
'''
import math

class Triangle:
    def __init__(self, coords):#координаты в виде [x1,y1,x2,y2,x3,y3]
        self.coords = {'x1':int(coords[0]), 'y1':int(coords[1]),
                       'x2': int(coords[2]), 'y2': int(coords[3]),
                       'x3': int(coords[4]), 'y3': int(coords[5])
                       }
    @property #декоратор для использования координат в расчетах
    def x1(self):
        return self.coords['x1']
    @property
    def x2(self):
        return self.coords['x2']
    @property
    def x3(self):
        return self.coords['x3']
    @property
    def y1(self):
        return self.coords['y1']
    @property
    def y2(self):
        return self.coords['y2']
    @property
    def y3(self):
        return self.coords['y3']

    @property #рассчитываем длины сторон
    def vec1(self):
        vec1 = math.sqrt((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2)
        return vec1
    @property
    def vec2(self):
        vec2 = math.sqrt((self.x3 - self.x2) ** 2 + (self.y3 - self.y2) ** 2)
        return vec2
    @property
    def vec3(self):
        vec3 = math.sqrt((self.x3 - self.x1) ** 2 + (self.y3 - self.y1) ** 2)
        return vec3

    @property #рассчитываем периметр
    def perim(self):
        return self.vec1 + self.vec2 + self.vec3

    @property #рассчитываем площадь
    def sqare(self):
        p = self.perim / 2
        sqare = math.sqrt(p * (p - self.vec1) * (p - self.vec2) * (p - self.vec3))
        return sqare

    def len(self): #рассчитываем высоту
        len = 2 / self.vec1 * self.sqare
        return len

tgl1 = Triangle([2, 4, 6, 5, 3, 8])
print(tgl1.coords)
print('Периметр = ', tgl1.perim)
print('Длины сторон = ', tgl1.vec1, tgl1.vec2, tgl1.vec3)
print('Площадь = ', tgl1.sqare)
print('Высота = ', tgl1.len())
