class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass_calc(self, thickness):
        print(f'{(self._length * self._width * 25 * thickness) // 1000}т')


road = Road(5000, 20)
road.mass_calc(5)
