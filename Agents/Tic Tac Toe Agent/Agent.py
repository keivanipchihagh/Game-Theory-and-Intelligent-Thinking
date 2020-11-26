# Imports
import math

# Board
board = [
    ['X', 'O', 'X'],
    ['O', 'O', 'X'],
    [' ', ' ', ' '],
]

PLAYER = 'X'
OPPONENT = 'O'
EMPTY = ' '
PLAYER_SCORE = 10
OPPONENT_SCORE = -10

# Checks if moves are avalible
def is_move_left(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == EMPTY:
                return True
    return False    

# Checks game status. Returns 'X' if player wins & 'O' if the opponent wins
def evaluate(board):
    # Check rows
    for i in range(len(board)):
        if board[i].count(PLAYER) == 3:
            return PLAYER_SCORE
        elif board[i].count(OPPONENT) == 3:
            return OPPONENT_SCORE

    # Check columns
    for i in range(len(board)):
        tmp = []
        for j in range(len(board[i])):
            tmp.append(board[j][i])

        if tmp.count(PLAYER) == 3:
            return PLAYER_SCORE
        elif board[i].count(OPPONENT) == 3:
            return OPPONENT_SCORE
    
    # Check diagonals
    tmp1 = []
    tmp2 = []
    for i in range(len(board)):
        tmp1.append(board[i][i])
        tmp2.append(board[i][len(board) - i - 1])
    
    if tmp1.count(PLAYER) == 3 or tmp2.count(PLAYER) == 3:
        return PLAYER_SCORE
    elif tmp1.count(OPPONENT) == 3 or tmp2.count(OPPONENT) == 3:
        return OPPONENT_SCORE

    return None

def minimax(board, depth, isMax):
    evaluation = evaluate(board = board)

    if evaluation == PLAYER:
        return PLAYER_SCORE
    elif evaluation == OPPONENT:
        return OPPONENT_SCORE
    elif evaluation == None:
        return 0

    if isMax:
        best = -1000

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == EMPTY:
                    board[i][j] = PLAYER

                    best = minimax(board = board, depth = depth + 1, isMax = not isMax)
                    board[i][j] = EMPTY
        return best
    else:
        best = +1000

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == EMPTY:
                    board[i][j] = OPPONENT

                    best = minimax(board = board, depth = depth + 1, isMax = not isMax)
                    board[i][j] = EMPTY
        return best

# Finds the best move
def get_best_move(board):

    best = -1000
    move = (-1, -1)

    for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == EMPTY:
                    board[i][j] = PLAYER

                    value = minimax(board = board, depth = 0, isMax = False)
                    board[i][j] = EMPTY

                    if value > best:
                        best = value
                        move = (i, j)

    print('Best move value:', best)
    return move

# Print
def print_board(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            print(board[i][j], end = '')

            if j < len(board[i]) - 1:
                print(' | ', end = '')

        if i < len(board) - 1:
            print('\n', '─' * 2, ' ', '─' * 3, ' ', '─' * 2, sep = '')

# Main
move = get_best_move(board = board)
print('Optimal move:', move)