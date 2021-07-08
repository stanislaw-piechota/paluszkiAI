import os

#instructions
print("Left -> l, Right -> r\n")
print("Example input: lr")
print("Meaning: Left hand's fingers go to oponent's right hand\n")
input("Click ENTER to continue")
os.system("cls")

def print_game():
    print(f"Player 1: {player[0]} {player[1]}")
    print(f"Player 2: {player2[0]} {player2[1]}\n")
def defense_input():
    while True:
        if tour%2: f, s = player, player2
        else: f, s = player2, player

        inp = input("Your move: ")
        if len(inp) != 2:
            print("Input must contain exactly 2 characters\n"); continue
        if inp[0] not in ['l', 'r'] or inp[1] not in ['l', 'r']:
            if inp == 'ss':
                if f in [[0, 2], [2, 0], [4, 0], [0, 4]]: return inp
                print("Splitting is not allowed in this configuration\n"); continue
            print("Allowed characters: l, r, ss\n"); continue
        if (inp[0] == 'l' and not f[0]) or (inp[0] == 'r' and not f[1]):
            print("You cannot use empty hands\n"); continue
        if (inp[1] == 'l' and not s[0]) or (inp[1] == 'r' and not s[1]):
            print("You cannot give fingers to empty hand\n"); continue
        return inp
def process_move(move):
    global player, player2
    if tour%2: f, s = player, player2
    else: f, s = player2, player

    if move == 'ss':
        if f[0]:
            f[1] = f[0]//2; f[0]=f[0]//2
        else:
            f[0] = f[1]//2; f[1]=f[1]//2
        return
    if move[0] == 'l':
        add = f[0]
    else: add = f[1]
    if move[1] == 'l':
        s[0] += add
    else: s[1] += add
    if s[0] >= 5: s[0] = 0
    if s[1] >= 5: s[1] = 0
def check_win():
    if player2 == [0,0]:
        print("Player 1 won!!!")
        return True
    if player == [0, 0]:
        print("Player 2 won!!!")
        return True
    return False

player2 = [1, 1]
player = [1, 1]
tour = 1
while True:
    print_game()
    print('PLAYER\'S 1 TURN')
    process_move(defense_input()); tour += 1
    if check_win(): break
    os.system("cls")

    print_game()
    print('PLAYER\'S 2 TURN')
    process_move(defense_input()); tour += 1
    if check_win(): break
    os.system("cls")
