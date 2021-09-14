class Data:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def to_number(cls, data):
        day, month, year = [i for i in [int(i) for i in data.split('-')]]
        return cls(day, month, year)

    @staticmethod
    def validation(obj):
        if obj.day not in range(1, 32):
            print('Ошибка! Проверьте дату')
        elif obj.month not in range(1, 13):
            print('Ошибка! Проверьте месяц')
        elif obj.year not in range(1, 2100):
            print('Ошибка! Проверьте год')


my_cls = Data.to_number('31-04-2104')
print(my_cls.day)
print(my_cls.month)
print(my_cls.year)
Data.validation(my_cls)