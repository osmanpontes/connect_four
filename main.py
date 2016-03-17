# reading from file
# with open("input.py", 'r') as f:
#     f.readline()
import random
import numpy

# Constants

HEIGHT = 7
WIDTH = 8

# Globals
hidden_to_out = numpy.matrix([[0.48236419],
                              [-0.03725872],
                              [-0.39602489],
                              [0.07409193],
                              [0.81089938],
                              [-1.93674674],
                              [0.6725581],
                              [-1.98317251],
                              [-0.41780737]])

input_to_hidden = numpy.matrix([[-0.28561078, -0.04274196, -0.55215352, -0.57908313, 0.17887027,
                                 0.50991852, 0.49300289, 1.25339788],
                                [-0.17579058, -1.21923801, 0.30758158, 0.56300691, 0.06916303,
                                 -0.70616871, 1.78544708, 0.39365811],
                                [-1.27914393, -0.18804559, -0.37360248, 1.14607991, 1.41174931,
                                 1.32979107, 0.25211527, 1.12561696],
                                [1.68530466, -0.21364127, 0.49435088, 0.49245091, -0.2824089,
                                 -0.56622527, -0.69273209, 1.70313743],
                                [0.58093986, -0.59350059, -1.420365, -1.10883449, -1.01628698,
                                 -2.29834861, 1.16089799, 0.03975122],
                                [0.46206786, -2.1148228, 0.72853972, -1.74022471, -0.1430083,
                                 -1.01710895, -1.24176706, -0.88925021],
                                [0.13661142, 1.10539174, 1.65316603, 0.49937462, -0.57246585,
                                 -1.19553593, 1.57487325, -1.05824656],
                                [-1.00295313, -0.72531021, 2.0054573, 0.38280913, 0.92661791,
                                 1.88605594, -0.79134631, -0.46786884],
                                [-0.28647267, -2.71849207, -0.9473718, 0.63081553, -0.27689898,
                                 0.76024189, 0.51265013, -1.50259552],
                                [0.51060359, -0.38708674, -1.28053861, 0.38298749, -0.3702601,
                                 -1.79932954, 2.25663825, -0.05984567],
                                [-0.10033861, 2.08753565, -0.88043766, -0.60093859, -0.82376587,
                                 -0.31083855, 0.04449479, 1.04981223],
                                [0.38176508, 1.37111987, -0.46815951, 1.05731885, -0.64563464,
                                 0.89938184, 0.08195393, 1.20960734],
                                [-2.46228771, 1.01657958, -1.17486337, -1.28450157, -0.05135417,
                                 0.70000832, 0.91333242, -0.21141291],
                                [-1.0350044, -0.12310044, -2.69056081, -0.30539907, -0.70560214,
                                 -1.02576423, 0.1669984, -0.73939103],
                                [0.25502175, 0.73252537, -0.1268164, -0.08695612, -0.66056867,
                                 0.80929858, -0.09524456, -0.07775764],
                                [0.48012547, -0.59117545, -0.01948508, 1.17637464, -0.21772096,
                                 0.25892363, 0.21959886, -0.34530491],
                                [0.08692939, -1.13924204, -0.06347337, -2.14243015, -0.95201403,
                                 0.79855741, 0.31962493, -0.39302961],
                                [-0.15245557, -0.93817411, -0.01979636, -0.3124263, 1.5699051,
                                 0.57836831, 0.40312424, -1.2178134],
                                [-0.36734202, -0.49294229, -1.65853618, 0.87547921, -0.15175368,
                                 2.45186715, -3.27932335, -0.23631797],
                                [-1.35025608, -1.36525855, 0.63049747, -0.19521052, -2.03316228,
                                 -1.3478502, -0.97447763, -0.73014779],
                                [-0.18056355, 0.05457017, -1.6202607, 0.15224295, 0.4751015,
                                 1.09913269, 0.60119867, -0.46628299],
                                [1.15998215, 0.70871, -1.08762912, -0.85478803, 1.19642502,
                                 -1.35210393, -0.22302522, -0.3488306],
                                [-1.06642367, -1.51973207, 0.67037775, -1.1872388, 0.93950949,
                                 0.60759659, -1.09246242, -0.86954031],
                                [-0.01742993, 0.48117339, -1.49654223, -0.61969311, -1.90454686,
                                 0.96406746, -0.06870136, -0.76257797],
                                [-0.264165, -1.43915835, -1.48223338, 1.91628239, -0.90072867,
                                 1.358849, -0.74885972, -0.76788371],
                                [-1.24422828, -1.07463517, -0.85586027, 0.18475006, -2.17381784,
                                 0.49436076, -0.03754727, 1.00392639],
                                [0.87162336, 1.14597165, -0.40802024, 0.50332737, -1.00389549,
                                 -0.54242376, -0.84970448, -1.50785052],
                                [-0.91366017, 0.87019375, 0.03894268, -0.18599569, -0.76653256,
                                 -0.9975156, 0.09202994, -0.13887661],
                                [-1.06177997, -1.20638375, 1.15313249, 0.55121615, 0.95997748,
                                 -0.94471489, 0.87413502, 1.03286088],
                                [-0.81507774, 0.51616005, -0.0658354, 0.30501946, 1.05670377,
                                 -2.17389412, 0.04357225, 0.75489567],
                                [-0.44874925, 1.00724252, 0.85413372, 0.61423548, 0.55811189,
                                 -1.60226178, 0.91790653, -0.35120767],
                                [1.41072529, -2.1070439, 2.01706879, 1.17143384, 1.68775711,
                                 -1.39396515, 1.58556136, 0.65479932],
                                [-0.55638453, -1.36441373, 0.51736951, -0.09211238, 0.5867477,
                                 0.30961505, -0.84023561, 0.42199292],
                                [0.26558735, 0.64253231, -0.86053482, -0.92217971, 0.15421059,
                                 0.19475972, -1.18586587, -0.35949452],
                                [1.28557519, 0.21569603, 0.48148874, -1.78848689, 0.06375189,
                                 -1.77321586, 0.24336627, 0.15772576],
                                [-0.65903431, 1.68585442, -0.63361823, -0.33423128, -0.03912994,
                                 -0.00904895, 0.18294645, -2.51887702],
                                [0.76782264, -0.06428748, 0.38113492, 0.17315488, -0.2680409,
                                 1.48125066, -1.3956268, 0.01107521],
                                [-0.51822338, 1.15051744, -0.09134207, 2.14485764, -1.6155781,
                                 -1.65015944, 0.52203747, -1.36057785],
                                [0.89895241, -0.39360199, 0.52250038, 0.72423746, 0.81565681,
                                 1.18675037, 0.32767282, 1.50829702],
                                [-1.04111665, -0.68085097, -0.061745, -0.27567876, 0.23012179,
                                 -1.14940241, -2.0663762, -1.02209429],
                                [0.65595512, -1.702894, 1.12317003, 1.90817109, 0.17132175,
                                 -1.57960557, -0.27492809, 1.30737389],
                                [0.15210815, 1.94317752, 0.65392861, 0.15434203, 0.84855989,
                                 0.69388203, 0.79495986, 0.60257883],
                                [-1.17149771, 1.07395774, -0.94218155, -0.36747567, 0.70695966,
                                 0.09732504, -1.92605353, 0.40065766],
                                [0.26765879, -0.17192407, 1.1559116, 0.56624885, 1.26317015,
                                 -1.08079601, -0.37989242, -0.2088028],
                                [0.09632606, 0.80606111, 0.71783698, 0.23733043, -0.11251347,
                                 1.36136606, 0.28149023, -0.10806947],
                                [1.09773694, 0.09046989, -1.65658895, -0.2660777, -0.89484015,
                                 -0.36554, 1.71772761, 2.52165715],
                                [2.11993551, -0.96175003, -1.77439753, 1.52438621, 0.62748715,
                                 -1.70627767, -0.06290678, 1.00154972],
                                [0.20370023, 0.66601434, -0.88723448, 0.12867531, -0.63235013,
                                 0.67212832, -1.23302648, 0.39148027],
                                [-0.17515326, 0.507151, -0.34591477, 0.54008024, -0.69199899,
                                 -0.90587555, -1.3077311, -0.40734708],
                                [-2.12511581, -0.41744711, 0.30730167, 0.19323893, -0.73664879,
                                 -0.74840353, -0.96477484, -1.21530061],
                                [-0.74751859, 0.72077974, 1.23609251, -0.68528015, 0.18811881,
                                 -0.37826877, -0.43241642, -0.12492603],
                                [-1.04296178, -0.63971523, 0.22654207, 0.40798657, -0.37288317,
                                 0.30414428, -1.78415483, 1.58726772],
                                [-1.14521298, 0.15388665, 1.4768428, 1.77598565, -0.14854827,
                                 -0.56547949, 1.42506456, 2.28067682],
                                [-0.41038232, 0.36279914, -0.50298582, 0.10840483, -0.49408611,
                                 -1.23506271, -0.85688671, -0.49461949],
                                [0.29232473, -0.14830731, 0.38883188, 1.17212772, -0.12736288,
                                 0.73594134, 0.21695779, -0.80818644],
                                [1.36298536, -0.48470678, -1.47940363, 0.11058177, -0.0074548,
                                 0.16880031, 0.47169811, 1.81987787],
                                [-1.20151198, -0.70864324, 0.63957972, 0.02686144, -1.69414762,
                                 -0.10798305, 0.19419012, 0.81649809]])


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


