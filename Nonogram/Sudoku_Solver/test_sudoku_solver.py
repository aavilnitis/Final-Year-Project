import unittest
from sudoku_solver import sudokuSolver


class TestSudokuSolver(unittest.TestCase):
    """
    A class used to test the sudokuSolver class.

    ...

    Attributes
    ----------
    board : list
        a 2D list representing a Sudoku board
    sudoku_solver : sudokuSolver
        a sudokuSolver object used for testing

    Methods
    -------
    setUp()
        Sets up the test environment.
    test_get_illegal_entries()
        Tests the get_illegal_entries method of the sudokuSolver object.
    test_find_empty_cell()
        Tests the find_empty_cell method of the sudokuSolver object.
    test_get_number_candidates()
        Tests the get_number_candidates method of the sudokuSolver object.
    test_order_by_candidates()
        Tests the order_cells_by_candidates_with_priority_queue method of the sudokuSolver object.
    test_solve_board()
        Tests the solve_board method of the sudokuSolver object.
    test_get_full_board()
        Tests the get_full_board method of the sudokuSolver object.
    """

    def setUp(self):
        # Define a sample sudoku board for testing
        self.board = [
            [8, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 3, 6, 0, 0, 0, 0, 0],
            [0, 7, 0, 0, 9, 0, 2, 0, 0],
            [0, 5, 0, 0, 0, 7, 0, 0, 0],
            [0, 0, 0, 0, 4, 5, 7, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 3, 0],
            [0, 0, 1, 0, 0, 0, 0, 6, 8],
            [0, 0, 8, 5, 0, 0, 0, 1, 0],
            [0, 9, 0, 0, 0, 0, 4, 0, 0],
        ]
        self.sudoku_solver = sudokuSolver(self.board)

    def test_get_illegal_entries(self):
        self.assertEqual(
            1 in self.sudoku_solver.get_illegal_entries(0, 1, self.sudoku_solver.board),
            False,
        )
        # Test if row validation works
        self.assertEqual(
            8 in self.sudoku_solver.get_illegal_entries(0, 1, self.sudoku_solver.board),
            True,
        )
        # Test if column validation works
        self.assertEqual(
            5 in self.sudoku_solver.get_illegal_entries(0, 1, self.sudoku_solver.board),
            True,
        )
        # Test if sub-grid validation works
        self.assertEqual(
            8 in self.sudoku_solver.get_illegal_entries(1, 1, self.sudoku_solver.board),
            True,
        )

    def test_find_empty_cell(self):
        # Find first empty and check it's not None
        first_empty = self.sudoku_solver.find_empty_cell(self.sudoku_solver.board)
        self.assertIsNotNone(first_empty)

        # Make first_empty not empty
        self.sudoku_solver.board[0][1] = 1

        # Find next empty cell and check it's a different one
        second_empty = self.sudoku_solver.find_empty_cell(self.sudoku_solver.board)
        self.assertNotEqual(first_empty, second_empty)

    def test_get_number_candidates(self):
        self.assertEqual(
            self.sudoku_solver.get_number_candidates(0, 0, self.sudoku_solver.board), 5
        )

    def test_order_by_candidates(self):
        self.assertIsNone(self.sudoku_solver.priorityQueue)
        self.sudoku_solver.order_cells_by_candidates_with_priority_queue()
        self.assertIsNotNone(self.sudoku_solver.priorityQueue)

    def test_solve_board(self):
        # Test that first row is not solved before running solve board
        num_empty = 0
        for i in range(9):
            if self.sudoku_solver.board[0][i] == 0:
                num_empty += 1
        self.assertNotEqual(num_empty, 0)

        # Set num_empty to zero, run solve_board and test if no cells are empty
        num_empty = 0
        if self.sudoku_solver.solve_board():
            for i in range(9):
                for j in range(9):
                    if self.sudoku_solver.board[i][j] == 0:
                        num_empty += 1
        self.assertEqual(num_empty, 0)

    def test_get_full_board(self):
        # Same as before, test if not solved
        num_empty = 0
        for i in range(9):
            if self.sudoku_solver.board[0][i] == 0:
                num_empty += 1
        self.assertNotEqual(num_empty, 0)

        # Run get_full_board and check if that is solved
        solved_board = self.sudoku_solver.get_full_board()
        num_empty = 0
        for i in range(9):
            for j in range(9):
                if solved_board[i][j] == 0:
                    num_empty += 1
        self.assertEqual(num_empty, 0)


if __name__ == "__main__":
    unittest.main()
