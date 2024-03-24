class nonogramSolver:
    def __init__(self, board, row_args, col_args):
        self.board = board
        self.row_args = row_args
        self.col_args = col_args
        self.simple_solved = False
        self.illegal = [[0 for _ in range(len(self.board[0]))] for _ in range(len(self.board))]

    def calculate_overlap(self, hints, length):
        if not hints:
            return None

        max_hint = max(hints)
        total_hint_length = sum(hints) + len(hints) - 1

        if total_hint_length < length:
            max_start = length - total_hint_length
            min_end = max_hint
            overlap_start = max_start
            overlap_end = min_end

            if overlap_start < overlap_end:
                return overlap_start, overlap_end

        return None

    def find_incomplete_row(self):
        for index, row in enumerate(self.board):
            if sum(row) != sum(self.row_args[index]):
                return index
        return None
    
    # Check if it's valid to place a hint starting from the given column index
    def valid(self, row, col):
        current_row = sum(self.board[row])
        current_col = sum([self.board[i][col] for i in range(len(self.board))])
        hint_row = sum(self.row_args[row])
        hint_col = sum(self.col_args[col])
        return current_row < hint_row and current_col < hint_col and self.illegal[row][col] == 0


    # Check validity of length of hint
    def hint_valid(self, row, col, hint):
        for i in range(hint):
            if not self.valid(row, col + i):
                return False
        return True

    def print_board(self):
        for i in range(len(self.board)):
            print(" ".join(str(self.board[i][j]) for j in range(len(self.board[0]))))

    def update_illegal(self, row, column):
        self.illegal[row][column] = 1
        
    def place_hint(self, row, col, hint):
        for i in range(hint):
            self.board[row][col + i] = 1
            # Update illegal entries
            if col + i - 1 >= 0:
                self.illegal[row][col + i - 1] = 1
            self.illegal[row][col + i] = 1
            if col + i + 1 < len(self.board[row]):
                self.illegal[row][col + i + 1] = 1
        return True
    
    def remove_hint(self, row, col, hint):
        for i in range(hint):
            self.board[row][col + i] = 0
            # Update illegal entries
            if col + i - 1 >= 0:
                self.illegal[row][col + i - 1] = 0
            self.illegal[row][col + i] = 0
            if col + i + 1 < len(self.board[row]):
                self.illegal[row][col + i + 1] = 0
        return True

    def solve_board(self):
        # if not self.simple_solved:
        #     self.solve_board_simple()

        unfinished_row = self.find_incomplete_row()
        if unfinished_row is None:
            return True

        print("starting this on row: ", unfinished_row)
        for hint in self.row_args[unfinished_row]:
            for start_pos in range(len(self.board[unfinished_row]) - hint + 1):
                if(self.hint_valid(unfinished_row, start_pos, hint)):
                    self.place_hint(unfinished_row, start_pos, hint)
                    self.print_board()
                    print("______________________")
                    if self.solve_board():
                        return True
                    self.remove_hint(unfinished_row, start_pos, hint)
        return False

    def solve_board_simple(self):
        len_row = len(self.row_args)
        len_col = len(self.col_args)

        # FIRST CASE: LENGTH OF ROW/COLUMN == LENGTH OF HINT

        # For every row hint: if len(hint) == len(row), fill in the row
        for i in range(len_row):
            if sum(self.row_args[i]) == len(self.board[i]):
                self.board[i] = [1] * len(self.board[i])

        # For every column hint: if len(hint) == len(col), fill in the column
        for i in range(len_col):
            if sum(self.col_args[i]) == len(self.board):
                for j in range(len(self.board)):
                    self.board[j][i] = 1

        # SECOND CASE: LENGTH OF ROW/COLUMN == LENGTH OF HINTS + GAPS
        for i in range(len_row):
            row_gaps = len(self.row_args[i]) - 1
            if (sum(self.row_args[i]) + row_gaps) == len(self.board[i]):
                pos = 0
                for index, hint in enumerate(self.row_args[i]):
                    # Fill in the cells for the hint
                    for _ in range(hint):
                        self.board[i][pos] = 1
                        pos += 1

                    # Add a gap after the hint, except for the last hint
                    if index < len(self.row_args[i]) - 1:
                        self.board[i][pos] = 0
                        pos += 1

        for i in range(len_col):
            col_gaps = len(self.col_args[i]) - 1
            if (sum(self.col_args[i]) + col_gaps) == len(self.board):
                pos = 0
                for index, hint in enumerate(self.col_args[i]):
                    # Fill in the cells for the hint
                    for _ in range(hint):
                        self.board[pos][i] = 1
                        pos += 1

                    # Add a gap after the hint, except for the last hint
                    if index < len(self.col_args[i]) - 1:
                        self.board[pos][i] = 0
                        pos += 1

        # THIRD CASE (Overlapping): Sum clues + sum spaces + sum largest clue > length of row/column

        # Overlapping for rows
        for i in range(len_row):
            overlap = self.calculate_overlap(self.row_args[i], len(self.board[i]))
            if overlap:
                start, end = overlap
                for pos in range(start, end):
                    self.board[i][pos] = 1

        # Overlapping for columns
        for i in range(len_col):
            overlap = self.calculate_overlap(self.col_args[i], len(self.board))
            if overlap:
                start, end = overlap
                for pos in range(start, end):
                    self.board[pos][i] = 1

        # FOURTH CASE: Edge cell (single) with hint > 1

        for t in range(2):
            # Edge cell case for rows left right
            for i in range(len_row):
                if self.board[i][0] == 1 and self.row_args[i][0] > 1:
                    for j in range(self.row_args[i][0]):
                        self.board[i][j] = 1

            # Edge cell case for cols down top
            for i in range(len_col):
                if self.board[-1][i] == 1 and self.col_args[i][-1] > 1:
                    for j in range(self.col_args[i][-1]):
                        self.board[len_row - j - 1][i] = 1

        self.simple_solved = True


if __name__ == "__main__":
    board = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
    
    # # Simple - castle
    # row_args = [(1,1,1),(5,),(3,),(1,1,), (3,)]
    # col_args = [(2,),(4,),(3, 1),(4,), (2,)]
    
    # # Simple - window/door
    # row_args = [(5,),(1,1,1,),(3,1,),(1,1,1), (5,)]
    # col_args = [(5,),(1,1,1,),(5,),(1,1), (5,)]
    
    # # Medium - plane
    # row_args = [(1,),(3,),(5,),(1,), (3,)]
    # col_args = [(1,),(2,1,),(5,),(2,1), (1,)]

    # # Difficult - smile
    row_args = [(2, 2,), (2, 2), (), (1, 1), (3,)]
    col_args = [(2, 1,), (2, 1,), (1,), (2, 1), (2, 1)]
    
    nonogram = nonogramSolver(board, row_args, col_args)
    if nonogram.solve_board():
        nonogram.print_board()
