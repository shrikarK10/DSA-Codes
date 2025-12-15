


def isSafe(board, row, col, N):
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solveNQUtil(board, col, N, solutions):
    if col >= N:
        solutions.append([row[:] for row in board])
        return

    for i in range(N):
        if isSafe(board, i, col, N):
            board[i][col] = 1
            solveNQUtil(board, col + 1, N, solutions)
            board[i][col] = 0

def solveNQ(N):
    board = [[0 for _ in range(N)] for _ in range(N)]
    solutions = []
    solveNQUtil(board, 0, N, solutions)
    print(f"Total solutions for {N}-Queens: {len(solutions)}\n")


# Example usage:
N = 5
solveNQ(N)

"""
Approach:
- I used a backtracking approach to solve the N-Queens problem.
- I used a 2D array board to represent the chessboard, where 1 represents a queen and 0 represents an empty cell.
- I used a helper function solveNQUtil to recursively try placing queens on the board.
- For each cell in the board, I checked if it was safe to place a queen using the isSafe function.
- If it was safe, I placed a queen on the cell and recursively called solveNQUtil to try placing queens on the remaining cells.
- If a solution was found, I added it to the solutions list.
- Finally, I returned the solutions list.
"""