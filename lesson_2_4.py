price_list = [34.87, 26.13, 48.76, 48, 97.68, 32.70, 46.87, 67, 46.58, 71.20, 120, 93, 10.29, 34, 88.67]
list_length = len(price_list)

# a
for ind, price in enumerate(price_list):
    price = int(price * 1000 // 10)
    rub = price // 100
    kop = price % 100
    if ind + 1 < list_length:
        print(f'{rub} руб {kop:02} коп', end=', ')
    else:
        print(f'{rub} руб {kop:02} коп')

# b
print('Before sorting: ', id(price_list))
price_list.sort()
print(price_list)
print('After sorting: ', id(price_list))

# c
new_list = price_list[::-1]

# d
print(new_list[:5])
