import random


def get_jokes(number_of_jokes=1, repeat_words=True):
    """
    Return a list of n jokes
    Number of jokes without repeat words = 5
    """

    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    jokes = []

    if not repeat_words:
        number_of_jokes = 5

    for i in range(number_of_jokes):
        noun, adverb, adjective = random.choice(nouns), random.choice(adverbs), random.choice(adjectives)
        if not repeat_words:
            nouns.remove(noun)
            adverbs.remove(adverb)
            adjectives.remove(adjective)
        jokes.append(f'{noun} {adverb} {adjective}')

    print(jokes)


# get_jokes(repeat_words=False, number_of_jokes=10)
# get_jokes(10)
