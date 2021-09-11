class Cell():
    def __init__(self, cell):
        try:
            self.cell = int(cell)
        except TypeError:
            print('Количество ячеек клетки должно быть целым числом!')
        except ValueError:
            print('Количество ячеек клетки должно быть целым числом!')

    def __str__(self):
        pass

    def __add__(self, other):
        return self.cell + other.cell

    def __sub__(self, other):
        if self.cell - other.cell < 0:
            return f'Внимание! Разность ячеек меньше нуля!'
        else:
            return self.cell - other.cell

    def __mul__(self, other):
        return self.cell * other.cell

    def __truediv__(self, other):
        return self.cell // other.cell

    def make_order(self, row):
        for i in range(0, self.cell // row):
            print('*' * row)
        print('*' * (self.cell % row))

first = Cell(14)
second = Cell(6)

print(first + second)
print(first - second)
print(first * second)
print(first / second)

first.make_order(3)