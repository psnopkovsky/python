salary_list = ['Иванов 19200.00\n', 'Петров 12900.00\n', 'Сидоров 73400.99\n', 'Коноплев 99500.00\n', 'Путин 1000000.00\n',
               'ИП_Бондарев 1000001.00\n']
with open ('salary_info.txt', 'x', encoding='utf-8') as new_obj:
    new_obj.writelines(salary_list)

sum_salary = 0
count_people = 0
with open ('salary_info.txt', 'r', encoding='utf-8') as read_info:
    for line in (read_info):
        count_people += 1
        sum_salary += float(line.split(' ')[1])
        if float(line.split(' ')[1]) < 20000.00:
            loh = line.split(' ')[0]
            print(f'Господин {loh}, ты не пробовал зарабатывать больше 20 кусков, а?')
mean_salary = sum_salary / count_people
print(f'Средний размер зарплаты равен: {mean_salary:.2f}')