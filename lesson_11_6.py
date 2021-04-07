import os


class Warehouse:
    balance = {1: ["Laser", "Printer", "HP 7800", 3],
               2: ["Ink-jet", "Printer", "Cannon 910", 5],
               3: ["Tablet", "Scanner", "Epson V19", 2],
               4: ["Slide", "Scanner", "Espada EC717", 3],
               5: ["Analog", "Copier", "Ricoh C5100S", 1],
               6: ["Digital", "Copier", "Triumph Adler 2507ci", 2]}

    @staticmethod
    def show_balance():
        ids = [key for key in warehouse.balance.keys()]
        ids.sort()
        for i in ids:
            print(f"{i}. {' '.join(warehouse.balance[i][0:-1])} - {warehouse.balance[i][-1]} pcs")

    @staticmethod
    def to_receive(id_, num):
        if id_ == 0:
            user_choice = input('Enter "p" to printer, "s" to scanner, "c" to copier: ')
            if user_choice == "p":
                new_equipment = Printer(input("Enter printer name: "),
                                        input("Enter printer technology: "))
            elif user_choice == "s":
                new_equipment = Scanner(input("Enter scanner name: "),
                                        input("Enter scanner type: "))
            elif user_choice == "c":
                new_equipment = Copier(input("Enter copier name: "),
                                       input("Enter scan principle: "))
            else:
                print(f'"{user_choice}" - unknown command ', end="")
                return
            Warehouse.balance[new_equipment.id_] = [*new_equipment.get_attrs(), 0]
            id_ = new_equipment.id_
        print(f"{num} pcs {Warehouse.balance[id_][0:-1]} to accepted to warehouse ", end="")
        Warehouse.balance[id_][-1] += num

    @staticmethod
    def to_send(id_, num, department):
        if num > Warehouse.balance[id_][-1]:
            print(f"Not enough {Warehouse.balance[id_][0:-1]}", end="")
        else:
            print(f"{num} pcs {Warehouse.balance[id_][0:-1]} sent to {department} ", end="")
            Warehouse.balance[id_][-1] -= num


class OfficeEquipment:
    id_ = 7

    def __init__(self, name):
        self.id_ = OfficeEquipment.id_
        self.type_ = self.get_type()
        self.name = name
        OfficeEquipment.id_ += 1

    @classmethod
    def get_type(cls):
        return cls.__name__


class Printer(OfficeEquipment):
    def __init__(self, name, technology):
        super().__init__(name)
        self.technology = technology

    def get_attrs(self):
        return [self.technology, self.type_, self.name]


class Scanner(OfficeEquipment):
    def __init__(self, name, scanner_type):
        super().__init__(name)
        self.scanner_type = scanner_type

    def get_attrs(self):
        return [self.scanner_type, self.type_, self.name]


class Copier(OfficeEquipment):
    def __init__(self, name, scan_principle):
        super().__init__(name)
        self.scan_principle = scan_principle

    def get_attrs(self):
        return [self.scan_principle, self.type_, self.name]


warehouse = Warehouse()
while True:
    os.system('cls||clear')
    warehouse.show_balance()
    print()
    user_input = input('Enter "a" to receive on warehouse, "s" to send to department, "e" to exit: ')
    if user_input == "e":
        break
    elif user_input == "a":
        try:
            user_input = int(input('Enter an ID (or "0" to add new equipment): '))
            if user_input == 0 or user_input in Warehouse.balance.keys():
                warehouse.to_receive(user_input, int(input("Enter quantity to receive: ")))
            else:
                print(f"ID {user_input} does not exist ", end="")
        except ValueError:
            print("Please enter an integer ", end="")
    elif user_input == "s":
        try:
            warehouse.to_send(int(input("Enter an ID: ")), int(input("Enter quantity to receive: ")),
                              input("Enter the name of the department: "))
        except ValueError:
            print("Please enter an integer ", end="")
    else:
        print(f"{user_input} - unknown command ", end="")
    input("(enter to return): ")
print("Goodbye!")
