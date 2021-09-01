test = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print('Встречаются единожды следующие элементы: ', [test[i] for i in range(len(test)) if test.count(test[i]) == 1])