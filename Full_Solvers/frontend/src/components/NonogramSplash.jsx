import React, { useState, useEffect } from "react";
import { useNavigate } from 'react-router-dom';

function NonogramSplash() {
    const [size, setSize] = useState("small");
    const navigate = useNavigate();

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

    const handleSizeChange = (e) => {
        setSize(e.target.value);
    }

    const handlePlayClick = () => {
        navigate(`/nonogram-game/${size}`);
    }

    return (
        <div className="nonogram-splash">
            <h1>Nonogram</h1>
            <p>Play and solve different difficulties of Nonograms with the help of an AI nonogram solver.</p>
            <div className="choice-screen">
                <select className="game-control" onChange={handleSizeChange}>
                    <option value="small">Small</option>
                    <option value="medium">Medium</option>
                    <option value="large">Large</option>
                    {windowWidth > 800 ? <option value="xl">XL</option> : null}
                </select>
                <button className="game-control" onClick={handlePlayClick}>Play</button>
            </div>
        </div>
    )
}

export default NonogramSplash