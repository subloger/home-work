import random

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(n):
    """
    Функция выполняет составление шуток
    путем подбора случайных элементов
    из трех списков.
    """

    joke = []
    for i in range(n):
        word_1 = random.choice(nouns)
        word_2 = random.choice(adverbs)
        word_3 = random.choice(adjectives)
        joke.append(f'{word_1} {word_2} {word_3}')
    return joke


print(get_jokes(4))