proceeds = int(input('Ваша выручка: '))
costs = int(input('Ваши издержки: '))
count_person = int(input('Численность фирмы: '))
if proceeds > costs:
    rent = (proceeds - costs) / proceeds
    profit_to_person = (proceeds - costs) / count_person
    print('Фирма работает с прибылью')
    print(f'Рентабельность выручки равна: {rent}')
    print(f'Прибыль на сотрудника равна: {profit_to_person} рублей')
elif proceeds < costs:
    print('Фирма работает с убытком')
else:
    print('Точка безубыточности')