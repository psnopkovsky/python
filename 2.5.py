raiting_list = [9, 7, 7, 5, 3, 3, 1]
your_number = int(input('Введите новый элемент рейтинга: '))
list_ = []
for i in range (len(raiting_list)):
    if raiting_list[i] < your_number:
        list_.append(i)

if len(list_) > 0:
    raiting_list.insert(list_[0], your_number)
else:
    raiting_list.append(your_number)
print('Новый рейтинг: ', raiting_list)