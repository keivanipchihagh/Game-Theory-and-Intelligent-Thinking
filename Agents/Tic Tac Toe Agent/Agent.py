# Imports
import math

# Board
board = [
    ['X', 'O', 'X'],
    ['O', 'O', ' '],
    [' ', ' ', ' '],
]

AI = 'X'
HUMAN = 'O'
EMPTY = ' '
AI_SCORE = 10
HUMAN_SCORE = -10

# Checks game status. Returns 'X' if AI wins & 'O' if the HUMAN wins
def evaluate(board):
    # Check rows
    for i in range(len(board)):
        if board[i].count(AI) == 3:
            return AI_SCORE
        elif board[i].count(HUMAN) == 3:
            return HUMAN_SCORE

    # Check columns
    for i in range(len(board)):
        tmp = []
        for j in range(len(board[i])):
            tmp.append(board[j][i])

        if tmp.count(AI) == 3:
            return AI_SCORE
        elif board[i].count(HUMAN) == 3:
            return HUMAN_SCORE
    
    # Check diagonals
    tmp1 = []
    tmp2 = []
    for i in range(len(board)):
        tmp1.append(board[i][i])
        tmp2.append(board[i][len(board) - i - 1])
    
    if tmp1.count(AI) == 3 or tmp2.count(AI) == 3:
        return AI_SCORE
    elif tmp1.count(HUMAN) == 3 or tmp2.count(HUMAN) == 3:
        return HUMAN_SCORE

    return None


def minimax(board, depth, isMax):
    evaluation = evaluate(board = board)

    if evaluation == AI:
        return AI_SCORE
    elif evaluation == HUMAN:
        return HUMAN_SCORE
    elif evaluation == None:
        return 0

    if isMax:
        best = -1000

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == EMPTY:
                    board[i][j] = AI

                    best = minimax(board = board, depth = depth + 1, isMax = not isMax)
                    board[i][j] = EMPTY
        return best
    else:
        best = +1000

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == EMPTY:
                    board[i][j] = HUMAN

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
                    board[i][j] = AI

                    value = minimax(board = board, depth = 0, isMax = False)
                    board[i][j] = EMPTY

                    if value > best:
                        best = value
                        move = (i, j)

    print('Best move value:', best)
    return move

# Main
move = get_best_move(board = board)
print('Optimal move:', move)