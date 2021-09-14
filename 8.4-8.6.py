class Orgtech:
    def __init__(self, name, cnt, price, *args):
        self.name = name
        self.cnt = cnt
        self.price = price
        self.order = []
        self.unit = {'Наименование': self.name, 'Количество': self.cnt, 'Цена за шт.': self.price}

    def __str__(self):
        return f'{self.name} : цена - {self.price}, количество - {self.cnt}'

    def take_item(self):
        end = 0
        while end == 0:
            try:
                position = input(f'Введите наименование: ')
                position_price = int(input(f'Введите цену за шт.: '))
                position_cnt = int(input('Введите количество: '))
                position_line = {'Наименование': position, 'Количество': position_cnt, 'Цена за шт.': position_price}
                self.unit.update(position_line)
                self.order.append(self.unit)
                self.unit = {}
                print(f'Текущее состояние: \n {self.order}')

                print('Для выхода введите "stop" или нажмите "enter" для продолжения')
                answer = input()
                if answer == 'stop':
                    end = 1
                    print(f'Склад полностью: {self.order}')
            except ValueError as err:
                print(f'Введены некорректные данные - проверьте тип!')


class Printer(Orgtech):
    def __init__(self, name, cnt, price, type_print):
        super().__init__(name, cnt, price)
        self.type = type_print


class Scaner(Orgtech):
    def __init__(self, name, cnt, price, size):
        super().__init__(name, cnt, price)
        self.size = size


class Xerox(Orgtech):
    def __init__(self, name, cnt, price, speed):
        super().__init__(name, cnt, price)
        self.speed = speed


my_printer = Printer('epson', 30, 12999, 'matrix')
my_scaner = Scaner('hp', 10, 10500, 'compact')
my_xerox = Xerox('xerox', 5, 23499.00, 'fast')
print(my_printer.type)
print(my_scaner.size)
print(my_xerox.speed, my_xerox.cnt)

my_printer.take_item()
print(my_printer.order)
