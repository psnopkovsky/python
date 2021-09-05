str_len = 0
while str_len == 0:
    str_ = input('Введите данные (для выхода оставить поле пустым и нажать Enter): ')
    if len(str_) > 0:
        with open('user_info.txt', 'a', encoding='utf-8') as f_obj:
            f_obj.writelines(str_ + '\n')
    else:
        str_len = 1

with open('user_info.txt', 'r', encoding='utf-8') as r_obj:
    for line in r_obj:
        print(line.strip())