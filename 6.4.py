class Car():
    """Это - автомобиль!"""

    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        print(f'Автомобиль - {self.name}, цвет - {self.color}, машина полицейская - {self.is_police}')

    def go(self):
        print(f'Машина {self.name} поехала')

    def stop(self):
        print(f'Машина {self.name} остановилась')

    def turn(self, direction):
        self.direction = direction
        print(f"Машина {self.name} повернула {'налево' if direction == 0 else 'направо'}")

    def show_speed(self):
        print(f'Текущая скорость автомобиля - {self.speed} ')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'Автомобиль {self.name} превысил допустимую скорость!')


class SportCar(Car):
    def show_speed(self):
        if self.speed > 200:
            print(f'Автомобиль {self.name} демонстрирует минимальную скорость!')
            self.name = 'Ferrari'
            print(f'Отныне ты зовешься {self.name}')


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'Автомобиль {self.name} превысил допустимую скорость!')


class PoliceCar(Car):
    def show_speed(self):
        if self.is_police == True:
            print(f'"Защищать и служить" - надпись на борту машины {self.name}')


lada = Car(70, 'white', 'kalina', False)
lada.show_speed()
lada.turn(9)

marshrut = TownCar(110, 'green', 'gazel', False)
marshrut.show_speed()

kamaz = WorkCar(42, 'red', 3160, False)
kamaz.show_speed()
kamaz.turn(0)

mustang = SportCar(345, 'yellow', 'muscle', False)
mustang.show_speed()

dps = PoliceCar(138, 'blue', 'musor', True)
dps.show_speed()