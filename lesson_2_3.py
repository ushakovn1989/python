original_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй',
                 'директор аэлита']
name = ''

for obj in original_list:
    name = obj.split()[-1]
    print(f'Привет, {name.title()}!')
