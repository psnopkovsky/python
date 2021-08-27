def division_func(number_1, number_2):
    try:
        result = number_1 / number_2
    except ZeroDivisionError as Err:
        print('division by zero not possible')
    else:
        return print(f'Частное равно: {result}')

division_func(int(input('Введите делимое: ')), int(input('Введите делитель: ')))

