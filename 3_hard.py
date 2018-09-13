# Задание - 1
# Давайте опишем пару сущностей player и enemy через словарь,
# который будет иметь ключи и значения:
# name - строка полученная от пользователя,
# health - 100,
# damage - 50.
# Поэксперементируйте с значениями урона и жизней по желанию.
# Теперь надо создать функцию attack(person1, person2), аргументы можете указать свои,
# функция в качестве аргумента будет принимать атакующего и атакуемого,
# функция должна получить параметр damage атакующего и отнять это количество
# health от атакуемого. Функция должна сама работать с словарями и изменять их значения.

import random

player = dict(name=input('Введите имя игрока:'), health=100, damage=50)
enemy = dict(name=input('Введите имя противника:'), health=100, damage=50)

print(player)
print(enemy)


def attack(pers1, pers2):
    pers2['health'] -= pers1['damage']


attack(player, enemy)

print('Значения после атаки:')
print(player)
print(enemy)

# Задание - 2
# Давайте усложним предыдущее задание, измените сущности, добавив новый параметр - armor = 1.2
# Теперь надо добавить функцию, которая будет вычислять и возвращать полученный урон по формуле damage / armor
# Следовательно у вас должно быть 2 функции, одна наносит урон, вторая вычисляет урон по отношению к броне.

# Сохраните эти сущности, полностью, каждую в свой файл,
# в качестве названия для файла использовать name, расширение .txt
# Напишите функцию, которая будет считывать файл игрока и его врага, получать оттуда данные, и записывать их в словари,
# после чего происходит запуск игровой сессии, где сущностям поочередно наносится урон,
# пока у одного из них health не станет меньше или равен 0.
# После чего на экран должно быть выведено имя победителя, и количество оставшихся единиц здоровья.

print('\n----------')
print('\nЗадание 2')

# восстанавливаем значения, добавляем ключ 'armor'
player['armor'] = 1.2
enemy['armor'] = 1.2
enemy['health'] = 100


def dmg(pers1, pers2):
    d = pers1['damage'] / pers2['armor']
    if pers2['health'] >= d:
        return d
    else:
        return pers2['health']


def attack(pers1, pers2):
    pers2['health'] -= dmg(pers1, pers2)


def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


def save_essence(p):
    with open(p['name'] + '.txt', 'w', encoding='UTF-8') as f:
        for x, y in p.items():
            f.write(str(x) + ':' + str(y) + '\n')


def read_essence(fname):
    with open(fname, 'r', encoding='UTF-8') as f:
        x = f.readlines()
        ret_value = {}
        for i in x:
            i1, i2 = i.strip().split(':')
            if isfloat(i2):
                i2 = float(i2)
            ret_value[i1] = i2
        return ret_value


save_essence(player)
save_essence(enemy)

player = read_essence(player['name'] + '.txt')
enemy = read_essence(enemy['name'] + '.txt')

print('Считаны данные:')
print(player)
print(enemy)

print('Начало игровой сессии...')

if random.randint(0, 1):
    pers1 = player
    pers2 = enemy
else:
    pers1 = enemy
    pers2 = player

print('Первым ходит {}'.format(pers1['name']))

while True:
    print('{} [{:.2f} hp] наносит урон {:.2f}'.format(pers1['name'], pers1['health'], dmg(pers1, pers2)))
    attack(pers1, pers2)
    if not pers2['health']:
        break
    print('{} [{:.2f} hp] наносит урон {:.2f}'.format(pers2['name'], pers2['health'], dmg(pers2, pers1)))
    attack(pers2, pers1)
    if not pers1['health']:
        break

if not pers1['health']:
    print('Победитель: {} [{:.2f} hp]'.format(pers2['name'], pers2['health']))
else:
    print('Победитель: {} [{:.2f} hp]'.format(pers1['name'], pers1['health']))