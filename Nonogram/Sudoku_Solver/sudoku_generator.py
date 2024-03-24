from sudoku_solver import sudokuSolver
import random
import copy

class sudokuGenerator:
    def __init__(self):
        self.board = [[0 for _ in range(9)] for _ in range(9)]
        self.N = 9
        
    def reset(self):
        self.board = [[0 for _ in range(9)] for _ in range(9)]
        
    def print_board(self, board):
        for i in range(self.N):
            print(" ".join(str(board[i][j]) for j in range(self.N)))

    def generate_random_index(self):
        return random.randint(0, 8), random.randint(0, 8)
    
    def is_solvable(self, board):
        solver = sudokuSolver(board)
        return solver.solve_board()
    
    def get_random_board(self):
        for i in range(1, 10):
            index = self.generate_random_index()
            if(self.board[index[0]][index[1]] != 1):
                self.board[index[0]][index[1]] = i
                    
        if(self.is_solvable(self.board)):
            result = copy.deepcopy(self.board)
            self.reset()
            return result
        else:
            self.reset()
            return self.get_random_board()
        
    # 0 = easy, 1 = medium, 2 = hard
    def get_game(self, difficulty):
        full_board = self.get_random_board()
        indices = []
        
        if difficulty == 0:
            while len(indices) < 40:
                index = self.generate_random_index()
                if index not in indices:
                    indices.append(index)
        elif difficulty == 1:
            while len(indices) < 50:
                index = self.generate_random_index()
                if index not in indices:
                    indices.append(index)
        else:
            while len(indices) < 60:
                index = self.generate_random_index()
                if index not in indices:
                    indices.append(index)
                    
        for index in indices:
            full_board[index[0]][index[1]] = 0
            
        return full_board
    
    def get_1d_game(self, difficulty):
        board = self.get_game(difficulty)
        return [cell for row in board for cell in row]
    
if __name__ == "__main__":
    generator = sudokuGenerator()
    print(generator.get_1d_game(0))
    generator = sudokuGenerator()
    print(generator.get_1d_game(0))
    generator = sudokuGenerator()
    print(generator.get_1d_game(0))
    generator = sudokuGenerator()
    print(generator.get_1d_game(0))