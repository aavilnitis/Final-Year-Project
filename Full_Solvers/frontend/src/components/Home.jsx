import "../nonogram.css"
import { useNavigate } from 'react-router-dom';
import React, { useEffect, useState } from "react";

function Home() {

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

    const navigate = useNavigate();
    
  return (
    <div className="start">
      <h1 style={{textAlign: "center"}}>Solving Puzzles and {windowWidth > 800 ? <br /> : null} Playing Games using AI!</h1>
      <p style={{fontSize: 18}}>Final Year Project - Aleksis Aleksandrs Vilnitis</p>
      <div className="start-buttons">
        <button onClick={() => navigate('/nonogram-game')} className="game-control">Play Nonogram</button>
        <button onClick={() => navigate('/sudoku-game')} className="game-control">Play Sudoku</button>
      </div>

    </div>
  )
}

export default Home
