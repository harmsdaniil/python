# Задача - 1
# Вам необходимо создать завод по производству мягких игрушек для детей.
# Вам надо продумать структуру классов,
# чтобы у вас был класс, который создает игрушки на основании:
#  Названия, Цвета, Типа (животное, персонаж мультфильма)
# Опишите процедуры создания игрушки в трех методах:
# -- Закупка сырья, пошив, окраска
# Не усложняйте пусть методы просто выводят текст о том, что делают.
# В итоге ваш класс по производству игрушек должен вернуть объект нового класса Игрушка.

# Задача - 2
# Доработайте нашу фабрику, создайте по одному классу на каждый тип, теперь надо в классе фабрика
# исходя из типа игрушки отдавать конкретный объект класса, который наследуется от базового - Игрушка


class Toy:
    def __init__(self, name, color, material):
        self.name = name
        self.color = color
        self.material = material


class Animal(Toy):
    pass


class Cartoon(Toy):
    pass


class Factory:
    def __init__(self, toy, count):
        self.toy = toy
        self.count = count

    def purchase_materials(self):
        print('Закупаем материал {} для игрушки {}'.format(self.toy.material, self.toy.name))

    def create(self):
        print('Вышиваем из материала {} игрушку {}'.format(self.toy.material, self.toy.name))

    def paint(self):
        print('Красим {} игрушек {}'.format(self.count, self.toy.name))


leo = Animal('Лев', 'оранжевый', 'хлопок')
chebur = Cartoon('Чебурашка', 'коричневый', 'пушнина')

leo_create = Factory(leo, 105)
chebur_create = Factory(chebur, 103)

leo_create.purchase_materials()
leo_create.create()
leo_create.paint()

chebur_create.purchase_materials()
chebur_create.create()
chebur_create.paint()