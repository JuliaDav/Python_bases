'''
Задача-1: Создать класс Матрица. В конструктор класса передавать переменную
содержащую матрицу в виде списка списков. В конструкторе класса преобразовать
список списков в привычный матричный вид. Переопределить стандартное поведение
методов __add__ и __str__ класса. Создать два экземпляра класса Матрица с данными.
Метод __add__ должен реализовывать сложение матриц, а __str__ - вывод итоговой
матрицы.
'''
class Matrix:
    def __init__(self, matr):
        self.matr = [[int(matr[0]), int(matr[1])], [int(matr[2]), int(matr[3])]]

    def __add__(self, other):
        return Matrix((self.matr[0][0] + other.matr[0][0], self.matr[0][1] + other.matr[0][1],\
                    self.matr[1][1] + other.matr[1][1], self.matr[1][0] + other.matr[1][0]))
    def __str__(self):
        for l in self.matr:
            print(l)
        return 'm3 = {}'.format(self.matr)

m1 = Matrix('1234')
m2 = Matrix('4321')
m3 = m1 + m2
print(m3)