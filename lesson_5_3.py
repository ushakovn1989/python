from itertools import zip_longest

tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']
# klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А']

needed_zip = zip_longest if len(tutors) > len(klasses) else zip
generator = ((name, klass) for name, klass in needed_zip(tutors, klasses))
print(type(generator), *generator, sep='\n')
