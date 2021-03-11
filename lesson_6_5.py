from sys import argv


def combine_strings(file_1, file_2, file_3):
    from itertools import zip_longest

    with open(file_1, 'r', encoding='utf-8') as users:
        with open(file_2, 'r', encoding='utf-8') as hobby:
            with open(file_3, 'w', encoding='utf-8') as users_hobby:

                new_strings = (f'{str(u).strip()}: {str(h).strip()}\n' for u, h in zip_longest(users, hobby))
                for string in new_strings:
                    users_hobby.write(string)


if len(argv) > 1:
    combine_strings(*argv[1:])
else:
    combine_strings('users.csv', 'hobby.csv', 'users_hobby.txt')
