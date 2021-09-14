class MyOnlyNumberException(Exception):
    def __init__(self, txt):
        self.text = txt

stop_words = ''
numbers = []
types = ['int', 'float']
while stop_words == '':
    num_ = input('Введите число (для выхода наберите "stop"): ')
    if num_ == 'stop':
        stop_words = 'stop'
    else:
        try:
            for i in num_:
                if i.isdigit() == True or i == '-' or i == '.':
                    num_ = float(num_)
                else:
                    raise MyOnlyNumberException('Ну это же не число ни разу! Будь внимателен!')
            numbers.append(num_)
        except (ValueError, MyOnlyNumberException) as err:
            print(err)
print(numbers)