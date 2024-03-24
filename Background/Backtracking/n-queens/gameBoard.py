class gameBoard:
    def __init__(self, N, board=None):
        if board == None:
            self.board = [[0 for _ in range(N)] for _ in range(N)]
        else:
            self.board = board
        self.N = N

    def _is_safe_row(self, row):
        is_safe = True
        # Check row
        for j in range(self.N):
            if self.board[row][j] != 0:
                is_safe = False
        return is_safe

    def _is_safe_column(self, column):
        is_safe = True

        # Check column
        # For efficiency this should be in range(column), but as test cases try weird grids this has to stay self.N for now
        for i in range(self.N):
            if self.board[i][column] != 0:
                is_safe = False
        return is_safe

    def _is_safe_diagonal(self, row, column):
        is_safe = True

        # Check upper left diagonal
        i = row
        j = column
        while i >= 0 and j >= 0:
            if self.board[i][j] != 0:
                is_safe = False
            i -= 1
            j -= 1

        # Check lower left diagonal
        i = row
        j = column
        while i < self.N and j >= 0:
            if self.board[i][j] != 0:
                is_safe = False
            i += 1
            j -= 1

        return is_safe

    def is_safe_entry(self, row, column):
        return (
            self._is_safe_row(row)
            and self._is_safe_column(column)
            and self._is_safe_diagonal(row, column)
        )

    def add_queen(self, row, column):
        self.board[row][column] = 1
        return self.board

    def remove_queen(self, row, column):
        self.board[row][column] = 0
        return self.board

    def printSolution(self):
        for i in range(self.N):
            for j in range(self.N):
                if self.board[i][j] == 1:
                    print("Q", end=" ")
                else:
                    print(".", end=" ")
            print()

    def solve_nq(self, column):
        # Base case 1: If N queens have been placed, solution has been found
        if column >= self.N:
            return True

        # Try every row in current column
        for i in range(self.N):
            # If queen is safe in current row, place it
            if self.is_safe_entry(i, column):
                self.board[i][column] = 1

                # Recursively see if queen in current position leads to solution
                if self.solve_nq(column + 1):
                    # Return True - solution has been found
                    return True

                # If queen in current position doesn't lead to solution, backtrack and try other rows
                self.board[i][column] = 0

        return False


if __name__ == "__main__":
    board = [
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
    ]

    N = 8
    gameBoard = gameBoard(N, board)
    if gameBoard.solve_nq(0):
        gameBoard.printSolution()
    else:
        print("Solution does not exist")
