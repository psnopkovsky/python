from sys import argv

name, arg_1, arg_2, arg_3 = argv

print('Имя скрипта: ', name)
print('Выработка в часах: ', arg_1, type(arg_1))
print('Ставка в час: ', arg_2, type(arg_2))
print('Премия: ', arg_3, type(arg_3))
try:
    for argument in argv[1:]:
        argument = int(argument)
    print('Заработная плата сотрудника: ', int(arg_1) * int(arg_2) + int(arg_3))
except:
    print('Аргументы не могут содержать буквы!')



