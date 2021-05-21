import random
draw = 0
win_player = 0
win_comp = 0
Mas = []
player = 1
x = 0

while player != 0:
    comp = random.randint(1, 3)
    player = int(input("""    1 - Ножницы
    2 - Бумага
    3 - Камень
    0 - Закончить игру
Выберите свою сторону: """))
    if player == 0:
        break

    if player > 3 or player < 1:
        print("Наверное, в вас прилетел камень.\nВ этот раз введите правильное число: ")
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
        draw += 1
        Mas.append("произошла ничья")
        print("Ничья")
    elif ((player == 1 and comp == 3) or (player == 2 and comp == 1) or (player == 3 and comp == 2)):
        win_comp += 1
        Mas.append('Вы проиграли')
        print("You Lose!")
    else:
        win_player += 1
        Mas.append('Вы победили')
        print('You Win!')
    x += 1

print('\t', '/'*5, 'Результаты игры', '/'*5)
for i in range(0, x, 1):
    print('\tВ', i + 1, 'раунде', Mas[i])
print('\n')

winning_percentage_player = round(float((win_player/x) * 100), 1)
winning_percentage_comp = round(float((win_comp/x) * 100), 1)
draw_percentage = round(float((draw/x) * 100), 1)

print(win_comp, "побед у компьютера -", winning_percentage_comp, '%')
print(win_player, "побед у игрока -", winning_percentage_player, '%')
print(draw, "ничьих -", draw_percentage, '%')
