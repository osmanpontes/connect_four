# reading from file
# with open("input.py", 'r') as f:
#     f.readline()
import random

HEIGHT = 7
WIDTH = 8


# functions
def valid_moves(state):
    return [i for i in xrange(0, len(state[0])) if state[0][i] == 0]


def move(state, move, player):
    new_state = [list(state[i]) for i in xrange(0, len(state))]
    for i in xrange(HEIGHT - 1, -1, -1):
        if new_state[i][move] == 0:
            new_state[i][move] = player
            break

    return new_state


def winner(state, last_move, player):
    if last_move == None:
        return 0
    last_move_line = None
    for i in xrange(0, HEIGHT):
        if state[i][last_move] != 0:
            last_move_line = i
            break

    # horizontal
    count = 0
    for j in xrange(last_move + 1, WIDTH):
        if state[last_move_line][j] == player:
            count += 1
        else:
            break

    for j in xrange(last_move - 1, -1, -1):
        if state[last_move_line][j] == player:
            count += 1
        else:
            break
    if count > 3:
        return player

    # vertical
    count = 0
    for i in xrange(last_move_line + 1, HEIGHT):
        if state[i][last_move] == player:
            count += 1
        else:
            break

    for i in xrange(last_move_line - 1, -1, -1):
        if state[i][last_move] == player:
            count += 1
        else:
            break
    if count > 3:
        return player

    # diagonal \
    count = 0
    line = last_move_line + 1
    col = last_move + 1
    while line < HEIGHT and col < WIDTH:
        if state[line][col] == player:
            count += 1
            line += 1
            col += 1
        else:
            break

    line = last_move_line - 1
    col = last_move - 1
    while line >= 0 and col >= 0:
        if state[line][col] == player:
            count += 1
            line -= 1
            col -= 1
        else:
            break

    if count > 3:
        return player

    # diagonal /
    count = 0
    line = last_move_line - 1
    col = last_move + 1
    while line >= 0 and col < WIDTH:
        if state[line][col] == player:
            count += 1
            line -= 1
            col += 1
        else:
            break

    line = last_move_line + 1
    col = last_move - 1
    while line < HEIGHT and col >= 0:
        if state[line][col] == player:
            count += 1
            line += 1
            col -= 1
        else:
            break

    if count > 3:
        return player

    return 0


# min-max
class Node(object):
    def __init__(self, value, state, player, last_move):
        self.value = value
        self.children = {}
        self.state = state
        self.player = player  # int
        self.last_move = last_move

    def populate_children(self):
        vm = valid_moves(self.state)
        for m in vm:
            new_state = move(self.state, m, self.player)
            child = Node(None, new_state, self.other_player(), m)
            self.children[m] = child

    def is_leaf(self):
        if valid_moves(self.state) == []:
            return True

        return winner(self.state, self.last_move, self.other_player()) != 0

    def other_player(self):
        return self.player % 2 + 1


def heuristic(node):
    return random.random()


def min_max(node, depth, maximizing_player):
    if depth == 0 or node.is_leaf():
        node.value = heuristic(node)
        return node.value

    node.populate_children()

    if maximizing_player:
        best_value = -float('inf')
        for child in node.children.values():
            v = min_max(child, depth - 1, False)
            best_value = max([best_value, v])
        node.value = best_value
        return node.value
    else:
        best_value = float('inf')
        for child in node.children.values():
            v = min_max(child, depth - 1, True)
            best_value = min([best_value, v])
        node.value = best_value
        return node.value


# # reading input
state = []

for i in xrange(0, HEIGHT):
    line = raw_input()
    state.append([int(i) for i in line.split(' ')])

player = int(raw_input())

# output

root = Node(None, state, player, None)

min_max(root, 5, True)

chosen_move = None
max_heuristic = -float('inf')
for key, child in root.children.iteritems():
    if child.value > max_heuristic:
        max_heuristic = child.value
        chosen_move = key

print chosen_move
# print [round(child.value, 2) for child in root.children.values()]
