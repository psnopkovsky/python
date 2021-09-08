class Road():
    def __init__(self):
        self._lenght = int(input('Введите длину покрытия в метрах: '))
        self._width = int(input('Введите ширину покрытия в метрах: '))

    def get_total_weight(self, n, t):
        self.normativ = n
        self.thickness = t
        result = self._lenght * self._width * self.normativ * self.thickness / 1000
        print(f'Масса асфальта для покрытия дороги: {result} тонн')


my_asf = Road()
my_asf.get_total_weight(25, 5)