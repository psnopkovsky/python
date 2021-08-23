phrase = input('Введите набор слов через пробел: ').split()
for i in range(len(phrase)):
    if len(phrase[i]) > 10:
        phrase[i] = phrase[i][:10]
    print(f'{i}: {phrase[i]}')