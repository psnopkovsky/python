def sum_counter (number_1, number_2, number_3):
    try:
        number_1, number_2, number_3 = float(number_1), float(number_2), float(number_3)
        list_ = [number_1, number_2, number_3]
        return print(f'Сумма двух наибольших чисел равна: {sum(list_) - min(list_)}')
    except ValueError as Err:
        print('Аргументами функции могут быть только целые или дробные числа. '
              'Ладно, я проглочу и строки, но там должны быть только числа!')

sum_counter('45', 2.9, 100)
