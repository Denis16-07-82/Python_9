# Реализовать базовый класс Worker (работник).
# # определить атрибуты: name, surname, position (должность), income (доход);
# # последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы:
# # оклад и премия, например, {"wage": wage, "bonus": bonus};
# # создать класс Position (должность) на базе класса Worker;
# # в классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# # и дохода с учётом премии (get_total_income);
# # проверить работу примера на реальных данных: создать экземпляры класса Position,
# # передать данные, проверить значения атрибутов, вызвать
# # методы экземпляров.
class Worker:
    name = 'Denis'
    surname = 'Naumov'
    position = 'engineer'
    dict_wage = {"wage": 100000, "bonus": 100000}
    _incom = 0

    def __init__(self):
        Worker._incom = list(Worker.dict_wage.values())[0]
        print(f'Оклад сотрудника {Worker.name}:{Worker._incom}')


A = Worker()


class Position:
    name = 'Denis'
    surname = 'Naumov'
    position = 'engineer'
    dict_wage = {"wage": 100000, "bonus": 100000}
    _incom = 0

    def get_full_name(self):
        print(f'Полное имя сотрудника,на должности {Position.position}:{Position.name} {Position.surname}')

    def get_total_income(self):
        for ln in Worker.dict_wage.values():
            Position._incom += ln
        print(f'Полный доход сотрудника {Position.name}:{Position._incom}')
B=Position()
B.get_full_name()
B.get_total_income()
