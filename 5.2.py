my_text = [f"""День знаний — это ведь не только о школьных линейках, первоклассниках с большими букетами цветов \
и об учёбе в школе.\n""", f"""День знаний — это о стремлении познавать доселе неизвестное, о росте и развитии, \
об обретении новых навыков и возможностей.\n""", f"""Это об учёбе в течение всей жизни, вне зависимости от \
возраста и социального положения.\n""", f"""Это о нас с вами.\n"""]

with open('first_september.txt', 'a', encoding='utf-8') as create_obj:
    create_obj.writelines(my_text)

str_count = 0
with open('first_september.txt', 'r', encoding='utf-8') as read_obj:
    for i, line in enumerate(read_obj):
        words_count = len(line.split(' '))
        print(f'В {i+1}-й строке - {words_count} слов')
        str_count += 1

print(f'Количество строк в тексте: {str_count}')