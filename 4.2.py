test_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
try:
    input_list = [int(number) for number in (input('Введите числа через пробел: ').split())]
    print('Исходный список: ', input_list)
    input_list =[input_list[i] for i in range(1, len(input_list)) if input_list[i - 1] < input_list[i]]
    print('Преобразованный список: ', input_list)
except ValueError:
    print('Необходимо вводить только целые числа')