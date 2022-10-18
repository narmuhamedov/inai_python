class JunDev:
    def __init__(self, name, laptop, salary, prog_lang):
        self.name = name
        self.laptop = laptop
        self.salary = salary
        self.prog_lang = prog_lang

    def prog_lang_write(self, language):
        if language == 'Python':
            print('Ты молодец')
        else:
            print('ты не молодец')


    def copy_paste(self, resourse):
        return f'Этот прогер копипастит с сайта - {resourse}'


    def __str__(self):
        return f'Имя - {self.name}\n' \
               f'Ноутбук - {self.laptop}\n' \
               f'ЗП - {self.salary}$\n' \
               f'Языки - {self.prog_lang}'

jundev1 = JunDev(name='John', laptop=True, salary=500, prog_lang='Python')
print(f'этот объект класса {jundev1}')
print(jundev1.copy_paste('StackOverFlow'))
print(jundev1.prog_lang_write(str(input())))
print('-'*50)
class MidDev(JunDev):
    def __init__(self, name, laptop, salary, prog_lang, expiriements, free_time):
        super().__init__(name, laptop, salary, prog_lang)
        self.ex = expiriements
        self.frt = free_time

    def can_be_tutor(self):
        return f'This is proger can be mentor for - {jundev1.name}'

    def __str__(self):
        return super(MidDev, self).__str__()+f'\n Опыт работы - {self.ex}\n' \
                                             f'Условное время - {self.frt}ч.'

middev1 = MidDev(name='Helena', laptop=True, salary=1500, prog_lang='Python Php Javascript',
                 expiriements=2, free_time=20)
print(f'этот объект класса {middev1}')
print(middev1.copy_paste('Other Resourse'))
print(middev1.can_be_tutor())
print('-'*50)
class SenDev(MidDev):
    def __init__(self, name, laptop, salary, prog_lang, expiriements, free_time, project_manager):
        super().__init__(name, laptop, salary, prog_lang, expiriements, free_time)
        self.pm = project_manager

    def team_lead(self):
        return f'This is proger can be teamlead for {jundev1.name}\n' \
               f'{middev1.name}'


    def __str__(self):
        return super(SenDev, self).__str__()+f'\n Проетк Менеджер - {self.pm}'


senprog1 = SenDev(name='Vasya', laptop=True, salary=5000, prog_lang='many', expiriements=10,
                  free_time=2, project_manager=True)

print(senprog1)
print(senprog1.copy_paste('All Resourse'))
print(senprog1.team_lead())

