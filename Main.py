import random
for x in range(0, 10, 1):
    comp = random.randint(1, 3)
    player = int(input("""    1 - Ножницы
    2 - Бумага
    3 - Камень
    Выбери свою сторону: """))

    if player > 3 or player < 1:
        print("Наверное, в вас прилетел камень.\n В этот раз введите правильное число")
        while player > 3 or player < 1:
            player = int(input())
            print("Ну введи нормально число")
            continue

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
