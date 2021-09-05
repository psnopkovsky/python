item_list = ['Информатика: 100(л) 50(пр) 20(лаб)\n', 'Физика: 30(л) 10(лаб)\n', 'Физкультура: 30(пр)\n',
         'Химия: 1(л) 5(лаб)\n']
with open('item.txt', 'x', encoding='utf-8') as w_obj:
    w_obj.writelines(item_list)

dict_ = {}
with open('item.txt', 'r', encoding='utf-8') as read_item:
    for line in read_item:
        StringVar = line.split()
        sum_number_str = 0
        for word in StringVar:
            www = []
            for i in range(len(word)):
                if word[i].isdigit() == True:
                    www.append(word[i])
            number = ''.join(www)
            if len(number) > 0:
                sum_number_str += int(number)
        dict_[StringVar[0]] = sum_number_str
print(dict_)