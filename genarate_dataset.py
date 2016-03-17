import copy

NUM_LINES = 6
NUM_COLUMNS = 7

with open("connect-4.data", "r") as f:
    with open("dataset.data", "w") as g:
        lines = f.readlines()
        for line in lines:
            line = line.replace('loss', '-1')
            line = line.replace('draw', '0')
            line = line.replace('win', '1')

            line = line.replace('x', '1')
            line = line.replace('o', '2')
            line = line.replace('b', '0')
            line = line.split(",")
            board = []
            for i in xrange(0, NUM_COLUMNS * 6, 6):
                col = line[i:i + 6]
                col.append('0')
                board.append(col)
            board1 = copy.deepcopy(board)
            board1.append(['0'] * (NUM_LINES + 1))
            board2 = copy.deepcopy(board)
            board2.insert(0, ['0'] * (NUM_LINES + 1))
            state1 = []
            state2 = []
            for i in xrange(0, NUM_LINES + 1):
                for j in xrange(0, NUM_COLUMNS + 1):
                    state1.append(board1[j][NUM_LINES - i])
                    state2.append(board2[j][NUM_LINES - i])
            result = line[-1].strip()
            state1.append(result)
            state2.append(result)
            g.write(",".join(state1) + "\n")
            g.write(",".join(state2) + "\n")
