import unittest
from smallSudoku import smallSudoku


class TestSmallSudokuSolver(unittest.TestCase):
    def setUp(self):
        self.board = [
            [2, 0, 3],
            [1, 0, 0],
            [0, 0, 1],
        ]
        self.full_board = [
            [2, 1, 3],
            [1, 3, 2],
            [3, 2, 1],
        ]
        self.sudoku_board = smallSudoku(self.board)
        self.full_sudoku_board = smallSudoku(self.full_board)

    # Test 1: test if a cell that is not empty returns False
    def test_not_empty(self):
        self.assertEquals(self.sudoku_board.is_safe(0, 0, 1), False)

    # Test 2&3: test if is_safe returns expected value looking at just the rows
    def test_row(self):
        self.assertEquals(self.sudoku_board.is_safe(1, 1, 1), False)
        self.assertEquals(self.sudoku_board.is_safe(0, 0, 1), False)

    # Test 4&5: test if is_safe returns expected value looking at just the columns
    def test_column(self):
        self.assertEquals(self.sudoku_board.is_safe(2, 1, 3), True)
        self.assertEquals(self.sudoku_board.is_safe(0, 1, 3), False)

    def test_is_complete(self):
        self.assertEquals(self.full_sudoku_board.solve_board(), True)

    def test_can_solve(self):
        self.assertEquals(self.sudoku_board.solve_board(), True)

    def test_solves_correctly(self):
        self.assertEquals(self.sudoku_board.get_full_board(), self.full_board)


if __name__ == "__main__":
    unittest.main()
