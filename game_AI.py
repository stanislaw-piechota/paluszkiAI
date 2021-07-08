import os
from math import inf
from sys import platform

if "win" in platform.lower(): command = "cls"
else: command = "clear"

print("Left -> l, Right -> r\n")
print("Example input: lr")
print("Meaning: Left hand's fingers go to oponent's right hand\n")
print("Splitting: ss\n")
input("Click ENTER to continue")
os.system(command)

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
    global cp, player
    n = NodeComp(1, cp[::], player[::])
    cp, player = update2(n.best, cp[::], player[::])
def check_win():
    if cp == [0,0]:
        print("You won!!!")
        return True
    if player == [0, 0]:
        print("Computer won!!!")
        return True
    return False

def possible_moves(cp, player):
    moves = []
    if cp[0]:
        if player[0]: moves.append('ll')
        if player[1]: moves.append('lr')
    if cp[1]:
        if player[0]: moves.append('rl')
        if player[1]: moves.append('rr')
    if cp in [[0,2], [2, 0], [0, 4], [4, 0]]:
        moves.append('ss')

    return moves
def player_moves(cp, player):
    moves = []
    if player[0]:
        if cp[0]: moves.append('ll')
        if cp[1]: moves.append('lr')
    if player[1]:
        if cp[0]: moves.append('rl')
        if cp[1]: moves.append('rr')
    if player in [[0,2], [2, 0], [0, 4], [4, 0]]:
        moves.append('ss')

    return moves
def update(move, cp, player):
    if move == 'ss':
        if player[0]: player = [player[0]//2, player[0]//2]
        else: player = [player[1]//2, player[1]//2]
        return cp, player
    if move[0] == 'l':
        add = player[0]
    else: add = player[1]
    if move[1] == 'l':
        cp[0] += add
    else: cp[1] += add

    if cp[0] >= 5: cp[0] = 0
    if cp[1] >= 5: cp[1] = 0
    return cp, player
def update2(move, cp, player):
    if move == 'ss':
        if cp[0]: cp = [cp[0]//2, cp[0]//2]
        else: cp = [cp[1]//2, cp[1]//2]
        return cp, player
    if move[0] == 'l':
        add = cp[0]
    else: add = cp[1]
    if move[1] == 'l':
        player[0] += add
    else: player[1] += add

    if player[0] >= 5: player[0] = 0
    if player[1] >= 5: player[1] = 0
    return cp, player

class NodePlayer():
    def __init__(self, depth, cp, player):
        self.moves = player_moves(cp[::], player[::])
        self.children = []
        self.value = inf
        for move in self.moves:
            cpc, playerc = update(move, cp[::], player[::])
            if depth <= 5:
                self.children.append(NodeComp(depth+1, cpc, playerc))
            else:
                self.children.append([cpc, playerc])
                if cpc == [0,0]: self.value = -inf
                elif self.value > 0: self.value = 0
        if depth > 5: return
        self.values = [child.value for child in self.children]
        try:
            self.value = min(self.values)
        except ValueError:
            self.value= inf

class NodeComp():
    def __init__(self, depth, cp, player):
        self.moves = possible_moves(cp[::], player[::])
        self.children = []
        self.value = -inf
        for move in self.moves:
            cpc, playerc = update2(move, cp[::], player[::])
            if depth <=5:
                self.children.append(NodePlayer(depth+1, cpc, playerc))
            else:
                self.children.append([cpc, playerc])
                if playerc == [0,0]: self.value = inf
                elif self.value < 0: self.value = 0
        if depth > 5: return
        self.values = [child.value for child in self.children]
        try:
            self.value = max(self.values)
            self.best = self.moves[self.values.index(self.value)]
        except ValueError:
            self.value = -inf

cp = [1, 1]
player = [1, 1]
'''n = NodeComp(1, cp, player)
print(n.best)'''

while True:
    print(f"Computer: {cp[0]} {cp[1]}")
    print(f"You:      {player[0]} {player[1]}\n")

    process_move(defense_input())
    if check_win(): break
    computer_move()
    if check_win(): break

    os.system(command)
