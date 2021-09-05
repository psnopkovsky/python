import json

with open('firm_info.txt', 'r', encoding='utf-8') as r_obj:
    cnt_firms = 0
    mean_profit = 0
    dict_ = {}
    for line in r_obj:

        result = int(line.split()[2]) - int(line.split()[3])
        if result < 0:
            print(f'{line.split()[0]} работает с убытком')
        else:
            print(f'Прибыль {line.split()[0]} равна {result}')
            mean_profit += result
            cnt_firms += 1
        dict_[line.split()[0]] = result

average_profit = round((mean_profit / cnt_firms), 1)
print(f'Средняя прибыль составляет: ', average_profit)

dict_2 = {'average_profit': average_profit}
final_list = [dict_, dict_2]

print(final_list)

with open('final_list.json', 'w') as json_w:
    json.dump(final_list, json_w)