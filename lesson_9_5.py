class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Start drawing')


class Pen(Stationary):
    def draw(self):
        print(f'Start drawing with {self.title}')


class Pencil(Stationary):
    def draw(self):
        print(f'Start drawing with {self.title}')


class Handle(Stationary):
    def draw(self):
        print(f'Start drawing with {self.title}')


pen = Pen('pen')
pencil = Pencil('pencil')
handle = Handle('handle')

for obj in pen, pencil, handle:
    obj.draw()
