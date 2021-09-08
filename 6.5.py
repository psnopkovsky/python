class Stationery():
    def __init__(self, title):
        self.title = title
        print(f'Я - {self.title}, я рисую лучше всех!')

    def draw(self):
        return print("Запуск отрисовки")


class Pen(Stationery):
    def draw(self):
        return print("Я хорошо умею писать буквы!")


class Pencil(Stationery):
    def draw(self):
        return print('Я твердый или мягкий....хотя могу быть твердо-мягким )))')


class Handle(Stationery):
    def draw(self):
        return print('В умелых руках я рисую не хуже seaborn (matplotlib отдыхает)!!!')


matplotlib = Stationery('matplotlib')
matplotlib.draw()

pen = Pen('гелевая ручка')
pen.draw()

pencil = Pencil('заточенный карандаш')
pencil.draw()

handle = Handle('Супер-маркер')
handle.draw()