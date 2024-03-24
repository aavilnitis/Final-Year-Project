import customtkinter as ctk
import random
from sudokuSolver import sudokuSolver

# Create window for GUI python game
window = ctk.CTk()
window.title("Sudoku")
window.geometry("600x500")

# Create sudoku frame that is going to hold the buttons
frame = ctk.CTkFrame(window, corner_radius=0)
frame.place(relx=0.5, rely=0.31, anchor=ctk.CENTER)

# Load in text file with sudoku games
with open("./Sudoku games/sudoku.txt", "r") as file:
    file_contents = file.read()

# Load in text file with sudoku games
sudoku_games = [file_contents[i : i + 81] for i in range(0, len(file_contents), 81)]


def clear_game():
    clear_selected()
    selected_cell = None
    global original_entry_indices
    original_entry_indices = []
    for row in range(9):
        for col in range(9):
            buttons[row][col].configure(text="")


def start_game():
    clear_game()
    global started, random_game
    started = True
    get_game_array()
    for row in range(9):
        for col in range(9):
            buttons[row][col].configure(hover_color=get_hover_color(row, col))
            if not random_game[row * 9 + col] == 0:
                buttons[row][col].configure(text=random_game[row * 9 + col])


def solve_game_function():
    global random_game
    game_board = []
    game_row = []
    for i in range(9):
        game_row = []
        for j in range(9):
            game_row.append(random_game[i * 9 + j])
        game_board.append(game_row)

    sudoku_board = sudokuSolver(game_board)
    if sudoku_board.solve_board():
        solved_sudoku = sudoku_board.get_full_board()
        enter_solved_board(solved_sudoku)
    else:
        print("Unable to solve this, fix the entries you entered")


def enter_solved_board(solved_board):
    for row in range(9):
        for col in range(9):
            buttons[row][col].configure(text=solved_board[row][col])


def get_game_array():
    # Get a random number and use it to choose one of loaded games
    global random_game
    random_index = random.randint(0, len(sudoku_games) - 1)
    random_game = []
    for element in sudoku_games[random_index]:
        random_game.append(int(element))

    for i, entry in enumerate(random_game):
        if entry != 0:
            original_entry_indices.append(i)


# Load in the indices of the original game board's non zero entries
original_entry_indices = []

# Variable that holds selected cell's button object, as well as the global indices i and j for number placement
selected_cell = None
global_i = -1
global_j = -1
started = False
random_game = []


# Assign the global variable selected_cell with a button object and change that buttons background color to indicate selection
def set_selected(i, j):
    global selected_cell, global_i, global_j, started
    clear_selected()
    if started:
        if not ((i * 9 + j) in original_entry_indices):
            buttons[i][j].configure(fg_color="#5ab0c7", hover_color="#5ab0c7")
            selected_cell = buttons[i][j]
            global_i = i
            global_j = j


# Loop through all the buttons and change their backgrounds and hover colors to the default to remove the selection indication
def clear_selected():
    global started
    for row in range(9):
        for col in range(9):
            if started:
                buttons[row][col].configure(
                    fg_color=get_fg_color(row, col),
                    hover_color=get_hover_color(row, col),
                )
            else:
                buttons[row][col].configure(
                    fg_color=get_fg_color(row, col), hover_color=get_fg_color(row, col)
                )


# Once a cell selection has been made and a number button is clicked, place that number in that cell if it's a valid entry
def place_number(i):
    global selected_cell, global_i, global_j, random_game
    clear_selected()
    # If there is a selection made
    if selected_cell != None:
        # If button isn't the delete button
        if i != 10:
            # If entry isn't illegal, place it there
            if i not in get_illegal_entries(global_i, global_j):
                selected_cell.configure(text=i)
                selected_cell = None
                random_game[global_i * 9 + global_j] = i
            else:
                print("selection invalid")
        else:
            selected_cell.configure(text="")
            selected_cell = None
            random_game[global_i * 9 + global_j] = 0
    else:
        print("No button selected")


# Show the subgrids by changing fg color and hover color depending on cell indices
def get_fg_color(i, j):
    if (i in [0, 1, 2, 6, 7, 8] and j in [0, 1, 2, 6, 7, 8]) or (
        i in [3, 4, 5] and j in [3, 4, 5]
    ):
        return "#1c4966"
    else:
        return "#1b3f5b"


def get_hover_color(i, j):
    if (i in [0, 1, 2, 6, 7, 8] and j in [0, 1, 2, 6, 7, 8]) or (
        i in [3, 4, 5] and j in [3, 4, 5]
    ):
        return "#296d98"
    else:
        return "#285e8e"


# Function that looks at the global variable random_game and returns all the numbers that are invalid for that cell
def get_illegal_entries(row, column):
    global random_game
    illegal_entries = []

    startRow = row // 3 * 3
    startCol = column // 3 * 3

    # subgrid
    for i in range(startRow, startRow + 3):
        for j in range(startCol, startCol + 3):
            illegal_entries.append(random_game[i * 9 + j])

    # row
    for i in range(9):
        illegal_entries.append(random_game[row * 9 + i])

    # column
    for i in range(9):
        illegal_entries.append(random_game[i * 9 + column])

    return illegal_entries


buttons = [
    [
        ctk.CTkButton(
            frame,
            text="",  # if random_game[i * 9 + j] == 0 else random_game[i * 9 + j],
            width=(300 / 9),
            height=(300 / 9),
            text_color="white" if not (i * 9 + j) in original_entry_indices else "red",
            fg_color=get_fg_color(i, j),
            hover_color=get_hover_color(i, j) if started else get_fg_color(i, j),
            border_width=1,
            corner_radius=0,
            command=lambda i=i, j=j: set_selected(i, j),
        )
        for j in range(9)
    ]
    for i in range(9)
]

for i in range(9):
    for j in range(9):
        buttons[i][j].grid(row=i, column=j)

# Create a new frame for the number buttons
number_frame = ctk.CTkFrame(
    window, width=300, height=30, fg_color="blue", corner_radius=0
)
number_frame.place(relx=0.5, rely=0.645, anchor=ctk.CENTER)

# Add 10 buttons to the number frame
number_buttons = [
    ctk.CTkButton(
        number_frame,
        text="X" if i == 10 else i,
        width=(300 / 10),
        height=30,
        fg_color="#1c4966",
        hover_color="#296d98",
        corner_radius=0,
        command=lambda i=i: place_number(i),
    )
    for i in range(1, 11)
]

for i in range(10):
    number_buttons[i].grid(row=0, column=i)

# Create a new frame for the control buttons
control_frame = ctk.CTkFrame(window, width=300, height=30, corner_radius=0)

load_game = ctk.CTkButton(
    control_frame,
    text="Load game",
    width=(300 / 2),
    height=30,
    fg_color="#285e8e",
    hover_color="#296d98",
    corner_radius=0,
    command=lambda: start_game(),
)

load_game.grid(row=0, column=0)

solve_game = ctk.CTkButton(
    control_frame,
    text="Solve game",
    width=(300 / 2),
    height=30,
    fg_color="#285e8e",
    hover_color="#296d98",
    corner_radius=0,
    command=lambda: solve_game_function(),
)

solve_game.grid(row=0, column=1)

control_frame.place(relx=0.5, rely=0.715, anchor=ctk.CENTER)

# run
window.mainloop()
