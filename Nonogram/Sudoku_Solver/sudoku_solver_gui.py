import customtkinter as ctk
import random
from sudoku_solver import sudokuSolver
from sudoku_generator import sudokuGenerator

class SudokuGUI:
    """
    A class used to create a graphical user interface for Sudoku puzzles.
    ...

    Attributes
    ----------
    all_games : str
        a string containing all Sudoku games
    sudoku_games : list
        a list of strings, each of length 81, representing Sudoku games
    selected_cell : CTkButton
        the currently selected button on the Sudoku board
    global_i : int
        the row index of the selected cell
    global_j : int
        the column index of the selected cell
    started : bool
        a flag indicating whether a game has started
    original_entry_indices : list
        a list of indices of the original entries in the Sudoku game
    random_game : list
        a list of 81 digits representing a random Sudoku game
    window : CTk
        the main window of the Sudoku GUI
    frame : CTkFrame
        the frame containing the Sudoku board and cells
    number_frame : CTkFrame
        the frame containing the number buttons
    control_frame : CTkFrame
        the frame containing the control buttons
    label_frame : CTkFrame
        the frame containing the error label
    buttons : list
        a 2D list of buttons representing the cells on the Sudoku board
    number_buttons : list
        a list of buttons representing the number buttons
    load_game_button : CTkButton
        the button used to load a game
    solve_game_button : CTkButton
        the button used to solve a game
    label : CTkLabel
        the label used to display error messages

    Methods
    -------
    get_fg_color(i, j)
        Returns the foreground color for a cell based on its indices.
    get_hover_color(i, j)
        Returns the hover color for a cell based on its indices.
    clear_buttons()
        Clears all the buttons on the board.
    start_game()
        Starts a new Sudoku game.
    set_selected(i, j)
        Sets a cell as selected and changes its background color.
    clear_selected()
        Clears the selection by restoring default background and hover colors.
    place_number(i)
        Places a number on the board if the selected cell is valid.
    get_illegal_entries(row, column)
        Returns a set of numbers that cannot be placed in the given cell.
    solve_game_function()
        Solves the Sudoku game using the SudokuSolver class.
    enter_solved_board(solved_board)
        Enters the solved game array into the Sudoku grid to show the solution.
    run()
        Runs the Sudoku game.
    """

    def __init__(self, all_games):
        """
        Constructs a new SudokuGUI object.

        Parameters
        ----------
        all_games : str
            a string containing all Sudoku games
        """
        # Load in text file with sudoku games
        self.all_games = all_games

        # Split string with all sudoku games into array with strings of length 81
        self.sudoku_games = [
            all_games[i : i + 81] for i in range(0, len(all_games), 81)
        ]

        # Global variables for Sudoku GUI
        self.selected_cell = None
        self.global_i = -1
        self.global_j = -1
        self.started = False
        self.original_entry_indices = []
        self.random_game = []

        # GUI setup code
        self.window = ctk.CTk()
        self.window.title("Sudoku Solver")
        self.window.geometry("600x500")

        self.frame = ctk.CTkFrame(self.window, corner_radius=0)
        self.frame.place(relx=0.5, rely=0.31, anchor=ctk.CENTER)

        self.number_frame = ctk.CTkFrame(self.window, fg_color="blue", corner_radius=0)
        self.number_frame.place(relx=0.5, rely=0.645, anchor=ctk.CENTER)

        self.control_frame = ctk.CTkFrame(self.window, corner_radius=0)
        self.control_frame.place(relx=0.5, rely=0.715, anchor=ctk.CENTER)

        self.label_frame = ctk.CTkFrame(
            self.window, corner_radius=0, height=20, width=300
        )
        # Adjust the placement of the label_frame to be under the buttons
        self.label_frame.place(relx=0.5, rely=0.85, anchor=ctk.CENTER)

        # 2.1 Create 81 buttons to represent the cells in Sudoku
        self.buttons = [
            [
                ctk.CTkButton(
                    self.frame,
                    text="",  # if random_game[i * 9 + j] == 0 else random_game[i * 9 + j],
                    width=(300 / 9),
                    height=(300 / 9),
                    text_color="white"
                    if (i * 9 + j) not in self.original_entry_indices
                    else "red",
                    fg_color=self.get_fg_color(i, j),
                    hover_color=self.get_hover_color(i, j)
                    if self.started
                    else self.get_fg_color(i, j),
                    border_width=1,
                    corner_radius=0,
                    command=lambda i=i, j=j: self.set_selected(i, j),
                )
                for j in range(9)
            ]
            for i in range(9)
        ]
        # 2.1.1 Add the buttons to the button frame
        for i in range(9):
            for j in range(9):
                self.buttons[i][j].grid(row=i, column=j)

        # 2.2 Create 10 number buttons, 1-9 for input options, 10 for a delete button
        self.number_buttons = [
            ctk.CTkButton(
                self.number_frame,
                text="X" if i == 10 else i,
                width=(300 / 10),
                height=30,
                fg_color="#1c4966",
                hover_color="#296d98",
                corner_radius=0,
                command=lambda i=i: self.place_number(i),
            )
            for i in range(1, 11)
        ]

        # 2.2.1 Add number and delete buttons to number frame
        for i in range(10):
            self.number_buttons[i].grid(row=0, column=i)

        # 2.3 Create solve and load game buttons
        # 2.3.1 Load game
        self.load_game_button = ctk.CTkButton(
            self.control_frame,
            text="Load game",
            width=(300 / 2),
            height=30,
            fg_color="#285e8e",
            hover_color="#296d98",
            corner_radius=0,
            command=lambda: self.start_game(),
        )

        # 2.3.2 Solve game
        self.solve_game_button = ctk.CTkButton(
            self.control_frame,
            text="Solve game",
            width=(300 / 2),
            height=30,
            fg_color="#285e8e",
            hover_color="#296d98",
            corner_radius=0,
            command=lambda: self.solve_game_function(),
        )

        # 2.3.3 Add solve_game and load_game buttons to control frame
        self.solve_game_button.grid(row=0, column=1)
        self.load_game_button.grid(row=0, column=0)

        self.label = ctk.CTkLabel(
            master=self.label_frame, text="", text_color="red", height=10
        )
        self.label.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)

    # Show the subgrids by changing fg color and hover color depending on cell indices
    def get_fg_color(self, i, j):
        """
        Returns the foreground color for a cell based on its indices.

        Parameters
        ----------
        i : int
            the row index of the cell
        j : int
            the column index of the cell

        Returns
        -------
        str
            the foreground color for the cell
        """
        if (i in [0, 1, 2, 6, 7, 8] and j in [0, 1, 2, 6, 7, 8]) or (
            i in [3, 4, 5] and j in [3, 4, 5]
        ):
            return "#1c4966"
        else:
            return "#1b3f5b"

    def get_hover_color(self, i, j):
        """
        Returns the hover color for a cell based on its indices.

        Parameters
        ----------
        i : int
            the row index of the cell
        j : int
            the column index of the cell

        Returns
        -------
        str
            the hover color for the cell
        """
        if (i in [0, 1, 2, 6, 7, 8] and j in [0, 1, 2, 6, 7, 8]) or (
            i in [3, 4, 5] and j in [3, 4, 5]
        ):
            return "#296d98"
        else:
            return "#285e8e"

    def clear_buttons(self):
        """
        Clears all the buttons on the board.
        """
        for row in range(9):
            for col in range(9):
                self.buttons[row][col].configure(text="")

    def start_game(self):
        """
        Starts a new Sudoku game.
        """
        self.label.configure(text="")
        self.selected_cell = None
        self.original_entry_indices = []
        self.random_game = []
        self.started = True

        self.clear_buttons()
        sudoku_generator = sudokuGenerator()
        self.random_game = sudoku_generator.get_1d_game(2)

        # Store the indices of the original elements to prevent selection on those
        for i, entry in enumerate(self.random_game):
            if entry != 0:
                self.original_entry_indices.append(i)

        # Set original elements in board
        for row in range(9):
            for col in range(9):
                self.buttons[row][col].configure(
                    hover_color=self.get_hover_color(row, col)
                )
                if not self.random_game[row * 9 + col] == 0:
                    self.buttons[row][col].configure(
                        text=self.random_game[row * 9 + col]
                    )

    def set_selected(self, i, j):
        """
        Sets a cell as selected and changes its background color.

        Parameters
        ----------
        i : int
            the row index of the cell
        j : int
            the column index of the cell
        """
        self.label.configure(text="")
        self.clear_selected()
        if self.started:
            if not ((i * 9 + j) in self.original_entry_indices):
                self.buttons[i][j].configure(fg_color="#5ab0c7", hover_color="#5ab0c7")
                self.selected_cell = self.buttons[i][j]
                self.global_i = i
                self.global_j = j

    def clear_selected(self):
        """
        Clears the selection by restoring default background and hover colors.
        """
        for row in range(9):
            for col in range(9):
                if self.started:
                    self.buttons[row][col].configure(
                        fg_color=self.get_fg_color(row, col),
                        hover_color=self.get_hover_color(row, col),
                    )
                else:
                    self.buttons[row][col].configure(
                        fg_color=self.get_fg_color(row, col),
                        hover_color=self.get_fg_color(row, col),
                    )

    def place_number(self, i):
        """
        Places a number on the board if the selected cell is valid.

        Parameters
        ----------
        i : int
            the number to be placed on the board
        """
        self.label.configure(text="")
        self.clear_selected()
        # If there is a selection made
        if self.selected_cell != None:
            # If button isn't the delete button
            if i != 10:
                # If entry isn't illegal, place it there
                if i not in self.get_illegal_entries(self.global_i, self.global_j):
                    self.selected_cell.configure(text=i)
                    self.selected_cell = None
                    self.random_game[self.global_i * 9 + self.global_j] = i
                else:
                    self.label.configure(text="Invalid number")
            else:
                self.selected_cell.configure(text="")
                self.selected_cell = None
                self.random_game[self.global_i * 9 + self.global_j] = 0
        else:
            self.label.configure(text="No button selected")

    def get_illegal_entries(self, row, column):
        """
        Returns a set of numbers that cannot be placed in the given cell.

        Parameters
        ----------
        row : int
            the row index of the cell
        column : int
            the column index of the cell

        Returns
        -------
        set
            a set of numbers that cannot be placed in the cell
        """
        illegal_entries = set()
        startRow = row // 3 * 3
        startCol = column // 3 * 3

        # subgrid
        for i in range(startRow, startRow + 3):
            for j in range(startCol, startCol + 3):
                illegal_entries.add(self.random_game[i * 9 + j])

        # row
        for i in range(9):
            illegal_entries.add(self.random_game[row * 9 + i])

        # column
        for i in range(9):
            illegal_entries.add(self.random_game[i * 9 + column])

        print(illegal_entries)
        return illegal_entries

    # Turn random_game array into 2d array and pass it to SudokuSolver to solve
    def solve_game_function(self):
        """
        Solves the Sudoku game using the SudokuSolver class.
        """
        self.label.configure(text="")
        self.clear_selected()
        game_board = []
        game_row = []
        for i in range(9):
            game_row = []
            for j in range(9):
                game_row.append(self.random_game[i * 9 + j])
                self.buttons[i][j].configure(hover_color=self.get_fg_color(i, j))
            game_board.append(game_row)

        sudoku_board = sudokuSolver(game_board)
        if sudoku_board.solve_board():
            solved_sudoku = sudoku_board.get_full_board()
            self.enter_solved_board(solved_sudoku)
        else:
            self.label.configure(
                text="Unable to solve this, fix the entries you entered"
            )

    def enter_solved_board(self, solved_board):
        """
        Enters the solved game array into the Sudoku grid to show the solution.

        Parameters
        ----------
        solved_board : list
            the solved Sudoku board
        """
        self.started = False
        for row in range(9):
            for col in range(9):
                self.random_game[row * 9 + col] = solved_board[row][col]
                self.buttons[row][col].configure(text=solved_board[row][col])

    def run(self):
        """
        Runs the Sudoku game.
        """
        self.window.mainloop()


with open("./sudoku_games/one_sudoku.txt", "r") as file:
    all_games = file.read()
sudoku = SudokuGUI(all_games)


sudoku.run()
