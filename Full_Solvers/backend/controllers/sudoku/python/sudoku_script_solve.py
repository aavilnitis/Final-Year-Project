from sudoku_solver import sudokuSolver
import sys
import json

board = json.loads(sys.argv[1])

solver = sudokuSolver(board)
sudoku_game = solver.get_full_board()

print(json.dumps(sudoku_game))

sys.stdout.flush()