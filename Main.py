import random
comp = random.randint(1, 3)
player = int(input("""    1 - Ножницы
    2 - Бумага
    3 - Камень
Выбери свою сторону: """))

if comp == 1:
    print('Копьютер выбрал: Ножницы')
elif comp == 2:
    print('Компьютер выбрал: Бумага')
elif comp == 3:
    print('Компьютер выбрал: Камень')

if player == comp:
    print("Ничья")
elif ((player == 1 and comp == 3) or (player == 2 and comp == 1) or (player == 3 and comp == 2)):
    print("You Lose!")
else:
    print('You Win!')