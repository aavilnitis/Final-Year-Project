from priority_queue import PriorityQueue
import copy

class sudokuSolver:
    """
    A class used to solve Sudoku puzzles.

    ...

    Attributes
    ----------
    board : list
        a 2D list representing the Sudoku board
    N : int
        the size of the Sudoku board (default is 9)
    calls : int
        a counter for the number of recursive calls (default is 0)
    priorityQueue : PriorityQueue
        a priority queue used to order cells by candidates

    Methods
    -------
    get_illegal_entries(row, column, board)
        Returns a set of numbers that cannot be placed in the given cell.
    get_number_candidates(row, column, board)
        Returns the number of possible candidates for a given cell.
    print_board()
        Prints the Sudoku board row by row.
    find_empty_cell(board)
        Finds the first empty cell in the board and returns its indices.
    order_cells_by_candidates_with_priority_queue()
        Orders the cells by the number of candidates using a priority queue.
    solve_board()
        Solves the Sudoku board using backtracking, returns True if solving is possible.
    get_full_board()
        Returns the solved Sudoku board as a 2D list.
    """

    def __init__(self, board, calls=0):
        """
        Parameters
        ----------
        board : list
            a 2D list representing the Sudoku board
        calls : int, optional
            a counter for the number of recursive calls (default is 0)
        """
        self.board = board
        self.N = 9
        self.calls = calls
        self.priorityQueue = None

    def get_illegal_entries(self, row, column, board):
        """
        Returns a set of numbers that cannot be placed in the given cell.

        Parameters
        ----------
        row : int
            the row index of the cell
        column : int
            the column index of the cell
        board : list
            the Sudoku board

        Returns
        -------
        set
            a set of numbers that cannot be placed in the cell
        """
        illegal_entries = set()

        startRow = row // 3 * 3
        startCol = column // 3 * 3

        # subgrid
        for i in range(startRow, startRow + 3):
            for j in range(startCol, startCol + 3):
                illegal_entries.add(board[i][j])

        # add all the existing row numbers
        for i in range(self.N):
            illegal_entries.add(board[row][i])

        # add all the existing column numbers
        for i in range(self.N):
            illegal_entries.add(board[i][column])

        # add edge case for the cell not being empty
        return illegal_entries

    def get_number_candidates(self, row, column, board):
        """
        Returns the number of possible candidates for a given cell.

        Parameters
        ----------
        row : int
            the row index of the cell
        column : int
            the column index of the cell
        board : list
            the Sudoku board

        Returns
        -------
        int
            the number of possible candidates for the cell
        """
        illegal_entries = self.get_illegal_entries(row, column, board)
        return self.N - len(illegal_entries)

    def print_board(self):
        """
        Prints the Sudoku board.
        """
        for i in range(self.N):
            print(" ".join(str(self.board[i][j]) for j in range(self.N)))

    def find_empty_cell(self, board):
        """
        Finds the first empty cell in the board.

        Parameters
        ----------
        board : list
            the Sudoku board

        Returns
        -------
        tuple
            the row and column indices of the first empty cell, or None if there are no empty cells
        """
        for i in range(self.N):
            for j in range(self.N):
                if board[i][j] == 0:
                    return (i, j)
        return None

    def order_cells_by_candidates_with_priority_queue(self):
        """
        Orders the cells by the number of candidates using a priority queue.
        """
        temp_board = copy.deepcopy(self.board)
        priority_queue = PriorityQueue()

        while True:
            empty_cell = self.find_empty_cell(temp_board)

            if not empty_cell:
                break

            row, column = empty_cell
            number_candidates = self.get_number_candidates(row, column, temp_board)

            # Insert directly into the priority queue, maintaining ordering
            priority_queue.insert(
                {"cell": empty_cell, "num_candidates": number_candidates},
                number_candidates,
            )
            temp_board[row][column] = 1

        self.priorityQueue = priority_queue

    def solve_board(self):
        """
        Solves the Sudoku board using backtracking.

        Returns
        -------
        bool
            True if the board is solved, False otherwise
        """
        # find the first empty cell
        self.order_cells_by_candidates_with_priority_queue()
        node = self.priorityQueue.pop_min()

        # if there are no empty cells that means the sudoku board is solved and can stop
        if not node:
            return True

        # if there is an empty cell, find the indices of the row and column for it
        else:
            empty_cell = node.data["cell"]
            row, column = empty_cell

        # try all the legal numbers in that empty cell and check if they are valid (from 1 to N)
        for i in range(1, self.N + 1):
            # if number is valid in that cell, check if it leads to a solution
            if i not in self.get_illegal_entries(row, column, self.board):
                # set number i in the cell of row i column j
                self.board[row][column] = i
                # if doing so leads to a solution return true
                self.calls += 1  # Increment the counter
                if self.solve_board():
                    return True
                # if not (backtrack) remove that number from that cell and try other options
                self.board[row][column] = 0

        # if for loop ends without returning true - there is no solution
        return False

    # get the solution in it's array form
    def get_full_board(self):
        """
        Returns the solved Sudoku board.

        Returns
        -------
        list
            the solved Sudoku board
        """
        self.solve_board()
        return self.board
