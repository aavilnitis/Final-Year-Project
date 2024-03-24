class simpleSolver:
    def __init__(self, row_args, col_args):
        self.board = [["?" for _ in range(len(col_args))] for _ in range(len(row_args))]
        self.row_args = row_args
        self.col_args = col_args
        self.len_row = len(row_args)
        self.len_col = len(col_args)

    def generate_row_possibilities(self, row_index):
        row = self.board[row_index]
        constraints = self.row_args[row_index]
        return self._generate_row_possibilities(row, constraints)

    def _generate_row_possibilities(self, row, constraints, start=0):
        if not constraints:
            return [[0 if cell == "?" else cell for cell in row]] if all(cell == "?" or cell == 0 for cell in row[start:]) else []
        
        first, *rest = constraints
        possibilities = []
        
        for i in range(start, len(row) - first + 1):
            if i > 0 and row[i - 1] == 1:
                continue
            
            new_row = row.copy()
            for j in range(i, i + first):
                if new_row[j] == "?":
                    new_row[j] = 1
            if i + first < len(row) and new_row[i + first] == "?": 
                new_row[i + first] = 0
            
            possibilities.extend(self._generate_row_possibilities(new_row, rest, i + first + 1))
        
        return [[0 if cell == "?" else cell for cell in possibility] for possibility in possibilities]

    def print_board(self):
        for i in range(len(self.board)):
            print(" ".join(str(self.board[i][j]) for j in range(len(self.board[0]))))
         
    # Length of the clue of filled cells is equal to length of row/column
    def simple_boxes(self):
        # For every row hint: if len(hint) == len(row), fill in the row
        for i in range(self.len_row):
            if sum(self.row_args[i]) == len(self.board[i]):
                self.board[i] = [1] * len(self.board[i])

        # For every column hint: if len(hint) == len(col), fill in the column
        for i in range(self.len_col):
            if sum(self.col_args[i]) == len(self.board):
                for j in range(len(self.board)):
                    self.board[j][i] = 1
                    
    # Length of the clue of filled cells is equal to zero
    def simple_crosses(self):
        # For every row hint: if len(hint) == len(row), fill in the row
        for i in range(self.len_row):
            if sum(self.row_args[i]) == 0:
                self.board[i] = [0] * len(self.board[i])

        # For every column hint: if len(hint) == len(col), fill in the column
        for i in range(self.len_col):
            if sum(self.col_args[i]) == 0:
                for j in range(len(self.board)):
                    self.board[j][i] = 0
       
    # Length of clue + required gaps is equal to length of row/column
    def simple_spaced_boxes(self):
        for i in range(self.len_row):
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

        for i in range(self.len_col):
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
                        
    def _overlapping(self, row_index):
        row_possibilities = self.generate_row_possibilities(row_index)

        # Initialize overlapping_row with ones
        overlapping_row = [1] * self.len_col

        # For each cell in the row
        for i in range(self.len_col):
            # Check if the cell is filled in all possibilities
            for possibility in row_possibilities:
                if possibility[i] != 1:
                    overlapping_row[i] = 0
                    break

        return overlapping_row
    
    def overlap(self):
        for i in range(self.len_row):
            overlap = self._overlapping(i)
            if sum(overlap) > 0:
                self.board[i] = overlap
                        
    

    def solve_board_simple(self):
        self.simple_boxes()
        self.simple_spaced_boxes()
        self.simple_crosses()
        self.overlap()

