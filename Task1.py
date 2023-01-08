# Напишите программу, удаляющую из текста все слова, содержащие "абв". В тексте используется разделитель пробел.
# in Number of words: 10
# out 
# авб абв бав абв вба бав вба абв абв абв
# авб бав вба бав вба

from random import sample


def list_of_words(count: int, alp: str = 'абв'):
    words_list = []
    for i in range(count):
        next_word = sample(alp, 3)
        words_list.append("".join(next_word))
    return " ".join(words_list)


# def list_rand_words(count: int, alp: str = 'абв'):
#     return " ".join("".join(sample(alp, 3)) for _ in range(count))


def change_list(words: str) -> str:
    return " ".join(words.replace("абв", "").split())


all_list = list_of_words(int(input("Укажите количество слов: ")))
print(all_list)
print(change_list(all_list))