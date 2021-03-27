#  Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты: speed, color, name, is_police(булево).
#  А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,\
#                      остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar)
#  и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
#
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
#  Вызовите методы и покажите результат.
class Car:
    speed = 100
    color = 'Red'
    name = 'Mersedes'
    is_police = bool

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def direction(self):
        print('Машина повернула налево')

    def show_speed(self):
        print(f'Скорость автомобиля {Car.name}:{Car.speed}')


class TownCar(Car):
    speed = 70

    def show_speed(self):
        if TownCar.speed > 60:
            print(f'Машина превышает скорость:ваша скорость{TownCar.speed}')
        else:
            print('Вы едете по правилам')


class SportCar(Car):
    pass


class WorkCar(Car):
    def __init__(self):
        WorkCar.speed = int(input('Выбирите скорость: '))

    def show_speed(self):
        if WorkCar.speed > 40:
            print(f'Машина превышает скорость:ваша скорость{WorkCar.speed}')
        else:
            print('Вы едете по правилам')


class PoliceCar(Car):
    pass


A = Car()
B = TownCar()
C = SportCar()
D = WorkCar()
E = PoliceCar()
A.show_speed()
print(B.speed)
B.show_speed()
print(D.speed)
D.show_speed()
