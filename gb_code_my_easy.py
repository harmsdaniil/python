haus_number = 45  # int (integer)
liter = 'Б'  # str (string)
room_number = 6

print('Задача 1')
print('Lenina',' ',int(haus_number),liter,' ','Kvartira #',int(room_number) )
ulitsa=input('Введите название улицы:')
print('Улица ', ulitsa)

print('Задача 2')
chislo=input('Введите число:')
print(int(chislo)+2)

print('Задача 3')
vozr=int(input('Введите свой возраст: '))
if  vozr>=18:
    print('Доступ разрешён')
else:
    print('Извините, пользование данным ресурсом разрешено только с 18 лет')