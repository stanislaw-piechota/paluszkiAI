import os
from random import choice, randint

#instructions
print("Left -> l, Right -> r\n")
print("Example input: lr")
print("Meaning: Left hand's fingers go to oponent's right hand\n")
input("Click ENTER to continue")
os.system("cls")

def defense_input():
    while True:
        inp = input("Your move: ")
        if len(inp) != 2:
            print("Input must contain exactly 2 characters\n"); continue
        if inp[0] not in ['l', 'r'] or inp[1] not in ['l', 'r']:
            if inp == 'ss':
                if player in [[0, 2], [2, 0], [4, 0], [0, 4]]: return inp
                print("Splitting is not allowed in this configuration\n"); continue
            print("Allowed characters: l, r, ss\n"); continue
        if (inp[0] == 'l' and not player[0]) or (inp[0] == 'r' and not player[1]):
            print("You cannot use empty hands\n"); continue
        if (inp[1] == 'l' and not cp[0]) or (inp[1] == 'r' and not cp[1]):
            print("You cannot give fingers to empty hand\n"); continue
        return inp
def process_move(move):
    global player
    if move == 'ss':
        if player[0]: player = [player[0]//2, player[0]//2]
        else: player = [player[1]//2, player[1]//2]
        return
    if move[0] == 'l':
        add = player[0]
    else: add = player[1]
    if move[1] == 'l':
        cp[0] += add
    else: cp[1] += add
    if cp[0] >= 5: cp[0] = 0
    if cp[1] >= 5: cp[1] = 0
def computer_move():
    if not cp[0]: add = cp[1]
    elif not cp[1]: add = cp[0]
    else: add = choice(cp)

    if not player[0]: player[1] += add
    elif not player[1]: player[0] += add
    else: player[randint(0, 1)] += add

    if player[0] >= 5: player[0] = 0
    if player[1] >= 5: player[1] = 0
def check_win():
    if cp == [0,0]:
        print("You won!!!")
        return True
    if player == [0, 0]:
        print("Computer won!!!")
        return True
    return False

cp = [1, 1]
player = [1, 1]
while True:
    print(f"Computer: {cp[0]} {cp[1]}")
    print(f"You:      {player[0]} {player[1]}\n")

    process_move(defense_input())
    if check_win(): break
    computer_move()
    if check_win(): break

    os.system("cls")
