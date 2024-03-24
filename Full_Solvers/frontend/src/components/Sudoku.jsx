import React, { useEffect, useState } from "react";
import "../sudoku.css";
import Spinner from "./Spinner";
import SudokuBoard from "./SudokuBoard";
import { useParams} from 'react-router-dom';

function Sudoku() {
  
  const [originalGame, setOriginalGame] = useState([]);
  const [sudokuGame, setSudokuGame] = useState([]);
  const { difficulty } = useParams();
  const [solvedSelf, setSolvedSelf] = useState(true);

  const nextGame = () => {
    fetch(`http://localhost:5000/sudoku/${difficulty}`)
      .then((response) => response.json())
      .then((data) => {
        setSudokuGame(data);
        setOriginalGame(data);
      });
    setSolvedSelf(true);
  }

  const solveGame = () => {
    console.log(JSON.stringify({game: sudokuGame}))
    fetch("http://localhost:5000/sudoku/solve", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ sudoku_game: sudokuGame }),
      
    })
      .then((response) => response.json())
      .then((data) => {
        setSudokuGame(data);
      });
      setSolvedSelf(false);
  }

  useEffect(() => {
    nextGame();
  }, []);

  if(sudokuGame.length === 0) {
    return <Spinner />
  }

  return (
    <div className="sudoku">
      <SudokuBoard solvedSelf = {solvedSelf} originalGame = {originalGame} sudokuGame={sudokuGame} setSudokuGame={setSudokuGame} nextGame={nextGame} solveGame={solveGame}/>
    </div>
  );
}

export default Sudoku;
