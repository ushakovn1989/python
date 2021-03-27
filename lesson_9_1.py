from time import sleep


class TrafficLight:
    def __init__(self):
        self.__color = ('red', 'yellow', 'green')

    def running(self):
        for color in self.__color:
            print(color)
            if color == 'red':
                sleep(7)
            elif color == 'yellow':
                sleep(2)
            else:
                sleep(4)


traffic_light = TrafficLight()
traffic_light.running()
