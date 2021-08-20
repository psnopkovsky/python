your_number = int(input('Введите число: '))
max_ = 0
while your_number != 0:
    ost = your_number % 10
    your_number = your_number // 10
    if ost > max_:
        max_ = ost

print(f'Максимальная цифра в вашем числе: {max_}')
