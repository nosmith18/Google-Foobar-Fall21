def check(board, x, y, move):
    if 0 <= x <= 7 and 0 <= y <= 7 and board[x][y] == -1:
        board[x][y] = move
    return board

def add_moves(board, x, y, move):
    board = check(board, x+1, y+2, move)
    board = check(board, x+1, y-2, move)
    board = check(board, x-1, y+2, move)
    board = check(board, x-1, y-2, move)
    board = check(board, x+2, y+1, move)
    board = check(board, x+2, y-1, move)
    board = check(board, x-2, y+1, move)
    board = check(board, x-2, y-1, move)
    return board

def solution(start, end):

    start_row = int(start/8)
    start_col = int(start % 8)
    end_row = int(end/8)
    end_col = int(end % 8)
    # print(start_row, start_col, end_row, end_col)

    board = [[-1 for j in range(8)] for i in range(8)]
    board[start_row][start_col] = 0
    move = 0

    while (board[end_row][end_col] == -1):
        for i in range(8):
            for j in range(8):
                if board[i][j] == move:
                    board = add_moves(board, i, j, move+1)
        move += 1
    return board[end_row][end_col]
