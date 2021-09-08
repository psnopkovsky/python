import time
import itertools


class TrafficLight:
    def __init__(self):
        self.__color = [['red', [7, 31]], ['yellow', [2, 33]],
                        ['green', [7, 32]], ['yellow', [2, 33]]]

    def running(self, number_iter):
        self.times = number_iter
        total_items = self.times * len(self.__color)
        for light in itertools.cycle(self.__color):
            if not total_items:
                break
            total_items -= 1
            print(f"\033[{light[1][1]}m\033[1m{light[0]}!", end=' ')
            time.sleep(light[1][0])
        print()
        print(f"\033[34m\033[1mСветофор устал, всем спать!!! ", end='\n')


traf = TrafficLight()
traf.running(3)