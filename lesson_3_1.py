def num_translate_adv(numeral):
    numerals = {'zero': 'ноль', 'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять',
                'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}
    if numeral.lower() in numerals:
        if numeral[0].isupper():
            print(numerals[numeral.lower()].title())
        else:
            print(numerals[numeral])
    else:
        return None


# num_translate_adv('one')
# num_translate_adv('Five')
# print(num_translate_adv('eleven'))
