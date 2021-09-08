class Worker():
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.wage = wage
        self.bonus = bonus
        self._income = {"wage": self.wage, "bonus": self.bonus}


class Position(Worker):

    def get_full_name(self):
        print(self.name + ' ' + self.surname)

    def get_total_income(self):
        self._income = self._income['wage'] + self._income['bonus']
        print(self.position, self._income)


i = Position('Pavel', 'Snopkovskiy', 'homework_maker', 50000, 12500)
i.get_full_name()
i.get_total_income()