my_list = input('Введите элементы списка через запятую: ')
my_list = my_list.split(', ')
print(f'Первоначальный список: {my_list}')

if len(my_list) % 2 == 0:
    for i in range(0, len(my_list), 2):
        my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
else:
    for i in range(0, len(my_list) - 1, 2):
        my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print(f'Список после изменений: {my_list}')
