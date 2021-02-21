cubes_odd_numbers = []
for i in range(1, 1001):
    if i % 2 == 1:
        cubes_odd_numbers.append(i ** 3)

sum_multiple_seven = 0
for number in cubes_odd_numbers:
    sum_digits_number = 0
    number_index = 1
    while number >= number_index:
        sum_digits_number += number % (number_index * 10) // number_index
        number_index *= 10
    if sum_digits_number % 7 == 0:
        sum_multiple_seven += number
print('a:', sum_multiple_seven)

for i in range(len(cubes_odd_numbers)):
    cubes_odd_numbers[i] += 17

sum_multiple_seven = 0
for number in cubes_odd_numbers:
    sum_digits_number = 0
    number_index = 1
    while number >= number_index:
        sum_digits_number += number % (number_index * 10) // number_index
        number_index *= 10
    if sum_digits_number % 7 == 0:
        sum_multiple_seven += number
print('b:', sum_multiple_seven)
