class smallSudoku:
    # initialise the board. note: N currently set to three but when expanding to larger boards change to len(self.board)
    def __init__(self, board):
        self.board = board
        self.N = 3

    # Checks if rows and colums don't already contain the number tried.
    def is_safe(self, row, column, number):
        illegal_entries = []

        # add all the existing row numbers
        for i in range(self.N):
            illegal_entries.append(self.board[row][i])

        # add all the existing column numbers
        for i in range(self.N):
            illegal_entries.append(self.board[i][column])

        # add edge case for the cell not being empty
        return number not in illegal_entries and self.board[row][column] == 0

    # prints all the elements in the board
    def print_board(self):
        for i in range(self.N):
            print(" ".join(str(self.board[i][j]) for j in range(self.N)))

    # finds the first empty cell in the board
    def find_empty_cell(self):
        for i in range(self.N):
            for j in range(self.N):
                if self.board[i][j] == 0:
                    return (i, j)
        return None

    # backtracking based small sudoku solver
    def solve_board(self):
        # find the first empty cell
        empty_cell = self.find_empty_cell()

        # if there are no empty cells that means the sudoku board is solved and can stop
        if not empty_cell:
            return True

        # if there is an empty cell, find the indices of the row and column for it
        else:
            row, column = self.find_empty_cell()

        # try all the legal numbers in that empty cell and check if they are valid (from 1 to N)
        for i in range(1, self.N + 1):
            # if number is valid in that cell, check if it leads to solution
            if self.is_safe(row, column, i):
                # set number i in the cell of row i column j
                self.board[row][column] = i
                # if doing so leads to a solution return true
                if self.solve_board():
                    return True
                # if not (backtrack) remove that number from that cell and try other options
                self.board[row][column] = 0
        # if for loop ends without returning true - there is no solution
        return False

    # get the solution in it's array form
    def get_full_board(self):
        self.solve_board()
        return self.board


if __name__ == "__main__":
    board = [
        [1, 3, 2],
        [3, 2, 1],
        [2, 1, 3],
    ]

    sudoku_board = smallSudoku(board)
    # print(sudoku_board.is_safe(0, 1, 3))
    # sudoku_board.print_board()
