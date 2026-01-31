N = 8
board = [-1] * N
row = 0

while row >= 0:
    board[row] += 1

    while board[row] < N:
        ok = True
        for r in range(row):
            if board[r] == board[row] or abs(board[r] - board[row]) == row - r:
                ok = False
                break
        if ok:
            break
        board[row] += 1

    if board[row] < N:
        if row == N - 1:
            for r in range(N):
                line = ""
                for c in range(N):
                    line += "Q " if board[r] == c else ". "
                print(line)
            break
        else:
            row += 1
            board[row] = -1
    else:
        board[row] = -1
        row -= 1
