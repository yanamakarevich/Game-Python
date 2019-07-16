import random
array=[1,2,3,4,5,6,7,8,9,10]
number=random.choice(array)
print("Угадай число которое я загадал? :)")
print("Подсказка: число от 1 до 10")
trying=int(1)
while True:
    a=int(input())
    if a==number:
        break
    if a!=number:
        if a>number:
            print("Не угадал. Твое число больше. Попробуй еще раз.")
            trying+=1
        elif a <number:
            print("Не угадал. Твое число меньше. Попробуй еще раз.")
            trying+=1
print("Ты угадал! Молодец!")
print("Колличество попыток: ",trying)
    
        
  

