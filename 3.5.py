total_sum = 0
q = 0
while q != 1:
    str_ = input('Вводите числа через пробел: ').split()
    local_sum = 0
    for i in range(len(str_)):
        if str_[i] == 'q':
            q = 1
            break
        else:
            try:
                str_[i] = int(str_[i])
                local_sum += str_[i]
            except:
                ValueError
                print('Err!')
    total_sum += local_sum
    print(f'Сумма элементов текущей итерации: {local_sum}, сумма нарастающим итогом: ({total_sum})')
    print('-' * 70)    