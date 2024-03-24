# Final Year Project: Playing Games and Solving Puzzles Using AI

This repository includes all files and documents associated with the creation of an AI based Sudoku and Nonogram solver.

## Authors

- @aavilnitis - Aleksis Aleksandrs Vilnitis

## Supervisor

- Magnus Wahlstrom


## Installation and usage

### 1. Terminal version for sudoku solver
To use the terminal implementation of the Sudoku solver:
```bash
  % cd Sudoku_Solver
  % python3 sudoku_solver.py
```
To change start grid for terminal implementation:
```bash
  % cd Sudoku_Solver
  modify sudoku_solver.py
  % python3 sudoku_solver.py
```

### 2. GUI version of sudoku solver
To use the GUI implementation of the Sudoku solver:
```bash
  % cd Sudoku_Solver
  % python3 sudoku_solver_gui.py
  press load_game to start playing
  select cell you want to modify
  select number you want to place
  press solve_board to solve the game
```
To change start grid for GUI implementation:
```bash
  % cd Sudoku_Solver
  % python3 sudoku_solver_gui.py
  press load_game to start playing
  press load_game to refresh game
```

### 3. Test files
To run the test files for both solver implementations:
```bash
  % cd Sudoku_Solver
  % python3 test_sudoku_solver_gui.py
    - close window that opens
  % python3 test_sudoku_solver.py
```

### 4. Background files
To run the background files:
```bash
  % cd Background
```
#### 4.1 Backtracking:
n-queens:
```bash
  % cd n-queens
  % python3 gameBoard.py
```
subset_sum:
```bash
  % cd subset_sum
  % python3 subset_sum.py
```
sudoku:
```bash
  % cd sudoku
  % python3 small_sudoku.py (3x3 sudoku)
  % python3 sudoku_solver.py (9x9 sudoku)
```
#### 4.2 GUI:
To run the background GUI files:
```bash
  % cd Background
  % cd GUI
  % python3 sudoku_GUI.py
```
#### 4.3 Web Sudoku:
To run the web version of a sudoku game:
```bash
  % cd Background
  % cd web-sudoku
  % npm install (or yarn)
  % npm start
```

## Repository structure
- ./Background
    - ./Backtracking
        - ./n-queens
        - ./subset_sum
        - ./sudoku
    - ./Data Structures
    - ./GUI
    - ./TDD-python
    - ./web-sudoku
- ./Diary
- ./Sudoku Solver
    - ./sudoku_games