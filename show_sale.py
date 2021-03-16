import sys


def show(start_string, end_string):
    with open('bakery.csv', 'r', encoding='utf-8') as f:
        for ind, line in enumerate(f, start=1):
            if ind > end_string != 0:
                break
            elif ind >= start_string:
                print(line.strip())


s, e = 1, 0

if len(sys.argv) == 3:
    s, e = int(sys.argv[1]), int(sys.argv[2])
elif len(sys.argv) == 2:
    s = int(sys.argv[1])

show(s, e)
