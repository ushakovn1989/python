class ComplexNumber:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __add__(self, other):
        real_number = self.x + other.x
        imaginary_unit = self.y + other.y
        return f"{real_number}{imaginary_unit:+}j"

    def __mul__(self, other):
        real_number = self.x*other.x - self.y*other.y
        imaginary_unit = self.x*other.y + other.x*self.y
        return f"{real_number}{imaginary_unit:+}j"


my_num_1 = ComplexNumber(2, 1)
my_num_2 = ComplexNumber(3, 5)

test_num_1 = 2+1j
test_num_2 = 3+5j

print(complex(my_num_1 + my_num_2) == test_num_1 + test_num_2)
print(complex(my_num_1 * my_num_2) == test_num_1 * test_num_2)

my_num_1 = ComplexNumber(5, 3)
my_num_2 = ComplexNumber(2, -1)

test_num_1 = 5+3j
test_num_2 = 2-1j

print(complex(my_num_1 + my_num_2) == test_num_1 + test_num_2)
print(complex(my_num_1 * my_num_2) == test_num_1 * test_num_2)
