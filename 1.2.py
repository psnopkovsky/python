time_in_sec = int(input('Введите время в секундах: '))
hour = time_in_sec // 3600
min = (time_in_sec % 3600) // 60
sec = (time_in_sec % 3600) % 60

if hour < 10:
    hour = f'0{hour}'
if min < 10:
    min = f'0{min}'
if sec < 10:
    sec = f'0{sec}'

print(f'Время в формате чч:мм:сс - {hour}:{min}:{sec}')
