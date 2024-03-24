import unittest
from gameBoard import gameBoard


class TestNQSolver(unittest.TestCase):
    def setUp(self):
        self.board = [[1, 0, 0, 0], [0, 0, 0, 0], [1, 0, 0, 0], [0, 0, 0, 0]]
        self.N = 4
        self.gameBoard = gameBoard(self.N, self.board)

    def test_is_safe_row(self):
        self.assertEquals(self.gameBoard._is_safe_row(1), True)
        self.assertEquals(self.gameBoard._is_safe_row(0), False)

    def test_is_safe_col_empty(self):
        self.assertEquals(self.gameBoard._is_safe_column(1), True)
        self.assertEquals(self.gameBoard._is_safe_column(0), False)

    def test_is_safe_diagonal(self):
        # Upper left safe
        self.assertEquals(self.gameBoard._is_safe_diagonal(2, 1), True)
        # Upper left unsafe
        self.assertEquals(self.gameBoard._is_safe_diagonal(1, 1), False)
        # Lower left safe
        self.assertEquals(self.gameBoard.is_safe_entry(1, 2), True)
        # Lower left unsafe
        self.assertEquals(self.gameBoard.is_safe_entry(1, 1), False)

    def test_add_queen(self):
        resulting_board = [
            [1, 0, 0, 0],
            [0, 0, 1, 0],
            [1, 0, 0, 0],
            [0, 0, 0, 0],
        ]  # Adding 1 at index [1][2]
        self.assertEquals(self.gameBoard.add_queen(1, 2), resulting_board)


if __name__ == "__main__":
    unittest.main()
