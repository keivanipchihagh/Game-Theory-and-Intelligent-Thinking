# Sudoku Solver
Simple Backtracking algorithm that solves the Sudoku for you 😎
## Structures
#### Print function
The ``` print_board ``` function prints a good looking form the sukodu board
#### Finding empty nodes
The ``` get_empty ``` function returns a tuple of the first empty node it finds
#### Validating an Insert
The ``` valid ``` function has gets three parameters:
- board Which is the main sukodu board
- number Which is the number we want to insert
- position A tuple containg the row & column of the insertion we ought to do

Basically we check if our insertion is valid by checking the row, column and the box

```python
# Validation
def valid(baord, number, position):
    # Check row
    for i in range(len(board[0])):
        if board[position[0]][i] == number and position[1] != i:
            return False
    
    # Check column
    for i in range(len(board)):
        if board[i][position[1]] == number and position[0] != i:
            return False

    # Check box
    box_x = position[1] // 3
    box_y = position[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == number and (i, j) != position:
                return False
    
    return True

```
#### Solving the problem
The ``` solve ``` function is pretty straight forward. First, It gets an empty node and tries validating and then inserting numbers from 1 to 9. It repeats the process for the other empty nodes and when no empty nodes are left, the solved board gets printed out.
Note that because we are using a recursive ```solve``` function, if something goes wrong wile inserting into a node, the algorithm **backtracks** and increments the previous node's value
```python
# Solves the problem (Recursive)
def solve(board):
    empty = get_empty(board = board)
    if not empty:
        return True
    else:
        row, column = empty

    for i in range(1, 10):
        if valid(board, i, (row, column)):
            board[row][column] = i

            if solve(board = board):
                return True
            board[row][column] = 0
    
    return False
    ```
