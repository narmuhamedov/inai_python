univer = list()
technikum = list()
army = list()
married = list()


abiturients = [
    {'name': 'Baitemir', 'ORT':110, 'gender': 'male'},
    {'name': 'Maktym', 'ORT': 0, 'gender': 'female'},
    {'name': 'Rustam', 'ORT': 20, 'gender': 'male'},
    {'name': 'Nurzada', 'ORT': 5, 'gender': 'female'},
    {'name': 'Artur', 'ORT': 90, 'gender': 'male'},
    {'name': 'Aaly', 'ORT': 20, 'gender': 'male'},
    {'name': 'Kyz Saikal', 'ORT': 0, 'gender': 'female'},
    {'name': 'Aijamal', 'ORT': 500, 'gender': 'female'},
    {'name': 'Aziz', 'ORT': 900, 'gender': 'male'},
    {'name': 'Jonh', 'ORT': 0, 'gender': 'male'}

]

def all_abit(lst):
    for i in lst:
        for key, value in i.items():
            print(f'{key}-{value}')

def selecion(lst, univer:list,technikum:list, army:list, married:list):
    for i in lst:
        if i['ORT']>=110:
            univer.append(i)
        elif i['ORT']<=109 and i['ORT']>=60:
            technikum.append(i)
        elif i['ORT']<=59 and i['gender']=='male':
            print(army.append(i))
        elif i['ORT']<=59 and i['gender']=='female':
            print(married.append(i))

selecion(abiturients, univer, technikum, army, married)
print('-'*30)
print(f'Univer - {univer}\n'
      f'Technikum - {technikum}\n'
      f'Army - {army}\n'
      f'Married - {married}')









#try exept

# try:
#     a = '12'
#     b = 12
#     print(a+b)
# except:
#     print('Ты шо такое дэлаешь?')



#функции в python

# def menu(**kwargs):
#     return kwargs
#
# eat = menu(morning='Бекон с яйцом и луком', luch='Суп с фрикадельками',dinner='Казкан мант')
# print(type(eat))


# def average(*args):
#     return f'{args}\n' \
#            f'{args}\n' \
#            f'{args}'
#
# a = average('qwer','qwert', 'qwert')
# print(a)



# def plus(a,b,c=12):
#     return a+b+c
# print(plus(2,3,3))

# def about_my_self(name, age, hobby, education, laptop):
#     return f'Имя - {name.capitalize()}\n' \
#            f'Возраст - {age}\n' \
#            f'Хобби - {hobby}\n' \
#            f'Образование-{education}\n' \
#            f'Ноутбук - {laptop}'
# about = about_my_self(str(input()), int(input()), str(input()),
#                       bool(input()), bool(input())
#                       )
#
# print(about)




#return
# def summa(a,b,c):
#     return (a+b+c)/3
#
# a = summa(1,3,44)
# print(a)
# print(summa(1,3,1))




# def greeting(name):
#     print(f'Hello {name}')
#
# greeting(str(input('Введите имя1? ')))
# greeting(str(input('Введите имя2? ')))
# greeting(str(input('Введите имя3? ')))

# def square(a, b):
#     print(a*b)
#
# square(12,21)
# square(321,1234)




# a = 12
# b = 12
# print(a+b)
#
# c = 21
# n = 22
# print(c+n)