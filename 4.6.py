from itertools import cycle, count

def number_(start, end, repeat):

    """Функция генерации списка по заданным прпаметрам с последующим повтором элементов
    - start: число, с которого запускается процесс генерации
    - end: условное значение для остановки генератора
    - repeat: условное значение для остановки повторяющегося перебора ранее сформированного списка.
    """
    
    list_number = []
    for i in count(start):
        if i > end:
            break
        else:
            list_number.append(i)
    print('Сгенерированный список: ', list_number)
    c = 0
    for j in cycle(list_number):
        if c > repeat:
            break
        else:
            list_number.append(j)
            c += 1
    print('Повторяющийся список: ', list_number)

number_(4, 29, 70)