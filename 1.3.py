n = int(input('Введите целое число: '))
count = 1
result = 0
while count < (n + 1):
    number_str = str(n) * count
    result += int(number_str)
    print(f'слагаемое: {number_str}')
    count += 1

print(f'Сумма слагаемых: {result}')
