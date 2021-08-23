season_dict = {'зима' : [12, 1, 2], 'весна' : [3, 4, 5], 'лето' : [6, 7, 8], 'осень' : [9, 10, 11]}
month_number = int(input('Введите число в 1 до 12 включительно: '))
for k, v in season_dict.items():
    if month_number in v:
        print(f'Это же {k}, милый человек!')

season_list = [['зима', 12, 1, 2], ['весна', 3, 4, 5], ['лето', 6, 7, 8], ['осень', 9, 10, 11]]
for element in season_list:
    if month_number in element:
        print(f'И с использованием списка - это тоже {element[0]}!')