def next_move(node):
    chosen_move = None
    max_heuristic = -float('inf')
    for key, child in node.children.iteritems():
        if child.value > max_heuristic:
            max_heuristic = child.value
            chosen_move = key
    return chosen_move


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


def minimax(node, depth, maximizing_player, heuristic):
    if depth == 0 or node.is_leaf():
        node.value = heuristic(node)
        return node.value

    node.populate_children()

    if maximizing_player:
        best_value = -float('inf')
        for child in node.children.values():
            best_value = max([best_value, minimax(child, depth - 1, False)])
    else:
        best_value = float('inf')
        for child in node.children.values():
            best_value = min([best_value, minimax(child, depth - 1, True)])

    node.value = best_value
    return node.value


def alphabeta(node, depth, alpha, beta, maximizing_player, heuristic):
    if depth == 0 or node.is_leaf():
        node.value = heuristic(node)
        return node.value

    node.populate_children()

    if maximizing_player:
        v = -float('inf')
        for child in node.children.values():
            v = max([v, alphabeta(child, depth - 1, alpha, beta, False, heuristic)])
            alpha = max([alpha, v])
            if beta <= alpha:
                break
    else:
        v = float('inf')
        for child in node.children.values():
            v = min([v, alphabeta(child, depth - 1, alpha, beta, True, heuristic)])
            beta = min([beta, v])
            if beta <= alpha:
                break
    node.value = v
    return node.value


def heuristic_random(node):
    return random.random()


def heuristic_nn(node):
    nn_input = numpy.array([i for lst in node.state for i in lst] + [1])
    # print nn_input
    h = numpy.concatenate((numpy.exp(nn_input * input_to_hidden), numpy.matrix([[1]])), axis=1) * hidden_to_out
    # print h
    return float(h) * (1 if node.player == 1 else -1)


def read_input():
    state = []
    for i in xrange(0, HEIGHT):
        line = raw_input()
        state.append([int(i) for i in line.split(' ')])
    player = int(raw_input())
    return [state, player]


# reading input
[state, player] = read_input()
# output

root = Node(None, state, player, None)

# minimax(root, 2, True, heuristic_random)
alphabeta(root, 6, -float('inf'), float('inf'), True, heuristic_nn)

print next_move(root)

# print [round(child.value, 2) for child in root.children.values()]
