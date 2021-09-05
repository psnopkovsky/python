numbers_info = ['One — 1\n', 'Two — 2\n', 'Three — 3\n', 'Four — 4\n']
numb_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
with open ('numbers_count.txt', 'x', encoding = 'utf-8') as numb_obj:
    numb_obj.writelines(numbers_info)

with open('numbers_count.txt', 'r', encoding = 'utf-8') as numb_read:
          for index, line in enumerate(numb_read):
            new_value = numb_dict[line.split(' ')[0]]
            print((new_value + ' ' + line.split(' ')[1] + ' ' + line.split(' ')[2]))