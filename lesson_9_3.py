class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']


loader = Position('Ivan', 'Ivanov', 'Loader', {'wage': 30000, 'bonus': 8000})
inspector = Position('Petr', 'Petrov', 'Inspector', {'wage': 35000, 'bonus': 7000})
shift_supervisor = Position('Sidr', 'Sidorov', 'Shift Supervisor', {'wage': 40000, 'bonus': 10000})

for worker in loader, inspector, shift_supervisor:
    print(worker.name, worker.surname, worker.position, worker._income)
    print(worker.get_full_name(), worker.get_total_income(), sep='\n')
    print('-' * 79)
