import os
import random

move_list = ['papel', 'pedra', 'tesoura']
player_count = 0
computer_count = 0

print('- - - - - - - - - -')
print('Bem-vindo ao jogo "Papel, Pedra e Tesoura!"')

def main_print():
    print('- - - - - - - - - -')
    print('\nPLACAR:')
    print('Você: {}'.format(player_count))
    print('Computador: {}'.format(computer_count))
    print('\n')
    print('Escolha seu lance:')
    print('0 - PAPEL | 1 - PEDRA | 2 - TESOURA')

# retorna um elemento da move_list aleatoriamente
def select_move():
    return random.choice(move_list)

# recebe a jogada do humano
def get_player_move():
    while True:
        try:
            player_move = int(input())
            if player_move not in [0, 1, 2]:
                raise
            return move_list[player_move]

        except Exception as e:
            print(e)

def select_winner(p_move, c_move):
# comparação dos duelos do humano vs. computador (pode ser o contrário)
    global player_count, computer_count
    if p_move == 'papel':
        # papel ganha da pedra
        if c_move == 'pedra':
            player_count += 1
            return 'p'
        # papel perde da tesoura
        if c_move == 'tesoura':
            computer_count += 1
            return 'c'
        # empate
        else:
            return 'd'

    if p_move == 'pedra':
        # pedra perde do papel
        if c_move == 'papel':
            computer_count += 1
            return 'c'
        # pedra ganha da tesoura
        if c_move == 'tesoura':
            player_count += 1
            return 'p'
        # empate
        else:
            return 'd'

    if p_move == 'tesoura':
        # tesoura perde da pedra
        if c_move == 'pedra':
            computer_count += 1
            return 'c'
        # tesoura ganha do papel
        if c_move == 'papel':
            player_count += 1
            return 'p'
        # empate
        else:
            return 'd'

again = 1 
while again == 1:
    main_print()
    player_move = get_player_move()
    computer_move = select_move()
    winner = select_winner(player_move, computer_move)

    print('')
    print('- - - - - - - - - -')
    print('Sua jogada: {}'.format(player_move.upper()))
    print('Jogada do computador: {}'.format(computer_move.upper()))
    if winner == 'p':
        print('Você venceu!')
    elif winner == 'c':
        print('Computador venceu!')
    else:
        print('Empate!')
    print('- - - - - - - - - -')

    while True:
        print('Jogar novamente?')
        print('0 - NÃO | 1 - SIM')
        next = int(input())
        if next == 0:
            again = 0
            break
        elif next == 1:
            break

    os.system("CLS")


    
