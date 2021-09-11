# к сожалению, так и не получилось добиться, чтобы результрующая матрица выводилась в принте, как
# исходные, а не в виде списка списков (((

import random


class Matrix():
    def __init__(self):
        self.m = int(input("Введите количество строк матрицы: "))
        self.n = int(input("Введите количество столбцов матрицы: "))
        print()
        self.matrix_list = []
        for i in range(self.m):
            self.matrix = [random.randint(0, 10) for _ in range(self.n)]
            self.matrix_list.append(self.matrix)

    def __str__(self):
        self.matrix_str = ''
        for elem in self.matrix_list:
            self.matrix_str += ' '.join([str(i) for i in elem]) + '\n'

        return self.matrix_str

    def __add__(self, other):
        c = []
        try:
            for i in range(len(self.matrix_list)):
                c.append([])
                for j in range(len(self.matrix_list[i])):
                    c[i].append(self.matrix_list[i][j] + other.matrix_list[i][j])
            self.matrix_list = c
            return self.matrix_list
        except IndexError:
            print(f'У меня не всегда получается складывать разные матрицы - '
                  f'лучше, чтобы они были одинакового размера!!!')

a = Matrix()
b = Matrix()
print(a)
print(b)
print(a + b)