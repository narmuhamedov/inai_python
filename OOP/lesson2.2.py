# class Car:
#     def __init__(self, title, volume, year, color):
#         self.title = title
#         self.volume = volume
#         self.year = year
#         self.color = color
#
#     def __str__(self):
#         return f'{self.title}\n' \
#                f'{self.volume}\n' \
#                f'{self.year}\n' \
#                f'{self.color}'
#
#
# class GazolineCar(Car):
#     def __init__(self, title, volume, year, color):
#         super().__init__(title, volume, year, color)
#
#     def __str__(self):
#         return super(GazolineCar, self).__str__()
#
# class ElectricCar(Car):
#     def __init__(self, title, volume, year, color):
#         super().__init__(title, volume, year, color)
#     def __str__(self):
#         return super(ElectricCar, self).__str__()
#
# class HybridCar(GazolineCar, ElectricCar):
#     def __init__(self, title, volume, year, color):
#         super().__init__(title, volume, year, color)
#
#     def __str__(self):
#         return super(HybridCar, self).__str__()



# class Engie:
#     def __init__(self, volume, title, mileage):
#         self.volume = volume
#         self.title = title
#         self.mileage = mileage
#
#     def __str__(self):
#         return f'{self.volume}\n' \
#                f'{self.title}\n' \
#                f'{self.mileage}'
#
#     def drive(self):
#         return f'This is engie can good drive for moto and car'
#
# class Moto(Engie):
#     def __init__(self, volume, title, mileage):
#         super().__init__(volume, title, mileage)
#
#     def __str__(self):
#         return super(Moto, self).__str__()
#
# moto_1 = Moto(volume=1.6, title='Toyo', mileage=6000)
# print(moto_1.drive())
# print(moto_1)
#
# class Auto(Engie):
#     def __init__(self, volume, title, mileage):
#         super().__init__(volume, title, mileage)
#     def __str__(self):
#         return super(Auto, self).__str__()
#
# auto1 = Auto(volume=5.0, title='V6', mileage=100000)
# print(auto1)
# print(auto1.drive())