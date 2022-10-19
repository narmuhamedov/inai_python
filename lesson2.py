import turtle
pen = turtle.Turtle()
pen.color("black")
pen.width(3)
pen.hideturtle()
pen.penup()
pen.setposition(-30, 60)
pen.pendown()
pen.forward(60)
pen.right(90)
pen.forward(120)
pen.right(90)
pen.forward(60)
pen.right(90)
pen.forward(120)
red_light=turtle.Turtle()
red_light.shape('circle')
red_light.color('red')
red_light.penup()
red_light.setposition(0,40)
yellow_light=turtle.Turtle()
yellow_light.shape('circle')
yellow_light.color('yellow')
yellow_light.penup()
yellow_light.setposition(0,0)
green_light=turtle.Turtle()
green_light.shape('circle')
green_light.color('green')
green_light.penup()
green_light.setposition(0,-40)

pen = turtle.Turtle()
pen.color("black")
pen.width(3)
pen.hideturtle()
pen.penup()
pen.setposition(+30, 60)
pen.goto(+30, 60)
pen.pendown()
pen.forward(60)
pen.goto(+30, 20)
pen.goto(+90, 20)
pen.goto(+30, -20)
pen.goto(+90, -20)
pen.goto(+30, -60)
pen.goto(+10, -60)
pen.goto(+10, -200)
pen.goto(-10, -200)
pen.goto(-10, -60)
pen.goto(-30, -60)
pen.goto(-90, -20)
pen.goto(-30, -20)
pen.goto(-90, 20)
pen.goto(-30, 20)
pen.goto(-30, 20)
pen.goto(-90, 60)
pen.goto(-30, 60)







#for while

# while 1:
#     exit = str(input('Вы хотите выйти? '))
#     if exit =='да':
#         print('Всего доброго!')
#         break
#

# box = 100
#
# box2 = 0
#
# while box != 0:
#     box -= 1
#     box2 += 1
#     print(f'С первого бокса-{box}')
#     print(f'Со второго бокса-{box2}')





# while 1:
#     print('Hepl me Please!!!')


# for i in 1,33,'qwerty', 'hello', 33.232,True,123:
#     print(i)





#if elif else

#
# time_ = str(input('Когда вы проснулись? '))
# if time_ == 'утром':
#     print(f'Вы проснулись в {time_} вы успеете на учебу!')
#
# elif time_== 'за 10' or time_== 'за 9' :
#     print(f'Вы проснулись в {time_} Вы пойдете на учебу?')
#     answer = str(input('Введите ваш ответ? да/нет'))
#     if answer == 'да':
#         print(f'Ваш ответ {answer} Вы молодец!')
#     elif answer == 'нет':
#         print(f'Ваш ответ {answer} Вы не молодец!')
#     else:
#         print('Мне ко второй!')
#
# elif time_ == 'обед':
#     print('Поздравляем ты потерял возможность учиться!')
#
# else:
#     print('Вас отчилили!')