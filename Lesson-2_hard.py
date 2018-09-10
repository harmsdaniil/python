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