import React from 'react'
import { useNavigate } from 'react-router-dom'

function NonogramControls({isSolved, solveGame, callNextGame, clearGame, checkBoard}) {

    const navigate = useNavigate();
  
    return (
        <div className="nonogram-controls">
            {isSolved ? null : <button onClick = {checkBoard} className="game-control">Check Game</button>}
            {isSolved ? null : <button onClick = {clearGame} className="game-control">Reset Game</button>}
            {isSolved ? null : <button onClick={solveGame} className="game-control">Solve Game</button>}
            <button onClick={callNextGame} className="game-control">Next Game</button>
            <button onClick={() => navigate('/nonogram-game')} className="game-control">Change Difficulty</button>
        </div>

  )
}

export default NonogramControls