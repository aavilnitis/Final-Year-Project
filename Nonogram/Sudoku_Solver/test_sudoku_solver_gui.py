import unittest
import tkinter as tk
from sudoku_solver_gui import SudokuGUI


class TestGUI(unittest.TestCase):
    """
    A class used to test the SudokuGUI class.

    ...

    Attributes
    ----------
    all_games : str
        a string containing all Sudoku games
    sudoku_solver : SudokuGUI
        a SudokuGUI object used for testing
    gui : CTk
        the main window of the SudokuGUI object

    Methods
    -------
    setUp()
        Sets up the test environment.
    test_gui_basics()
        Tests the basic functionality of the SudokuGUI object.
    test_cell_buttons()
        Tests the cell buttons of the SudokuGUI object.
    test_get_fg_color()
        Tests the get_fg_color method of the SudokuGUI object.
    test_get_hover_color()
        Tests the get_hover_color method of the SudokuGUI object.
    test_number_buttons()
        Tests the number buttons of the SudokuGUI object.
    test_control_buttons()
        Tests the control buttons of the SudokuGUI object.
    test_load_game()
        Tests the load_game method of the SudokuGUI object.
    test_set_selected()
        Tests the set_selected method of the SudokuGUI object.
    test_set_selected_invalid()
        Tests the set_selected method of the SudokuGUI object with invalid input.
    test_clear_selected()
        Tests the clear_selected method of the SudokuGUI object.
    test_place_number()
        Tests the place_number method of the SudokuGUI object.
    """

    def setUp(self):
        with open("./sudoku_games/one_sudoku.txt", "r") as file:
            self.all_games = file.read()
        self.sudoku_solver = SudokuGUI(self.all_games)
        self.gui = self.sudoku_solver.window

    def test_gui_basics(self):
        # Test if solver is created
        self.assertIsNotNone(self.sudoku_solver)

        # Test if GUI window is created and title correct
        self.assertIsNotNone(self.gui)
        self.assertEqual(self.gui.title(), "Sudoku Solver")

        # Test if sudoku, number and control frames exist
        self.assertIsNotNone(self.gui.children["!ctkframe"])
        self.assertIsNotNone(self.gui.children["!ctkframe2"])
        self.assertIsNotNone(self.gui.children["!ctkframe3"])

    def test_cell_buttons(self):
        # Test that sudoku solver has array of buttons
        self.assertIsNotNone(self.sudoku_solver.buttons)
        # Test if said array is length 9
        self.assertEqual(len(self.sudoku_solver.buttons), 9)

    def test_get_fg_color(self):
        # Test cells in the corners of the grid
        self.assertEqual(self.sudoku_solver.get_fg_color(0, 0), "#1c4966")
        self.assertEqual(self.sudoku_solver.get_fg_color(8, 8), "#1c4966")

        # Test cells in the middle of the grid
        self.assertEqual(self.sudoku_solver.get_fg_color(4, 4), "#1c4966")
        self.assertEqual(self.sudoku_solver.get_fg_color(3, 3), "#1c4966")

    def test_get_hover_color(self):
        # Test cells in the corners of the grid
        self.assertEqual(self.sudoku_solver.get_hover_color(0, 0), "#296d98")
        self.assertEqual(self.sudoku_solver.get_hover_color(8, 8), "#296d98")

        # Test cells in the middle of the grid
        self.assertEqual(self.sudoku_solver.get_hover_color(4, 4), "#296d98")
        self.assertEqual(self.sudoku_solver.get_hover_color(3, 3), "#296d98")

    def test_number_buttons(self):
        # Test that sudoku solver has array of number buttons
        self.assertIsNotNone(self.sudoku_solver.number_buttons)
        # Test if said array is length 10 (9 numbers 1 delete button)
        self.assertEqual(len(self.sudoku_solver.number_buttons), 10)

    def test_control_buttons(self):
        # Test that sudoku solver has start button
        self.assertIsNotNone(self.sudoku_solver.load_game_button)
        # Test that sudoku solver has load button
        self.assertIsNotNone(self.sudoku_solver.solve_game_button)

    def test_load_game(self):
        # Test if array is empty at start
        self.assertEqual(len(self.sudoku_solver.random_game), 0)
        # Call start game and check if length is 81 after
        self.sudoku_solver.start_game()
        self.assertEqual(len(self.sudoku_solver.random_game), 81)

    def test_set_selected(self):
        # Test that selected is None at first
        self.assertIsNone(self.sudoku_solver.selected_cell)
        # Start game so original indices loaded and selection possible
        self.sudoku_solver.start_game()
        # Select valid selection
        self.sudoku_solver.set_selected(0, 0)
        # Test if selection not None
        self.assertIsNotNone(self.sudoku_solver.selected_cell)

    def test_set_selected_invalid(self):
        # Check that selected is None at first
        self.assertIsNone(self.sudoku_solver.selected_cell)
        # Start game so original indices loaded and selection possible
        self.sudoku_solver.start_game()
        # Select invalid selection
        self.sudoku_solver.set_selected(0, 2)
        # Test if selection None
        self.assertIsNone(self.sudoku_solver.selected_cell)

    def test_clear_selected(self):
        pass  # Could not test because doesn't make selection None, instead changes background and hover colors

    def test_place_number(self):
        # Start game so original indices and random_game loaded and selection possible
        self.sudoku_solver.start_game()
        # Check that number is 0 before placing
        self.assertEqual(self.sudoku_solver.random_game[0], 0)
        # Select valid selection
        self.sudoku_solver.set_selected(0, 0)
        # Place valid number
        self.sudoku_solver.place_number(4)
        # Test if number was placed
        self.assertEqual(self.sudoku_solver.random_game[0], 4)

    def test_illegal_entries(self):
        # Start game so original indices and random_game loaded and selection possible
        self.sudoku_solver.start_game()
        # Test if illegal entries match with expected values
        self.assertEqual(
            self.sudoku_solver.get_illegal_entries(0, 0), {0, 1, 2, 3, 6, 7, 8, 9}
        )

    def test_solve_game(self):
        # Start game so original indices and random_game loaded and selection possible
        self.sudoku_solver.start_game()
        # Run function that solves the game
        self.sudoku_solver.solve_game_function()

        # Check if solved board is correct
        self.assertEqual(self.sudoku_solver.random_game[0], 4)
        self.assertEqual(self.sudoku_solver.random_game[1], 8)
        self.assertEqual(self.sudoku_solver.random_game[2], 3)
        self.assertEqual(self.sudoku_solver.random_game[3], 9)
        self.assertEqual(self.sudoku_solver.random_game[4], 2)


if __name__ == "__main__":
    unittest.main()
