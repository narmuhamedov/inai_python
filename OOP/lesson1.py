#Создать суперкласс(на ваше усмотрение) к нему добавить минимум 10 атрибутов
#Провести через self
#Создать пару методов к супер классу и создать объекты

#Создать 2 дочених класса унаследовать их методы и атрибуты от супер класса
# и так же создать к 2м классам свои собственные арибуты и методы
#создать объекты к классам





# class NormalFather:
#     def __init__(self, muscul, sport, books, cook):
#         self.m = muscul
#         self.s = sport
#         self.b = books
#         self.c = cook
#
#     def millitary(self,yes_no):
#         return f'{yes_no}'
#
#     def __str__(self):
#         return f'{self.m}\n' \
#                f'{self.s}\n' \
#                f'{self.b}\n' \
#                f'{self.c}'
#
# obj1 = NormalFather(True, True, True, True)
# print(obj1.millitary(True))
# print(obj1)
#
# class NotNormalSoon(NormalFather):
#     def __init__(self, muscul, sport, books, cook, vodka, lgbt, gender):
#         super().__init__(muscul, sport, books, cook)
#         self.v = vodka
#         self.lgt = lgbt
#         self.g = gender
#
#
#     def __str__(self):
#         return super(NotNormalSoon, self).__str__()+f'{self.v}\n' \
#                                                     f'{self.lgt}\n' \
#                                                     f'{self.g}'
#
# soon1 = NotNormalSoon(muscul=False, sport=False, books=True, cook=False,
#                       vodka=True, lgbt=True, gender=False)
#
# print('-'*50)
# print(soon1.millitary(False))
# print(soon1)





# class Person:
#     #This is magic method for write attribute
#     def __init__(self, name, age, height, hobby, nummer):
#         self.name = name
#         self.age = age
#         self.height = height
#         self.hobby = hobby
#         self.nummer = nummer
#
#     #This is object method
#     def speak(self, language):
#         if language == 'Russian':
#             return f'Меня зовут {self.name} Я говорю на {language} я живу в СНГ'
#         elif language == 'Deutsch':
#             return f'Меня зовут {self.name} Я говорю на {language} я живу в Deutschland'
#         elif language == 'Japan':
#             return f'Меня зовут {self.name} Я говорю на {language} я живу в Японии'
#         else:
#             return f'Я не живу в этих странах!'
#
#     #This is magic method for output
#     def __str__(self):
#         return f'Имя - {self.name}\n' \
#                f'Возраст - {self.age}\n' \
#                f'Рост - {self.height}\n' \
#                f'Хобби - {self.hobby}\n' \
#                f'Номер т. - {self.nummer}'
#
# human1 = Person(name="Radomir", age=25, height=1.84, hobby='Read Books', nummer=True)
# human2 = Person('John', 20, 1.90, 'qwerty', False)
# print(human1)
# print(human1.speak(str(input('На каком языке вы говорите? '))))
# print('-'*50)
# print(human2)