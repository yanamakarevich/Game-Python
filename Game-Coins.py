import random
print("Игра \"Монетки\" приветсвует тебя, мой юный друг!")
print("Правила очень просты. У тебя есть 10 монет. За каждое подбрасываение ты отдаешь 1 монету, если угадал - получаешь 2 монетки! Если нет - теряешь 1 монету.")
print("Максимальный выйгрыш 20 монет. Это в два раза больше чем у тебя есть! Испытай удачу!")
array=[0,1]
money=10
while money<20:
    print("\n1 - Подбросить(Стоимость - 1 монета), 0 - Закончить игру")
    option=int(input())
    if option==1:
        print("0 - Орёл, 1 - Решка")
        option=int(input())
        yesNo=random.choice(array)
        if option==yesNo:
            print("\nДа! Поздравляю! +2 монеты у тебя на счету.")
            money+=2
            print("У тебя",money,"монет")
        elif option!=yesNo:
            print("\nОуч.. мне жаль, минус 1 монета на твоем счету. Попробуй еще раз!")
            money-=1
            print("У тебя",money,"монет")
    elif option==0:
        break
if money>10:
    print("\nПоздравляю! Ты заработал",money-10,"монет на этом! Возвращайся и выигрывай еще больше!")
    print("У тебя",money,"монет!")
elif money<10:
    print("\nНе расстраивайся, что-то теряем, что-то находим. Ты потерял",10-money,"монет. Повезет в следующий раз!")
    print("У тебя",money,"монет.")
elif money==10:
    print("\nНу ты ничего не выйграл, но зато ничего и не потерял! Тоже неплохо!")
    print("Ты уходишь с тем же, с чем и пришел.",money,"монет.")
    
