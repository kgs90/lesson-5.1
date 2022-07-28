import random

greeting = ('Игра "Забери все конфеты!" '
    'Основные правила : '
    'Нам будет дано некоторое количество конфет, '
    'за один ход мы можем взять не более определённого количества. '
    'Итак, начнём!')
            

messages = ['Ваша очередь брать конфеты', 'возьмите конфеты', 
            'сколько конфет возьмёте?', 'берите, еще', 'Ваш ход']


def play_game(n, m, players, messages):
    count = 0
    if n%10 == 1 and 9 > n > 10: letter = 'а'
    elif 1 < n%10 < 5 and 9 > n > 10: letter = 'ы'
    else: letter = ''
    while n > 0:
        print(f'{players[count%2]}, {random.choice(messages)}')
        move = int(input())
        if move > n or move > m:
            print(f'Это слишком много, можно взять не более {m} конфет{letter}, у нас всего {n} конфет{letter}')
            attempt = 3
            while attempt > 0:
                if n >= move <= m:
                    break
                print(f'Попробуйте ещё раз, у Вас {attempt} попытки')
                move = int(input())
                attempt -=1
            else: 
                return print(f'Очень жаль, у Вас не осталось попыток. Game over!')
        n = n - move
        if n > 0: print(f'Осталось {n} конфет{letter}')
        else: print('Все конфеты разобраны.')
        count +=1
    return players[not count%2]

print(greeting)

player1 = input('Первый игрок, введите имя\n')
player2 = input('Второй игрок, введите имя\n')
players = [player1, player2]

n = int(input('Сколько конфет будем разыгрывать?\n '))
m = int(input('Сколько максимально будем брать конфет за один ход?\n '))

winer = play_game(n, m, players, messages)
if not winer:
    print('У нас нет победителя.')
else: print(f'Поздравляю! В этот раз победил {winer}!')