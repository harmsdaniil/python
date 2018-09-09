# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.
print('easy')
print('\nЗадание 1')
fructi=['яблоко', 'груша', 'мандарин', 'апельсин', 'банан']
for index, name in enumerate(fructi):
    print(f'{index+1} {name:>10}')

# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.
print('\nЗадание 2')
spisok_1={1,2,3,4,5}
spisok_2={3,4,5,6,7}

print(spisok_1-spisok_2)

# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

print('\nЗадание 3')

celie=[1,15,29,3,4,56]
new_spisok=[]
for i in range(len(celie)):
    if celie[i] % 2 == 0:
        new_spisok.append(celie[i] / 4)
    else:
        new_spisok.append(celie[i] * 2)
print(new_spisok)



print('\nnormal')
print('\nЗадание 1')

# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]

import math
list_1=[2, -5, 8, 9, -25, 25, 16]
list_2=[]
for item in list_1:
    if item>0 and math.sqrt(item)%1 == 0:
        list_2.append(int(math.sqrt(item)))
print(list_2)


print('\nЗадание 2')
# Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.
# Склонением пренебречь (2000 года, 2010 года)

date = input ('Введите дату в формате dd.mm.yyyy: ')
new_date =  (date.split('.'))
day = {'01':'первое',
       '02':'второе',
       '03':'третье',
       '04':'четвертое',
       '05':'пятое',
       '06':'шестое',
       '07':'седьмое',
       '08':'восьмое',
       '09':'девятое',
       '10':'десятое',
       '11':'одинадцатое',
       '12':'двенадцатое',
       '13':'тринадцатое',
       '14':'четырнадцатое',
       '15':'пятьнадцатое',
       '16':'шестьнадцатое',
       '17':'семнадцатое',
       '18':'восемнадцатое',
       '19':'девятнадцатое',
       '20':'двадцатое',
       '21':'двадцать первое',
       '22':'двадцать второе',
       '23':'двадцать третье',
       '24':'двадцать четвертое',
       '25':'двадцать пятое',
       '26':'двадцать шестое',
       '27':'двадцать седьмое',
       '28':'двадцать восьмое',
       '29':'двадцать девятое',
       '30':'дридцатое',
       '31':'тридцать первое'}
month = {'01':'января',
         '02':'февраля',
         '03':'марта',
         '04':'апреля',
         '05':'мая',
         '06':'июня',
         '07':'июля',
         '08':'августа',
         '09':'сентября',
         '10':'октября',
         '11':'ноября',
         '12':'декабря'}
print('Сегодня {} {} {} года.'.format(day[new_date[0]], (month[new_date[1]]), new_date[2]))



print('\nЗадание 3')
# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random

import random
count = int (input('Введите количество элементов: '))
mylist = []
n = 0
while n < count:
    mylist.append(random.randint(-100, 100))
    n +=1
print(mylist)

print('\nЗадание 4')
# Задача-4: Дан список, заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут:
# а) неповторяющиеся элементы исходного списка:
# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
# б) элементы исходного списка, которые не имеют повторений:
# например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]

# Решение а)
print('\n4-а')

list_3 = [1, 2, 4, 5, 6, 2, 5, 2]
new_list = set(list_3)
print(new_list)

# Решение б)
print('\n4-б')

list_4 = []
for item in list_3:
    if list_3.count(item) == 1:
        list_4.append(item)
print(list_4)



print('\nhard')
print('\nЗадание 1')

# Задание-1: уравнение прямой вида y = kx + b задано в виде строки.
# Определить координату y точки с заданной координатой x.
# equation = 'y = -12x + 11111140.2121'
# x = 2.5
# вычислите и выведите y

equation = 'y = -12x + 11111140.2121'
x = 2.5
znach = equation.split()
znach_1 = str(znach[2])
znach[2] = znach_1[:-1]
y = float(znach[2]) * x + float(znach[4])
print(y)

print('\nЗадание 2')
# Задание-2: Дата задана в виде строки формата 'dd.mm.yyyy'.
# Проверить, корректно ли введена дата.
# Условия корректности:
# 1. День должен приводиться к целому числу в диапазоне от 1 до 30(31)
#  (в зависимости от месяца, февраль не учитываем)
# 2. Месяц должен приводиться к целому числу в диапазоне от 1 до 12
# 3. Год должен приводиться к целому положительному числу в диапазоне от 1 до 9999
# 4. Длина исходной строки для частей должна быть в соответствии с форматом
#  (т.е. 2 символа для дня, 2 - для месяца, 4 - для года)

# Пример корректной даты
# date = '01.11.1985'

# Примеры некорректных дат
# date = '01.22.1001'
# date = '1.12.1001'
# date = '-2.10.3001'


days_count_by_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
date = input('Введите дату:')
day, month, year = date.split('.')

if len(day) == 2 and len(month) == 2 and len(year) == 4:
    if 0 < int(month) <= 12 \
            and 0 < int(year) <= 9999 \
            and 0 < int(day) <= days_count_by_month[int(month)]:
        print('Дата корректна')
    else:
        print('Дата некорректна')
else:
    print('Длина одной из частей даты некорректна')