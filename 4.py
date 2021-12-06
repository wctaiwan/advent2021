numbers = []
boards = []

with open('input4.txt') as f:
    numbers = [int(x) for x in f.readline().strip().split(',')]
    f.readline()

    line = f.readline()
    while line != '':
        board = [[int(x) for x in line.strip().split()]]
        for i in range(4):
            line = f.readline()
            board.append([int(x) for x in line.strip().split()])
        boards.append(board)
        f.readline()
        line = f.readline()

reversed_numbers = [x for x in reversed(numbers)]

last_winning_number = None
last_winning_board = None
for number in reversed_numbers:
    for board in boards:
        for i in range(5):
            for j in range(5):
                if board[i][j] == number:
                    board[i][j] = -number-1
        has_bingo = False
        for row in range(5):
            if all([x >= 0 for x in board[row]]):
                has_bingo = True
        for col in range(5):
            if all([x >= 0 for x in [board[i][col] for i in range(5)]]):
                has_bingo = True
        if not has_bingo:
            last_winning_number = number
            last_winning_board = board
            break
    if last_winning_number is not None:
        break

remaining_sum = 0
for i in range(5):
    for j in range(5):
        if last_winning_board[i][j] < 0:
            remaining_sum += -1 * (last_winning_board[i][j] + 1)
remaining_sum -= last_winning_number # restore state after calling the last winning number
print(remaining_sum * last_winning_number)