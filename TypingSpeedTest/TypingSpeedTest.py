from random import randint
import time


def generator(sentence):
    while len(sentence) < 70:
        sentence += text[randint(0, len(text)) - 1] + '. '
        if 100 >= len(sentence) >= 90:
            return sentence
    return generator('')


def proverka(test, sentence):

    cnt = 0
    test = list(test)
    sentence = list(sentence)

    if len(test) == len(sentence) + 1:

        cnt -= 1

        for i in range(0, len(test) - 2):
            if test[i] == sentence[i] or test[i] == sentence[i + 1] or test[i] == sentence[i - 1]:
                cnt += 1
            else:
                test[i] = '#'

    if len(test) > len(sentence) + 1:
        return 'Ошибка ввода'

    if len(test) < len(sentence) + 1:
        while len(test) != len(sentence):
            test += '#'

        for i in range(0, len(test) - 1):
            if test[i] == sentence[i] or test[i] == sentence[i + 1] or test[i] == sentence[i - 1]:
                cnt += 1
            else:
                test[i] = '#'

    result = (cnt * 100) // (len(sentence) - 1)

    if test[:-1] == '#':
        cnt -= 1

    if cnt < 0:
        result = 0

    return f'{str(result)}%'


f = open('Текст.txt')
text = list(set(f.read().split('. ')))
for i in range(len(text)):
    text[i] = text[i].replace('\n', ' ')
    text[i] = text[i].replace('«', '"')
    text[i] = text[i].replace('»', '"')
sentence = generator('')[:-1]

countdown = ['3', '2', '1...']
print('Приготовьтесь печатать', end='', flush=True)

for i in countdown:
    time.sleep(1)
    print('\r' + i + ' ' * 21, end='', flush=True)

time.sleep(1)
print(f'\r{sentence}', flush=True)

sentence = sentence.replace('—', '-')

start_time = time.time()

test = input()
LenTest = len(test)

end_time = time.time()
elapsed_time = end_time - start_time

print(f'Символов в минуту: {int(LenTest * 60 // elapsed_time)} \nАккуратность: {proverka(test, sentence)}')


