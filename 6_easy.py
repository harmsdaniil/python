# Задача - 1
# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
#  о том что машина поехала, остановилась, повернула(куда)

# Задача - 2
# Посмотрите на задачу-1 подумайте как выделить общие признаки классов
# в родительский и остальные просто наследовать от него.


# Сразу запихнул всё в суперкласс, для полицейской машины добавил метод "Погоня"

class Car:
    def __init__(self, speed, color, name, is_police = False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        if is_police:
            print(name + ' - машина полицейских')

    def go(self):
        print('Машина {} тронулась с места'.format(self.name))

    def stop(self):
        print('Машина {} остановилась'.format(self.name))

    def turn(self, direction):
        print('Машина {} повернула {}'.format(self.name, direction))

class TownCar(Car):
    pass

class SportCar(Car):
    pass

class WorkCar(Car):
    pass

class PoliceCar(Car):
    def pogonja(self):
        print('Полицейская машина {} начала погоню за преступником'.format(self.name))


town_car = TownCar(100, 'Чёрная', 'Копейка')
town_car.go()

sport_car = SportCar(200, 'red', 'Ferrari')
sport_car.turn('направо')

police_car = PoliceCar(100, 'Белый', 'Бобик', True)
police_car.stop()
police_car.go()
police_car.pogonja()