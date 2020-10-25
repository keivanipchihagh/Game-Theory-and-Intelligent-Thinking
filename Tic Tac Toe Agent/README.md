# Tic Tac Toe Agent
Agent that solves Tic Tac Toe using minimax algorithm
## Structure
#### Check for avalible moves
The ```is_move_left``` function checks if any move is avalible for the agent to play.
#### Evaluating game state
Simple enough, the ```evaluate``` function checks if any players have won the game by checking the rows, columns and diagonal
#### Printing the board
Simple ```print_board``` function to print the board with a bit of formatting
#### Minimax algorithm
The brain of the agent, the ```minimax``` function, evaluates the board and only if game is running, checks all possible scenarios that might happen and returns the move (Watch this [video](https://www.youtube.com/watch?v=trKjYdBASyQ) to find out how the algorithm works)
```python
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
```
#### Getting the best move
The ```get_best_move``` function uses the minimax algorithm to calculate a score for each cell and choose a cell with the optimum score
```python
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
```
