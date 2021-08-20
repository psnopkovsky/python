first_dist = int(input('Результат первого дня: '))
dist_to = int(input('Желаемый результат: '))
n = 1
print(f'{n}-й день: {first_dist:.2f}')
while first_dist < dist_to:
    first_dist = first_dist * 1.1
    n += 1
    print(f'{n}-й день: {first_dist:.2f}')
print(f'Тебя ждет марафон!!! Ты достиг желаемый результат на {n}-й день')