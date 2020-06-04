from sys import stdin
import copy


# ошибки в вычисления
class MatrixError(BaseException):
    def __init__(self, matrix1, matrix2):
        self.matrix1 = copy.deepcopy(matrix1)
        self.matrix2 = copy.deepcopy(matrix2)


# главный класс
class Matrix:
    # иницилизация
    def __init__(self, lis):
        self.inp = lis
        self.matrix = copy.deepcopy(lis)

    # вывод в виде матрицы
    def __str__(self):
        string = ""
        for i in self.matrix:
            for j in i:
                string += '%s\t' % j
            string = string[:-1] + '\n'
        return string[:-1]

    # длина и ширина матрицы
    def size(self):
        self.lines = len(self.matrix)
        self.columns = len(self.matrix[0])
        return self.lines, self.columns

    # суммирование элементов в массиве
    def __add__(self, other):
        # проверка на ошибку в размерах массивов
        if len(self.matrix) == len(other.matrix)\
                and len(self.matrix[0]) == len(other.matrix[0]):
            res = Matrix
            res.mat = []
            for i in range(len(self.matrix)):
                temp = []
                for j in range(len(self.matrix[0])):
                    x = self.matrix[i][j] + other.matrix[i][j]
                    temp.append(x)
                res.mat.append(temp)
        else:
            raise MatrixError(self, other)
        return Matrix(res.mat)

    # умножение левых элементов массива на правое число
    def __mul__(self, number):
        res = []
        if isinstance(number, int) or isinstance(number, float):
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[0])):
                    res[i][j] = self.matrix[i][j] * number
        return Matrix(res)

    # умножение правых элементов массива на левое число
    __rmul__ = __mul__

    # транспонирация матрицы
    def transpose(self):
        self.matrix = list(zip(*self.matrix))
        return Matrix(self.matrix)

    def transposed(self):
        return Matrix(list(zip(*self.matrix)))


exec(stdin.read())
