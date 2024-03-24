from sudoku_generator import sudokuGenerator
import sys
import json

difficulty = json.loads(sys.argv[1])

generator = sudokuGenerator()
sudoku_game = generator.get_game(difficulty)

print(json.dumps(sudoku_game))

sys.stdout.flush()