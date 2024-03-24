from nonogram_solver import nonogramSolver
import sys
import json

input = json.loads(sys.argv[1])
output = input

row_args = input[0]
col_args = input[1]

if row_args and col_args:
    solver = nonogramSolver(row_args, col_args)
    output = solver.get_solved_board()

print(json.dumps(output))

sys.stdout.flush()