check_list = [38, 147, 3972, 56108, 468927]
for duration in check_list:
    print('duration', duration)
    seconds = duration % 60
    minutes = duration // 60 % 60
    hours = duration // 3600 % 24
    days = duration // 86400 % 24
    print(days, 'ден', hours, 'час', minutes, 'мин', seconds, 'сек')
