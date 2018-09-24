# Задача - 1
# Ранее мы с вами уже писали игру, используя словари в качестве
# структур данных для нашего игрока и врага, давайте сделаем новую, но уже с ООП
# Опишите базовый класс Person, подумайте какие общие данные есть и у врага и у игрока
# Не забудьте, что у них есть помимо общих аттрибутов и общие методы.
# Теперь наследуясь от Person создайте 2 класса Player, Enemy.
# У каждой сущности должы быть аттрибуты health, damage, armor
# У каждой сущности должно быть 2 метода, один для подсчета урона, с учетом брони противника,
# второй для атаки противника.
# Функция подсчета урона должна быть инкапсулирована
# Вам надо описать игровой цикл так же через класс.
# Создайте экземпляры классов, проведите бой. Кто будет атаковать первым оставляю на ваше усмотрение.

class Person:
    def __init__(self, health, damage, armor):
        self.health = health
        self.damage = damage
        self.armor = armor

    def _result_damage(self, enemy):
        return self.damage / enemy.armor

    def attack(self, enemy):
        enemy.health -= self._result_damage(enemy)

class Player(Person):
    def name(self):
        self.name = input('введите имя героя: ')


class Enemy(Person):
    def name(self):
        self.name = input('введите имя противника: ')

player = Player(100, 100, 1.2)
player.name()

enemy = Enemy(100, 50, 1.2)
enemy.name()

class Game:
    def __init__(self, player, enemy):
        self._player = player
        self._enemy = enemy

    def start(self):
        last_attacker = self._player
        while self._player.health > 0 and self._enemy.health > 0:
            if last_attacker == self._player:
                self._enemy.attack(self._player)
                last_attacker = self._enemy
            else:
                self._player.attack(self._enemy)
                last_attacker = self._player
        if player.health > 0:
            print('{} победил.'.format(player.name))
        else:
            print('{} победил.'.format(enemy.name))


game = Game(player, enemy)

game.start()
