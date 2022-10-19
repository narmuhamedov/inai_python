#Полиорфизм
class Engish:
    def __init__(self, language):
        self.language = language

    def greeting(self):
        return f'This is person can say {self.language}'

class Germany:
    def __init__(self, language):
        self.language = language

    def greeting(self):
        return f'Das ist man spriht auf {self.language} '

class Russian:
    def __init__(self, language):
        self.language = language

    def greeting(self):
        return f'Этот человек говорит на {self.language}'

english = Engish('Good morning')
germany = Germany('Guten Morgen')
russian = Russian('Доброе утро')

print(english.greeting())
print(germany.greeting())
print(russian.greeting())




#Инкапсуляция
# class Acount:
#     def __init__(self, login, password, secret_key):
#         self.login = login
#         self.password = password
#         self.__secret_key = secret_key
#
#
#     def __str__(self):
#         return f'login - {self.login}\n' \
#                f'password - {self.password}\n' \
#                #f'secret_key - {self.secret_key}'
#
# acc1 = Acount(login='admin', password=12345)
# print(acc1)
#
#
#



#Абстракция и наследие
# class Car:
#     def __init__(self, title, marka, volume):
#         self.title = title
#         self.marka = marka
#         self.volume = volume
#
#     def __str__(self):
#         return f'title - {self.title}\n' \
#                f'marka - {self.marka}\n' \
#                f'volume - {self.volume}'
#
#
# usual_car = Car(title='Vaz-21-07', marka='Lada', volume=1.5)
# print(usual_car)
# print('-'*20)
#
# class EuropeAuto(Car):
#     def __init__(self, title, marka, volume, abs, airbag, esp):
#         super().__init__(title, marka, volume)
#         self.abs = abs
#         self.airbag = airbag
#         self.esp = esp
#
#     def __str__(self):
#         return super(EuropeAuto, self).__str__()+f'\n abs - {self.abs}\n' \
#                                                  f'airbag - {self.airbag}\n' \
#                                                  f'esp - {self.esp}'
