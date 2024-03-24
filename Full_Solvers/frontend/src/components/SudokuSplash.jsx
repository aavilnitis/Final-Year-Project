import React, { useState } from "react";
import { useNavigate } from 'react-router-dom';

function SudokuSplash() {
    const [difficulty, setDifficulty] = useState("easy");
    const navigate = useNavigate();

    const handleDifficultyChange = (e) => {
        setDifficulty(e.target.value);
    }

    const handlePlayClick = () => {
        navigate(`/sudoku-game/${difficulty}`);
    }

    return (
        <div className="nonogram-splash">
            <h1>Sudoku</h1>
            <p>Play and solve different difficulties of Sudoku puzzles with the help of an AI sudoku solver.</p>
            <div className="choice-screen">
                <select className="game-control" onChange={handleDifficultyChange}>
                    <option value="easy">Easy</option>
                    <option value="medium">Medium</option>
                    <option value="hard">Hard</option>
                </select>
                <button className="game-control" onClick={handlePlayClick}>Play</button>
            </div>
        </div>
    )
}

export default SudokuSplash