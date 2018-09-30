import random
 
class Card:
    def __init__(self, rows_amount=3, cols_amount=9, nums_per_row=5, max_num=90):
        self._rows_amount = rows_amount
        self._cols_amount = cols_amount
        self._nums_per_row = nums_per_row
        self._max_num = max_num
 
class CommonCard(Card):
    counter = 0
    def __init__(self):
        Card.__init__(self, rows_amount=3, cols_amount=9, nums_per_row=5, max_num=20)
        self._title = ' '
        self._card = [['' for _ in range(self._cols_amount)] for _ in range(self._rows_amount)]   #генерим карточку - три строки с пустыми значениями
        self._nums = random.sample(range(1, self._max_num + 1), self._nums_per_row * self._rows_amount)    #генерим 15 чисел от 1 до 90 - в нашу карточку
        self._pixels = self._cols_amount * 3 - 1  #высчитываем сколько нам нужно мест в карточке???
        self.__class__.counter += 1
        self._nums_for_game = self._nums[:]
 
    @classmethod
    def get_created_instances_count(cls):
        return cls.counter
 
    def __del__(self):
        self.__class__.counter -= 1
 
    @property
    def nums(self):
        return len(self._nums_for_game)
 
    def _header(self):
        return '{:-^{}}'.format(self._title, self._pixels)
 
    def _mapping_card(self):
        for row in self._card:
            while row.count(True) != self._nums_per_row:
                i = random.randrange(self._cols_amount)
                if not row[i]:
                    row[i] = True
 
    def _filling_card_with_numbers(self):
        for i, row in enumerate(self._card):
            tmp = sorted(self._nums[i * self._nums_per_row:(i + 1) * self._nums_per_row], reverse=True)
            for j, item in enumerate(row):
                if item:
                    self._card[i][j] = tmp.pop()
 
    def __str__(self):
        res = list()
        res.append(self._header())
        for row in self._card:
            res.append(' '.join(['{:<2}'.format(x) for x in row]))
        res.append('-' * self._pixels)
        return '\n'.join(res)
 
 
    def modify_card(self, num):
        i = int(self._nums.index(num) / self._nums_per_row)
        self._card[i][self._card[i].index(num)] = '-'
        self._nums_for_game.remove(num)
 
    def check_num(self, num):
        return num in self._nums
 
    def create_card(self):
        self._mapping_card()
        self._filling_card_with_numbers()
 
class PlayerCard(CommonCard):
    def __init__(self, rows_amount=3, cols_amount=9, nums_per_row=5, max_num=90):
        CommonCard.__init__(self)
        self._name = 'Игрок {}'.format(self.get_created_instances_count())
        self._title = ' ' + 'Карточка игрока {}'.format(self.get_created_instances_count()) + ' '
 
    @property
    def name(self):
        return self._name
 
class ComputerCard(CommonCard):
    def __init__(self, rows_amount=3, cols_amount=9, nums_per_row=5, max_num=90):
        CommonCard.__init__(self)
        self._title = ' ' + 'Карточка компьютера' + ' '
        self._name = 'Компьютер'
 
        @property
        def name(self):
            return self._name
 
class Game(Card):
    def __init__(self):
        Card.__init__(self, rows_amount=3, cols_amount=9, nums_per_row=5, max_num=20)
        self._do = ['1', '2', 'exit']
        self._menu = '1 - играть с компьютером\n2 - играть с другом\nexit - выйти из игры'
        self._unit1 = None
        self._unit2 = None
 
 
    def _init_game(self):
        answer = ''
        while answer not in self._do:
            print(self._menu)
            answer = input()
        if answer == '1':
            self._init_game_pve()
        elif answer == '2':
            self._init_game_pvp()
        else:
            exit()
 
    def _create_cards(self):
        self._unit1.create_card()
        self._unit2.create_card()
 
    def _init_game_pve(self):
        self._unit1 = PlayerCard()
        self._unit2 = ComputerCard()
        self._create_cards()
 
    def _init_game_pvp(self):
        self._unit1 = PlayerCard()
        self._unit2 = PlayerCard()
        self._create_cards()
 
    def _get_random_num(self):
        random_numbers = random.sample(range(1, self._max_num + 1), self._max_num)
        for i in random_numbers:
            yield i, self._max_num - random_numbers.index(i) - 1
 
    def _check_answer(self, unit, num, answer):
        if answer == 'exit':
            print('Приходите еще поиграть')
            exit()
        elif answer != 'y' and answer != 'n':
            self._check_answer(unit, num, input('Зачеркнуть цифру? (y/n)'))
        elif answer == 'y' and unit.check_num(num):
            unit.modify_card(num)
            return 0
        elif answer == 'n' and not unit.check_num(num):
            return 0
        elif answer == 'y' and not unit.check_num(num):
            print('{} нет на вашей карточке.'.format(num), end=' ')
            return 1
        elif answer == 'n' and unit.check_num(num):
            print('{} на вашей карточке.'.format(num), end=' ')
            return 1
        else:
            print('Что-то пошло не так', answer)
            return 1
 
    def _clean(self):
        del self._unit1
        del self._unit2
 
    def _lets_play(self):
        num_generator = self._get_random_num()
        gen_res = next(num_generator)
        num = gen_res[0]
        left = gen_res[1]
 
        while self._unit1.nums and self._unit2.nums:
            print(self._unit1)
            print(self._unit2)
 
            print('Новый бочонок: {} (осталось {})'.format(num, left))
            print('Ходит {}'.format(self._unit1.name))
 
            if self._check_answer(self._unit1, num, input('Зачеркнуть цифру? (y/n)')):
                if type(self._unit2) == PlayerCard:
                    return '{}, к сожалению, вы проиграли.\nПоздравляем, {}! Вы победили'.format(self._unit1.name, self._unit2.name)
                else:
                    return '{}, к сожалению, вы проиграли.'.format(self._unit1.name)
            if type(self._unit2) == PlayerCard:
                print('Ходит {}'.format(self._unit2.name))
                if self._check_answer(self._unit2, num, input('Зачеркнуть цифру? (y/n)')):
                    return '{}, к сожалению, вы проиграли.\nПоздравляем, {}! Вы победили'.format(self._unit2.name, self._unit1.name)
            else:
                if self._unit2.check_num(num):
                    self._unit2.modify_card(num)
 
            gen_res = next(num_generator)
            num = gen_res[0]
            left = gen_res[1]
 
        if not self._unit1.nums and not self._unit2.nums:
            return 'Ничья!'
        elif self._unit2.nums:
            return 'Поздравляем, {}, вы победили!'.format(self._unit1.name)
        else:
            if type(self._unit2) == PlayerCard:
                return 'Поздравляем, {}, вы победили!'.format(self._unit2.name)
            else:
                return 'Компьютер успел первым. Попробуйте еще раз.'
 
    def main(self):
        while True:
            answer = input('Сыграем? (y/n)')
            if answer == 'y':
                self._init_game()
                print(self._lets_play())
                self._clean()
            elif answer == 'n':
                print('До свидания!')
                return
 
if __name__ == '__main__':
    game = Game()
    game.main()