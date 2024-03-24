import React, { useState } from "react";

function Nonogram() {
  const [selected, setSelected] = useState([]);

  const grid = [[0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0]];
  const row_hints = [[1,1,1], [5], [3], [1,1], [3]]
  const column_hints = [[2], [4], [3,1], [4], [2]]

  const handleClick = (rowIndex, cellIndex) => {
    const cellId = rowIndex * grid.length + cellIndex;
    if (selected.includes(cellId)) {
      setSelected(selected.filter(id => id !== cellId));
    } else {
      setSelected([...selected, cellId]);
    }
  }


  return (
    <div className="nonogram">
        <div className="full-board">
            <div className="row-hints">
                {row_hints.map((row, rowIndex) => (
                    <div key={rowIndex} className='row-hint'>
                        {row.map((cell, cellIndex) => (
                        <div key={rowIndex * 9 + cellIndex}>
                            {cell}
                        </div>
                        ))}
                    </div>
                ))}
                
            </div>
            <div className="game-and-col-hints">
                <div className="col-hints">
                    {column_hints.map((col, colIndex) => (
                        <div key={colIndex} className='col-hint'>
                            {col.map((cell, cellIndex) => (
                            <div key={colIndex * 9 + cellIndex}>
                                {cell}
                            </div>
                            ))}
                        </div>
                    ))}
                </div>
                <div className="nonogram-game">
                    {grid.map((row, rowIndex) => (
                    <div key={rowIndex} className='nonogram-row'>
                        {row.map((cell, cellIndex) => (
                        <button 
                            onClick={() => handleClick(rowIndex, cellIndex)}
                            className={`nonogram-cell ${selected.includes(rowIndex * grid.length + cellIndex) ? "selected" : ""}`}
                            key={rowIndex * grid.length + cellIndex}
                        >
                            {cell !== 0 ? cell : ""}
                        </button>
                        ))}
                    </div>
                    ))}
                </div>
            </div>
        </div>
    </div>
  );
}

export default Nonogram;
