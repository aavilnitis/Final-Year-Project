class nonogramSolver:
    def __init__(self, row_args, col_args):
        self.board = [[0 for _ in range(len(col_args))] for _ in range(len(row_args))]
        self.row_args = row_args
        self.col_args = col_args
        self.num_rows = len(row_args)
        self.num_cols = len(col_args)

    # prints the board in a readable format
    def print_board(self):
        for x in range(len(self.board[0])):
            print("---", end="")
        print()
        for row in self.board:
            print(' '.join('#' if cell == 2 else '.' for cell in row))
        for x in range(len(self.board[0])):
            print("---", end="")
        print()
        
    def get_current_row_hints(self):
        row_hints = []

        for i in range(self.num_rows):
            current_hint = []
            sum_ = 0
            for j in range(self.num_cols):
                if self.board[i][j] == 2:
                    sum_ += 1
                else:
                    if sum_ > 0:
                        current_hint.append(sum_)
                        sum_ = 0
            if sum_ > 0: 
                current_hint.append(sum_)
            if len(current_hint) == 0:
                current_hint.append(0)
            row_hints.append(current_hint)

        return row_hints

    def get_current_column_hints(self):
        column_hints = []

        for i in range(self.num_cols):
            current_hint = []
            sum_ = 0
            for j in range(self.num_rows):
                if self.board[j][i] == 2:
                    sum_ += 1
                else:
                    if sum_ > 0:
                        current_hint.append(sum_)
                        sum_ = 0
            if sum_ > 0:
                current_hint.append(sum_)
            if len(current_hint) == 0:
                current_hint.append(0)
            column_hints.append(current_hint)

        return column_hints
    
    def is_board_solved(self):
        current_row_hints = self.get_current_row_hints()
        current_col_hints = self.get_current_column_hints()
        return current_row_hints == self.row_args and current_col_hints == self.col_args
    
    # returns the index of the first row with an empty cell, otherwise returns -1 to indicate that the board is full
    def find_empty_row(self):
        for i in range(len(self.board)):
            if self.board[i][0] == 0:
                return i
        return -1
    
    # returns a list of all possible ways to place the hints in the row
    def generate_possibilities(self, row_index):
        row = self.board[row_index]
        constraints = self.row_args[row_index]
        return self._generate_possibilities(row, constraints)

    # recursive funciton to generate all possible ways to place the hints in the row
    def _generate_possibilities(self, row, constraints, start=0):
        if not constraints:
            return [row] if all(cell == 1 for cell in row[start:]) else []
        
        first, *rest = constraints
        possibilities = []
        
        for i in range(start, len(row) - first + 1):
            if i > 0 and row[i - 1] == 2:
                continue
            
            new_row = row.copy()
            new_row[i:i + first] = [2] * first 
            if i + first < len(row): 
                new_row[i + first] = 1
                
            # replace all 0's with 1's (0's are unplaced cells, 1's are "empty" cells)
            new_row = [1 if cell == 0 else cell for cell in new_row]
            
            possibilities.extend(self._generate_possibilities(new_row, rest, i + first + 1))
        
        return possibilities
    
    # validates column starting from the top of the board to the current height
    def are_columns_valid(self, curr_board_height):
        block_height = 0
        block_index = 0
        row_index = 0
        for col_index in range(self.num_cols):
            while row_index <= curr_board_height:
                
                # if current block index > length of current column hint and cell is coloured - invalid
                if block_index == len(self.col_args[col_index]) and self.board[row_index][col_index] == 2:
                    return False
                
                # if current cell is filled, increment block height
                if self.board[row_index][col_index] == 2:
                    block_height += 1
                    
                    # if block height > hint - invalid
                    if block_height > self.col_args[col_index][block_index]:
                        return False
                    row_index += 1
                
                # if it isn't filled, perform checks
                elif self.board[row_index][col_index] == 1:
                    # if no current block, move on to next row
                    if block_height == 0:
                        row_index += 1
                    
                    # if it is the exact right size, move on to next block and row
                    elif block_height == self.col_args[col_index][block_index]:
                        block_height = 0
                        block_index += 1
                        row_index += 1
                    # else it's invalid
                    else:
                        return False
                elif self.board[row_index][col_index] == 0:
                    row_index += 1
                    
            block_height = 0
            block_index = 0
            row_index = 0
        return True

    # backtracking algorithm 
    def solve_board(self):
        # if no empty rows, the board is solved
        if self.find_empty_row() == -1:
            return True
        
        # for every row starting from first unfinished, try all possibilities and backtrack when necessary
        for row_index in range(self.find_empty_row(), len(self.board)):
            for row in self.generate_possibilities(row_index):
                self.board[row_index] = row
                if(self.are_columns_valid(row_index)):
                    if self.solve_board():
                        return True
                    for i in range(len(self.board[row_index])):
                        self.board[row_index][i] = 0
                for i in range(len(self.board[row_index])):
                        self.board[row_index][i] = 0    
            return False
        
    def get_solved_board(self):
        if self.solve_board():
            return self.board
        return None