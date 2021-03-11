parsing_list = []
addresses_with_gets = {}

with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    for string in f:
        string = string.split()
        parsing_list.append((string[0], string[5][1:], string[6]))

for ind in parsing_list:
    addresses_with_gets.setdefault(ind[0], 0)
    addresses_with_gets[ind[0]] += 1

nums_gets = 0
spammer = None

for k, v in addresses_with_gets.items():
    if v > nums_gets:
        spammer, nums_gets = k, v

print(spammer, nums_gets)
