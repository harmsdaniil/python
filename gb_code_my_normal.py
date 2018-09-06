#Задача 1

chislo=int(input('Введите число больше 0, но меньше 10: '))
while chislo<=0 or chislo>=10:
    print('Число не принадлежит диапазону "Больше нуля, меньше десяти". Введите верное значение: ')
    chislo=int(input())
else:
    print(chislo**2)


#Задача 2

a=int(input('Введите значение для переменной "а": '))
b=int(input('Введите значение для переменной "b": '))
a=a+b
b=a-b
print('b=' + str(b))
a=a-b
print('a=' + str(a))