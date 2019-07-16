def computer():
    print("Мой ход.\n1 - Давай")
    go=int(input())
    if go==1:
        hodComp=random.choice(eaqleTails)
        if hodComp==1:
            print("Ура! Вы победили! А вашему компьютеру пора в утиль..")
            print("Поздравляю!")
            sys.exit()
        elif hodComp==0:
            print("Похоже сегодня мой день. Можете ли сказать такое и ты?")
            print("Осталось",6-i,"зарядов.")
def people():
    print("Твой ход. 1 - Крутить барабан")
    drum=int(input())
    if drum==1:
        hodPeople=random.choice(eaqleTails)
        if hodPeople==1:
            print("К сожалению вы уже не прочтете эти слова.")
            print("Вы проиграли и вас больше нет.")
            print("Возможно именно так однажды компьтеры захватят мир..")
            sys.exit() 
        elif hodPeople==0:
            print("Хм...ну допустим повезло.")
            print("Осталось",6-i,"зарядов.")
import sys
import random
eaqleTails=[0,1]
print("Давай сыграем с тобой в одну игру? Останется только один, либо ты либо я!")
print("Правила простые, у нас на двоих 6 зарядов, в одном из них пуля. Будем стрелять по очереди.")
print("Подбросим монетку. Что выбираешь? \nОрел - 0, Решка - 1")
option=int(input())
a=random.choice(eaqleTails)
if option==a:
    print("Ты начинаешь.")
    for i in range(1,7):
        if i%2!=0:
            people()
        elif i%2==0:
            computer()
elif option!=a:
    print("Я начинаю.")
    for i in range(1,7):
        if i%2!=0:
            computer()
        elif i%2==0:
            people()




