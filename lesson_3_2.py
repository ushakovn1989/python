def thesaurus_adv(*args):
    result_dict = {}

    for full_name in args:
        first_name, second_name = full_name.split()
        result_dict.setdefault(second_name[0], {})
        result_dict[second_name[0]].setdefault(first_name[0], [])
        result_dict[second_name[0]][first_name[0]].append(full_name)
    return result_dict


# print(thesaurus_adv('Иван Сергеев', 'Инна Серова', 'Петр Алексеев', 'Илья Иванов', 'Анна Савельева'))
