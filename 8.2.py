class MyZeroException(Exception):
    def __init__(self, txt):
        self.txt = txt


num_1, num_2 = [num for num in [int(i) for i in input('Введите два числа через запятую: ').split(',')]]

try:
    if num_2 != 0:
        print(f'Результат деления {num_1} / {num_2} равен: ', num_1 / num_2)
    else:
        raise MyZeroException('Ты же не собираешься делить на ноль?')
except MyZeroException as err:
    print(err)