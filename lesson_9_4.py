from random import choice


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'The {self.color} {self.name} rides')

    def stop(self):
        print(f'The {self.color} {self.name} stopped')
        self.speed = 0

    def turn(self, direction):
        print(f'The {self.color} {self.name} turned {direction}')

    def show_speed(self):
        print(f'The {self.color} {self.name} speed {self.speed}')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'The {self.color} {self.name} over speed ({self.speed})')
        else:
            super().show_speed()


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'The {self.color} {self.name} over speed ({self.speed})')
        else:
            super().show_speed()


class PoliceCar(Car):
    pass


town_car = TownCar(0, 'black', 'Mazda', False)
sport_car = SportCar(0, 'red', 'Ferrari', False)
work_car = WorkCar(0, 'yellow', 'Renault', False)
police_car = PoliceCar(0, 'white', 'Ford', True)

for car in town_car, sport_car, work_car, police_car:
    print(car.color, car.name, car.speed, car.is_police, end='\n\n')
    car.go()
    for cur_speed in 40, 60, 80:
        car.speed = cur_speed
        car.show_speed()
    car.turn(choice(('left', 'right')))
    car.stop()
    print('-' * 79)
