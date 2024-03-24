import React, { useEffect, useState } from "react";
import { useNavigate } from 'react-router-dom';
import Spinner from "./Spinner"

function SudokuBoard({ solvedSelf, originalGame, sudokuGame, nextGame, setSudokuGame, solveGame}) {
    const [selected, setSelected] = useState({row: null, cell: null})

    const [cellWidth, setCellWidth] = useState(450 / 9);
    const [windowWidth, setWindowWidth] = useState(window.innerWidth);

    useEffect(() => {
        const handleResize = () => {
            setWindowWidth(window.innerWidth);
        };

        window.addEventListener('resize', handleResize);

        return () => {
            window.removeEventListener('resize', handleResize);
        };
    }, []);

    useEffect(() => {
        if(windowWidth < 800){
            setCellWidth(300 / 9);
        } else {
            setCellWidth(450 / 9);
        }
    }, [windowWidth]);

    const navigate = useNavigate();

    const selectCell = (row, cell) => {
        if(originalGame[row][cell] === 0) {
            setSelected({row, cell})
        }
    }

    const is_valid = (row, col, num) => {
        // Check the row
        for(let i = 0; i < 9; i++) {
            if(sudokuGame[row][i] === num) {
                return false;
            }
        }
    
        // Check the column
        for(let i = 0; i < 9; i++) {
            if(sudokuGame[i][col] === num) {
                return false;
            }
        }
    
        // Check the box
        let startRow = row - row % 3;
        let startCol = col - col % 3;
        for(let i = 0; i < 3; i++) {
            for(let j = 0; j < 3; j++) {
                if(sudokuGame[i + startRow][j + startCol] === num) {
                    return false;
                }
            }
        }
    
        return true;
    }

    const isSolved = () => {
        for(let i = 0; i < 9; i++) {
            for(let j = 0; j < 9; j++) {
                if(sudokuGame[i][j] === 0) {
                    return false;
                }
            }
        }
        return true;
    }

    useEffect(() => {
        if(isSolved()) {
            if(solvedSelf){
                navigate('/victory/sudoku')
            }
        }
    }, [sudokuGame])

    

    const place_number = (number) => {
        if(selected.row !== null && selected.cell !== null && is_valid(selected.row, selected.cell, number)) {
            let newSudokuGame = sudokuGame.map(row => [...row])
            newSudokuGame[selected.row][selected.cell] = number
            setSudokuGame(newSudokuGame)
            setSelected({row: null, cell: null})
        } else {
            setSelected({row: null, cell: null})
        }
    }
    
    const handleKeyDown = (event) => {
        if(selected.row !== null && selected.cell !== null) {
            const number = parseInt(event.key);
            if(number >= 1 && number <= 9) {
                place_number(number);
            }
        }
    }

    useEffect(() => {
        window.addEventListener('keydown', handleKeyDown);
        return () => {
            window.removeEventListener('keydown', handleKeyDown);
        }
    }, [selected, sudokuGame]);

    const callNextGame = () => {
        nextGame()
        setSelected({row: null, cell: null})
    }

    const clearSelectRemove = (row, col) => {
        if(selected.row !== null && selected.cell !== null){
            setSelected({row: null, cell: null})
        }

        if(originalGame[row][col] === 0) {
            let newSudokuGame = sudokuGame.map(row => [...row])
            newSudokuGame[row][col] = 0
            setSudokuGame(newSudokuGame)
        }
    }

    if(sudokuGame.length === 0) {
        return <Spinner />
    }

    return (
        <div className="sudoku-game">
            <div className="game-and-buttons">
                <div className="sudoku-board">
                    {sudokuGame.map((row, rowIndex) => (
                        row.map((cell, cellIndex) => (
                            <div 
                                style={{width: cellWidth, height: cellWidth}}
                                onClick={() => selectCell(rowIndex, cellIndex)}
                                onDoubleClick={() => clearSelectRemove(rowIndex, cellIndex)}
                                key={rowIndex + "-" + cellIndex} 
                                className={`sudoku-cell ${originalGame[rowIndex][cellIndex] !== 0 ? 'bold-cell' : ''} ${(rowIndex === selected.row && cellIndex === selected.cell) ? 'selected' : ''}  ${(cellIndex % 3 !== 2) ? 'border-right-thin' : ''} ${(rowIndex % 3 !== 2) ? 'border-bottom-thin' : ''} ${(rowIndex % 3 === 2 && rowIndex !== 8) ? 'border-bottom' : ''} ${(cellIndex % 3 === 2 && cellIndex !== 8) ? 'border-right' : ''}`}
                            >
                                {cell === 0 ? "" : cell}
                            </div>
                        ))
                    ))}
                </div>

                <div className="sudoku-controls">
                    {[1, 2, 3, 4, 5, 6, 7, 8, 9].map((number) => (
                        <button 
                            style={{width: cellWidth, height: cellWidth}}
                            onClick={() => place_number(number)} 
                            key={number} 
                            className="sudoku-button"
                        >
                            {number}
                        </button>
                    ))}
                </div>
            </div>
            

            <div className="game-controls">
                <button onClick={() => navigate('/sudoku-game')} className="game-control">Change Difficulty</button>
                <button onClick = {solveGame} className="game-control">Solve Game</button>
                <button onClick={callNextGame} className="game-control">Next Game</button>  
            </div>
        </div>
    )
}

export default SudokuBoard