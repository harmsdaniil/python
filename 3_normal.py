# Задание - 1
# Вам даны 2 списка одинаковой длины, в первом списке имена людей, во втором зарплаты,
# вам необходимо получить на выходе словарь, где ключ - имя, значение - зарплата.
# Запишите результаты в файл salary.txt так, чтобы на каждой строке было 2 столбца,
# столбцы разделяются пробелом, тире, пробелом. в первом имя, во втором зарплата, например: Vasya - 5000
# После чего прочитайте файл, выведите построчно имя и зарплату минус 13% (налоги ведь),
# Есть условие, не отображать людей получающих более зарплату 500000, как именно
#  выполнить условие решать вам, можете не писать в файл
# можете не выводить, подумайте какой способ будет наиболее правильным и оптимальным,
#  если скажем эти файлы потом придется передавать.
# Так же при выводе имя должно быть полностью в верхнем регистре!
# Подумайте вспоминая урок, как это можно сделать максимально кратко, используя возможности языка Python.

names = ['Кондрат', 'Велимир', 'Даниил']
salaries = ['10000', '20000', '5000000']
#создаём функцию для возвращения верхнего регистра
def upp(names):
    nameupp = []
    for name in names:
        nameupp.append(name.upper())
    return nameupp

salaries_dict = dict(zip(upp(names), salaries)) #готовим словарь через dict, где имена в верхнем регистре и суммы. Используем краткую форму zip

def make_beauty_list(salaries_dict): #функция для вывода в виде 'имя - '
    for name in salaries_dict.keys():
        print(name + ' ' '-' ' ' + salaries_dict[name])


list_to_write = make_beauty_list(salaries_dict)

with open('salary.txt', 'w+', encoding='UTF-8') as file:
    for line in salaries_dict.keys():
        file.write(line + ' ' '-' ' ' + salaries_dict[line] + '\n')

with open('salary.txt', 'r', encoding='UTF-8') as file:
    for line in file:
        people = (line).split()
        people_salary = int(people[2])
        if people_salary >= 500000:
            continue
        else:
            print(people_salary - (people_salary * 0.13))