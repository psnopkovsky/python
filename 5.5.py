import random
numb_int = [x ** 2 for x in range(random.randint(1, 5))]
numb_int_neg = [random.randint(-10, 0) for _ in range(random.randint(1, 5))]
numb_float = [round(random.random(), 2) for _ in range(random.randint(1, 5))]
number_list = numb_int + numb_int_neg + numb_float
number_str = ' '.join(map(str, number_list))
with open('number_list.txt', 'w') as f_obj:
        f_obj.write(f'{number_str}')
with open('number_list.txt') as r_obj:
        content = r_obj.read()
        print(f'{type(content)} ----> {content}')
content = [float(x) for x in content.split(' ')]
sum_ = 0
for i in content:
        sum_ += i
print('Сумма чисел в файле: ', sum_)
