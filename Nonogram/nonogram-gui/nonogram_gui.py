import customtkinter as ctk
import json

# GAME LOGIC
def get_current_row_hints(board, num_rows, num_cols):
    row_hints = []

    for i in range(num_rows):
        current_hint = []
        sum_ = 0
        for j in range(num_cols):
            if board[i][j] == 1:
                sum_ += 1
            else:
                if sum_ > 0:
                    current_hint.append(sum_)
                    sum_ = 0
        if sum_ > 0: 
            current_hint.append(sum_)
        row_hints.append(current_hint)

    return row_hints

def get_current_column_hints(board, num_rows, num_cols):
    column_hints = []

    for i in range(num_cols):
        current_hint = []
        sum_ = 0
        for j in range(num_rows):
            if board[j][i] == 1:
                sum_ += 1
            else:
                if sum_ > 0:
                    current_hint.append(sum_)
                    sum_ = 0
        if sum_ > 0:
            current_hint.append(sum_)
        column_hints.append(current_hint)

    return column_hints

def is_board_solved(board, row_args, col_args):
    current_row_hints = get_current_row_hints(board, len(row_args), len(col_args))
    current_col_hints = get_current_column_hints(board, len(row_args), len(col_args))
    return current_row_hints == row_args and current_col_hints == col_args

# Assign the global variable selected_cell with a button object and change that buttons background color to indicate selection
def set_selected(i, j):
    global board, row_args, col_args
    if board[i][j] == 0:
        buttons[i][j].configure(fg_color="black", hover_color="#292929")
        board[i][j] = 1
    else:
        board[i][j] = 0
        buttons[i][j].configure(fg_color="#fff", hover_color="#cfcfcf")
        
    if(is_board_solved(board, row_args, col_args)):
        show_victory()
        
def show_victory():
    game_board.place_forget()
    row_hints.place_forget()
    col_hints.place_forget()
    victory.place(relx = 0.5, rely = 0.5, anchor=ctk.CENTER)

# Create window for GUI python game
window = ctk.CTk()
window.title("Sudoku")
window.geometry("800x800")

# GAME CONTRAINTS

# Load data from the JSON file
with open('games.json', 'r') as file:
    nonogram_data = json.load(file)
    
selected_game = nonogram_data['5x5_boards'][0]
row_args = selected_game["row_args"]
col_args = selected_game["col_args"]

board = [[0 for _ in range(len(col_args))] for _ in range(len(row_args))]

# CELL AND FRAME SIZING
cell_size = 400/max(len(row_args), len(col_args))
frame_height = cell_size * len(row_args)
frame_width = cell_size * len(col_args)

# Create a game board rectangle (middle)
game_board = ctk.CTkFrame(window, fg_color="#2ecc71")
game_board.place(relx = 0.5, rely = 0.5, anchor=ctk.CENTER)

# Create a row hint rectangle (left)
row_hints = ctk.CTkFrame(window, fg_color="blue", width=100, height=len(row_args)*cell_size)
row_hints.place(x=350-0.5*frame_width, rely=0.5, anchor=ctk.CENTER)

# Create a column hint rectangle (left)
col_hints = ctk.CTkFrame(window, fg_color="red", width=len(col_args)*cell_size, height=100)
col_hints.place(relx = 0.5, y=350-0.5*frame_height, anchor=ctk.CENTER)

victory = ctk.CTkLabel(
    window,
    text= "Congratulations, you have won!",
    text_color="#cfcfcf"
)

buttons = [
    [
        ctk.CTkButton(
            game_board,
            text="",  # if random_game[i * 9 + j] == 0 else random_game[i * 9 + j],
            width=cell_size,
            height=cell_size,
            text_color="white",
            fg_color="#fff",
            hover_color="#cfcfcf",
            border_width=1,
            corner_radius=0,
            command=lambda i=i, j=j: set_selected(i, j),
        )
        for j in range(len(col_args))
    ]
    for i in range(len(row_args))
]

for i in range(len(row_args)):
    for j in range(len(col_args)):
        buttons[i][j].grid(row=i, column=j)
        
row_hint_texts = [' '.join(map(str, hint)) for hint in row_args]

rows = [
        ctk.CTkButton(
            row_hints,
            text=row_hint_texts[i],
            width=(100),
            height=cell_size,
            text_color="black",
            fg_color="#cfcfcf",
            hover_color="#cfcfcf",
            border_width=1,
            corner_radius=0,
        )
    for i in range(len(row_args))
]

for i in range(len(row_args)):
        rows[i].grid(row=i, column =0)
        
col_hint_texts = ['\n'.join(map(str, hint)) for hint in col_args]

cols = [
        ctk.CTkButton(
            col_hints,
            text=col_hint_texts[i],
            width=cell_size,
            height=100,
            text_color="black",
            fg_color="#cfcfcf",
            hover_color="#cfcfcf",
            border_width=1,
            corner_radius=0,
        )
    for i in range(len(col_args))
]

for i in range(len(col_args)):
        cols[i].grid(row=0, column =i)
        
window.mainloop()