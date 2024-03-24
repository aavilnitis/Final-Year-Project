import React, { useEffect, useState } from "react";
import { useParams } from 'react-router-dom';
import "../nonogram.css";
import Spinner from "./Spinner";
import NonogramBoard from "./NonogramBoard";


function Nonogram() {

  const { size } = useParams();
  const [allGames, setAllGames] = useState([]);
  const [currentGame, setCurrentGame] = useState(0);
  const [rowArgs, setRowArgs] = useState([]);
  const [colArgs, setColArgs] = useState([]);
  const [solvedBoard, setSolvedBoard] = useState([[]]);
  const [nonogramBoard, setNonogramBoard] = useState(Array.from({length: rowArgs.length}, () => Array(colArgs.length).fill(0)));

  useEffect(() => {
    fetch(`http://localhost:5000/nonogram/${size}`)
      .then((response) => response.json())
      .then((data) => {
        setAllGames(data);
        setRowArgs(data[currentGame][0]);
        setColArgs(data[currentGame][1]);
      });
  }, [size, currentGame]);

  useEffect(() => {
    if(rowArgs.length === 0 || colArgs.length === 0) {
      return;
    }
    fetch("http://localhost:5000/nonogram/solve", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({row_args: rowArgs, col_args: colArgs}),
      
    })
      .then((response) => response.json())
      .then((data) => {
        setSolvedBoard(data);
      });
  }, [rowArgs, colArgs]);
  
  const nextGame = () => {
    if (currentGame + 1 < allGames.length) {
      setCurrentGame(currentGame + 1);
      setRowArgs(allGames[currentGame + 1][0]);
      setColArgs(allGames[currentGame + 1][1]);
    } else {
      setCurrentGame(0);
      setRowArgs(allGames[0][0]);
      setColArgs(allGames[0][1]);
    }
  };

  const solveGame = () => {
    fetch("http://localhost:5000/nonogram/solve", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({row_args: rowArgs, col_args: colArgs}),
      
    })
      .then((response) => response.json())
      .then((data) => {
        setNonogramBoard(data);
      });
  };

  if(rowArgs.length === 0 || colArgs.length === 0) {
    return <Spinner />
  }

  return (
    <div className="nonogram">
        <NonogramBoard rowArgs={rowArgs} colArgs={colArgs} callNextGame = {nextGame} nonogramBoard={nonogramBoard} setNonogramBoard={setNonogramBoard} solveGame={solveGame} solvedBoard={solvedBoard} currentGame={currentGame} gameCount={allGames.length}/>
    </div>
  );
}

export default Nonogram;


