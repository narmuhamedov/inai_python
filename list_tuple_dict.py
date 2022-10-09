# data_types = [1,3, 'hello', 'text', 1234, 34.23]
# data_types2 =list()
# data_types2.append(data_types.pop(0))
# data_types2.append(data_types.pop(0))
# data_types2.append(data_types.pop(0))
# print(data_types2)

# data_types2 = [12,33, 'hello']
# data_types2.extend(data_types)
# print(data_types2)


# data_types2 = []

# for i in data_types:
#     if type(i) == str:
#         data_types2.append(i)
# print(data_types2)

# #структура данных list tuple dict - списки кортежи и словари
# spisok1 = [1, 3, 5, 10, 20, 50, 100, 200,500, '1k', '2k', '5k']
# spisok2 = ['nothing','nothing','nothing','nothing', 'Т.Молдо',
#            'К.Датка', 'Т.Сатылганов', 'А.Осмонов', 'Каралаев',
#            'Ж.Баласагын', 'Манас', 'Чокморов']
# print(spisok1)
# print(spisok2)
#
# money = dict(zip(spisok1,spisok2))
# print(money)
#
# for keys, values in money.items():
#     print(f'{keys}-{values}')

# #dict - словари
# student = {
#     'name': 'Jony',
#     'age': 18,
#     'height': 1.90,
#     2004: 'monkey',
#     'education': False,
#     True: 'work',
#     'number': ['0550777888', '0777666555'],
# }
#
# #Добавление
# student['course'] = 1
# #Удаление
# del student[True]
#
# #Изменить
# student['education'] = 'clear'
#
# print(student)
# print(student.keys())
# print(student.values())
#
# for keys, values in student.items():
#     print(f'{keys}:{values}')


# print(student[2004])
# print(type(student))


# nominal = (1,3,5,10,20,50,100,200,500,1000,2000,5000,1)
# print(type(nominal))
# print(nominal.count(1))
# print(nominal.index(10))
#
# nominal = list(nominal)
# nominal.append('123')
# nominal = tuple(nominal)
# print(type(nominal))
# print(nominal)

# number = [3,1,4,5,6,11,33,231,123,5543,323454,23,11]
# number.sort()
# number.reverse()
# print(number)

# word = 'hello'
# word = list(word)
# word.reverse()
# print(word)


# name = 'Jony'
# name = list(name)
# print(name)

# text = ['hello', 123, 'inai', 45, True, 33.12, False, 123.443]


#измение
# text[0] = 'I Love Python'

#remove, del
# text.remove(123.443)
# del text[-1]

#append, insert
# text.insert(2, 'hello world')
# text.append('Projector')
# text.append('student')
# text.append(123)
# text.append(34.55)
# print(text)

# print(type(text))