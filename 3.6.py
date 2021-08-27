def int_func(word):

    """ Функция фильтрации латинских слов, начинающихся с маленькой буквы
    - если в слове есть кириллические символы, то возвращает None
    - если в слове есть цифры, то возвращает None
    - если в слове есть заглавные буквы, то возвращает None

    """

    symbol_list = list(word)
    for symbol in symbol_list:
        if symbol.isdigit() == True:
            return None
            break
        elif ord(symbol) > ord('z') or ord(symbol) < ord('a'):
            return None
            break
        elif symbol.isupper == True:
            return None
            break
        else:
            continue
    return word.title()


str_ = input('Введите слова на латинском языке с маленькой буквы через пробел: ').split()
for word in str_:
    word = int_func(word)
    if word != None:
        print(word, end=' ')